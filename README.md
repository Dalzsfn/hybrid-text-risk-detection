# Hybrid Text Risk Detection Engine

Sistema híbrido para la detección y clasificación de patrones de riesgo en textos largos (correos, tickets, documentos PDF).

Proyecto originalmente desarrollado como parte del curso **Estructuras de Datos y Algoritmos II (EDA II)** y posteriormente extendido de forma personal para incorporar técnicas de **Machine Learning y análisis semántico**.

---

## Objetivo

Detectar automáticamente patrones de riesgo dentro de textos largos y clasificarlos según su severidad:

- Queja leve  
- Reclamo  
- Reclamo crítico  
- Riesgo legal  

El sistema combina:

- Algoritmos clásicos de Pattern Matching
- Similitud vectorial (TF-IDF)
- Clasificación supervisada (Logistic Regression)

---

## Enfoque híbrido

1️) Segmentación del texto en frases  
2️) Detección exacta mediante
* Knuth–Morris–Pratt (KMP)
* Boyer–Moore (BM)  

3️) Detección aproximada mediante similitud TF-IDF  
4️) Clasificación de severidad usando Machine Learning  
5️) Determinación de severidad máxima por documento

---

## Componentes actuales

### Algoritmos clásicos

- Implementación propia de:
  - KMP
  - Boyer–Moore
- Comparación de tiempos de ejecución
- Normalización de texto

### Módulo de Machine Learning (en desarrollo)

- Vectorización TF-IDF
- Clasificador Logistic Regression
- Filtrado por similitud coseno
- Detección por frase en textos largos

---

## Arquitectura del proyecto




---

## Estado actual

✔ Sistema determinístico funcional (KMP + Boyer–Moore)  
✔ Detección de múltiples patrones por mensaje  
✔ Prototipo híbrido para textos largos  
✔ Clasificación por severidad usando ML  
⚠ Ajuste fino de thresholds en progreso  
⚠ Integración completa en módulo productivo pendiente  

---

## Motivación técnica

Los algoritmos clásicos permiten coincidencias exactas eficientes, pero presentan limitaciones ante:

- Variaciones léxicas
- Reformulaciones
- Sinónimos
- Ambigüedad contextual

La incorporación de similitud vectorial y clasificación supervisada permite extender el sistema hacia un enfoque más robusto y adaptable.

---

## Requisitos

- Python 3.12+
- scikit-learn
- pandas
- numpy

---

## Nota

Este repositorio representa la evolución de un proyecto académico hacia un motor híbrido de detección de riesgo basado en reglas y aprendizaje automático, desarrollado como proyecto personal de experimentación y mejora arquitectónica.