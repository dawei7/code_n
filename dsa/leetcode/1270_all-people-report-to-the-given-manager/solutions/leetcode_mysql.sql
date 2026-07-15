SELECT candidate.employee_id
FROM Employees AS candidate
JOIN Employees AS direct_manager
  ON candidate.manager_id = direct_manager.employee_id
JOIN Employees AS upper_manager
  ON direct_manager.manager_id = upper_manager.employee_id
WHERE candidate.employee_id <> 1
  AND upper_manager.manager_id = 1;
