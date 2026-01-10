import time
from algoritmos.kmp import find_kmp
from algoritmos.boyer_moore import find_boyer_moore


def medir_algoritmos(texto, patron):
    inicio_kmp = time.perf_counter_ns()
    pos_kmp = find_kmp(texto, patron)
    fin_kmp = time.perf_counter_ns()

    inicio_bm = time.perf_counter_ns()
    pos_bm = find_boyer_moore(texto, patron)
    fin_bm = time.perf_counter_ns()

    return {
        "pos_kmp": pos_kmp,
        "tiempo_kmp_ns": fin_kmp - inicio_kmp,
        "pos_bm": pos_bm,
        "tiempo_bm_ns": fin_bm - inicio_bm
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
