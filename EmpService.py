#Import Libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy.sql import select

#Creating the Flask Instance 
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'empCrud.sqlite')

#Creating SQLAlchemy Instance
db = SQLAlchemy(app)

#Creating Marshmallow Instance
ma = Marshmallow(app)

#Model for Employee
class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	empName = db.Column(db.String(80), unique=False)
	empAge = db.Column(db.Integer)
	location = db.Column(db.String(80))

	def __init__(self,empName,empAge,location):
		self.empName = empName
		self.empAge = empAge
		self.location = location

#Schema for Employee Table
class EmployeeSchema(ma.Schema):
	class Meta:
		#Fields to expose
		fields = ('id','empName','empAge','location')

#Model for Transaction
class Transaction(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	success = db.Column(db.Integer,default=0)
	failure = db.Column(db.Integer,default=0)

	def __init__(self,success,failure):
		self.success = success
		self.failure = failure

#Schema for Transaction
class TransactionSchema(ma.Schema):
	class Meta:
		#Fields to expose
		fields = ('success','failure')



#Creating instance of schemas
emp_schema = EmployeeSchema()
emps_schema = EmployeeSchema(many=True)
transaction_schema = TransactionSchema()


#Intializing Transaction 
def intialize_transaction():
	dummy_record = Transaction(0, 0)
	db.session.add(dummy_record)
	db.session.commit()


#Return Transaction Count
def TransactionCount(value):
	t = Transaction.query.get(1)
	success , failure = t.success , t.failure
	if value == 1:
		success += 1
	else:
		failure += 1
	t.success , t.failure = success , failure
	db.session.commit()


# endpoint to create new Employee
@app.route("/employee", methods=["POST"])
def add_employee():
	try:
	    emp_name = request.json['empName']
	    emp_age = request.json['empAge']
	    location = request.json['location']

	    new_emp = Employee(emp_name, emp_age, location)

	    db.session.add(new_emp)
	    db.session.commit()

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return emp_schema.jsonify(new_emp)
	except Exception as e:
		print(e)
		TransactionCount(0)



# endpoint to show all employee
@app.route("/employee", methods=["GET"])
def get_employee():
	try:
	    all_employees = Employee.query.all()
	    result = emps_schema.dump(all_employees)

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return jsonify(result.data)
	except Exception as e:
		print(e)
		TransactionCount(0)


# endpoint to get user detail by empName
@app.route("/emp/name/<empName>", methods=["GET"])
def emp_detail_by_name(empName):
	try:
	    emp = Employee.query.filter_by(empName = empName)

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return emps_schema.jsonify(emp)
  	except Exception as e:
  		print(e)
  		TransactionCount(0)


#endpoint to get employee detail  by age
@app.route("/emp/age/<empAge>", methods=["GET"])
def emp_detail_by_age(eAge):
	try:
	    emp = Employee.query.filter_by(empAge = empAge)

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return emps_schema.jsonify(emp)
	except Exception as e:
		print(e)
		TransactionCount(0)

#endpoint to get employee detail by id
@app.route("/emp/<id>", methods=["GET"])
def emp_detail_by_id(id):
	try:
	    emp = Employee.query.get(id)

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return emp_schema.jsonify(emp)
   	except Exception as e:
   		print(e)
   		TransactionCount(0)

#endpoint to get employee detail by location
@app.route("/emp/location/<location>", methods=["GET"])
def emp_detail_by_location(location):
	try:
		emp = Employee.query.filter_by(location = location)

		#Logging to Transaction Table
		TransactionCount(1)
		return emps_schema.jsonify(emp)
	except Exception as e:
		print(e)
		TransactionCount(0)


# endpoint to update user
@app.route("/emp/<id>", methods=["PUT"])
def emp_update(id):
	try:
	    emp = Employee.query.get(id)
	    empName = request.json['empName']
	    empAge = request.json['empAge']
	    location = request.json['location']

	    emp.empName = empName
	    emp.empAge = empAge
	    emp.location = location


	    db.session.commit()

	    #Logging to Transaction Table
	    TransactionCount(1)
	    return emp_schema.jsonify(emp)
	except Exception as e:
		print(e)
		TransactionCount(0)

# endpoint to delete user
@app.route("/emp/<id>", methods=["DELETE"])
def emp_delete(id):
	try:
	    emp = Employee.query.get(id)
	    db.session.delete(emp)
	    db.session.commit()

	    #Logging to Transaction Table
	    TransactionCount(1)

	    return emp_schema.jsonify(emp)
   	except Exception as e:
   		print(e)
   		TransactionCount(0)

#endpoint to fetch all the transaction Count
@app.route("/transc", methods=["GET"])
def get_tCount():
	try:
		t = Transaction.query.get(1)

		#Logging to Transaction Table
		TransactionCount(1)
		return transaction_schema.jsonify(t)
	except Exception as e:
		print(e)
		TransactionCount(0)


if __name__ == '__main__':
	intialize_transaction()
	app.run(debug=True)
