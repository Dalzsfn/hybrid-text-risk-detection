import time
from backend.app.algorithms.kmp import find_kmp
from backend.app.algorithms.boyer_moore import find_boyer_moore

def medir_algoritmos(texto, patron, repeticiones=5):
    tiempos_kmp = []
    tiempos_bm = []

    pos_kmp = pos_bm = -1

    for _ in range(repeticiones):
        ini = time.perf_counter_ns()
        pos_kmp = find_kmp(texto, patron)
        fin = time.perf_counter_ns()
        tiempos_kmp.append(fin - ini)

        ini = time.perf_counter_ns()
        pos_bm = find_boyer_moore(texto, patron)
        fin = time.perf_counter_ns()
        tiempos_bm.append(fin - ini)

    return {
        "pos_kmp": pos_kmp,
        "tiempo_kmp_ns": sum(tiempos_kmp) // repeticiones,
        "pos_bm": pos_bm,
        "tiempo_bm_ns": sum(tiempos_bm) // repeticiones,
        "repeticiones": repeticiones
    }

