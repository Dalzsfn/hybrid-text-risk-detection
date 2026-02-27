# Hybrid Text Risk Detection Engine

Sistema híbrido para la detección y clasificación de patrones de riesgo en textos largos.

Proyecto desarrollado inicialmente en el curso **Estructuras de Datos y Algoritmos II (EDA II)** y posteriormente extendido de forma independiente para integrar técnicas de **Machine Learning, similitud semántica y arquitectura cliente-servidor con FastAPI**.

---

## Objetivo

Detectar automáticamente patrones de riesgo dentro de textos extensos y archivos para clasificarlos según su severidad:

- Queja leve  
- Reclamo  
- Reclamo crítico  
- Riesgo legal  

El sistema combina enfoques determinísticos y probabilísticos para lograr mayor robustez.

---

## Enfoque híbrido

1. Segmentación del texto en frases

2. Detección exacta mediante:
    - Knuth–Morris–Pratt (KMP)
    - Boyer–Moore (BM)

3. Detección aproximada mediante:
    - Vectorización TF-IDF  
    - Similitud coseno  

4. Clasificación supervisada:
    - Logistic Regression  

5. Determinación de severidad máxima por documento  

---

## Arquitectura del sistema

Frontend (React)  
↓  
API REST (FastAPI)  
↓  
Motor híbrido de detección  
↓  
Clasificación ML  
↓  
Respuesta JSON estructurada  

---

## Componentes técnicos

### Algoritmos clásicos

- Implementación propia de KMP  
- Implementación propia de Boyer–Moore  
- Comparación de tiempos de ejecución  
- Normalización y limpieza de texto  

### Machine Learning

- TF-IDF Vectorizer  
- Logistic Regression  
- Similitud coseno para filtrado semántico  
- Clasificación por frase en textos largos  

### Backend

- FastAPI  
- Manejo de archivos (PDF, Excel, CSV)  
- Endpoint REST `/analizar`  

---

## Estado actual

✔ Sistema determinístico funcional  
✔ Detección híbrida exacta + semántica  
✔ Clasificación por severidad  
✔ API REST operativa  
✔ Frontend con separación de coincidencias exactas y aproximadas  
⚠ Ajuste fino de thresholds en progreso  
⚠ Migración futura de CSV a base de datos  
⚠ Dockerización pendiente  

---

## Instalación

### 1️) Clonar repositorio

```bash
git clone https://github.com/Dalzsfn/hybrid-text-risk-detection.git
cd hybrid-text-risk-detection 
```

### 2) Entorno virtual

Crear entorno:

```bash
python -m venv venv
```

Activar entorno:

* Windows

```bash
venv\Scripts\activate
```

* macOS/Linux

```bash
source venv/bin/activate
```

### 3) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4) Ejecutar backend

```bash
uvicorn backend.api.main_api:app --reload
```

### 5) Ejecutar frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Requisitos

Python 3.12+

Node.js (para frontend React)

Dependencias del backend definidas en:

`requirements.txt` 
