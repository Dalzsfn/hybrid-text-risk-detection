from typing import List
import csv
import io

from PyPDF2 import PdfReader
import pandas as pd
from fastapi import UploadFile


# =====================
# 📄 TXT → TEXTO
# =====================
def leer_txt(archivo: UploadFile) -> str:
    contenido = archivo.file.read().decode("utf-8", errors="ignore")
    return contenido


# =====================
# 📄 PDF → TEXTO
# =====================
def leer_pdf(archivo: UploadFile) -> str:
    reader = PdfReader(archivo.file)
    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text() or ""

    return texto


# =====================
# 📊 CSV → TEXTO
# (para ANALIZAR MENSAJES)
# =====================
def leer_csv_como_texto(archivo: UploadFile) -> str:
    contenido = archivo.file.read().decode("utf-8", errors="ignore")
    lector = csv.reader(io.StringIO(contenido))

    texto = ""
    for fila in lector:
        texto += " ".join(fila) + "\n"

    return texto


# =====================
# 📊 EXCEL → TEXTO
# (para ANALIZAR MENSAJES)
# =====================
def leer_excel_como_texto(archivo: UploadFile) -> str:
    df = pd.read_excel(archivo.file)

    texto = ""
    for _, fila in df.iterrows():
        texto += " ".join(map(str, fila.values)) + "\n"

    return texto
