import tensorflow as tf
from keras.src.layers import TimeDistributed, Reshape, Attention, Lambda
from tensorflow.keras.layers import Input, Concatenate, Dense, LSTM
from tensorflow.keras.models import Model
from partsFirstLayers.visitorid import create_visitorid_embedding
from partsFirstLayers.salesHistory import create_history_browsing_embedding
from partsFirstLayers.time import create_time_inputs
from partsFirstLayers.categoryid import create_categoryid_embedding
from partsFirstLayers.parentid import create_parentid_embedding
from partsFirstLayers.propertyItems import create_property_embedding


def create_model():
    visitor_embedding, visitor_input = create_visitorid_embedding()

    item_embedding, item_input = create_history_browsing_embedding()

    property_item_embedding, (property_category_input, input_text, numeric_input) = create_property_embedding()

    concatenated_time, time_inputs = create_time_inputs()

    event_input = Input(shape=(7, 3), name='event')
    event_layer = TimeDistributed(Dense(3, activation='relu'))(event_input)

    available = Input(shape=(7,), name='available')
    available = Reshape((7, 1))(available)
    available_layer = TimeDistributed(Dense(1, activation='relu'))(available)

    category_embedding, categoryid_input = create_categoryid_embedding()

    parentid_embedding, parentid_input = create_parentid_embedding()

    all_item_features = Concatenate()(
        [item_embedding, property_item_embedding, concatenated_time, event_layer, available_layer, category_embedding,
         parentid_embedding])

    lstm_output = LSTM(828, return_sequences=False, name="LSTM")(all_item_features)

    final_input = Concatenate()([visitor_embedding, lstm_output])

    x1 = Dense(828, use_bias=False, activation=tf.nn.elu)(final_input)
    x2 = Dense(1000, use_bias=False, activation=tf.nn.elu)(x1)
    x3 = Dense(1200, use_bias=False, activation=tf.nn.elu)(x2)
    x4 = Dense(1320, activation=tf.nn.elu)(x3)

    output = Dense(25002, activation='softmax')(x4)

    model = Model(inputs=[visitor_input, item_input, property_category_input, input_text, numeric_input, *time_inputs,
                          event_input, available, categoryid_input, parentid_input], outputs=output)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model
