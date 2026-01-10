from sistema import cargar_patrones, cargar_mensajes, analizar_mensaje


def mostrar_menu():
    print("\n" + "=" * 50)
    print(" SISTEMA DE DETECCIÓN DE RECLAMOS CRÍTICOS ")
    print("=" * 50)
    print("1. Analizar mensajes desde archivo")
    print("2. Analizar mensaje manual")
    print("3. Ver patrones cargados")
    print("0. Salir")


def opcion_analizar_archivo():
    patrones = cargar_patrones("data/patrones.csv")
    mensajes = cargar_mensajes("data/mensajes.csv")

    print("\n>>> Analizando mensajes del archivo...\n")

    for m in mensajes:
        print("-" * 50)
        print("Mensaje:", m["mensaje"])

        resultados = analizar_mensaje(m["mensaje"], patrones)

        if not resultados:
            print("➡ Sin reclamos detectados")
        else:
            for r in resultados:
                res = r["resultado"]
                print(f"Patrón detectado: {r['patron']}")
                print(f"Categoría: {r['categoria']}")
                print(f"Nivel de alerta: {r['alerta']}")
                print(f"Sugerencia de acción: {r['sugerencia']}")
                print(f"KMP -> Posición: {res['pos_kmp']} | Tiempo(ns): {res['tiempo_kmp_ns']}")
                print(f"BM  -> Posición: {res['pos_bm']} | Tiempo(ns): {res['tiempo_bm_ns']}")


def opcion_analizar_manual():
    patrones = cargar_patrones("data/patrones.csv")
    mensaje = input("\nIngrese el mensaje del cliente:\n> ")

    resultados = analizar_mensaje(mensaje, patrones)

    print("\n>>> Resultado del análisis\n")

    if not resultados:
        print("➡ Sin reclamos detectados")
    else:
        for r in resultados:
            res = r["resultado"]
            print("-" * 40)
            print(f"Patrón detectado: {r['patron']}")
            print(f"Categoría: {r['categoria']}")
            print(f"Nivel de alerta: {r['alerta']}")
            print(f"KMP -> Posición: {res['pos_kmp']} | Tiempo(ns): {res['tiempo_kmp_ns']}")
            print(f"BM  -> Posición: {res['pos_bm']} | Tiempo(ns): {res['tiempo_bm_ns']}")


def opcion_ver_patrones():
    patrones = cargar_patrones("data/patrones.csv")

    print("\n>>> Patrones cargados:\n")

    for p in patrones:
        print(f"- {p['patron']} | {p['categoria']} | Alerta: {p['nivel_alerta']}")


def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            opcion_analizar_archivo()
        elif opcion == "2":
            opcion_analizar_manual()
        elif opcion == "3":
            opcion_ver_patrones()
        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
