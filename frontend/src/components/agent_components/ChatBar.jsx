import { IoSend } from "react-icons/io5";
import { useState } from "react";
import api from "../../api";
import { RiResetLeftFill } from "react-icons/ri";

function ChatBar({ setMessages, loading, setLoading }) {
  const [input, setInput] = useState("");
  const [chatId, setChatId] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) {
      return;
    }

    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setInput("");
    setLoading(true);
    api
      .post("/chat", { chat_id: chatId, content: input })
      .then((res) => {
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: res.data.content },
        ]);
        if (!chatId) {
          setChatId(res.data.chat_id);
        }
      })
      .catch((e) => {
        alert(e);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const reset = () => {
    setChatId(null)
    setMessages([])
  }

  return (
    <form
      onSubmit={(e) => handleSubmit(e)}
      className="w-full border-t-2 border-gray-400 mt-auto h-20 flex items-center justify-center px-15 space-x-7"
    >
      <button onClick={() => reset()} type="button" className="text-2xl hover:cursor-pointer transition-transform"><RiResetLeftFill/></button>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Stel een vraag"
        className="rounded-md py-1 flex-1 border-2 border-gray-300 text-xl"
      />
      <button
        disabled={loading}
        type="submit"
        className="bg-blue-300 px-4 py-1.5 text-2xl text-white rounded-sm hover:cursor-pointer hover:bg-blue-200 transition-all duration-75 disabled:hover:bg-blue-300 disabled:hover:cursor-not-allowed"
      >
        <IoSend />
      </button>
    </form>
  );
}

export default ChatBar;
