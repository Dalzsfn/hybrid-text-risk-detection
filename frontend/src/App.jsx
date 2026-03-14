import { BrowserRouter, Routes, Route } from "react-router-dom"
import Header from "./components/Header"

import MessageInput from "./pages/MessageInput"
import PatternConfig from "./pages/PatternConfig"
import Stats from "./pages/Stats"

function App() {
  return (
    <BrowserRouter>
      <Header />

      <main className="p-6 max-w-4xl mx-auto">
        <Routes>
          <Route path="/" element={<MessageInput />} />
          <Route path="/patrones" element={<PatternConfig />} />
          <Route path="/estadisticas" element={<Stats />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App
