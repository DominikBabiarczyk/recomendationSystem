from prepareData.get_date import get_date
from prepareData.helpersFunctions.padMatrix import get_completed_matrix
from prepareData.helpersFunctions.padVector import get_completed_data
from prepareData.item_properties import get_property_descriptions_numbers
from prepareData.queries.get_browsing_before_purchase import get_browsing_before_purchase
import numpy as np
from sqlalchemy.engine import Engine


def fill_batch(final_data: np.array, engine: Engine, all_id: np.array) -> None:
    history_browsing_list = []
    property_list = [[] for i in range(3)]
    data_list = [[] for i in range(12)]
    events_list = []
    available_list = []
    category_list = []
    parent_id_list = []

    batch = []
    for id_events in all_id:
        df_browsing = get_browsing_before_purchase(engine, id_events)

        history_browsing = df_browsing['itemid_viewed_within_3_hours'].to_numpy()
        history_browsing = get_completed_data(history_browsing, 7)
        history_browsing_list.append(history_browsing)

        id_browsing = df_browsing['id'].to_numpy()

        property_browsing_item, descriptions_browsing_item, numbers_browsing_item = get_property_descriptions_numbers(
            id_browsing, engine)

        for i, box in enumerate([property_browsing_item, descriptions_browsing_item, numbers_browsing_item]):
            property_list[i].append(box)

        date = get_date(df_browsing)
        for i, box in enumerate(date):
            data_list[i].append(box)

        events = df_browsing[["visiting", "addingtocard", "transaction"]].to_numpy()
        events = get_completed_matrix(events, 7)
        events_list.append(events)

        available = df_browsing['available'].to_numpy()
        available = get_completed_data(available, 7)
        available_list.append(available)

        category_id = df_browsing['categoryid'].to_numpy()
        category_id = get_completed_data(category_id, 7)
        category_list.append(category_id)

        parent_id = df_browsing['parentid'].to_numpy()
        parent_id = get_completed_data(parent_id, 7)
        parent_id_list.append(parent_id)

    final_data.append(np.array(history_browsing_list, dtype=np.float32))
    for item in property_list:
        final_data.append(np.array(item, dtype=np.float32))
    for item in data_list:
        final_data.append(np.array(item, dtype=np.float32))
    final_data.append(np.array(events_list, dtype=np.float32))
    final_data.append(np.array(available_list, dtype=np.float32))
    final_data.append(np.array(category_list, dtype=np.float32))
    final_data.append(np.array(parent_id_list, dtype=np.float32))
