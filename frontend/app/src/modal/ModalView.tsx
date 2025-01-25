import React from "react";
import TablePropperties from "./TableProperties"

interface EditableTableProps{
    setIsModalOpen: React.Dispatch<React.SetStateAction<number | null>>;
    rows: number[][];
    setRows: React.Dispatch<React.SetStateAction<number[][]>>;
}

const TableProperties:React.FC<EditableTableProps> = ({setIsModalOpen, rows, setRows}) => {
    return(
        <div>
            <div className="fixed inset-0 bg-zinc-800 bg-opacity-75 flex justify-center items-center z-50">
                <div className="bg-gray-800 w-[40%] h-[75%] rounded-lg shadow-lg p-6">
                    <div className="flex justify-between h-fit py-3">
                        <h2 className="text-xl font-bold mb-4">Właściwości danego przedmiotu</h2>
                        
                        <button
                            onClick={() => setIsModalOpen(null)}
                            className=" bg-red-500 w-fit h-fit text-white px-4 py-2 rounded hover:bg-red-600"
                        >
                            Zamknij
                        </button>
                    </div>

                    <div>
                        <TablePropperties rows={rows} setRows={setRows}></TablePropperties>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default TableProperties;