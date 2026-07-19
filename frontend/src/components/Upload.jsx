import { useState } from "react";
import axios from "axios";

function Upload({
  documents,
  setDocuments,
  selectedDocument,
  setSelectedDocument,
}) {
  const [file, setFile] = useState(null);
  const [uploadResult, setUploadResult] = useState(null);


  const handleUpload = async () => {
    if (!file) {
        setUploadResult({
            message: "Please select a PDF first."
        });
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );
setUploadResult(response.data);

const newDocument = {
  id: response.data.document_id,
  name: response.data.filename,
};

setDocuments((prev) => [...prev, newDocument]);

// Automatically select the newly uploaded paper
setSelectedDocument(response.data.document_id);
    } catch (error) {
    console.error(error);

    setUploadResult({
        message: "Upload failed."
    });
    }
};

  return (
  <div className="max-w-4xl mx-auto mt-8 bg-white rounded-2xl shadow-lg p-8">

    <h2 className="text-3xl font-bold mb-6">
      📄 Upload Research Paper
    </h2>

    <div className="flex items-center gap-4">

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="border rounded-lg p-2 flex-1"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg transition"
      >
        Upload
      </button>

    </div>

    {file && (
      <div className="mt-5 text-gray-700">
        <strong>Selected File:</strong> {file.name}
      </div>
    )}

    {documents.length > 0 && (
        <div className="mt-6">

             <label className="block font-semibold mb-2">
                📚 Uploaded Papers
            </label>

            <select
                value={selectedDocument}
                onChange={(e) => setSelectedDocument(e.target.value)}
                className="w-full border rounded-lg p-2"
         >
        {documents.map((doc) => (
             <option
                    key={doc.id}
                    value={doc.id}
             >
                {doc.name}
            </option>
        ))}
    </select>

  </div>
)}


    {uploadResult && (
        <div className="mt-6 bg-green-50 border border-green-300 rounded-lg p-4">

            <p className="font-semibold">
                {uploadResult.message}
            </p>

            {uploadResult.filename && (
            <>
                <p>📄 File: {uploadResult.filename}</p>
                <p>🧩 Chunks: {uploadResult.total_chunks}</p>
                <p>🧠 Embedding Size: {uploadResult.embedding_dimension}</p>
            </>
            )}

        </div>
    )}

  </div>
);
}

export default Upload;