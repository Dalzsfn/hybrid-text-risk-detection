import csv
import io
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATRONES_PATH = os.path.join(BASE_DIR, "data", "patrones.csv")

# 📥 LEER PATRONES DESDE CSV
def leer_patrones_csv(archivo):
    contenido = archivo.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(contenido))
    patrones = []

    for fila in reader:
        if len(fila) < 4:
            continue
        patrones.append({
            "patron": fila[0],
            "categoria": fila[1],
            "nivel_alerta": fila[2],
            "sugerencia": fila[3]
        })

    return patrones


# 📥 LEER PATRONES DESDE EXCEL
def leer_patrones_excel(archivo):
    df = pd.read_excel(archivo.file)
    patrones = []

    for _, fila in df.iterrows():
        patrones.append({
            "patron": str(fila[0]),
            "categoria": str(fila[1]),
            "nivel_alerta": str(fila[2]),
            "sugerencia": str(fila[3])
        })

    return patrones


# 📥 LEER PATRONES DESDE TXT
def leer_patrones_txt(archivo):
    contenido = archivo.file.read().decode("utf-8")
    patrones = []

    for linea in contenido.splitlines():
        partes = linea.split(";")
        if len(partes) < 4:
            continue
        patrones.append({
            "patron": partes[0],
            "categoria": partes[1],
            "nivel_alerta": partes[2],
            "sugerencia": partes[3]
        })

    return patrones


# 💾 GUARDAR PATRONES EN CSV
def guardar_patrones(patrones):
    with open(PATRONES_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in patrones:
            writer.writerow([
                p["patron"],
                p["categoria"],
                p["nivel_alerta"],
                p["sugerencia"]
            ])
