from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PATRONES_PATH = DATA_DIR / "patrones.csv"
MODEL_DIR = BASE_DIR / "ml"
MODEL_PATH = MODEL_DIR / "modelo.pkl"