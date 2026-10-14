function Orderregel({orderregel, onClick}) {
    return (
        <div className="flex flex-row rounded-sm py-3 px-6 justify-between mb-1 shadow-md">
            <h3>{orderregel.artikel_omschrijving}</h3>
            <div className="flex space-x-4">
            <h3>{orderregel.aantal}x</h3>
            <h3>€{orderregel.bedrag}</h3>
            </div>
        </div>
    )
}

export default Orderregel