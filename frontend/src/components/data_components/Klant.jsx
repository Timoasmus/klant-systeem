function Klant({ klant, onClick }) {
  return (
    <div className="border border-gray-200 flex flex-row rounded-sm py-3 px-6 justify-between mb-1 shadow-md hover:-translate-y-0.5 transition-all hover:bg-gray-100 duration-100 hover:cursor-pointer" onClick={onClick}>
      <h3>{klant.naam}</h3>
      <h3 className="text-gray-500/75">
        {klant.aanbrenger && `Aanbrenger: ${klant.aanbrenger_naam}`}
      </h3>
    </div>
  );
}

export default Klant;
