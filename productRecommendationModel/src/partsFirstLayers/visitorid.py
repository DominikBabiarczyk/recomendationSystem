from typing import Tuple
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense
from tensorflow import Tensor
import tensorflow as tf


def create_visitorid_embedding() -> Tuple[Tensor, tf.keras.layers.Input]:
    item_input = Input(shape=(1,), name='visitorid')
    embedding_dim = 7
    n_items = 2577

    item_embedding = Embedding(input_dim=n_items, output_dim=embedding_dim)(item_input)
    item_embedding = Dense(units=7, activation='relu')(item_embedding)
    item_embedding = Dense(units=7, activation=tf.nn.elu)(item_embedding)

    item_embedding = Flatten()(item_embedding)
    return item_embedding, item_input
