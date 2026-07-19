UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;

SELECT id, name, sex, salary
FROM Salary
ORDER BY id;
