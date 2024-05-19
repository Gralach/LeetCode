# Write your MySQL query statement below
SELECT IFNULL(MAX(num), NULL) as num
FROM (SELECT num, COUNT(num) as c
FROM MyNumbers
GROUP BY 1) a
WHERE c = 1