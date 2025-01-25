from typing import Tuple
from keras.src.layers import TimeDistributed
from tensorflow.keras.layers import Input, Embedding, Dense
from tensorflow import Tensor
import tensorflow as tf


def create_categoryid_embedding() -> Tuple[Tensor, tf.keras.layers.Input]:
    categoryid_input = Input(shape=(7,), name='categoryid')
    embedding_dim = 10
    n_items = 803

    item_embedding = Embedding(input_dim=n_items, output_dim=embedding_dim)(categoryid_input)
    item_embedding = TimeDistributed(Dense(10, activation='relu'))(item_embedding)
    item_embedding = TimeDistributed(Dense(5, activation=tf.nn.elu))(item_embedding)

    return item_embedding, categoryid_input
