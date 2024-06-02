import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from pandas import read_csv
from app.database import Base, engine, l_session
from app.models import InfoWaw

# Base.metadata.create_all(engine)
app = FastAPI()
# def request_api(url):
#     response = requests.get(url)
#     return response.json()['result']

# def get_air_quality(url, district):
#     result = request_api(url)
#     return [{'street': result[i]["address"]["street"],
#              'air quality': result[i]["ijp"]["name"]} for i in range(0, len(result))
#             if result[i]["address"]["district"] == district.title()]


@app.get("/")
async def introduction():
    return 'Put the district name after the slash (e.g./Żoliborz).'


@app.get("/{district}")
async def get_data_db_info(district: str):
    data = pd.read_csv('app/Data.csv')
    data.index = data['District_name']
    try:
        return data.loc[district.title()].to_dict()
    except KeyError:
        raise HTTPException(404, f'There is no information about such a district.'
                                 f'Please select from the list{data["District_name"].tolist()}')


# if __name__ == "__main__":
#     uvicorn.run("app.main:app", reload=True)

