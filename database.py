from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


##UTILIZING SQLalchemy as ORM


URL_DATABASE= 'postgresql://postgres:Admin@localhost:5433/cogoport-assesment'

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False  , bind=engine)

Base = declarative_base()