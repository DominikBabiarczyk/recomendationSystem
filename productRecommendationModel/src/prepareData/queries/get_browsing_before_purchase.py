import pandas as pd


def get_browsing_before_purchase(engine, id):
    query = (f"SELECT * FROM browse_product_before_purchasing"
             f" where id_events_on_item = {id} "
             f"order by view_order desc limit 7")
    browsing_before_purchase = pd.read_sql(query, engine)

    return browsing_before_purchase
