import numpy as np


def get_completed_data(vector, required_shape):
    current_shape = vector.shape[-1]
    padding_needed = max(0, required_shape - current_shape)
    pad_data = np.pad(vector, (0, padding_needed), 'constant', constant_values=0)

    return pad_data
