import { useState } from "react";

import Header from "./components/Header";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {

  const [documents, setDocuments] = useState([]);
  const [selectedDocument, setSelectedDocument] = useState("");

  return (
    <div className="min-h-screen bg-gray-100">

      <Header />

      <Upload
        documents={documents}
        setDocuments={setDocuments}
        selectedDocument={selectedDocument}
        setSelectedDocument={setSelectedDocument}
      />

      <Chat
        selectedDocument={selectedDocument}
      />

    </div>
  );
}

export default App;