import re
from sklearn.metrics.pairwise import cosine_similarity
from backend.ml.model_handler import load_ml_components

UMBRAL_MODELO = 0.60
UMBRAL_SIMILITUD = 0.5


def segmentar_texto(texto):
    frases = re.split(r'[.!?]\s+', texto)
    return [f.strip() for f in frases if f.strip()]


def analizar_texto(texto):
    modelo, vectorizer, patrones_vec, patrones_texto = load_ml_components()
    frases = segmentar_texto(texto)
    resultados = []

    for frase in frases:
        probas = modelo.predict_proba([frase])[0]
        categoria_index = probas.argmax()
        categoria = modelo.classes_[categoria_index]
        prob_modelo = float(probas[categoria_index])

        frase_vec = vectorizer.transform([frase])
        similitudes = cosine_similarity(frase_vec, patrones_vec)[0]

        max_index = similitudes.argmax()
        max_similitud = float(similitudes.max())
        patron_relacionado = patrones_texto[max_index]

        if  max_similitud > UMBRAL_SIMILITUD:

            resultados.append({
                "frase": frase,
                "categoria": categoria,
                "tipo_match": "aproximado",
                "confianza_modelo": prob_modelo,
                "confianza_patron": max_similitud,
                "patron_relacionado": patron_relacionado
            })

    return resultados