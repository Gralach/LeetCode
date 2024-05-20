# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') as Products
FROM Activities
GROUP BY 1