# Write your MySQL query statement below
SELECT DISTINCT a.product_id, IFNULL(b.new_price,10) as price
FROM Products a 
LEFT JOIN (SELECT product_id, new_price
FROM Products
WHERE (product_id, change_date) IN (
SELECT DISTINCT product_id , MAX(change_date) OVER(PARTITION BY product_id) AS max_date
FROM Products
WHERE change_date <= '2019-08-16')) b ON a.product_id = b.product_id