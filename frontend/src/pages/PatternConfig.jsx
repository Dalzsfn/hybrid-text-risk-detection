import { useEffect, useState } from "react"
import FileUpload from "../components/FileUpload"

function PatternConfig() {

  const [patron, setPatron] = useState("")
  const [categoria, setCategoria] = useState("Reclamo")
  const [alerta, setAlerta] = useState("Medio")
  const [sugerencia, setSugerencia] = useState("")
  const [mensajeManual, setMensajeManual] = useState(null)
  const [errorManual, setErrorManual] = useState(null)

  const [archivo, setArchivo] = useState(null)
  const [mensajeArchivo, setMensajeArchivo] = useState(null)
  const [errorArchivo, setErrorArchivo] = useState(null)

  const [patrones, setPatrones] = useState([])
  const [filtroCategoria, setFiltroCategoria] = useState("Todos")

  const agregarPatron = async () => {
    setMensajeManual(null)
    setErrorManual(null)

    if (!patron || !sugerencia) {
      setErrorManual("Complete todos los campos")
      return
    }

    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/patrones`, {
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
        setMensajeManual("Patrón agregado correctamente")
        setPatron("")
        setSugerencia("")
        cargarPatrones()
      }
    } catch {
      setErrorManual("No se pudo conectar con el servidor")
    }
  }

  const subirArchivo = async () => {
    if (!archivo) return

    setMensajeArchivo(null)
    setErrorArchivo(null)

    const formData = new FormData()
    formData.append("archivo", archivo)

    try {
      const res = await fetch(
        `${import.meta.env.VITE_API_URL}/patrones/cargar-archivo`,
        { method: "POST", body: formData }
      )

      const data = await res.json()

      if (data.error) {
        setErrorArchivo(data.error)
      } else {
        setMensajeArchivo(`${data.cantidad} patrones cargados`)
        setArchivo(null)
        cargarPatrones()
      }
    } catch {
      setErrorArchivo("No se pudo conectar con el servidor")
    }
  }

  const eliminarArchivo = () => {
    setArchivo(null)
    setMensajeArchivo(null)
    setErrorArchivo(null)
  }

  const cargarPatrones = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/patrones`)
      const data = await res.json()
      setPatrones(data)
    } catch {
      console.error("Error cargando patrones")
    }
  }

  const eliminarPatron = async (patron) => {
    if (!confirm("¿Eliminar este patrón?")) return

    await fetch(
      `${import.meta.env.VITE_API_URL}/patrones/${encodeURIComponent(patron)}`,
      { method: "DELETE" }
    )

    cargarPatrones()
  }

  useEffect(() => {
    cargarPatrones()
  }, [])

  const patronesFiltrados =
    filtroCategoria === "Todos"
      ? patrones
      : patrones.filter(p => p.categoria === filtroCategoria)

  return (
    <div className="max-w-4xl mx-auto space-y-10">

      {/* ================= MANUAL ================= */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold">Agregar patrón</h2>

        <input
          className="border p-2 w-full"
          placeholder="Patrón"
          value={patron}
          onChange={e => setPatron(e.target.value)}
        />

        <select
          className="border p-2 w-full"
          value={categoria}
          onChange={e => setCategoria(e.target.value)}
        >
          <option>Queja leve</option>
          <option>Reclamo</option>
          <option>Reclamo crítico</option>
          <option>Riesgo legal</option>
        </select>

        <select
          className="border p-2 w-full"
          value={alerta}
          onChange={e => setAlerta(e.target.value)}
        >
          <option>Crítico</option>
          <option>Alto</option>
          <option>Medio</option>
          <option>Bajo</option>
        </select>

        <textarea
          className="border p-2 w-full"
          placeholder="Sugerencia"
          value={sugerencia}
          onChange={e => setSugerencia(e.target.value)}
        />

        <button
          onClick={agregarPatron}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Guardar
        </button>

        {mensajeManual && <p className="text-green-600">{mensajeManual}</p>}
        {errorManual && <p className="text-red-600">{errorManual}</p>}
      </section>

      {/* ================= ARCHIVO ================= */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold">Cargar desde archivo</h2>

        {!archivo && (
          <FileUpload
            title="Subir archivo"
            description="TXT, CSV o Excel"
            onFileSelect={setArchivo}
          />
        )}

        {archivo && (
          <div className="flex justify-between bg-gray-100 p-3 rounded">
            <span>📎 {archivo.name}</span>
            <button
              onClick={eliminarArchivo}
              className="text-red-600"
            >
              Eliminar
            </button>
          </div>
        )}

        <button
          onClick={subirArchivo}
          disabled={!archivo}
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Cargar
        </button>
      </section>

      {/* ================= LISTADO ================= */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold">Patrones existentes</h2>

        <select
          className="border p-2"
          value={filtroCategoria}
          onChange={e => setFiltroCategoria(e.target.value)}
        >
          <option>Todos</option>
          <option>Queja leve</option>
          <option>Reclamo</option>
          <option>Reclamo crítico</option>
          <option>Riesgo legal</option>
        </select>

        {patronesFiltrados.map(p => (
          <div
            key={p.patron}
            className="border rounded p-3 flex justify-between"
          >
            <div>
              <b>{p.patron}</b>
              <p className="text-sm">
                {p.categoria} · {p.nivel_alerta}
              </p>
            </div>

            <button
              onClick={() => eliminarPatron(p.patron)}
              className="text-red-600"
            >
              Eliminar
            </button>
          </div>
        ))}
      </section>

    </div>
  )
}

export default PatternConfig
