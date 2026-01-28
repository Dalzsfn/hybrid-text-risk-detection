import logo from "../assets/logo.jpeg"

function Header() {
  return (
    <header className="bg-white shadow-sm px-6 py-4 flex items-center gap-4">
      
      <img
        src={logo}
        alt="Logo empresa"
        className="w-10 h-10 object-contain"
      />

      <div>
        <h1 className="text-xl font-bold text-gray-800">
          WISEcheck
        </h1>
        <p className="text-sm text-gray-500">
          Mockup – Estructuras de Datos II
        </p>
      </div>

    </header>
  )
}

export default Header
