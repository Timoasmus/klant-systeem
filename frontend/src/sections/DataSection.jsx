import { useState } from "react";
import Klanten from "../components/data_components/Klanten";
import Orders from "../components/data_components/Orders";
import Orderregels from "../components/data_components/Orderregels";
import { IoIosArrowBack } from "react-icons/io";
import Loader from "../components/Loader";

function DataSection() {
  const [activeScreen, setActiveScreen] = useState("klanten");
  const [activeKlant, setActiveKlant] = useState();
  const [activeOrder, setActiveOrder] = useState();
  const [loading, setLoading] = useState(false);

  const screens = {
    klanten: (
      <Klanten
        setActiveScreen={setActiveScreen}
        setActiveKlant={setActiveKlant}
        setLoading={setLoading}
      />
    ),
    orders: (
      <Orders
        setActiveScreen={setActiveScreen}
        activeKlant={activeKlant}
        setActiveOrder={setActiveOrder}
        setLoading={setLoading}
      />
    ),
    orderregels: (
      <Orderregels 
        activeOrder={activeOrder}
        setLoading={setLoading} 
      />
    )
  };

  return (
    <section className="w-1/2 border-r-2 border-r-gray-300 flex flex-col">
      <nav className="h-15 w-full flex items-center px-3 space-x-5 shadow-sm">
        {activeScreen !== "klanten" && (
          <button
            className="bg-blue-300 px-4 py-1.5 text-2xl text-white rounded-sm hover:cursor-pointer hover:bg-blue-200 transition-all duration-75"
            onClick={() => {
              setActiveScreen((current) =>
                current === "orders" ? "klanten" : "orders",
              );
            }}
          >
            <IoIosArrowBack />
          </button>
        )}
        <h2 className="text-xl">{activeScreen}</h2>
      </nav>
     {loading ? (<div className="flex flex-1 items-center justify-center">
    <Loader />
  </div>) : screens[activeScreen]}
    </section>
  );
}

export default DataSection;
