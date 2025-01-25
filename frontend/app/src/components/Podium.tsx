import React from "react";
import BarChart from "./BarChart"


interface PodiumProps{
    predictions: number[][]
}


const Podium:React.FC <PodiumProps> = ({predictions}) => {

    return(
    

<div className="flex items-end w-[300px] h-[300px] m-[80px]">
    <div className='flex flex-col justify-center items-center text-white'>
        <div className='flex justify-center mb-2'>
            <span className="font-extrabold text-lg">{Number(predictions[1][0]).toFixed(0)}</span>
        </div>
        <div className='flex justify-center h-[170px] w-[99px] bg-gray-500 rounded-lg shadow-lg'>
            <div className="flex flex-col justify-between items-center py-2">
                <span className="text-sm">{Number(predictions[1][1]*10000).toFixed(2)}</span>
                <span className="font-extrabold text-5xl text-gray-300">2</span>
            </div>
        </div>
    </div>

    <div className='bg-gray-600 h-[170px] w-[1px] mx-2'></div>

    <div className='flex flex-col justify-center items-center text-white'>
        <div className='flex justify-center mb-2'>
            <span className="font-extrabold text-lg">{Number(predictions[0][0]).toFixed(0)}</span>
        </div>
        <div className='flex justify-center h-[250px] w-[100px] bg-yellow-500 rounded-lg shadow-lg'>
            <div className="flex flex-col justify-between items-center py-2">
                <span className="text-sm">{Number(predictions[0][1] * 10000).toFixed(2)}</span>
                <span className="font-extrabold text-5xl">1</span>
            </div>
        </div>
    </div>

    <div className='bg-gray-600 h-[120px] w-[1px] mx-2'></div>

    <div className='flex flex-col justify-center items-center text-white'>
        <div className='flex justify-center mb-2'>
            <span className="font-extrabold text-lg">{Number(predictions[2][0]).toFixed(0)}</span>
        </div>
        <div className='flex justify-center h-[120px] w-[99px] bg-amber-800 rounded-lg shadow-lg'>
            <div className="flex flex-col justify-between items-center py-2">
                <span className="text-sm">{Number(predictions[2][1] * 10000).toFixed(2)}</span>
                <span className="font-extrabold text-5xl text-gray-300">3</span>
            </div>
        </div>
    </div>
</div>




    );
};

export default Podium;