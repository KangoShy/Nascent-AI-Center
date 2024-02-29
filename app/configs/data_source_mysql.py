from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config as conf

MYSQL_DATABASE_URL = "mysql://" + conf.mysql_user + ":" + conf.mysql_pass + "@" + conf.mysql_address + "/" + \
                     conf.mysql_db_name

engine = create_engine(MYSQL_DATABASE_URL)

Session = sessionmaker(autoflush=False, bind=engine)
session = Session()

Base = declarative_base()
