import joblib
from pathlib import Path
from backend.api.config import MODEL_PATH

_model_cache = None

def load_ml_components():
    global _model_cache

    if _model_cache is None:

        model_path = Path(MODEL_PATH)

        if not model_path.exists():
            raise FileNotFoundError(
                f"No se encontró el modelo en {MODEL_PATH}. "
                "Ejecuta primero el script de entrenamiento."
            )

        model_data = joblib.load(model_path)
        if "pipeline" not in model_data:
            raise ValueError("El archivo del modelo no contiene 'pipeline'.")

        if "patrones_vec" not in model_data:
            raise ValueError("El archivo del modelo no contiene 'patrones_vec'.")

        if "patrones_texto" not in model_data:
            raise ValueError("El archivo del modelo no contiene 'patrones_texto'.")

        pipeline = model_data["pipeline"]
        patrones_vec = model_data["patrones_vec"]
        patrones_texto = model_data["patrones_texto"]

        if "tfidf" not in pipeline.named_steps:
            raise ValueError(
                "El pipeline no contiene el paso 'tfidf'."
            )

        vectorizer = pipeline.named_steps["tfidf"]

        _model_cache = (pipeline, vectorizer, patrones_vec, patrones_texto)

    return _model_cache