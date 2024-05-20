# Write your MySQL query statement below
SELECT product_name, a.unit
FROM Products p
INNER JOIN (
SELECT product_id, SUM(unit) as unit
FROM Orders o
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY 1
HAVING unit >= 100) a
ON p.product_id = a.product_id