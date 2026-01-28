import { useState } from "react"

function MessageInput() {
  const [mensaje, setMensaje] = useState("")
  const [resultados, setResultados] = useState(null)

  const analizar = async () => {
    const res = await fetch("http://127.0.0.1:8000/analizar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensaje })
    })

    const data = await res.json()
    setResultados(data.resultados)
  }

  return (
    <div className="p-6">
      <textarea
        className="w-full border p-3"
        placeholder="Ingrese el mensaje del cliente"
        value={mensaje}
        onChange={e => setMensaje(e.target.value)}
      />

      <button
        onClick={analizar}
        className="mt-4 bg-blue-600 text-white px-4 py-2 rounded"
      >
        Analizar
      </button>

      {resultados && (
        <div className="mt-6">
          <h3 className="font-bold">Resultados</h3>
          {resultados.length === 0 && <p>Sin reclamos</p>}

          {resultados.map((r, i) => (
            <div key={i} className="border p-3 mt-2">
              <p><b>Patrón:</b> {r.patron}</p>
              <p><b>Categoría:</b> {r.categoria}</p>
              <p><b>Alerta:</b> {r.alerta}</p>
              <p><b>Sugerencia:</b> {r.sugerencia}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default MessageInput
