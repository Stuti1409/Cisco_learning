import repo_json_dict as repo

def menu():
    message = '''
Options are:
1 - Create Flight
2 - List All Flight
3 - Read Flight By Id
4 - Update Flight
5 - Delete Fight
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        number = input('Number:')
        airline_name = input('Airline_name:')
        capacity = int(input('Capacity:'))
        price = float(input('Price:'))
        source = input('Source:')
        destination = input('Destination:')

        flight = {'id':id, 'number':number, 'airline_name':airline_name, 
                    'capacity':capacity, 'price':price, 'source': source, 'destination': destination}

        repo.create_flight(flight)

        print('Flight Created Successfully.')
    elif choice == 2:
        print('List of Employees:')
        for flight in repo.read_all_flight():
            print(flight)
    elif choice == 3:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight == None:
            print('Flight not found.')
        else:
            print(flight)
    elif choice == 4:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight == None: 
            print('Flight Not Found')
        else:
            print(flight)
            price = float(input('New Price:'))
            new_flight = {'id':flight['id'], 
                'number':flight['number'], 
                'airline_name':flight['airline_name'], 
                'price':price, 
                'capacity':flight['capacity'],
                'source':flight['source'],
                'destination':flight['destination']}
            repo.update(id, new_flight)
            print('Flight updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight == None: 
            print('Flight Not Found')
        else:
            repo.delete_flight(id)
            print('Flight Deleted Succesfully.')
    elif choice == 6: 
        print('Thank you for using Application')

    return choice 

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    
menus()