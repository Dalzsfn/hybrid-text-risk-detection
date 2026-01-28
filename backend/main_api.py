from fastapi import FastAPI
from pydantic import BaseModel
from sistema import cargar_patrones, analizar_mensaje

app = FastAPI()

# Cargar patrones UNA sola vez
patrones = cargar_patrones("data/patrones.csv")


# -------- MODELOS --------

class MensajeEntrada(BaseModel):
    mensaje: str


# -------- ENDPOINTS --------

@app.get("/")
def root():
    return {"status": "API WISEcheck activa"}


@app.post("/analizar")
def analizar(data: MensajeEntrada):
    resultados = analizar_mensaje(data.mensaje, patrones)
    return {
        "mensaje": data.mensaje,
        "resultados": resultados
    }
