SELECT u.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u
  ON u.id = e.id
ORDER BY e.id;
