class FlightException(Exception):
    pass 

class FlightNotFoundError(FlightException):
    pass 

class FlightAlreadyExistError(FlightException):
    pass 

class DatabaseError(FlightException):
    pass 