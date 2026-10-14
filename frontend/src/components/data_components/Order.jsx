function Order({order, onClick}) {
    return (
        <div className="flex flex-row rounded-sm py-3 px-6 justify-between mb-1 shadow-md hover:-translate-y-0.5 transition-all hover:bg-gray-100 duration-100 hover:cursor-pointer" onClick={onClick}>
            <h3>{order.datum}</h3>
            <h3>€{order.totaalbedrag}</h3>
        </div>
    )
}

export default Order