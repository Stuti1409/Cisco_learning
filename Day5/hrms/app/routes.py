from flask import Flask, request, jsonify
import app.crud as crud
from app.config import config

app = Flask(__name__)
# db conn str
app.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URL']
app.config['SQLALCHEMY_ECHO'] = True

crud.db.init_app(app) #app to db configuration update

# create tables
with app.app_context():
    crud.db.create_all()

@app.route("/employees", methods = ['POST'])
def create():
    employee_dict = request.json
    crud.create_employee(employee_dict)
    emp_id = employee_dict['id']
    savedEmployee_dict = crud.read_by_id(emp_id)
    # send the mail
    return jsonify(savedEmployee_dict)

@app.route("/employees", methods = ['GET'])
def read_all():
    employees_dict = crud.read_all_employee()
    return jsonify(employees_dict)

@app.route("/employees/<app_id>", methods=['GET'])
def read_by_id(app_id):
    app_id = int(app_id)
    employee_dict = crud.read_by_id(app_id)
    return jsonify(employee_dict)

@app.route("/employees/<app_id>", methods=['PUT'])
def update(app_id):
    app_id = int(app_id)
    employee_dict = request.json
    crud.update(app_id, employee_dict)
    savedEmployee_dict = crud.read_by_id(app_id)
    return jsonify(savedEmployee_dict)

@app.route("/employees/<app_id>", methods=['DELETE'])
def delete_employee(app_id):
    app_id = int(app_id)
    crud.delete_employee(app_id)
    return jsonify("Deleted successfully")