import pandas as pd
import numpy as np

from typing import List
from sqlalchemy import Engine
from prepareData.fillBatch import fill_batch


def get_batch_data(engine: Engine, batch_size: int = 1, offset: int = 0) -> List[np.array]:

    query = f"SELECT * FROM events_on_item LIMIT {batch_size} OFFSET {offset}"
    df = pd.read_sql(query, engine)

    visitorid = df['visitorid'].to_numpy()
    id = df['id']
    all_id = id.to_numpy()
    np.expand_dims(visitorid, axis=1)
    final_data = [np.array(visitorid, dtype=np.float32)]

    fill_batch(final_data, engine, all_id)

    return final_data

