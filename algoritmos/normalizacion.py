import unicodedata
import re


def normalizar_texto(texto: str) -> str:
    """
    Convierte el texto a una forma normalizada:
    - Minúsculas
    - Sin tildes
    - Sin signos de puntuación
    """
    # pasar a minúsculas
    texto = texto.lower()

    # eliminar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # eliminar signos de puntuación
    texto = re.sub(r'[^\w\s]', '', texto)

    return texto
