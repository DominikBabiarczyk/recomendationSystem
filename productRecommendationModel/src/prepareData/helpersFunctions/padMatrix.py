import numpy as np


def get_completed_matrix(matrix: np.ndarray, required_shape_y: int, shape_matrix=(0, 0)) -> np.ndarray:

    if matrix.size == 0:
        shape_y = shape_matrix[0]
        shape_x = shape_matrix[1]
        matrix = np.zeros((shape_y, shape_x))
    else:
        shape_y = matrix.shape[0]
        shape_x = matrix.shape[1]

    padding_needed = max(0, required_shape_y - shape_y)
    for i in range(padding_needed):
        new_vector = np.zeros(shape_x)
        matrix = np.vstack((matrix, new_vector))

    return matrix
