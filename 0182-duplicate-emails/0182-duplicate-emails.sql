# Write your MySQL query statement below
SELECT email
FROM Person
Group by email
having Count(email) >1;