# Write your MySQL query statement below
SELECT ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity a2), 2) as fraction
FROM Activity a1
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (SELECT player_id, MIN(event_date) as yes
FROM Activity
GROUP BY 1)