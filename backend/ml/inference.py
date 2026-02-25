from backend.ml.model_handler import load_model
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def segmentar_texto(texto):
    frases = re.split(r'[.!?]\s+', texto)
    return [f.strip() for f in frases if f.strip()]

def es_candidata_por_similitud(frase, threshold=0.30):
    frase_vec = vectorizer.transform([frase])
    similitudes = cosine_similarity(frase_vec, patrones_vec)
    max_similitud = similitudes.max()
    return max_similitud > threshold

def analizar_texto(texto):
    modelo = load_model()
    frases = segmentar_texto(texto)
    resultados = []

    for frase in frases:
        categoria = modelo.predict([frase])[0]
        prob = max(modelo.predict_proba([frase])[0])

        if prob > 0.60:
            resultados.append({
                "frase": frase,
                "categoria": categoria,
                "probabilidad": float(prob)
            })

    return resultados