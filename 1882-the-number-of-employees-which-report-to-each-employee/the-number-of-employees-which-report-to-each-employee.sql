# Write your MySQL query statement below
SELECT employee_id, name, reports_count, ROUND(average_age) as average_age 
FROM (SELECT DISTINCT reports_to, COUNT(reports_to) as reports_count, AVG(age) as average_age 
FROM Employees 
GROUP BY 1) b 
JOIN Employees a ON b.reports_to = a.employee_id
ORDER BY 1