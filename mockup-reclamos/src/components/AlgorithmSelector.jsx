function AlgorithmSelector() {
  return (
    <div>
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Algoritmo de Pattern Matching
      </label>
      <select className="w-full border border-gray-300 rounded-lg px-3 py-2">
        <option>Fuerza Bruta</option>
        <option>KMP</option>
        <option>Boyer-Moore</option>
      </select>
    </div>
  )
}

export default AlgorithmSelector
