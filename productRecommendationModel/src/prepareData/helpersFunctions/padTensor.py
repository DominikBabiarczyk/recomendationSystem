import numpy as np


def get_completed_tensor(matrix: np.ndarray, required_shape_z: int) -> np.ndarray:
    shape_z = matrix.shape[0]
    shape_y = matrix.shape[1]
    shape_x = matrix.shape[2]

    padding_needed = max(0, required_shape_z - shape_z)
    for i in range(padding_needed):
        zeros_matrix = np.zeros((1, shape_y, shape_x))
        matrix = np.concatenate((matrix, zeros_matrix), axis=0)

    return matrix