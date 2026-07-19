import { useState } from "react";
import axios from "axios";

function Chat({ selectedDocument }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    if (!question.trim()) return;

    if (!selectedDocument) {
        setAnswer("Please upload and select a research paper first.");
        return;
    }

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question: question,
          document_id: selectedDocument,
        }
      );

      setAnswer(response.data.answer);

    } catch (error) {
      console.error(error);
      setAnswer("Failed to get an answer.");
    }
  };

  return (
    <div className="max-w-4xl mx-auto mt-8 bg-white rounded-2xl shadow-lg p-8">

      <h2 className="text-3xl font-bold mb-6">
        💬 Chat with Research Paper
      </h2>

      <textarea
        rows="3"
        placeholder="Ask a question about the paper..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full border rounded-lg p-3"
      />

      <button
        onClick={askQuestion}
        className="mt-4 bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg"
      >
        Ask AI
      </button>

      {answer && (
        <div className="mt-6 bg-gray-100 rounded-lg p-4">
          <h3 className="font-bold mb-2">🤖 Answer</h3>
          <p>{answer}</p>
        </div>
      )}

    </div>
  );
}

export default Chat;