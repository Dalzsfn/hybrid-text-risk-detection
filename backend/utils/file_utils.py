import csv
import io
from PyPDF2 import PdfReader
import pandas as pd
from fastapi import UploadFile

from algoritmos.normalizacion import normalizar_texto


def leer_txt(archivo: UploadFile) -> str:
    contenido = archivo.file.read().decode("utf-8", errors="ignore")
    texto = normalizar_texto(contenido)

    if not texto:
        raise ValueError("El archivo TXT está vacío")

    return texto



def leer_pdf(archivo: UploadFile) -> str:
    reader = PdfReader(archivo.file)
    texto = ""

    for pagina in reader.pages:
        extraido = pagina.extract_text()
        if extraido:
            texto += extraido + " "

    texto = normalizar_texto(texto)

    if not texto:
        raise ValueError("El archivo PDF no contiene texto")

    return texto



def leer_csv_como_texto(archivo: UploadFile) -> str:
    contenido = archivo.file.read().decode("utf-8", errors="ignore")
    lector = csv.reader(io.StringIO(contenido))

    texto = ""
    for fila in lector:
        texto += " ".join(fila) + " "

    texto = normalizar_texto(texto)

    if not texto:
        raise ValueError("El archivo CSV está vacío")

    return texto



def leer_excel_como_texto(archivo: UploadFile) -> str:
    df = pd.read_excel(archivo.file)

    if df.empty:
        raise ValueError("El archivo Excel está vacío")

    texto = ""
    for _, fila in df.iterrows():
        texto += " ".join(map(str, fila.values)) + " "

    texto = normalizar_texto(texto)

    if not texto:
        raise ValueError("El archivo Excel no contiene texto válido")

    return texto
