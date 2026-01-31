import { useState } from "react"
import FileUpload from "../components/FileUpload"

function PatternConfig() {

  // ---------- FORM MANUAL ----------
  const [patron, setPatron] = useState("")
  const [categoria, setCategoria] = useState("Reclamo")
  const [alerta, setAlerta] = useState("Medio")
  const [sugerencia, setSugerencia] = useState("")
  const [mensajeManual, setMensajeManual] = useState(null)
  const [errorManual, setErrorManual] = useState(null)

  // ---------- ARCHIVO ----------
  const [archivo, setArchivo] = useState(null)
  const [mensajeArchivo, setMensajeArchivo] = useState(null)
  const [errorArchivo, setErrorArchivo] = useState(null)

  // ---------- AGREGAR MANUAL ----------
  const agregarPatron = async () => {
    setMensajeManual(null)
    setErrorManual(null)

    if (!patron || !sugerencia) {
      setErrorManual("Complete todos los campos")
      return
    }

    try {
      const res = await fetch("http://127.0.0.1:8000/patrones", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          patron,
          categoria,
          nivel_alerta: alerta,
          sugerencia
        })
      })

      const data = await res.json()

      if (data.error) {
        setErrorManual(data.error)
      } else {
        setMensajeManual("✅ Patrón agregado correctamente")
        setPatron("")
        setSugerencia("")
      }

    } catch {
      setErrorManual("No se pudo conectar con el servidor")
    }
  }

  // ---------- CARGAR ARCHIVO ----------
  const subirArchivo = async () => {
    if (!archivo) return

    setMensajeArchivo(null)
    setErrorArchivo(null)

    const formData = new FormData()
    formData.append("archivo", archivo)

    try {
      const res = await fetch(
        "http://127.0.0.1:8000/patrones/cargar-archivo",
        { method: "POST", body: formData }
      )

      const data = await res.json()

      if (data.error) {
        setErrorArchivo(data.error)
      } else {
        setMensajeArchivo(
          `✅ ${data.cantidad} patrones cargados correctamente`
        )
        setArchivo(null)
      }

    } catch {
      setErrorArchivo("No se pudo conectar con el servidor")
    }
  }

  return (
    <div className="max-w-3xl mx-auto space-y-10">

      {/* ================= MANUAL ================= */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold">
          ➕ Agregar patrón manualmente
        </h2>

        <input
          className="border rounded p-2 w-full"
          placeholder="Patrón (texto a buscar)"
          value={patron}
          onChange={e => setPatron(e.target.value)}
        />

        <select
          className="border rounded p-2 w-full"
          value={categoria}
          onChange={e => setCategoria(e.target.value)}
        >
          <option>Reclamo crítico</option>
          <option>Riesgo legal</option>
          <option>Reclamo</option>
          <option>Queja leve</option>
        </select>

        <select
          className="border rounded p-2 w-full"
          value={alerta}
          onChange={e => setAlerta(e.target.value)}
        >
          <option>Crítico</option>
          <option>Alto</option>
          <option>Medio</option>
          <option>Bajo</option>
        </select>

        <textarea
          className="border rounded p-2 w-full"
          placeholder="Sugerencia de acción"
          value={sugerencia}
          onChange={e => setSugerencia(e.target.value)}
        />

        <button
          onClick={agregarPatron}
          className="bg-blue-600 text-white px-5 py-2 rounded"
        >
          Guardar patrón
        </button>

        {mensajeManual && (
          <div className="bg-green-100 text-green-700 p-3 rounded">
            {mensajeManual}
          </div>
        )}

        {errorManual && (
          <div className="bg-red-100 text-red-700 p-3 rounded">
            {errorManual}
          </div>
        )}
      </section>

      {/* ================= ARCHIVO ================= */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold">
          📂 Cargar patrones desde archivo
        </h2>

        <FileUpload
          title="Subir archivo de patrones"
          description="Formatos: TXT, CSV o Excel"
          onFileSelect={file => setArchivo(file)}
        />

        {archivo && (
          <p className="text-sm text-gray-600">
            📎 {archivo.name}
          </p>
        )}

        <button
          onClick={subirArchivo}
          className="bg-green-600 text-white px-5 py-2 rounded"
        >
          Cargar archivo
        </button>

        {mensajeArchivo && (
          <div className="bg-green-100 text-green-700 p-3 rounded">
            {mensajeArchivo}
          </div>
        )}

        {errorArchivo && (
          <div className="bg-red-100 text-red-700 p-3 rounded">
            {errorArchivo}
          </div>
        )}
      </section>

    </div>
  )
}

export default PatternConfig
