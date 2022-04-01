from decimal import Decimal
import yandex_geocoder 
from yandex_geocoder import Client
import pandas as pd
from yandex_geocoder import (
    InvalidKey,
    NothingFound,
)

def load_dataset():
  citiDF = pd.read_excel('residential28.xls')
  return citiDF
citiDF = load_dataset()
#print(type(citiDF))
#print(len(citiDF))
locations = citiDF.values.tolist()

client = Client("0a46a34b-d8d4-4088-bf01-5dc08a16664a")

for location in locations:
 try:
    coordinates = client.coordinates(str(location))
    print (coordinates)
 except AttributeError:
    print ("None")
 except ValueError:
     print ("None")

    

#coordinates = client.coordinates("г. Минск, пер. Макаёнка,  4")
#assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))
#print(coordinates)

#address = client.address(Decimal("37.587093"), Decimal("55.733969"))
#assert address == "Россия, Москва, улица Льва Толстого, 16"



