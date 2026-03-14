import { Link } from "react-router-dom"

function Navigation() {
  return (
    <nav className="flex gap-4 mt-2 text-sm">
      <Link to="/" className="hover:underline">Ingreso</Link>
      <Link to="/patrones" className="hover:underline">Patrones</Link>
      <Link to="/estadisticas" className="hover:underline">Estadísticas</Link>
    </nav>
  )
}

export default Navigation
