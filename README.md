# 📘 Proyecto EDA II  
## Sistema de Detección Temprana de Reclamos Críticos  
**Algoritmos KMP y Boyer–Moore**

---

## 1. Descripción general

Este proyecto corresponde al curso **Estructuras de Datos y Algoritmos II (EDA II)** y tiene como objetivo el diseño e implementación de un sistema funcional para la **detección temprana de reclamos críticos en textos de atención al cliente**, utilizando **algoritmos clásicos de Pattern Matching**:

- **Knuth–Morris–Pratt (KMP)**
- **Boyer–Moore (BM)**

El sistema analiza mensajes textuales provenientes de clientes (correos, tickets, reclamos) y detecta patrones asociados a:

- Quejas leves  
- Reclamos  
- Reclamos críticos  
- Riesgos legales  

> ⚠️ No se utiliza Inteligencia Artificial, cumpliendo estrictamente el enfoque algorítmico solicitado en el proyecto.

---

## 2. Estado actual del proyecto

Hasta este punto, el proyecto ha avanzado completamente en las **fases de diseño, prototipo funcional y validación algorítmica**, quedando listo para iniciar la **implementación completa correspondiente al Trabajo Opcional (Examen Final)**.

### ✔ Funcionalidades implementadas

- Implementación propia y completa de:
  - Algoritmo **KMP**
  - Algoritmo **Boyer–Moore**
- Lectura de patrones desde archivo externo (`patrones.csv`)
- Lectura de mensajes desde archivo externo (`mensajes.csv`)
- Normalización de texto:
  - Conversión a minúsculas
  - Eliminación de tildes
  - Eliminación de signos de puntuación
- Detección de múltiples patrones por mensaje
- Clasificación por:
  - Categoría
  - Nivel de alerta
- Asociación de **sugerencia de acción por patrón**
- Medición de tiempos de ejecución:
  - KMP vs Boyer–Moore (nanosegundos)
- Menú interactivo por consola
- Manejo básico de errores
- Proyecto portable (rutas absolutas basadas en el archivo)

---

## 3. Arquitectura actual del sistema

La arquitectura actual del proyecto es **modular**, clara y alineada a buenas prácticas de software académico.

```text
ProyectoEDA2_SegundoBimestre/
│
├── main.py                # Punto de entrada del sistema
├── menu.py                # Menú por consola
├── sistema.py             # Lógica central del sistema
├── medicion.py            # Medición de tiempos de ejecución
├── normalizacion.py       # Preprocesamiento de texto
│
├── algoritmos/
│   ├── kmp.py             # Implementación KMP
│   └── boyer_moore.py     # Implementación Boyer–Moore
│
├── data/
│   ├── patrones.csv       # Patrones, categorías y sugerencias
│   └── mensajes.csv       # Mensajes de clientes
│
└── Proyecto_EDAII.pdf     # Enunciado oficial del proyecto

```
## 4. Flujo lógico del sistema

1. El usuario ejecuta `main.py`.
2. Se muestra un **menú por consola**.
3. El sistema carga:
   - Patrones desde `data/patrones.csv`
   - Mensajes desde `data/mensajes.csv`
4. Cada mensaje es:
   - Normalizado (minúsculas, sin tildes, sin puntuación)
   - Analizado con **KMP**
   - Analizado con **Boyer–Moore**
5. Si se detecta un patrón:
   - Se identifica la categoría
   - Se asigna el nivel de alerta
   - Se muestra la sugerencia de acción asociada
6. Se reportan:
   - Posiciones detectadas por cada algoritmo
   - Tiempo de ejecución (nanosegundos) de KMP y Boyer–Moore

---

## 5. Ejemplo de salida en consola

```text
Mensaje: PESIMO SERVICIO nunca solucionan nada

Patrón detectado: pésimo servicio
Categoría: Reclamo crítico
Nivel de alerta: Alto
Sugerencia de acción: Escalar el reclamo a atención prioritaria

KMP -> posición: 0 | tiempo(ns): 18300
BM  -> posición: 0 | tiempo(ns): 9400

```

## 6. Justificación técnica (EDA II)

- El algoritmo **Knuth–Morris–Pratt (KMP)** permite evitar comparaciones redundantes mediante el uso de la función de failure, garantizando un tiempo de ejecución lineal en el peor caso.
- El algoritmo **Boyer–Moore** optimiza la búsqueda realizando comparaciones desde el final del patrón y aplicando saltos eficientes, lo que en la práctica reduce significativamente el número de comparaciones.
- Ambos algoritmos son ejecutados sobre los mismos mensajes y patrones, permitiendo una **comparación directa de desempeño**.
- Las limitaciones semánticas del sistema (sinónimos, ironía, errores gramaticales o contexto) se reconocen explícitamente, ya que el enfoque del proyecto es estrictamente algorítmico y no basado en inteligencia artificial.

---

## 7. Próxima etapa: Trabajo Opcional (Examen Final)

A partir de este punto, el proyecto se encuentra listo para iniciar la **Implementación Completa y Funcional**, correspondiente al **Trabajo Opcional (Evaluación tipo Examen Final)**, la cual incluirá:

- Gestión dinámica de patrones:
  - Agregar patrones desde el menú.
  - Eliminar patrones existentes sin recompilar el sistema.
- Persistencia de resultados en archivos externos.
- Medición de rendimiento con promedios reales de ejecución.
- Manejo robusto de errores:
  - Archivos inexistentes o vacíos.
  - Patrones no encontrados.
  - Mensajes sin reclamos.
- Sistema completamente funcional, sin uso de frameworks complejos ni bases de datos.

---

## 8. Requisitos para ejecutar el proyecto

- Python **3.12** o superior.
- Sistema operativo Windows, Linux o macOS.
- Ejecutar el sistema desde la carpeta raíz del proyecto mediante el comando:

```bash
python main.py
```
## 9. Nota final

Este README documenta el **avance real del proyecto antes de iniciar la implementación del Trabajo Opcional (Evaluación tipo Examen Final)**, evidenciando el dominio de **algoritmos clásicos de búsqueda de patrones (KMP y Boyer–Moore)**, un diseño **modular y funcional del sistema**, y el **cumplimiento estricto** de los requerimientos establecidos en el curso **Estructuras de Datos y Algoritmos II (EDA II)**.
