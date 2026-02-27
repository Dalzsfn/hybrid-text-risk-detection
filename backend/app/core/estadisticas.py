from collections import defaultdict
from typing import Dict, List

_estadisticas = {
    "total_analisis": 0,
    "tiempo_kmp_ns": [],
    "tiempo_bm_ns": [],
    "categorias": defaultdict(int),
    "tipos_match": defaultdict(int),
    "historial_ejecuciones": []
}

def registrar_resultados(resultados: List[Dict]):
    _estadisticas["total_analisis"] += 1

    tiempos_kmp = []
    tiempos_bm = []

    for r in resultados:

        categoria = r.get("categoria")
        if categoria:
            _estadisticas["categorias"][categoria] += 1

        tipo_match = r.get("tipo_match")
        if tipo_match:
            _estadisticas["tipos_match"][tipo_match] += 1

        resultado_algoritmo = r.get("resultado")

        if resultado_algoritmo:
            tiempo_kmp = resultado_algoritmo.get("tiempo_kmp_ns")
            tiempo_bm = resultado_algoritmo.get("tiempo_bm_ns")

            if tiempo_kmp:
                tiempos_kmp.append(tiempo_kmp)

            if tiempo_bm:
                tiempos_bm.append(tiempo_bm)

    ejecucion = {
        "kmp": sum(tiempos_kmp) // len(tiempos_kmp) if tiempos_kmp else 0,
        "boyer_moore": sum(tiempos_bm) // len(tiempos_bm) if tiempos_bm else 0
    }

    _estadisticas["historial_ejecuciones"].append(ejecucion)

    _estadisticas["tiempo_kmp_ns"].extend(tiempos_kmp)
    _estadisticas["tiempo_bm_ns"].extend(tiempos_bm)

def obtener_estadisticas():
    def promedio(valores):
        return sum(valores) // len(valores) if valores else 0

    return {
        "total_analisis": _estadisticas["total_analisis"],

        "tiempos_promedio_ns": {
            "kmp": promedio(_estadisticas["tiempo_kmp_ns"]),
            "boyer_moore": promedio(_estadisticas["tiempo_bm_ns"])
        },

        "conteo_categorias": dict(_estadisticas["categorias"]),

        "conteo_tipos_match": dict(_estadisticas["tipos_match"]),

        "historial_ejecuciones": _estadisticas["historial_ejecuciones"]
    }

def reset_estadisticas():
    _estadisticas["total_analisis"] = 0
    _estadisticas["tiempo_kmp_ns"].clear()
    _estadisticas["tiempo_bm_ns"].clear()
    _estadisticas["categorias"].clear()
    _estadisticas["tipos_match"].clear()
    _estadisticas["historial_ejecuciones"].clear()