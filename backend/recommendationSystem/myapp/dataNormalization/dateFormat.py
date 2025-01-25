
import numpy as np
def get_data_after_format(hour, minute, date):

    month_sin = np.zeros(7, dtype='float32')
    month_cos = np.zeros(7, dtype='float32')
    day_sin = np.zeros(7, dtype='float32')
    day_cos = np.zeros(7, dtype='float32')
    day_week_sin = np.zeros(7, dtype='float32')
    day_week_cos = np.zeros(7, dtype='float32')
    hour_sin = np.zeros(7, dtype='float32')
    hour_cos = np.zeros(7, dtype='float32')
    minute_sin = np.zeros(7, dtype='float32')
    minute_cos = np.zeros(7, dtype='float32')
    second_sin = np.zeros(7, dtype='float32')
    second_cos = np.zeros(7, dtype='float32')
    for i, one_date in enumerate(date):

        if(one_date is None):
            continue

        month_sin[i] = np.cos((2 * np.pi * one_date['month']) / 12)
        month_cos[i] = np.cos((2 * np.pi * one_date['month']) / 12)
        day_sin[i] = np.sin((2 * np.pi * one_date['day'])/31)
        day_cos[i] = np.sin((2 * np.pi * one_date['day'])/31)
        day_week_sin[i] = np.cos((2 * np.pi * one_date['dayOfWeek'])/7)
        day_week_cos[i] = np.cos((2 * np.pi * one_date['dayOfWeek'])/7)
        hour_sin[i] = np.cos((2 * np.pi * hour)/24)
        hour_cos[i] = np.cos((2 * np.pi * hour)/24)
        minute_sin[i] = np.cos((2 * np.pi * minute)/60)
        minute_cos[i] = np.cos((2 * np.pi * minute)/60)

    date_set = [month_sin, month_cos, day_sin, day_cos, day_week_sin, day_week_cos, hour_sin, hour_cos, minute_sin, minute_cos, second_sin, second_cos]
    result = [data.reshape(1, 7) for data in date_set]

    return result
