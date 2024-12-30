import pandas as pd


def get_properties_of_item(engine, id):
    query = (f"SELECT * FROM properties_of_item"
             f" where id_viewed_item = {id} ")
    df_property = pd.read_sql(query, engine)

    return df_property
