import pickle

flight = {'flight_number': 'I700', 'airline': 'Indigo', 
          'capacity': 225, 'price': 4500,
          'source': 'Banglore', 'destination': 'Hyderabad'}
file_name = 'flight.dat'

print('Before file:', flight)

with open(file_name, 'wb') as writer:
    pickle.dump(flight, writer) #flight is written byte by byte into flight.dat
    print('saved the flight to file')

with open(file_name, 'rb') as reader:
    flight_from_file = pickle.load(reader) #the byte by byte from the file is read from flight.dat
    print('Flight after read from file:', flight_from_file)