import time
from algoritmos.kmp import find_kmp
from algoritmos.boyer_moore import find_boyer_moore


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

    
''''
from medicion import medir_algoritmos

casos = [
    ("Pésimo servicio, nunca solucionan nada", "pésimo servicio"),
    ("Si no arreglan hoy, voy a demandar", "voy a demandar"),
    ("Gracias por la atención", "fraude"),
]

for texto, patron in casos:
    r = medir_algoritmos(texto, patron)
    print("Texto:", texto)
    print("Patrón:", patron)
    print("Resultado:", r)
    print("-" * 40)
'''
