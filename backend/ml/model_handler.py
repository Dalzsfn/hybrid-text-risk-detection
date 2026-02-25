import joblib
from pathlib import Path
from backend.api.config import MODEL_PATH, MODEL_DIR
import os

_model = None
_vectorizer = None
_patrones_vec = None
_patrones_texto = None


def load_ml_components():
    global _model, _vectorizer, _patrones_vec, _patrones_texto

    if _model is None:
        if not Path(MODEL_PATH).exists():
            raise FileNotFoundError(
                f"No se encontró el modelo en {MODEL_PATH}. "
                "Ejecuta primero el script de entrenamiento."
            )

        _model = joblib.load(MODEL_PATH)

        if "tfidf" not in _model.named_steps:
            raise ValueError(
                "El modelo cargado no contiene un paso 'tfidf' en el pipeline."
            )

        _vectorizer = _model.named_steps["tfidf"]

        patrones_path = MODEL_DIR / "patrones.pkl"

        if not patrones_path.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo de patrones en {patrones_path}"
            )

        _patrones_texto = joblib.load(patrones_path)
        
        _patrones_vec = _vectorizer.transform(_patrones_texto)

    return _model, _vectorizer, _patrones_vec, _patrones_texto