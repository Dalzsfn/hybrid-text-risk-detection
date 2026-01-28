import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import csv
import os

from sistema import cargar_patrones, analizar_mensaje


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Detección de Reclamos Críticos")
        self.root.geometry("800x600")

        #  TÍTULO 
        titulo = tk.Label(
            root,
            text="Sistema de Detección de Reclamos Críticos",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        #  MENSAJE 
        lbl_msg = tk.Label(root, text="Mensaje del cliente:")
        lbl_msg.pack(anchor="w", padx=10)

        self.txt_mensaje = scrolledtext.ScrolledText(root, height=5)
        self.txt_mensaje.pack(fill="x", padx=10, pady=5)

        #  BOTONES 
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_manual = tk.Button(
            frame_botones,
            text="Analizar mensaje",
            width=20,
            command=self.analizar_manual
        )
        btn_manual.grid(row=0, column=0, padx=5)

        btn_archivo = tk.Button(
            frame_botones,
            text="Analizar mensajes desde archivo",
            width=30,
            command=self.analizar_archivo
        )
        btn_archivo.grid(row=0, column=1, padx=5)

        # RESULTADOS 
        lbl_res = tk.Label(root, text="Resultados:")
        lbl_res.pack(anchor="w", padx=10)

        self.txt_resultados = scrolledtext.ScrolledText(root, height=18)
        self.txt_resultados.pack(fill="both", expand=True, padx=10, pady=5)

  
    # FUNCIONES
   
    def analizar_manual(self):
        mensaje = self.txt_mensaje.get("1.0", tk.END).strip()

        if not mensaje:
            messagebox.showwarning("Advertencia", "Ingrese un mensaje.")
            return

        try:
            patrones = cargar_patrones("data/patrones.csv")
            resultados = analizar_mensaje(mensaje, patrones)

            self.txt_resultados.delete("1.0", tk.END)
            self.mostrar_resultados(mensaje, resultados)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def analizar_archivo(self):
        try:
            ruta = filedialog.askopenfilename(
                title="Seleccionar archivo de mensajes",
                filetypes=[
                    ("Archivos CSV", "*.csv"),
                    ("Archivos TXT", "*.txt")
                ]
            )

            if not ruta:
                return  # usuario canceló

            patrones = cargar_patrones("data/patrones.csv")
            mensajes = []

            extension = os.path.splitext(ruta)[1].lower()

            # LECTURA SEGÚN EXTENSIÓN 
            if extension == ".csv":
                with open(ruta, encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    if "mensaje" not in reader.fieldnames:
                        messagebox.showerror(
                            "Error",
                            "El archivo CSV debe tener una columna llamada 'mensaje'"
                        )
                        return
                    for row in reader:
                        mensajes.append(row["mensaje"])

            elif extension == ".txt":
                with open(ruta, encoding="utf-8") as f:
                    for linea in f:
                        linea = linea.strip()
                        if linea:
                            mensajes.append(linea)

            else:
                messagebox.showerror("Error", "Formato de archivo no soportado")
                return

            self.txt_resultados.delete("1.0", tk.END)

            for mensaje in mensajes:
                resultados = analizar_mensaje(mensaje, patrones)
                self.mostrar_resultados(mensaje, resultados)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resultados(self, mensaje, resultados):
        self.txt_resultados.insert(tk.END, "=" * 60 + "\n")
        self.txt_resultados.insert(tk.END, f"Mensaje: {mensaje}\n")

        if not resultados:
            self.txt_resultados.insert(tk.END, "➡ Sin reclamos detectados\n\n")
            return

        for r in resultados:
            res = r["resultado"]
            self.txt_resultados.insert(tk.END, f"\nPatrón detectado: {r['patron']}\n")
            self.txt_resultados.insert(tk.END, f"Categoría: {r['categoria']}\n")
            self.txt_resultados.insert(tk.END, f"Nivel de alerta: {r['alerta']}\n")
            self.txt_resultados.insert(tk.END, f"Sugerencia: {r['sugerencia']}\n")
            self.txt_resultados.insert(
                tk.END,
                f"KMP -> posición: {res['pos_kmp']} | tiempo(ns): {res['tiempo_kmp_ns']}\n"
            )
            self.txt_resultados.insert(
                tk.END,
                f"BM  -> posición: {res['pos_bm']} | tiempo(ns): {res['tiempo_bm_ns']}\n"
            )

        self.txt_resultados.insert(tk.END, "\n")


# EJECUCIÓN 
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
