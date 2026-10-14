import { useEffect, useState } from "react";
import api from "../../api";
import Orderregel from "./Orderregel";

function Orderregels({ activeOrder, setLoading }) {
  const [orderregels, setOrderregels] = useState([]);

  useEffect(() => {
    fetchOrderregels()
  }, [activeOrder])

  const fetchOrderregels = () => {
    if (activeOrder) {
      setLoading(true)
      api
        .get(`/orderregels/${activeOrder}`)
        .then((res) => {
          setOrderregels(res.data);
        })
        .catch((e) => {
          alert(e);
        }).finally(() => {
          setLoading(false)
        });
    }
  };

  return (
    <div className="h-full overflow-y-auto w-full">
      {orderregels.length > 0 ? (orderregels.map((orl) => (
        <Orderregel
          key={`${orl.order_}${orl.volgnr}`}
          orderregel={orl}
        />
      ))): <h2 className="m-2">De order bevat geen orderregels</h2>}
    </div>
  );
}

export default Orderregels
