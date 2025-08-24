/* Write your T-SQL query statement below */
select EmployeeUNI.unique_id, Employees.name
from Employees
Left join EmployeeUni 
ON Employees.id = EmployeeUni.id;