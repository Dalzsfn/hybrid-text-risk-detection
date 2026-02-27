from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.api.patterns import router as patrones_router
from backend.app.core.estadisticas import registrar_resultados,obtener_estadisticas,reset_estadisticas
from backend.app.core.sistema import cargar_patrones, analizar_mensaje
from backend.utils.pattern_loader import PATRONES_PATH
from backend.utils.file_utils import leer_txt,leer_pdf,leer_csv_como_texto,leer_excel_como_texto

app = FastAPI()
app.include_router(patrones_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API WISEcheck activa"}

@app.post("/analizar")
async def analizar(
    mensaje: str = Form(""),
    archivo: UploadFile = File(None)
):
    texto = mensaje.strip() if mensaje else ""

    if not texto and not archivo:
        return {"error": "No se recibió ningún mensaje ni archivo para analizar"}

    try:
        if archivo:
            if not archivo.filename:
                return {"error": "Archivo inexistente"}

            nombre = archivo.filename.lower()

            if nombre.endswith(".txt"):
                texto += leer_txt(archivo)
            elif nombre.endswith(".pdf"):
                texto += leer_pdf(archivo)
            elif nombre.endswith(".csv"):
                texto += leer_csv_como_texto(archivo)
            elif nombre.endswith(".xlsx"):
                texto += leer_excel_como_texto(archivo)
            else:
                return {"error": "Formato no soportado"}

    except ValueError as e:
        return {"error": str(e)}

    if not texto.strip():
        return {"error": "El contenido a analizar está vacío"}

    patrones = cargar_patrones(PATRONES_PATH)
    resultados = analizar_mensaje(texto, patrones)

    registrar_resultados(resultados)

    return {"resultados": resultados}



@app.get("/estadisticas")
def estadisticas():
    return obtener_estadisticas()

@app.post("/estadisticas/reset")
def reset_stats():
    reset_estadisticas()
    return {"status": "Estadísticas reiniciadas correctamente"}

