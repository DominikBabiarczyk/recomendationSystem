import React, { useState } from "react";

interface TablePredicitonsProps{
    rows: number[][];
    setRows: React.Dispatch<React.SetStateAction<number[][]>>;
}

const TablePredicitons: React.FC<TablePredicitonsProps> = ({rows, setRows}) => {
    const columnLimits = [1105, 47634, 1000000];

    const updateCell = (rowIndex: number, colIndex: number, value: string) => {
        if (setRows !== null && rows !== null){
            let numericValue = Math.max(0, Number(value)); // Nie pozwalamy na wartości ujemne
            numericValue = Math.min(numericValue, columnLimits[colIndex]); 
            const updatedRows = rows.map((row, rIdx) =>
                rIdx === rowIndex
                    ? row.map((cell, cIdx) => (cIdx === colIndex ? numericValue : cell))
                    : row
            );
            setRows(updatedRows);
        }
    };
    
    return(
<div className="p-4 max-h-[760px] overflow-y-auto border border-gray-800 rounded-lg bg-gray-800 shadow-md">
  <table className="table-fixed border-collapse w-full text-center rounded-xl overflow-hidden">
    <thead>
      <tr className="bg-gray-600">
        <th className="px-4 py-2 text-gray-200 text-sm font-semibold w-[50px]">Lp</th>
        <th className="px-4 py-2 text-gray-200 text-sm font-semibold">Kategoria</th>
        <th className="px-4 py-2 text-gray-200 text-sm font-semibold">Opis</th>
        <th className="px-4 py-2 text-gray-200 text-sm font-semibold">Wartość</th>
      </tr>
    </thead>
    <tbody>
      {rows.map((row, rowIndex) => (
        <tr
          key={rowIndex}
          className={`${
            rowIndex % 2 === 0 ? "bg-gray-800" : "bg-gray-800"
          } hover:bg-gray-600`}
        >
          <td className="px-4 py-2 text-gray-300 w-max-[10px] font-medium w-[50px]">{rowIndex + 1}</td>
          {row.map((cell, colIndex) => (
            <td key={colIndex} className="px-4 py-2 text-gray-300">
              <input
                type="number"
                value={cell}
                onChange={(e) => updateCell(rowIndex, colIndex, e.target.value)}
                className=" w-[150px] px-2 py-1 bg-white text-gray-900 text-center rounded focus:ring focus:ring-gray-500"
              />
            </td>
          ))}
        </tr>
      ))}
    </tbody>
  </table>
</div>

      

    );
}

export default TablePredicitons;