from tensorflow.keras.layers import Input, Embedding, Flatten
from tensorflow import Tensor
import tensorflow as tf
from typing import Tuple
from tensorflow.keras.layers import Input, TimeDistributed, Dense


def create_history_browsing_embedding() -> Tuple[Tensor, tf.keras.layers.Input]:
    embedding_dim = 13
    n_items = 25002
    history_length = 7

    item_input = Input(shape=(history_length,), name='itemid_history')

    item_embedding = Embedding(input_dim=n_items, output_dim=embedding_dim)(item_input)
    item_embedding = TimeDistributed(Dense(13, activation='relu'))(item_embedding)
    item_embedding = TimeDistributed(Dense(10, activation=tf.nn.elu))(item_embedding)

    return item_embedding, item_input
