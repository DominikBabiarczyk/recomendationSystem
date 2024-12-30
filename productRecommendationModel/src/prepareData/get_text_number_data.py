import numpy as np
import pandas as pd
from sqlalchemy import Engine
from typing import Tuple
from prepareData.helpersFunctions.padVector import get_completed_data
from prepareData.helpersFunctions.padMatrix import get_completed_matrix


def get_text_number_data(id_property: np.array, engine: Engine) -> Tuple[np.array, np.array]:
    final_vector_text_for_each_properties = []
    final_vector_number_for_each_properties = []
    for id in id_property:
        query = f"SELECT * FROM separated_words where original_id = {id} "
        df = pd.read_sql(query, engine)
        description = df['unique_id'].to_numpy()
        description = get_completed_data(description, 3)
        final_vector_text_for_each_properties.append(description)

        query = f"SELECT * FROM separated_number where original_id = {id} "
        df = pd.read_sql(query, engine)
        numbers = df['normalized_value'].to_numpy()
        numbers = get_completed_data(numbers, 3)
        final_vector_number_for_each_properties.append(numbers)

    pad_to_all_properties_text = np.array(get_completed_matrix(np.array(final_vector_text_for_each_properties), 40, (1, 3)))
    pad_to_all_properties_numbers = np.array(get_completed_matrix(np.array(final_vector_number_for_each_properties), 40, (1, 3)))

    return pad_to_all_properties_text, pad_to_all_properties_numbers
