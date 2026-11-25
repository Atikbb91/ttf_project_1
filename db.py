from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://test_9jvl_user:mwLN1cv7SbWXRo27g2srp1SLpYcQFfk0@dpg-dc38f9h5efls73b5sbk0-a.virginia-postgres.render.com/test_9jvl"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
