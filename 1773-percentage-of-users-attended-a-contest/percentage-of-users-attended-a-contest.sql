# Write your MySQL query statement below
SELECT DISTINCT contest_id, 
       ROUND(COUNT(user_id) OVER(PARTITION BY contest_id)/(SELECT COUNT(DISTINCT user_id) FROM Users) * 100 , 2) as percentage
FROM Register
ORDER BY 2  DESC , 1 ASC