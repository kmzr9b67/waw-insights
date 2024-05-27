from models import *
from fastapi import *
from creds import *
import requests
import uvicorn

URL_AIR_QL = (f'https://api.um.warszawa.pl/api/action/air_sensors_get/?apikey={API_KEY}')

Base.metadata.create_all(engine)
app = FastAPI()


def request_api(url):
    response = requests.get(url)
    return response.json()['result']


def get_air_quality(url, district):
    result = request_api(url)
    return [{'street': result[i]["address"]["street"],
             'air quality': result[i]["ijp"]["name"]} for i in range(0, len(result))
            if result[i]["address"]["district"] == district]


@app.get("/")
async def introduction():
    return 'Put the district name after the slash (e.g. /Żoliborz).'


@app.get("/{district}")
async def get_data_db_info(district: str):
    air_quality = get_air_quality(URL_AIR_QL, district)
    try:
        dane = l_session.query(InfoWaw).filter(InfoWaw.District == district.title()).all()[0]
        return {district.title():
                    {'Crimes': dane.Crimes,
                     'Density of population': dane.Density,
                     'Green spaces per person': dane.Green_space},
                'air quality': air_quality}
    except IndexError:
        return 'No data available for this district. The district is not on the list.'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
