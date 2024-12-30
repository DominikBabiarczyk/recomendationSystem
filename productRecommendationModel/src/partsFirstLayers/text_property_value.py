import tensorflow as tf
from typing import Tuple
from keras.src.layers import Reshape, TimeDistributed, Dense


def create_text_input() -> [tf.keras.layers.Concatenate, Tuple[tf.keras.Input, tf.keras.Input]]:

    max_length = 3  # Słowa w jednym zdaniu
    embedding_dim = 14
    history_length = 7  # Liczba przedmiotów w historii
    numeric_feature_dim = 3  # Liczba cech numerycznych na właściwość
    num_properties = 40  # Liczba właściwości

    # Dane tekstowe
    input_text = tf.keras.Input(shape=(history_length, num_properties, max_length), name="property_description")
    embedding_layer = tf.keras.layers.Embedding(input_dim=47634, output_dim=embedding_dim, input_length=max_length)(input_text)

    # Dane numeryczne
    numeric_input = tf.keras.Input(shape=(history_length, num_properties, numeric_feature_dim), name="numeric_input")
    numeric_input_reshape = Reshape((7, 40, 3, 1))(numeric_input)

    embedding_layer = TimeDistributed(Dense(14, activation='relu'))(embedding_layer)
    embedding_layer = TimeDistributed(Dense(5, activation=tf.nn.elu))(embedding_layer)

    concatenated_text_number = tf.keras.layers.Concatenate(axis=-1)([embedding_layer, numeric_input_reshape])

    return concatenated_text_number, (input_text, numeric_input)
