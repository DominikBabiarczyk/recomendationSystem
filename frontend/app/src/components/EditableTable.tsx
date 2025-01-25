import React, { useState, useRef, useEffect } from 'react';
import { DateRangePicker, RangeKeyDict } from "react-date-range";
import "react-date-range/dist/styles.css"; // style for the calendar
import "react-date-range/dist/theme/default.css"; // theme css


interface EditableTableProps{
    setIsModalForItem: React.Dispatch<React.SetStateAction<number | null>>
    rows: number[][]
    setRows: React.Dispatch<React.SetStateAction<number[][]>>
    idVisitor: number[]
    setIdVisitor: React.Dispatch<React.SetStateAction<number[]>>
    selectedDate: Date | null;
    setSelectedDate: React.Dispatch<React.SetStateAction<Date | null>>
}

const EditableTable: React.FC<EditableTableProps> = ({setIsModalForItem, rows, setRows, idVisitor, setIdVisitor, selectedDate, setSelectedDate}) => {
    const columnLimits = [25002, 2, 1, 803, 241, 23, 59];
    const nameParameters = ["przedmiot", "zdarzenie", "dostępność", "kategoria", "pokrewna kategoria", "godzina", "minuta"]
    const namesButtons = ["Data", "Właściwość"]
    const [isCalendaryVisible, setIsCalendaryVisible] = useState<boolean>(false);
    const calendarRef = useRef<HTMLDivElement>(null); 

    const addRow = () => {
        if(rows.length < 7){
            setRows([...rows, Array(7).fill(0)]);
        }
    };

    const handleDateSelect = (ranges: any) => {
      
      setSelectedDate(ranges.selection.startDate);
    };

    const deleteRow = (rowIndex: number) => {
        const updatedRows = rows.filter((_, index) => index !== rowIndex);
        setRows(updatedRows);
    };

    const updateVisitorId = (value: string) => {
        let numericValue = Math.max(0, Number(value));
        numericValue = Math.min(numericValue, 2577);
        setIdVisitor([numericValue])
    }

    const updateCell = (rowIndex: number, colIndex: number, value: string) => {
        let numericValue = Math.max(0, Number(value)); // Usuwamy wartości ujemne
        numericValue = Math.min(numericValue, columnLimits[colIndex]); 
        const updatedRows = rows.map((row, rIdx) =>
            rIdx === rowIndex
                ? row.map((cell, cIdx) => (cIdx === colIndex ? numericValue : cell))
                : row
        );
        setRows(updatedRows);
    };

    const onClickButtonAdditions = (name: String, rowIndex: number) => {
        if(name == "Właściwość"){
            setIsModalForItem(rowIndex);
        }else if(name == "Data"){
            setIsCalendaryVisible(true);
        }
    }

    const handleOutsideClick = (event: MouseEvent) => {
        if (calendarRef.current && !calendarRef.current.contains(event.target as Node)) {
            setIsCalendaryVisible(false); // Zamknij kalendarz
        }
    };

    useEffect(() => {
        if (isCalendaryVisible) {
            document.addEventListener("mousedown", handleOutsideClick);
        } else {
            document.removeEventListener("mousedown", handleOutsideClick);
        }
        return () => {
            document.removeEventListener("mousedown", handleOutsideClick);
        };
    }, [isCalendaryVisible]);

    return (
<div className="p-4">
  <div className="flex flex-col space-y-4">
    {/* Table for Visitor ID */}
    <table className="table-auto border-collapse w-fit mx-auto text-center text-white">
      <thead>
        <tr>
          <th className="px-4 py-2 text-lg font-bold text-neutral-700">
            Id Odwiedzającego
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td className="px-4 py-2">
            <input
              type="number"
              value={idVisitor[0]}
              onChange={(e) => updateVisitorId(e.target.value)}
              className="w-full px-2 py-1 text-black text-center border rounded"
            />
          </td>
        </tr>
      </tbody>
    </table>

    {/* Main Data Table */}
    <table className="table-auto border-collapse w-full text-center text-white">
      <thead>
        <tr>
          <th className="px-4 py-2 text-lg font-bold text-gray-600">Lp</th>
          {Array.from({ length: 7 }, (_, i) => (
            <th key={i} className="px-4 py-2 text-lg font-bold text-gray-600">
              {nameParameters[i]}
            </th>
          ))}
          {namesButtons.map((name, index) => (
            <th key={index} className="px-4 py-2 text-lg font-bold text-gray-600">
              {name}
            </th>
          ))}
          <th className="px-4 py-2 text-lg font-bold text-gray-600">Akcje</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((row, rowIndex) => (
          <tr key={rowIndex} className="hover:bg-gray-800">
            <td className="px-4 py-2 font-bold">{rowIndex + 1}</td>
            {row.map((cell, colIndex) => (
              <td key={colIndex} className="px-4 py-2">
                <input
                  type="number"
                  value={cell}
                  onChange={(e) => updateCell(rowIndex, colIndex, e.target.value)}
                  className="w-full px-2 py-1 text-black text-center border rounded"
                />
              </td>
            ))}
            {namesButtons.map((elem, buttonIndex) => (
              <td key={buttonIndex} className="px-4 py-2">
                <button
                  onClick={() => onClickButtonAdditions(elem, rowIndex)}
                  className="bg-gray-700 hover:bg-gray-600 text-white font-bold py-1 px-3 rounded"
                >
                  Wprowadź
                </button>
              </td>
            ))}
            <td className="px-4 py-2">
              <button
                onClick={() => deleteRow(rowIndex)}
                className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded"
              >
                Usuń
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>

  {/* Date Picker */}
  {isCalendaryVisible && (
    <div ref={calendarRef} className="fixed z-10 ml-[1250px] border-primary-500">
      <style jsx global>{`
        .rdrDefinedRangesWrapper,
        .rdrDateRangePickerWrapper .rdrInputRanges {
          display: none !important;
        }
      `}</style>
      <DateRangePicker
        ranges={[
          {
            startDate: selectedDate || new Date(),
            endDate: selectedDate || new Date(),
            key: "selection",
          },
        ]}
        onChange={handleDateSelect}
        months={1}
        direction="horizontal"
        showMonthAndYearPickers
        moveRangeOnFirstSelection={false}
        staticRanges={[]}
        rangeColors={["#85878B"]}
      />
    </div>
  )}

  {/* Add Row Button */}
  <button
    onClick={addRow}
    className="mt-4 bg-gray-700 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded"
  >
    Dodaj Wiersz
  </button>
</div>


    );
};

export default EditableTable;
