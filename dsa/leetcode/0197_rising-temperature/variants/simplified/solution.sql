-- Write your PostgreSQL query statement below
SELECT w1.id
FROM
    Weather AS w1
    JOIN Weather AS w2
        ON (w1.recordDate::date - w2.recordDate::date) = 1 AND w1.temperature > w2.temperature;
