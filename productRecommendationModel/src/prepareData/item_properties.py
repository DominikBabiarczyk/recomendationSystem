from typing import Tuple

import numpy as np
from sqlalchemy import Engine

from prepareData.get_text_number_data import get_text_number_data
from prepareData.helpersFunctions.padMatrix import get_completed_matrix
from prepareData.helpersFunctions.padTensor import get_completed_tensor
from prepareData.helpersFunctions.padVector import get_completed_data
from prepareData.queries.properties_of_item import get_properties_of_item


def get_property_descriptions_numbers(id_browsing: np.array, engine: Engine) -> Tuple[np.array, np.array, np.array]:
    property_browsing_item = []
    descriptions_browsing_item = np.empty((0,), dtype=object)
    numbers_browsing_item = np.empty((0,), dtype=object)

    for id in id_browsing:
        df_property = get_properties_of_item(engine, id)
        category = df_property['property'].to_numpy()
        property_browsing_item.append(get_completed_data(category, 40))

        id_property = df_property['id'].to_numpy()

        descriptions, numbers = get_text_number_data(id_property, engine)
        descriptions = np.expand_dims(descriptions, axis=0)
        numbers = np.expand_dims(numbers, axis=0)

        if descriptions_browsing_item.size == 0:
            descriptions_browsing_item = descriptions
        else:
            descriptions_browsing_item = np.vstack([descriptions_browsing_item, descriptions])

        if numbers_browsing_item.size == 0:
            numbers_browsing_item = numbers
        else:
            numbers_browsing_item = np.vstack([numbers_browsing_item, numbers])

    property_browsing_item = get_completed_matrix(np.array(property_browsing_item), 7)

    descriptions_browsing_item = get_completed_tensor(descriptions_browsing_item, 7)
    numbers_browsing_item = get_completed_tensor(numbers_browsing_item, 7)

    return property_browsing_item, descriptions_browsing_item, numbers_browsing_item
