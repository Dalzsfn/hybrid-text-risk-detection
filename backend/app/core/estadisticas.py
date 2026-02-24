from collections import defaultdict
from typing import Dict, List



_estadisticas = {
    "total_analisis": 0,
    "tiempo_kmp_ns": [],
    "tiempo_bm_ns": [],
    "categorias": defaultdict(int),
    "historial_ejecuciones": []   # 👈 NUEVO
}



def registrar_resultados(resultados: List[Dict]):
    _estadisticas["total_analisis"] += 1

    tiempos_kmp = []
    tiempos_bm = []

    for r in resultados:
        res = r["resultado"]

        tiempos_kmp.append(res["tiempo_kmp_ns"])
        tiempos_bm.append(res["tiempo_bm_ns"])

        categoria = r["categoria"]
        _estadisticas["categorias"][categoria] += 1

    # Promedio POR EJECUCIÓN
    ejecucion = {
        "kmp": sum(tiempos_kmp) // len(tiempos_kmp) if tiempos_kmp else 0,
        "boyer_moore": sum(tiempos_bm) // len(tiempos_bm) if tiempos_bm else 0
    }

    _estadisticas["historial_ejecuciones"].append(ejecucion)

    # Mantener estadísticas globales
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

        "historial_ejecuciones": _estadisticas["historial_ejecuciones"]  # 👈 NUEVO
    }



def reset_estadisticas():
    """
    Limpia todas las estadísticas (útil para pruebas).
    """
    _estadisticas["total_analisis"] = 0
    _estadisticas["tiempo_kmp_ns"].clear()
    _estadisticas["tiempo_bm_ns"].clear()
    _estadisticas["categorias"].clear()
    _estadisticas["historial_ejecuciones"].clear()

