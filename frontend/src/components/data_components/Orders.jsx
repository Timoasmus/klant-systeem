import { useEffect, useState } from "react";
import api from "../../api"
import Order from "./Order";

function Orders({ activeKlant, setActiveScreen, setActiveOrder, setLoading }) {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, [activeKlant]);

  const fetchOrders = () => {
    if (activeKlant) {
      setLoading(true)
      api
        .get(`/orders/${activeKlant}`)
        .then((res) => {
          setOrders(res.data);
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
      {orders.length > 0 ? (
        orders.map((o) => (
          <Order
            key={o.nr}
            order={o}
            onClick={() => {
              setActiveScreen("orderregels");
              setActiveOrder(o.nr);
            }}
          />
        ))
      ) : (
        <h2 className="m-2">Deze klant heeft geen orders</h2>
      )}
    </div>
  );
}

export default Orders;
