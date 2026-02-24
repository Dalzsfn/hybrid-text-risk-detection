import csv
import io
import pandas as pd
from backend.api.config import PATRONES_PATH


def leer_patrones_csv(archivo):
    contenido = archivo.file.read().decode("utf-8-sig")
    reader = csv.reader(io.StringIO(contenido))
    patrones = []

    next(reader, None)  # saltar encabezado
    for fila in reader:
        if len(fila) < 4:
            continue
        patrones.append({
            "patron": fila[0].strip(),
            "categoria": fila[1].strip(),
            "nivel_alerta": fila[2].strip(),
            "sugerencia": fila[3].strip()
        })

    return patrones


def leer_patrones_excel(archivo):
    df = pd.read_excel(archivo.file)
    patrones = []

    for _, fila in df.iterrows():
        patrones.append({
            "patron": str(fila[0]).strip(),
            "categoria": str(fila[1]).strip(),
            "nivel_alerta": str(fila[2]).strip(),
            "sugerencia": str(fila[3]).strip()
        })

    return patrones


def leer_patrones_txt(archivo):
    contenido = archivo.file.read().decode("utf-8")
    patrones = []

    for linea in contenido.splitlines():
        partes = linea.split(",")
        if len(partes) < 4:
            continue
        patrones.append({
            "patron": partes[0].strip(),
            "categoria": partes[1].strip(),
            "nivel_alerta": partes[2].strip(),
            "sugerencia": partes[3].strip()
        })

    return patrones



def leer_patrones_csv_base():
    if not PATRONES_PATH.exists():
        return []

    with open(PATRONES_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def guardar_patrones(patrones):
    PATRONES_PATH.parent.mkdir(exist_ok=True)

    with open(PATRONES_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["patron", "categoria", "nivel_alerta", "sugerencia"]
        )
        writer.writeheader()
        writer.writerows(patrones)
