import pytest 
from db import db_setup
from db import repo_sql_dict as repo

@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)
    #
    db_setup.Base.metadata.create_all(db_setup.engine)
    yield 
    db_setup.Base.metadata.drop_all(db_setup.engine)
    
def test_create_employee():
    flight = {'id':1001,'number':'I007','airline_name':'Indigo','capacity':250,'price':5000,'source':'Kanpur','destination':'Hyderabad'}
    repo.create_employee(flight)
    #
    savedflight = repo.read_by_id(1001)
    assert (savedflight != None)
    assert (savedflight['id'] == 101)
    assert (savedflight['number'] == 'I007')
    assert (savedflight['airline_name'] == 'Indigo')
    assert (savedflight['capacity'] == 250)
    assert (savedflight['price'] == 5000)
    assert (savedflight['source'] == 'Kanpur')
    assert (savedflight['destination'] == 'Hyderabad')