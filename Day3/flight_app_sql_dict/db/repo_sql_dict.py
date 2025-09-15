from .db_setup import session, Flight 
from .log import logging 
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import FlightNotFoundError, FlightAlreadyExistError, DatabaseError
#CRUD (Create, Read All | Read One, Update, Delete)
#Flight App - SQL DB - dict element
def create_flight(flight):
    try:
        flight_model = Flight (id = flight['id'],
            number = flight['number'],
            airline_name = flight['airline_name'],
            capacity = flight['capacity'],
            price = flight['price'],
            source = flight['source'],
            destination = flight['destination'] )
        session.add(flight_model) #INSERT stmt db 
        session.commit() 
        logging.info("flight created.")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate flight id:%s",ex)
        raise FlightAlreadyExistError(f"Flight id={flight['id']} exists already.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating flight:%s",ex)
        raise DatabaseError("Error in creating flight.")
def read_all_employee():
    flights = session.query(Flight).all()
    dict_flight = []
    for flight in flights:
        flight_dict = {'id':flight.id, 
            'number':flight.number,
            'airline_name':flight.airline_name,
            'capacity':flight.capacity, 'price':flight.price,'source':flight.source, 'destination':flight.destination}
        dict_flight.append(flight_dict)
    logging.info("read all employees.")
    return dict_flight 
def read_model_by_id(id):
    flight = session.query(Flight).filter_by(id = id).first()
    logging.info("read flight model.")
    return flight

def read_by_id(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return None
    flight_dict = {'id':flight.id,
        'number':flight.number,
        'airline_name':flight.airline_name,
        'capacity':flight.capacity, 'price':flight.price,'source':flight.source, 'destination':flight.destination} 
    logging.info("read employee for given id.")
    return flight_dict 

def update(id, new_flight):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return 
    flight.salary = new_flight['salary']
    session.commit()
    logging.info("flight salary updated.")
    
def delete_flight(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f"flight not found {id}.")
        return
    session.delete(flight)
    session.commit()
    logging.info("flight deleted.")
    