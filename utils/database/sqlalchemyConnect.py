from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://admin:root@localhost/work_bot")
connection = engine.connect()
