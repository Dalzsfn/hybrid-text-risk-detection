from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from urllib.parse import unquote
from backend.utils.pattern_loader import leer_patrones_csv_base,guardar_patrones,leer_patrones_csv,leer_patrones_excel,leer_patrones_txt

router = APIRouter()

class PatronEntrada(BaseModel):
    patron: str
    categoria: str
    nivel_alerta: str
    sugerencia: str


@router.get("/patrones")
def obtener_patrones():
    return leer_patrones_csv_base()


@router.post("/patrones")
def agregar_patron(patron: PatronEntrada):
    patrones = leer_patrones_csv_base()

    if any(p["patron"] == patron.patron for p in patrones):
        return {"error": "El patrón ya existe"}

    patrones.append({
        "patron": patron.patron,
        "categoria": patron.categoria,
        "nivel_alerta": patron.nivel_alerta,
        "sugerencia": patron.sugerencia
    })

    guardar_patrones(patrones)
    return {"ok": True}


@router.delete("/patrones/{patron}")
def eliminar_patron(patron: str):
    patron = unquote(patron)
    patrones = leer_patrones_csv_base()
    patrones = [p for p in patrones if p["patron"] != patron]
    guardar_patrones(patrones)
    return {"ok": True}


@router.post("/patrones/cargar-archivo")
async def cargar_archivo(archivo: UploadFile = File(...)):
    if not archivo.filename:
        return {"error": "Archivo inexistente"}

    try:
        nombre = archivo.filename.lower()

        if nombre.endswith(".csv"):
            nuevos = leer_patrones_csv(archivo)
        elif nombre.endswith(".xlsx"):
            nuevos = leer_patrones_excel(archivo)
        elif nombre.endswith(".txt"):
            nuevos = leer_patrones_txt(archivo)
        else:
            return {"error": "Formato no soportado"}

        if not nuevos:
            return {"error": "El archivo no contiene patrones válidos"}

    except Exception:
        return {"error": "No se pudo procesar el archivo"}

    patrones = leer_patrones_csv_base()

    for p in nuevos:
        if not any(x["patron"] == p["patron"] for x in patrones):
            patrones.append(p)

    guardar_patrones(patrones)
    return {"cantidad": len(nuevos)}

