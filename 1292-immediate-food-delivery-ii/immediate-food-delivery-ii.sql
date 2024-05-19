SELECT ROUND(AVG(order_date = customer_pref_delivery_date)* 100, 2) AS immediate_percentage
FROM Delivery
WHERE (order_date, customer_id) IN (SELECT MIN(order_date), customer_id FROM Delivery GROUP BY 2)