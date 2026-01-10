import csv
from medicion import medir_algoritmos
from algoritmos.normalizacion import normalizar_texto


def cargar_patrones(path):
    patrones = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            patrones.append(row)
    return patrones


def cargar_mensajes(path):
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
