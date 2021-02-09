import os
import csv
import geopy
import pandas as pd
from geopy.geocoders import Nominatim

redLightLoc = os.path.join("..", "Group-4-","Resources", "red-light-camera-locations.csv")
#redLightLoc = "../Resources/red-light-camera-locations"
#speedCamLoc = "../Resources/speed-camera-locations"

latList = []
longList = []

#Opening file and reading in lines
with open(redLightLoc, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        Latitude = row[5]
        Longitude = row[6]
        latList.append(Latitude)
        longList.append(Longitude)
    #print(latList)
    #print(longList)
    latDF = pd.DataFrame(latList,columns=['Latitude'])
    longDF = pd.DataFrame(longList, columns = ['Longitude'])
    #print(latDF)
    #print(longDF)    

def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['postcode']


geolocator = Nominatim(user_agent='asdf')

df = pd.DataFrame({
    'Lat': latList,
    'Lon': longList
})

zipcodes = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='Lat', lon_field='Lon')
print(zipcodes)

#zipcodes.to_csv(zipcodes, sep='\t', encoding='utf-8')

# file = open('zip.csv', 'w+', newline = '')
# with file:
#     write = csv.writer(file)
#     write.writerows(zipcodes)

