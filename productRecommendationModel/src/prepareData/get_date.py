from typing import List

import numpy as np

from prepareData.helpersFunctions.padVector import get_completed_data


def get_date(df_browsing: np.array) -> List:
    date_list = []
    all_data = ["month_cos", "month_sin", "day_cos", "day_sin", "day_of_week_cos", "day_of_week_sin", "hour_cos",
                "hour_sin", "minute_cos", "minute_sin", "second_sin", "second_cos"]
    for data in all_data:
        normalized_data = df_browsing[data].to_numpy()
        normalized_data = get_completed_data(normalized_data, 7)
        date_list.append(normalized_data)

    return date_list
