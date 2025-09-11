import db_json as db 
#CRUD (Create, Read All | Read One, Update, Delete)
#Flight App - JSON Persistent Store (DB) - dict element
file_name = 'flights.json' 
flights = db.read_from_file(file_name) #[] # [{id, number, airline_name, seats, price, source, destination}, ...]

def create_flight(flight):
    global flights 
    flights.append(flight)
    db.write_to_file(flights, file_name)

def read_all_flight():
    return flights 

def read_by_id(id):
    for flight in flights:
        if flight['id'] == id:
            return flight 
    return None 

def update(id, new_flight):#new_flight is update at id
    global flights
    I = 0
    for flight in flights:
        if flight['id'] == id:
            flights[I] = new_flight
            db.write_to_file(flights, file_name)
            break 
        I += 1
    
def delete_flight(id):
    global flights
    index = -1
    I = 0
    for flight in flights:
        if flight['id'] == id:
            index = I
            break 
        I += 1
    if index != -1:
        flights.pop(index)
        db.write_to_file(flights, file_name)