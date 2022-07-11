# Write your MySQL query statement below
SELECT name as 'Customers'
FROM customers
WHERE customers.id not in
(
    select customerid from orders
)
