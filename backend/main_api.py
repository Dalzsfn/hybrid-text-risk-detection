from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv
import os

# 🔹 Lectura de MENSAJES
from utils_archivos import (
    leer_txt,
    leer_pdf,
    leer_csv_como_texto,
    leer_excel_como_texto
)

# 🔹 Lectura de PATRONES
from utils_patrones import (
    leer_patrones_csv,
    leer_patrones_excel,
    leer_patrones_txt,
    guardar_patrones
)

from sistema import cargar_patrones, analizar_mensaje

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATRONES_PATH = os.path.join(BASE_DIR, "data", "patrones.csv")

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- MODELOS --------
class PatronEntrada(BaseModel):
    patron: str
    categoria: str
    nivel_alerta: str
    sugerencia: str

# -------- ENDPOINTS --------

@app.get("/")
def root():
    return {"status": "API WISEcheck activa"}

# 📩 ANALIZAR MENSAJE / ARCHIVO
@app.post("/analizar")
async def analizar(
    mensaje: str = Form(""),
    archivo: UploadFile = File(None)
):
    texto_total = mensaje or ""

    if archivo:
        nombre = archivo.filename.lower()

        if nombre.endswith(".txt"):
            texto_archivo = leer_txt(archivo)

        elif nombre.endswith(".pdf"):
            texto_archivo = leer_pdf(archivo)

        elif nombre.endswith(".csv"):
            texto_archivo = leer_csv_como_texto(archivo)

        elif nombre.endswith(".xlsx"):
            texto_archivo = leer_excel_como_texto(archivo)

        else:
            return {"error": "Formato no soportado"}

        texto_total += "\n" + texto_archivo

    patrones = cargar_patrones(PATRONES_PATH)
    resultados = analizar_mensaje(texto_total, patrones)

    return {
        "texto_analizado": texto_total,
        "resultados": resultados
    }

# ➕ AGREGAR PATRÓN MANUAL
@app.post("/patrones")
def agregar_patron(p: PatronEntrada):
    with open(PATRONES_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            p.patron,
            p.categoria,
            p.nivel_alerta,
            p.sugerencia
        ])
    print("📂 Guardando en:", os.path.abspath(PATRONES_PATH))

    return {"status": "Patrón agregado correctamente"}

# 📂 CARGAR PATRONES DESDE ARCHIVO
@app.post("/patrones/cargar-archivo")
async def cargar_patrones_archivo(archivo: UploadFile = File(...)):
    nombre = archivo.filename.lower()

    if nombre.endswith(".csv"):
        patrones = leer_patrones_csv(archivo)

    elif nombre.endswith(".xlsx"):
        patrones = leer_patrones_excel(archivo)

    elif nombre.endswith(".txt"):
        patrones = leer_patrones_txt(archivo)

    else:
        return {"error": "Formato no soportado"}

    guardar_patrones(patrones)

    return {
        "status": "Patrones cargados correctamente",
        "cantidad": len(patrones)
    }
