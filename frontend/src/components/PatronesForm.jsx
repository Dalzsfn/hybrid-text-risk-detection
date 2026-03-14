import { useState } from "react"

function PatronesForm() {
  const [patron, setPatron] = useState("")
  const [categoria, setCategoria] = useState("Reclamo")
  const [alerta, setAlerta] = useState("Bajo")
  const [sugerencia, setSugerencia] = useState("")
  const [msg, setMsg] = useState("")

  const guardar = async () => {
    const res = await fetch("http://127.0.0.1:8000/patrones", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        patron,
        categoria,
        alerta,
        sugerencia
      })
    })

    if (res.ok) {
      setMsg("Patrón guardado correctamente")
      setPatron("")
      setSugerencia("")
    } else {
      setMsg("Error al guardar patrón")
    }
  }

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h2 className="text-xl font-bold mb-4">Agregar patrón</h2>

      <input
        className="w-full border p-2 mb-3"
        placeholder="Patrón a detectar"
        value={patron}
        onChange={e => setPatron(e.target.value)}
      />

      <select
        className="w-full border p-2 mb-3"
        value={categoria}
        onChange={e => setCategoria(e.target.value)}
      >
        <option>Reclamo crítico</option>
        <option>Riesgo legal</option>
        <option>Reclamo</option>
        <option>Queja leve</option>
      </select>

      <select
        className="w-full border p-2 mb-3"
        value={alerta}
        onChange={e => setAlerta(e.target.value)}
      >
        <option>Crítico</option>
        <option>Alto</option>
        <option>Medio</option>
        <option>Bajo</option>
      </select>

      <textarea
        className="w-full border p-2 mb-3"
        placeholder="Sugerencia para este patrón"
        value={sugerencia}
        onChange={e => setSugerencia(e.target.value)}
      />

      <button
        onClick={guardar}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Guardar patrón
      </button>

      {msg && <p className="mt-3">{msg}</p>}
    </div>
  )
}

export default PatronesForm
