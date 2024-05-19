# Write your MySQL query statement below
SELECT DISTINCT class
FROM Courses
WHERE class IN (SELECT class FROM(
SELECT class, COUNT(student) as c
FROM Courses
GROUP BY 1
HAVING c >=5) as b)
