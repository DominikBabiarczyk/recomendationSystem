import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface BarChartProps {
  dataPredict: number[][];
}

const BarChart: React.FC<BarChartProps> = ({ dataPredict }) => {
  const labels = dataPredict.map((item) => item[0]);
  const values = dataPredict.map((item) => item[1]);

  const data = {
    labels,
    datasets: [
      {
        label: '', // Removed 'Votes'
        data: values,
        backgroundColor: 'rgba(255, 99, 132, 0.5)', // Original color
        borderColor: 'rgba(255, 99, 132, 1)', // Original color
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Prawdopodobieństwo przewidywanej kategorii',
        color: 'rgba(255, 99, 132, 1)', // Match bar color
        font: {
          size: 24,
          weight: 'bold',
        },
      },
      legend: {
        labels: {
          color: '#FFFFFF',
          font: {
            size: 16,
          },
        },
      },
      tooltip: {
        callbacks: {
          label: function (context: any) {
            return `${context.raw}`;
          },
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Kategorie',
          color: 'rgba(255, 99, 132, 1)', // Match bar color
          font: {
            size: 18,
            weight: 'bold',
          },
        },
        ticks: {
          color: '#FFFFFF',
          font: {
            size: 14,
          },
        },
      },
      y: {
        title: {
          display: true,
          text: 'Prawdopodobieństwo',
          color: 'rgba(255, 99, 132, 1)', // Match bar color
          font: {
            size: 18,
            weight: 'bold',
          },
        },
        min: 0.0014, // Rescaled Y-axis
        max: 0.00145, // Rescaled Y-axis
        ticks: {
          color: '#FFFFFF',
          font: {
            size: 14,
          },
        },
      },
    },
  };

  return <Bar data={data} options={options} />;
};

export default BarChart;
