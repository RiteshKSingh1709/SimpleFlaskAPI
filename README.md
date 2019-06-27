# SimpleFlaskAPI

### Initalize the Virtual Environment
source venc/bin/activate

### Run Python App 
delete empCrud.sqlite <br>
run `python EmpService.py`<br>
app will run at Port - 5000 (Make sure some other app is not using this port)

### Endpoint Defined

- /employee (GET)  - To get all the employees records
- /employee (POST) - To insert employee record
- /emp/name/<empName> (GET) - Get Employee record by employee name
- /emp/age/<empAge> (GET) - Get Employee record by employee age
- /emp/<id> (GET) - Get Employee record by id
- /emp/location/<location> (GET) - Get Employee by location
- /emp/<id> (PUT) - Update employee record by id
- /emp/<id> (DELETE) - Delete employee record by id
  
### Schema for Employee
 - id - Primary Key
 - empName(String) - Employee Name
 - empAge (Age) - Employee Age
 - location (String) - Employee location
 
