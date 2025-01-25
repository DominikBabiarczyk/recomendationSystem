import numpy as np
from .dateFormat import get_data_after_format

def get_normalized_data(visitor_id, main_product_information, item_properties, selected_data_state):
    mean_value = 136280.05817
    std_value = 712850.49643
    visitor_id_n = np.array(visitor_id, dtype='float32')

    item_id = np.zeros((1, 7), dtype='float32')
    event = np.zeros((1, 7, 3), dtype='float32')
    available = np.zeros((1, 7), dtype='float32')
    category = np.zeros((1, 7), dtype='float32')
    parent_category = np.zeros((1, 7), dtype='float32')
    hour = np.zeros(7, dtype='float32')
    minute = np.zeros(7, dtype='float32')

    for i in range(len(main_product_information)):
        item_id[0, i] = main_product_information[i][0]
        event[0, i, main_product_information[i][1]] = 1
        available[0, i] = main_product_information[i][2]
        category[0, i] = main_product_information[i][3]
        parent_category[0, i] = main_product_information[i][4]
        hour = main_product_information[i][5]
        minute = main_product_information[i][6]

    item_properties_n = np.array(item_properties, dtype=np.float64)

    properties_item = item_properties_n[:, :, 0]
    properties_item[properties_item != 0] = (properties_item[properties_item != 0] + mean_value) / std_value
    properties_item = properties_item.reshape(1, 7, 40)

    description_properties_item = np.zeros((7, 40, 3))
    description_properties_item[:, :, 0] = item_properties_n[:, :, 1]
    description_properties_item = description_properties_item.reshape(1, 7, 40, 3)

    numbers_properties_item = np.zeros((7, 40, 3))
    numbers_properties_item[:, :, 0] = item_properties_n[:, :, 2]
    numbers_properties_item = numbers_properties_item.reshape(1, 7, 40, 3)

    date_set = get_data_after_format(hour, minute, selected_data_state)

    all_data_set = [visitor_id_n, item_id, properties_item, description_properties_item, numbers_properties_item, *date_set, event, available, category, parent_category]

    return all_data_set
