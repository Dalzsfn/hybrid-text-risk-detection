import { useEffect, useState } from "react"

function Stats() {
  const [stats, setStats] = useState(null)
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const cargarEstadisticas = () => {
    setLoading(true)

    fetch("http://127.0.0.1:8000/estadisticas")
      .then(res => {
        if (!res.ok) throw new Error("Error al cargar estadísticas")
        return res.json()
      })
      .then(data => {
        setStats(data)
        setError(null)
      })
      .catch(err => {
        console.error(err)
        setError("No se pudieron cargar las estadísticas")
      })
      .finally(() => {
        setLoading(false)
      })
  }

  const resetEstadisticas = () => {
    const confirmar = window.confirm(
      "¿Estás seguro de que deseas reiniciar todas las estadísticas?"
    )

    if (!confirmar) return

    fetch("http://127.0.0.1:8000/estadisticas/reset", {
      method: "POST"
    })
      .then(res => {
        if (!res.ok) throw new Error("Error al reiniciar estadísticas")
        return res.json()
      })
      .then(() => {
        setStats({
          total_analisis: 0,
          tiempos_promedio_ns: {
            kmp: 0,
            boyer_moore: 0
          },
          conteo_categorias: {},
          historial_ejecuciones: []
        })
        setError(null)
      })
      .catch(err => {
        console.error(err)
        setError("No se pudieron reiniciar las estadísticas")
      })
  }

  useEffect(() => {
    cargarEstadisticas()
  }, [])

  if (loading && !stats) {
    return <p className="text-gray-500">Cargando estadísticas...</p>
  }

  if (error) {
    return <p className="text-red-500">{error}</p>
  }

  if (!stats) {
    return null
  }

  return (
    <div className="space-y-6">
      {/* HEADER */}
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold">Estadísticas del sistema</h2>

        <button
          onClick={resetEstadisticas}
          className="px-4 py-2 text-sm bg-red-600 text-white rounded hover:bg-red-700"
        >
          Resetear estadísticas
        </button>
      </div>

      {/* TOTAL */}
      <div className="p-4 border rounded">
        <p>
          Total de análisis realizados:{" "}
          <strong>{stats.total_analisis}</strong>
        </p>
      </div>

      {/* TIEMPOS PROMEDIO */}
      <div className="p-4 border rounded">
        <h3 className="font-medium mb-2">
          Tiempo promedio de ejecución (ns)
        </h3>
        <p>
          KMP: <strong>{stats.tiempos_promedio_ns.kmp}</strong>
        </p>
        <p>
          Boyer–Moore:{" "}
          <strong>{stats.tiempos_promedio_ns.boyer_moore}</strong>
        </p>
      </div>

      {/* HISTORIAL DE EJECUCIONES */}
      <div className="p-4 border rounded">
        <h3 className="font-medium mb-2">
          Historial de tiempos por análisis (ns)
        </h3>

        {stats.historial_ejecuciones.length === 0 ? (
          <p className="text-gray-500">No hay ejecuciones registradas</p>
        ) : (
          <table className="w-full text-sm border-collapse">
            <thead>
              <tr className="border-b">
                <th className="text-left p-2">#</th>
                <th className="text-left p-2">KMP (ns)</th>
                <th className="text-left p-2">Boyer–Moore (ns)</th>
              </tr>
            </thead>
            <tbody>
              {stats.historial_ejecuciones.map((e, index) => (
                <tr key={index} className="border-b">
                  <td className="p-2">{index + 1}</td>
                  <td className="p-2">{e.kmp}</td>
                  <td className="p-2">{e.boyer_moore}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* CATEGORÍAS */}
      <div className="p-4 border rounded">
        <h3 className="font-medium mb-2">Reclamos por categoría</h3>

        {Object.keys(stats.conteo_categorias).length === 0 ? (
          <p className="text-gray-500">No hay reclamos detectados</p>
        ) : (
          <ul className="list-disc ml-6">
            {Object.entries(stats.conteo_categorias).map(
              ([categoria, cantidad]) => (
                <li key={categoria}>
                  {categoria}: <strong>{cantidad}</strong>
                </li>
              )
            )}
          </ul>
        )}
      </div>
    </div>
  )
}

export default Stats
