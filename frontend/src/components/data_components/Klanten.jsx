import { useEffect, useState } from "react";
import api from "../../api";
import Klant from "./Klant";

function Klanten({setActiveScreen, setActiveKlant, setLoading}) {
  const [klanten, setKlanten] = useState([])

  useEffect(() => {
    fetchKlanten()
  }, [])

  const fetchKlanten = () => {
    setLoading(true)
    api
      .get("/klanten")
      .then((res) => {
        setKlanten(res.data)
      })
      .catch((e) => {
        alert(`Er ging iets fout: ${e}`)
      }).finally(() => {
        setLoading(false)
      });
  };

  return <div className="h-full overflow-y-auto w-full">
    {klanten.length > 0 ? (klanten.map((k) => (
        <Klant
          key={k.nr}
          klant={k}
          onClick={() => {
            setActiveScreen("orders")
            setActiveKlant(k.nr)
          }}
        />
    ))): <h2 className="m-2">Nog geen klanten in het systeem</h2>}
  </div>;
}

export default Klanten;
