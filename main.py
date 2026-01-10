from sistema import cargar_patrones, cargar_mensajes, analizar_mensaje

print(">>> MAIN INICIADO <<<")

            
from menu import ejecutar_menu

if __name__ == "__main__":
    ejecutar_menu()


patrones = cargar_patrones("data/patrones.csv")
mensajes = cargar_mensajes("data/mensajes.csv")

print("Patrones cargados:", len(patrones))
print("Mensajes cargados:", len(mensajes))

for m in mensajes:
    print("=" * 50)
    print("Mensaje:", m["mensaje"])

    resultados = analizar_mensaje(m["mensaje"], patrones)

    if not resultados:
        print("➡ Sin reclamos detectados")
    else:
        for r in resultados:
            res = r["resultado"]
            print("Patrón:", r["patron"])
            print("Categoría:", r["categoria"])
            print("Alerta:", r["alerta"])
            print("KMP -> posición:", res["pos_kmp"],
                  " tiempo(ns):", res["tiempo_kmp_ns"])
            print("BM  -> posición:", res["pos_bm"],
                  " tiempo(ns):", res["tiempo_bm_ns"])
