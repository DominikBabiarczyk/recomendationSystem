from sqlalchemy import create_engine


def get_engine():
    username = 'root'
    password = 'haslo123'
    host = '127.0.0.1'
    port = '3306'
    database = 'browsing_before_purchase'

    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
    return engine
