from starlette.testclient import TestClient

from database import Base
from models import *
from schemas import *
from fastapi import *
from sqlalchemy.orm import *
from pandas import read_csv

Base.metadata.create_all(engine)
app = FastAPI()
@app.get("/")
async def introduction():
    return f'After path  and / write a district name and click enter button.'

@app.get("/{district}")
async def get_data_db_to_API(district: str):
    try:
        dane = l_session.query(InfoWaw).filter(InfoWaw.District == district).all()[0]
        return {'Crimes':dane.Crimes,
                'Density of population': dane.Density,
                'Green spaces per person': dane.Green_space}
    except IndexError:
        return 'No data available for this district. The district is not on the list.'