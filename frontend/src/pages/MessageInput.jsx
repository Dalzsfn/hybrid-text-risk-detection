import { useState } from "react"
import FileUpload from "../components/FileUpload"

function MessageInput() {
  const [mensaje, setMensaje] = useState("")
  const [archivo, setArchivo] = useState(null)
  const [resultados, setResultados] = useState(null)
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState(null)

  const analizar = async () => {
    setCargando(true)
    setError(null)
    setResultados(null)

    try {
      const formData = new FormData()
      formData.append("mensaje", mensaje)

      if (archivo) {
        formData.append("archivo", archivo)
      }

      const res = await fetch("http://127.0.0.1:8000/analizar", {
        method: "POST",
        body: formData
      })

      const data = await res.json()

      if (data.error) {
        setError(data.error)
      } else {
        setResultados(data.resultados)
      }

    } catch {
      setError("No se pudo conectar con el servidor")
    }

    setCargando(false)
  }

  const eliminarArchivo = () => {
    setArchivo(null)
  }

  // 🔹 Separar resultados de forma segura
  const exactos = resultados?.filter(r => r.tipo_match === "exacto") || []
  const aproximados = resultados?.filter(r => r.tipo_match === "aproximado") || []

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">

      {/* TEXTO */}
      <textarea
        className="w-full border rounded-lg p-3 min-h-[120px]"
        placeholder="Ingrese el mensaje del cliente..."
        value={mensaje}
        onChange={e => setMensaje(e.target.value)}
      />

      {/* FILE UPLOAD */}
      {!archivo && (
        <FileUpload
          title="Subir archivo"
          description="PDF, TXT, CSV o Excel"
          onFileSelect={file => setArchivo(file)}
        />
      )}

      {/* ARCHIVO SELECCIONADO */}
      {archivo && (
        <div className="flex items-center justify-between bg-gray-100 p-3 rounded">
          <span className="text-sm">
            📎 <strong>{archivo.name}</strong>
          </span>

          <button
            onClick={eliminarArchivo}
            className="text-red-600 text-sm hover:underline"
          >
            Eliminar
          </button>
        </div>
      )}

      {/* BOTÓN ANALIZAR */}
      <button
        onClick={analizar}
        disabled={cargando}
        className="bg-blue-600 text-white px-6 py-2 rounded-lg disabled:opacity-50"
      >
        {cargando ? "Analizando..." : "Analizar"}
      </button>

      {/* ERROR */}
      {error && (
        <div className="bg-red-100 text-red-700 p-3 rounded">
          {error}
        </div>
      )}

      {/* RESULTADOS */}
      {resultados && (
        <div className="space-y-6">
          <h3 className="font-bold text-lg">Resultados</h3>

          {resultados.length === 0 && (
            <p className="text-green-600">
              ✅ No se detectaron reclamos
            </p>
          )}

          {/* ================= EXACTOS ================= */}
          {exactos.length > 0 && (
            <div className="space-y-3">
              <h4 className="font-semibold text-md text-blue-700">
                🔵 Patrones exactos detectados
              </h4>

              {exactos.map((r, i) => (
                <div key={i} className="border rounded p-4 bg-blue-50">
                  <p><b>Patrón:</b> {r.patron}</p>
                  <p><b>Categoría:</b> {r.categoria}</p>
                  <p><b>Alerta:</b> {r.alerta}</p>
                  <p><b>Sugerencia:</b> {r.sugerencia}</p>
                </div>
              ))}
            </div>
          )}

          {/* ================= APROXIMADOS ================= */}
          {aproximados.length > 0 && (
            <div className="space-y-3">
              <h4 className="font-semibold text-md text-orange-700">
                🟠 Posibles patrones detectados
              </h4>

              {aproximados.map((r, i) => (
                <div key={i} className="border rounded p-4 bg-orange-50">
                  <p><b>Posible patrón:</b> {r.patron}</p>
                  <p><b>Categoría:</b> {r.categoria}</p>
                  <p><b>Alerta:</b> {r.alerta}</p>
                  <p><b>Sugerencia:</b> {r.sugerencia}</p>
                  <p><b>Confianza patrón:</b> {(r.confianza_patron * 100).toFixed(2)}%</p>
                  <p><b>Confianza modelo:</b> {(r.confianza_modelo * 100).toFixed(2)}%</p>
                </div>
              ))}
            </div>
          )}

        </div>
      )}

    </div>
  )
}

export default MessageInput