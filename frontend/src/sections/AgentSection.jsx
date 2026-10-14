import ChatBar from "../components/agent_components/ChatBar";
import TextBubble from "../components/agent_components/TextBubble";
import { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import { LuBotMessageSquare } from "react-icons/lu";

function AgentSection() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth",
  });
}, [messages])

  return (
    <section className="w-1/2 h-full flex flex-col relative">
      <div className="flex-1 min-h-0 overflow-y-auto p-10 ">
        <div className="min-h-full flex flex-col justify-end ">
          {messages.map((m, i) =>
            m.role === "user" ? (
              <TextBubble key={i} text={m.content} />
            ) : (
              <div key={i} className="text-xl mt-5 w-2/3">
                <ReactMarkdown>{m.content}</ReactMarkdown>
              </div>
            ),
          )}
         <div ref={messagesEndRef} />
        </div>
        
      </div>

    {loading && (
        <LuBotMessageSquare
          className="text-7xl text-blue-300 animate-bounce absolute bottom-24 left-10"
        />
      )}
      <ChatBar loading={loading} setLoading={setLoading} setMessages={setMessages} />
    </section>
  );
}

export default AgentSection;
