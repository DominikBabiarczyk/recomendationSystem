import React from "react";
import BarChart from "./BarChart"


interface PodiumTablePredicitons{
    predictions: number[][]
}


const TablePredicitons:React.FC <PodiumTablePredicitons> = ({predictions}) => {

    return(
<div className="w-full overflow-x-auto my-10">
    <table className="table-auto border-collapse mx-auto shadow-md rounded-xl overflow-hidden">
        <thead>
            <tr className="bg-gray-800 text-white">
                <th className="px-6 py-3 text-center text-sm font-semibold">ID Produktu</th>
                {predictions.map((element, i) => (
                    <th key={i} className="px-6 py-3 text-center text-sm font-semibold">
                        {Number(element[0]).toFixed(0)}
                    </th>
                ))}
            </tr>
        </thead>
        <tbody>
            <tr className="odd:bg-gray-700 even:bg-gray-600 text-white">
                <td className="px-6 py-3 text-center text-sm font-medium">Wynik Przewidywania</td>
                {predictions.map((element, i) => (
                    <td key={i} className="px-6 py-3 text-center text-sm">
                        {Number(element[1] * 10000).toFixed(2)}
                    </td>
                ))}
            </tr>
        </tbody>
    </table>
</div>

    );
};

export default TablePredicitons;