function FileUpload({ title, description, onFileSelect }) {

  const handleFile = (file) => {
    if (file) onFileSelect(file)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    handleFile(e.dataTransfer.files[0])
  }

  return (
    <div
      onDragOver={e => e.preventDefault()}
      onDrop={handleDrop}
      className="border-2 border-dashed border-gray-300 rounded-xl p-6 text-center bg-white hover:border-blue-400 transition cursor-pointer"
    >
      <h2 className="font-semibold text-gray-700 mb-1">
        {title}
      </h2>

      <p className="text-sm text-gray-500 mb-3">
        {description}
      </p>

      <label className="inline-block bg-blue-600 text-white px-4 py-2 rounded cursor-pointer hover:bg-blue-700">
        Seleccionar archivo
        <input
          type="file"
          accept=".pdf,.txt,.csv,.xlsx"
          hidden
          onChange={e => handleFile(e.target.files[0])}
        />
      </label>

      <p className="text-xs text-gray-400 mt-3">
        O arrastra el archivo aquí
      </p>
    </div>
  )
}

export default FileUpload
