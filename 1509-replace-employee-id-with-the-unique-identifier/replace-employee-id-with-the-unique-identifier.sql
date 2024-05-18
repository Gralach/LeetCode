# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees as E
LEFT JOIN EmployeeUNI as U ON E.id = U.id 