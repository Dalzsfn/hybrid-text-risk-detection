function FileUpload({ title, description }) {
  return (
    <div className="border-2 border-dashed border-gray-300 rounded-xl p-6 text-center bg-white">
      <h2 className="font-semibold text-gray-700 mb-1">
        {title}
      </h2>
      <p className="text-sm text-gray-500 mb-3">
        {description}
      </p>
      <div className="text-gray-400 text-sm">
        Arrastra el archivo aquí o haz clic para seleccionar
      </div>
    </div>
  )
}

export default FileUpload
