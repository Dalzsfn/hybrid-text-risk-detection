from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from backend.utils.pattern_loader import leer_patrones_csv_base,guardar_patrones,leer_patrones_csv,leer_patrones_excel,leer_patrones_txt
from backend.database.queries import get_patterns, add_pattern, delete_pattern

router = APIRouter()

class PatronEntrada(BaseModel):
    patron: str
    categoria: str
    nivel_alerta: str
    sugerencia: str


@router.get("/patrones")
def obtener_patrones():
    return get_patterns()


@router.post("/patrones")
def agregar_patron(patron: PatronEntrada):
    patrones = get_patterns()

    if any(p["patron"] == patron.patron for p in patrones):
        return {"error": "El patrón ya existe"}

    add_pattern(patron.patron, patron.categoria, patron.nivel_alerta, patron.sugerencia)
    return {"ok": True}


@router.delete("/patrones/{patron}")
def eliminar_patron(patron: str):
    delete_pattern(patron)


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

