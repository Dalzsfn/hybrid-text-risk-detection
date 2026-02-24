import unicodedata
import re


def normalizar_texto(texto: str) -> str:
    """
    Normaliza texto para análisis:
    - Minúsculas
    - Sin tildes
    - Sin signos de puntuación
    - Sin saltos de línea
    - Sin espacios duplicados
    """
    if not texto:
        return ""

    # minúsculas
    texto = texto.lower()

    # eliminar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # eliminar signos de puntuación
    texto = re.sub(r'[^\w\s]', ' ', texto)

    # eliminar saltos de línea y espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()
