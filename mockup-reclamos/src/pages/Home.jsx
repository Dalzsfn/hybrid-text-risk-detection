import FileUpload from "../components/FileUpload"
import AlgorithmSelector from "../components/AlgorithmSelector"
import ResultCard from "../components/ResultCard"

function Home() {
  return (
    <main className="p-6 max-w-4xl mx-auto space-y-6">

      <FileUpload
        title="Archivo de texto"
        description="Texto base donde se realizará la búsqueda"
      />

      <FileUpload
        title="Archivo de patrones"
        description="Patrones que se desean encontrar en el texto"
      />

      <AlgorithmSelector />

      <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition">
        Ejecutar algoritmo
      </button>

      <ResultCard />
    </main>
  )
}

export default Home
