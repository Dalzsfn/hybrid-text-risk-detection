import csv
from backend.app.core.medicion import medir_algoritmos
from backend.utils.normalization import normalizar_texto
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def cargar_patrones(path_relativo):
    path = os.path.join(BASE_DIR, path_relativo)
    patrones = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            patrones.append(row)
    return patrones


def cargar_mensajes(path_relativo):
    path = os.path.join(BASE_DIR, path_relativo)
    mensajes = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mensajes.append(row)
    return mensajes



def analizar_mensaje(mensaje, patrones):
    resultados = []

    mensaje_n = normalizar_texto(mensaje)

    for p in patrones:
        patron_n = normalizar_texto(p["patron"])
        r = medir_algoritmos(mensaje_n, patron_n)

        if r["pos_kmp"] != -1 or r["pos_bm"] != -1:
            resultados.append({
                "patron": p["patron"],
                "categoria": p["categoria"],
                "alerta": p["nivel_alerta"],
                "sugerencia": p["sugerencia"],
                "resultado": r
            })

    return resultados
