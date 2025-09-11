import json

flight = {'flight_number': 'I700', 'airline': 'Indigo', 
          'capacity': 225, 'price': 4500,
          'source': 'Banglore', 'destination': 'Hyderabad'}
file_name = 'flight.json'

print('Before file:', flight)

with open(file_name, 'w') as writer:
    json.dump(flight, writer) 
    print('saved the flight to json file')

with open(file_name, 'rb') as reader:
    flight_from_file = json.load(reader) 
    print('Flight after read from json file:', flight_from_file)