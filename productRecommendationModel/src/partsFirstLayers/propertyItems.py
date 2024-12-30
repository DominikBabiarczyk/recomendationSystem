from typing import Tuple
from keras.src.layers import Reshape, TimeDistributed
from tensorflow.keras.layers import Embedding, Dense, LSTM, Input
from tensorflow import Tensor
import tensorflow as tf
from partsFirstLayers.text_property_value import create_text_input


def create_property_embedding() -> Tuple[Tensor, Tuple[Input, Input, Input]]:
    max_properties = 40
    property_embedding_dim = 6
    history_length = 7
    num_property_categories = 1105

    property_category_input = Input(shape=(history_length, max_properties), name='property_category_history')

    property_category_embedding = Embedding(input_dim=num_property_categories, output_dim=property_embedding_dim)(
        property_category_input)
    property_category_embedding = TimeDistributed(Dense(6, activation='relu'))(property_category_embedding)
    property_category_embedding = TimeDistributed(Dense(5, activation=tf.nn.elu))(property_category_embedding)

    concatenated_text_number, (input_text, numeric_input) = create_text_input()

    concatenated_text_number = Reshape((7, 40, 18))(concatenated_text_number)

    property_representation = tf.keras.layers.Concatenate(axis=-1)(
        [property_category_embedding, concatenated_text_number])

    property_flattened = Reshape((7, 920))(property_representation)
    property_flattened = TimeDistributed(Dense(920, activation='relu'))(property_flattened)
    property_flattened = TimeDistributed(Dense(320, activation=tf.nn.elu))(property_flattened)

    return property_flattened, (property_category_input, input_text, numeric_input)
