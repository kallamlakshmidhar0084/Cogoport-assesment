from sqlalchemy import Boolean , Column , ForeignKey , Integer , String
from database import Base


class Configurations(Base):
    __tablename__ = 'configurations'

    id = Column(Integer , primary_key=True , index=True)
    country_code=Column(Integer , index=True)
    configuration=Column(String , index=True)