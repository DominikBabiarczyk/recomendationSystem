import pandas as pd


def get_output_data(engine, batch_size, offset):

    query = f"SELECT * FROM events_on_item LIMIT {batch_size} OFFSET {offset}"
    df = pd.read_sql(query, engine)

    purchased_item = df['itemid'].to_numpy()
    return purchased_item
