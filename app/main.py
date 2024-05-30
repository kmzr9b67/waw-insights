from json import loads, dumps
import pandas as pd
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from pandas import read_csv
from app.creds import API_KEY
from app.database import Base, engine, l_session
from app.models import InfoWaw

URL_AIR_QL = (f'https://api.um.warszawa.pl/api/action/air_sensors_get/?apikey={API_KEY}')

Base.metadata.create_all(engine)
app = FastAPI()

def get_data(district):
    data = read_csv('app/Data.csv')
    data.index = data['District']
    try:
        return data.loc[district.title()]
    except KeyError:
        raise HTTPException(404, f'There is no information about such a district.'
                             f'Please select from the list{data['District'].tolist()}')


def request_api(url):
    response = requests.get(url)
    return response.json()['result']


def get_air_quality(url, district):
    result = request_api(url)
    return [{'street': result[i]["address"]["street"],
             'air quality': result[i]["ijp"]["name"]} for i in range(0, len(result))
            if result[i]["address"]["district"] == district.title()]


@app.get("/")
async def introduction():
    return 'Put the district name after the slash (e.g./Żoliborz).'


@app.get("/{district}")
async def get_data_db_info(district: str):
    try:
        air_quality = get_air_quality(URL_AIR_QL, district)
        dane = get_data(district)
        return dane, air_quality
    except IndexError:
        return 'No data available for this district. The district is not on the list.'


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
