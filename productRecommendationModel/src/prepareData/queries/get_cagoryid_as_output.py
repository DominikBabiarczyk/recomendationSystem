import pandas as pd


def get_category_as_output(engine, batch_size, offset):
    query = f"SELECT * FROM category_prediction.item_categories LIMIT {batch_size} OFFSET {offset}"
    df = pd.read_sql(query, engine)

    category_purchased_item = df['hashed_categoryid'].to_numpy()
    return category_purchased_item
