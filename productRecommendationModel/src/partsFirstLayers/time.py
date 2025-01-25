from keras.src.layers import Reshape
from tensorflow.keras.layers import Input, Flatten, Concatenate


def create_time_inputs():
    time_pairs = [('month_cos', 'month_sin'), ('day_cos', 'day_sin'),
                  ('day_of_week_cos', 'day_of_week_sin'), ('hour_cos', 'hour_sin'),
                  ('minute_cos', 'minute_sin'), ('second_cos', 'second_sin')]
    time_inputs = []
    concatenated_pairs = []

    for cos_feature, sin_feature in time_pairs:
        cos_input = Input(shape=(7,), name=f'{cos_feature}')
        sin_input = Input(shape=(7,), name=f'{sin_feature}')
        time_inputs.extend([cos_input, sin_input])

        cos_input = Reshape((7, 1))(cos_input)  # Kształt (7, 1)
        sin_input = Reshape((7, 1))(sin_input)

        concatenated_pair = Concatenate(axis=-1)([cos_input, sin_input])

        concatenated_pairs.append(concatenated_pair)

    concatenated_time_inputs = Concatenate()(concatenated_pairs)

    return concatenated_time_inputs, time_inputs
