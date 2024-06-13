from fastapi import FastAPI , HTTPException , Depends
from pydantic import BaseModel
from typing import List , Annotated
import models 
from database import engine , SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
models.Base.metadata.create_all(bind=engine) #creates tables in postgres



class ConfigurationBase(BaseModel):
    country_code: int
    configuration: str


def connect_db():  #connecting db 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency=Annotated[Session , Depends(connect_db)]



## end points 
#adding data to the table 
@app.post("/create_configuration")
async def create_configuration(configurations : ConfigurationBase , db : db_dependency):
    db_country_code=models.Configurations(country_code=configurations.country_code , configuration=configurations.configuration)
    db.add(db_country_code )
    db.commit()
    db.refresh(db_country_code)


#getting configuration provided country code
@app.get("/get_configuration/{country_code}")
async def get_configuration(country_code : int , db:db_dependency):
    result=db.query(models.Configurations).filter(models.Configurations.country_code==country_code).first()
    if not result:
        raise HTTPException(status_code=404 , detail="Country code not found")
    return result

#updating configuration provided country code
@app.put("/update_configuration/{country_code}/{configuration}")
async def update_configuration(country_code : int , db:db_dependency , configuration:str):
    result=db.query(models.Configurations).filter(models.Configurations.country_code==country_code).first()
    result.configuration=configuration
    db.commit()
    db.refresh(result)
    return result

#deleting configuration provided country code
@app.delete("/delete_configuration/{country_code}")
async def delete_configuration(country_code : int , db:db_dependency):
    result=db.query(models.Configurations).filter(models.Configurations.country_code==country_code).first()
    db.delete(result)
    db.commit()
    


    

