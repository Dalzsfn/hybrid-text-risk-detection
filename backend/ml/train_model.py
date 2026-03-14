import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from backend.api.config import PATRONES_PATH, MODEL_PATH
from backend.utils.normalization import normalizar_texto

def entrenar_modelo():
    df = pd.read_csv(PATRONES_PATH)
    X = df["patron"]
    y = df["categoria"]

    stopwords_es = [
        "el", "la", "los", "las", "un", "una",
        "de", "del", "y", "o", "que", "en", "a"
    ]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            preprocessor=normalizar_texto,
            stop_words=stopwords_es,
            max_features=250,
            ngram_range=(1, 2)
        )),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X, y)

    patrones_vec = pipeline.named_steps["tfidf"].transform(X)
    
    model_data = {
    "pipeline": pipeline,
    "patrones_vec": patrones_vec,
    "patrones_texto": X
    }

    joblib.dump(model_data, MODEL_PATH)

if __name__ == "__main__":
    entrenar_modelo()