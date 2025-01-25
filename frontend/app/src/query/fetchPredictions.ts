export const fetchPredictions = async (
    mainProductsInformations: number[][],
    idVisitor: number[],
    selectedDateStates: (Date | null)[],
    ItemPropertiesState: number[][][]
): Promise<{processedData: any; predictions:number[][]}> => {
    const payload = {
        mainProductsInformations,
        idVisitor,
        selectedDateStates: selectedDateStates.map((date) =>
            date
                ? {
                      month: date.getMonth() + 1, // Miesiące są indeksowane od 0, więc dodaj 1
                      day: date.getDate(),
                      dayOfWeek: date.getDay(), // Niedziela = 0, Poniedziałek = 1, itd.
                  }
                : null
        ),
        ItemPropertiesState,
    };

    const response = await fetch('http://127.0.0.1:8000/api/get_predictions/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    });

    if (!response.ok) {
        throw new Error('Nie udało się pobrać predykcji');
    }

    return await response.json(); // Zwraca dane jako tablica liczb
};
