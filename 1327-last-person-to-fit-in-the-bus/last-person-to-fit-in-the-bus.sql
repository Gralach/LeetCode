# Write your MySQL query statement below
SELECT person_name
FROM Queue
WHERE turn = (
SELECT MAX(turn)
FROM(
SELECT turn, person_id, weight, SUM(weight) OVER(ORDER BY turn) as tot
FROM Queue) a
WHERE tot <= 1000)