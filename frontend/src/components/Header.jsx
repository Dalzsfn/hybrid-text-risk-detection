import logo from "../assets/veritas.png"
import Navigation from "./Navigation"

function Header() {
  return (
    <header className="bg-white shadow-sm px-6 py-4">
      <div className="flex items-center gap-4">
        <img
          src={logo}
          alt="Logo empresa"
          className="w-10 h-10 object-contain"
        />

        <div>
          <h1 className="text-xl font-bold text-gray-800">
            Veritas
          </h1>
          <p className="text-sm text-gray-500">
          </p>
        </div>
      </div>

      {/* Menú de navegación */}
      <div className="mt-4">
        <Navigation />
      </div>
    </header>
  )
}

export default Header
