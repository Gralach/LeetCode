# Write your MySQL query statement below
SELECT p.product_id, CASE WHEN purchase_date IS NOT NULL THEN ROUND(SUM(price * units) / SUM(units), 2) ELSE 0 END as average_price 
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
WHERE purchase_date BETWEEN start_date AND end_date OR purchase_date IS NULL
GROUP BY 1