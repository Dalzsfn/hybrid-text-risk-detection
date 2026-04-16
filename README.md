# Hybrid Text Risk Detection Engine

Proyecto desarrollado inicialmente en el curso Estructuras de Datos y Algoritmos II (EDA II) y posteriormente extendido de forma independiente para integrar técnicas de Machine Learning, similitud semántica y arquitectura cliente-servidor con FastAPI.

Motor hibrido para deteccion y clasificacion de patrones de riesgo en texto libre y archivos.

El proyecto combina algoritmos clasicos de busqueda de cadenas con un pipeline de Machine Learning para mejorar cobertura y robustez en escenarios reales.

## Tabla de contenido

- Descripcion general
- Caracteristicas
- Flujo de procesamiento
- Arquitectura
- Stack tecnologico
- Requisitos
- Configuracion del entorno
- Ejecucion local
- Ejecucion con Docker Compose
- Endpoints de la API
- Formatos de archivo soportados
- Estado del proyecto

## Descripcion general

Objetivo: detectar expresiones de riesgo en mensajes extensos, clasificarlas por severidad y devolver resultados estructurados para consumo por UI o integracion externa.

Niveles de severidad utilizados:

- Queja leve
- Reclamo
- Reclamo critico
- Riesgo legal

## Caracteristicas

- Deteccion exacta con implementaciones propias de KMP y Boyer-Moore.
- Deteccion aproximada con TF-IDF + similitud coseno.
- Clasificacion supervisada con Logistic Regression.
- API REST en FastAPI para analisis, estadisticas y gestion de patrones.
- Frontend en React + Vite para carga de texto/archivo y visualizacion de resultados.
- Inicializacion automatica de tabla y carga de patrones base al arrancar el backend.

## Flujo de procesamiento

1. Ingreso de texto (manual o desde archivo).
2. Normalizacion y segmentacion.
3. Deteccion exacta (KMP/BM).
4. Deteccion aproximada (similitud semantica).
5. Clasificacion de severidad.
6. Respuesta JSON con coincidencias y metadatos.

## Arquitectura

Frontend (React/Vite)
-> API REST (FastAPI)
-> Motor hibrido de deteccion
-> Clasificacion ML
-> Respuesta JSON

## Stack tecnologico

- Backend: FastAPI, SQLAlchemy, psycopg2, pandas, scikit-learn
- Base de datos: PostgreSQL
- Frontend: React 19, Vite, Tailwind CSS
- Contenedores: Docker, Docker Compose

## Requisitos

- Python 3.12 o superior
- Node.js 20 o superior
- Docker Desktop (opcional, recomendado)

## Configuracion del entorno

1. Clonar repositorio

```bash
git clone https://github.com/Dalzsfn/hybrid-text-risk-detection.git
cd hybrid-text-risk-detection
```

2. Crear archivo de entorno en raiz

Windows:

```bash
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Variables esperadas en `.env`:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
DB_NAME=hybrid_risk
```

3. Crear archivo de entorno para frontend

Windows:

```bash
copy frontend\.env.example frontend\.env
```

macOS/Linux:

```bash
cp frontend/.env.example frontend/.env
```

Valor por defecto:

```env
VITE_API_URL=http://localhost:8000
```

## Ejecucion local

### 1) Backend

Desde la raiz del proyecto:

```bash
python -m venv .venv
```

Activar entorno virtual:

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias del backend:

```bash
pip install -r backend/requirements.txt
```

Iniciar API (ejecutar desde carpeta `backend`):

```bash
cd backend
uvicorn api.main_api:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

En otra terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend disponible en `http://localhost:5173`.

## Ejecucion con Docker Compose

Levantar todo el stack (PostgreSQL + backend + frontend):

```bash
docker compose up --build
```

Servicios:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- PostgreSQL: `localhost:5432`

Al iniciar, el backend crea la tabla `patterns` (si no existe) y carga/actualiza patrones desde `backend/data/patrones.csv`.

## Endpoints de la API

Base URL local: `http://localhost:8000`

- `GET /` estado de servicio
- `POST /analizar` analiza texto o archivo
- `GET /estadisticas` consulta estadisticas acumuladas
- `POST /estadisticas/reset` reinicia estadisticas
- `GET /patrones` lista patrones
- `POST /patrones` crea un patron
- `DELETE /patrones/{patron}` elimina un patron
- `POST /patrones/cargar-archivo` carga patrones desde archivo

## Formatos de archivo soportados

Para analisis (`/analizar`):

- `.txt`
- `.pdf`
- `.csv`
- `.xlsx`

Para carga masiva de patrones (`/patrones/cargar-archivo`):

- `.txt`
- `.csv`
- `.xlsx`

## Estado del proyecto

- Implementacion hibrida operativa (exacta + aproximada).
- Clasificacion por severidad en produccion academica.
- Persistencia en PostgreSQL con seed inicial automatico.
- Frontend funcional para analisis y gestion de patrones.

Siguientes mejoras:

- Ajuste fino de umbrales de similitud y confianza.
- Actualización del modelo por agregación/eliminación de patrones.

