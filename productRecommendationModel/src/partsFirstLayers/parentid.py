import tensorflow as tf
from typing import Tuple
from tensorflow.keras.layers import Input, Embedding, Flatten, TimeDistributed, Dense
from tensorflow import Tensor


def create_parentid_embedding() -> Tuple[Tensor, tf.keras.layers.Input]:
    parentid_input = Input(shape=(7,), name='parentid')
    embedding_dim = 4
    n_items = 242

    parentid_embedding = Embedding(input_dim=n_items, output_dim=embedding_dim)(parentid_input)
    parentid_embedding = TimeDistributed(Dense(4, activation='relu'))(parentid_embedding)
    parentid_embedding = TimeDistributed(Dense(4, activation=tf.nn.elu))(parentid_embedding)

    return parentid_embedding, parentid_input
