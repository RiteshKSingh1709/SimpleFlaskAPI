# SimpleFlaskAPI

### Initalize the Virtual Environment
`source venv/bin/activate`

### Run Python App 
delete empCrud.sqlite <br>
run `python EmpService.py`<br>
app will run at default port - 5000 (Make sure some other app is not using this port)

### Endpoint Defined

- /employee (GET)  - To get all the employees records
- /employee (POST) - To insert employee record
- /emp/name/&lt;empName&gt; (GET) - Get Employee record by employee name
- /emp/age/&lt;empAge&gt; (GET) - Get Employee record by employee age
- /emp/&lt;id&gt; (GET) - Get Employee record by id
- /emp/location/&lt;location&gt; (GET) - Get Employee by location
- /emp/&lt;id&gt; (PUT) - Update employee record by id
- /emp/&lt;id&gt; (DELETE) - Delete employee record by id
- /transc (GET) -  To get all the success and failure count of above transcation
  
### Schema for Employee
 - id - Primary Key
 - empName(String) - Employee Name
 - empAge (Integer) - Employee Age
 - location (String) - Employee location
 
