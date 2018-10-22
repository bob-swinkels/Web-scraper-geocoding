import json
import geocoder
import geopy.distance
import csv
from sys import argv
script, filename = argv

city_centre = {
    'Enschede': [52.220850, 6.890950], 
    'Maastricht': [50.849850, 5.687260], 
    'Rotterdam': [51.922910, 4.470590], 
    'Eindhoven': [51.436600, 5.478000], 
    'Delft': [52.011900, 4.360260], 
    'Breda': [51.589320, 4.774470], 
    'Tilburg': [51.555120, 5.090490], 
    'sGravenhage': [52.080190, 4.310130], 
    'Groningen': [53.214470, 6.566480], 
    'Leeuwarden': [53.203410, 5.791310], 
    'Leiden': [52.157802, 4.489240], 
    'Utrecht': [52.091260, 5.122750], 
    'Amsterdam': [52.373170, 4.890660], 
    'sHertogenbosch': [51.690090, 5.303690], 
    'Nijmegen': [51.841690, 5.858650]}

with open(filename, 'r') as f:
    appartments_list = json.load(f)
    with open('processed_list.csv', 'w', newline='') as csvfile:
        datafile = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        datafile.writerow(['City','Distance to city centre (km)', 'Area of room (m2)','Number of rooms','Price (euro)','URL'])
        i = 0
        for appartment in appartments_list:
            i += 1
            g = geocoder.arcgis(appartment['postal_code'] + ' ' + appartment['city'])
            coord1 = city_centre[appartment['city']]
            coord2 = g.latlng
            distance = round(geopy.distance.vincenty(coord1, coord2).km, 2)
            print("Writing to file", i, "of", len(appartments_list), ">>>>>>", [appartment['city'], distance, appartment['size'], appartment['rooms'], appartment['price'], appartment['url']])
            datafile.writerow([appartment['city'], distance, appartment['size'], appartment['rooms'], appartment['price'], appartment['url']])
        