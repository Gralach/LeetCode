# Write your MySQL query statement below
SELECT Employee.name
FROM Employee
JOIN (SELECT managerId, COUNT(id) as t FROM Employee GROUP BY managerId) as b
ON b.managerId = Employee.id
WHERE b.t >= 5