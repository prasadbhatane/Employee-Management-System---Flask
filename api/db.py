import sqlalchemy as sal
from sqlalchemy.orm import sessionmaker
from settings import MYSQL_CONNECTION_STRING

engine = sal.create_engine(MYSQL_CONNECTION_STRING)
connection = engine.connect()

# session
session = sessionmaker()
session.configure(bind=engine)
my_session = session()
