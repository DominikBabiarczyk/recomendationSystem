import numpy as np


def get_top_ten_result(prediction_set):
    prediction_set_flatten = prediction_set.flatten()

    top_indices = np.argsort(prediction_set_flatten)[-10:][::-1]

    top_values = prediction_set_flatten[top_indices]

    result = np.column_stack((top_indices, top_values))

    return result