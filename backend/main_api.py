from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from routes.patrones import router as patrones_router
from medicion import medir_algoritmos
from algoritmos.normalizacion import normalizar_texto
from estadisticas import (
    registrar_resultados,
    obtener_estadisticas,
    reset_estadisticas
)

from sistema import cargar_patrones, analizar_mensaje
from utils_patrones import PATRONES_PATH

from utils_archivos import (
    leer_txt,
    leer_pdf,
    leer_csv_como_texto,
    leer_excel_como_texto
)


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
    texto = mensaje or ""

    if archivo:
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

    patrones = cargar_patrones(PATRONES_PATH)
    resultados = analizar_mensaje(texto, patrones)

    # 🔥 REGISTRAR ESTADÍSTICAS AQUÍ
    registrar_resultados(resultados)

    return {"resultados": resultados}


@app.get("/estadisticas")
def estadisticas():
    return obtener_estadisticas()

@app.post("/estadisticas/reset")
def reset_stats():
    reset_estadisticas()
    return {"status": "Estadísticas reiniciadas correctamente"}

