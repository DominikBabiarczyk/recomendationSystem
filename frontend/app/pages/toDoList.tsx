"use client";
import React, { useState } from 'react';
import BarChart from '../src/components/BarChart';
import Podium from '../src/components/Podium';
import TablePredicitons from '../src/components/TablePredictions';
import EditableTable from '../src/components/EditableTable';
import { fetchPredictions } from '../src/query/fetchPredictions';
import TableProperties from '../src/modal/ModalView';

const createRowProperties = () =>
    Array.from({ length: 40 }, () => Array(3).fill(0));

const PredictionsPage: React.FC = () => {
    const [predictions, setPredictions] = useState<number[][]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [itemPositionInHistory, setitemPositionInHistory] = useState<number | null>(null);
    const [mainProductsInformations, setmainProductsInformations] = useState<number[][]>([[...Array(7).fill(0)]]);
    const [idVisitor, setIdVisitor] = useState<number[]>([...Array(1).fill(0)])
    const selectedDateStates = [
        useState<Date | null>(null),
        useState<Date | null>(null),
        useState<Date | null>(null),
        useState<Date | null>(null),
        useState<Date | null>(null),
        useState<Date | null>(null),
        useState<Date | null>(null),
    ];
    
    const selectedDateState: [Date | null, React.Dispatch<React.SetStateAction<Date | null>>] =
        itemPositionInHistory !== null
            ? selectedDateStates[itemPositionInHistory]
            : selectedDateStates[0];
    
    const selectedDateValue = selectedDateState[0];
    const setSelectedDateValue = selectedDateState[1];
    

    const ItemPropertiesState = [
        useState(createRowProperties()),
        useState(createRowProperties()),
        useState(createRowProperties()),
        useState(createRowProperties()),
        useState(createRowProperties()),
        useState(createRowProperties()),
        useState(createRowProperties()),
    ];

    const selectedState:
    [number[][], React.Dispatch<React.SetStateAction<number[][]>>] =
    itemPositionInHistory !== null
        ? ItemPropertiesState[itemPositionInHistory]
        : ItemPropertiesState[0];

    const selectedmainProductsInformationsProperties = selectedState[0] ;
    const setSelectedmainProductsInformationsProperties = selectedState[1] ;

    const getPredictions = async () => {
        setLoading(true);
        setError(null);
    
        try {
            // Przygotowanie danych
            const selectedDates = selectedDateStates.map(([date]) => date);
            const itemProperties = ItemPropertiesState.map(([rows]) => rows);
    
            // Wywołanie API
            const data = await fetchPredictions(
                mainProductsInformations,
                idVisitor,
                selectedDates,
                itemProperties
            );
    
            // Aktualizacja stanu z odpowiedzią
            setPredictions(data.predictions);
        } catch (error: any) {
            setError(error.message || 'Wystąpił błąd');
        } finally {
            setLoading(false);
        }
    };
    

    if (error) {
        return <div>Błąd: {error}</div>;
    }

    return (
        <div className="flex flex-col w-full h-full items-center">
            <div>
                <EditableTable setIsModalForItem={setitemPositionInHistory} rows={mainProductsInformations} setRows={setmainProductsInformations} idVisitor={idVisitor} setIdVisitor={setIdVisitor} selectedDate={selectedDateValue} setSelectedDate={setSelectedDateValue}/>
            </div>

            <div
                onClick={getPredictions}
                className="flex w-fit border-2 bg-gray-700 hover:bg-gray-600 rounded-xl hover:cursor-pointer"
            >   
                <p className="flex font-bold m-5">Daj predykcję</p>
            </div>

            {/* <TablePredicitons predictions={predictions} /> */}

            {predictions.length > 0 && (
                <>
                    <TablePredicitons predictions={predictions} />

                    <div className="flex justify-between max-w-[1600px] items-center rounded-xl bg-gray-700 p-4 w-full">
                        <Podium predictions={predictions} />
                        <div className="flex  w-[950px] h-[450px]">
                            <BarChart dataPredict={predictions} />
                        </div>
                    </div>
                </>
            )}

            {itemPositionInHistory !== null && (<TableProperties setIsModalOpen={setitemPositionInHistory} rows={selectedmainProductsInformationsProperties} setRows={setSelectedmainProductsInformationsProperties}></TableProperties>)}
        </div>
    );
};

export default PredictionsPage;
