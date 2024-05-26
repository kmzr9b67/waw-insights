from pprint import pprint
import requests
from creds import *
#TODO aplikacja ma miec interfacepod wzgledem wyboru dzielnicy
#TODO aplikacja bedzie zwaracać dashbord na którym bedzie określone jaki jest obecnie stan powietrze w danym miesjcu

ID = 550

DICTIONARY_AIR_PROBS = {
    530: 'MOKOTÓW',
    550: 'SŁUŻEW',
    552: 'BRUDNO',
    10955: 'WŁOCHY',
    10956: 'RADOŚC',
    16533: 'BIELANY'
}

AREA_OF_DISTRICT = {

}
URL_AIR_POLLUTION = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{ID}'
URL_AIR_QL = (f'https://api.um.warszawa.pl/api/action/air_sensors_get/?apikey={API_KEY}')
DZIELNICA = "Wawer"
LAS = ('75bedfd5-6c83-426b-9ae5-f03651857a48')
#TODO dodac zmienną w kodzie
URL_FOREST = 'https://api.um.warszawa.pl/api/action/datastore_search/?resource_id=75bedfd5-6c83-426b-9ae5-f03651857a48&filters={"dzielnica":"Wawer"}'
URL_ALONE_TRE = 'https://api.um.warszawa.pl/api/action/datastore_search/?resource_id=ed6217dd-c8d0-4f7b-8bed-3b7eb81a95ba&filters={"dzielnica":"Wawer"}'
URL_BUDDY_TRE = 'https://api.um.warszawa.pl/api/action/datastore_search/?resource_id=913856f7-f71b-4638-abe2-12df14334e1a&filters={"dzielnica":"Wawer"}'
def get_result(URL):
    result = requests.get(URL)
    return result.json()

def request_API(URL):
    return get_result(URL)['result']

def get_air_ql(URL, DZIELNICA):
    pass

#TODO 1 ceny nieruchomosci

#TODO 2 liczba lasów
def get_forest():
    result = request_API(URL_FOREST)
    result_2 = request_API(URL_ALONE_TRE)
    result_3 = request_API(URL_BUDDY_TRE)
    return {'Number of treas in forests': result['total'], 'Number of treas (lonely)': result_2['total'],
            'Number of treas (in group)': result_3['total'],'Total': result['total']+ result_2['total']+result_3['total']}

print(get_forest())

#TODO wstawić do SQLALchemy
    #Dane o powierzchni
    #Dane o przestępwstawch w 2023
    #Dane o ludności
    #Saldo migracji
    #Bezrobocie zrejestrowana 

#TODO 3 Średnie wyniki w szkolach

