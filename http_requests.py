import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
starttime = input('Input start time: ')
endtime = input('Input end time: ')
latitude = input('Input latitude: ')
longitude = input('Input longitude: ')
maxradius = input('Input max radius km: ')
magnitude = input('Input min magnitude: ')

response = requests.get(url, headers={'Accept':'application.json'}, params={'format':'geojson',
                                                                            'starttime': {starttime},
                                                                            'endtime': {endtime},
                                                                            'latitude': {latitude},
                                                                            'longitude': {longitude},
                                                                            'maxradiuskm': {maxradius},
                                                                            'minmagnitude': {magnitude}})
# print(response.text)
response_data = response.json()
earthquake_list = response_data['features']
count = 0
for item in earthquake_list:
    count += 1
    print(f"{count}. Place: {item['properties']['place']}. Magnitude: {item['properties']['mag']}")
    # for key,values in items['properties']:
    #     if ['place'] in key:
    #         print(f"Place: {items['place']}. Magnitude: {items['magnitude']}")
# print(type(response.json()))
# data = response.json()
# for place in response.json():

# print(data['features'][1]['properties']['place'])