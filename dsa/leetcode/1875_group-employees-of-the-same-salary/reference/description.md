## Description

The `Employees` table records a unique identifier, name, and salary for every employee. Form teams by salary: a team must contain at least two employees, every employee with a given repeated salary belongs to the same team, and an employee whose salary occurs only once is omitted entirely.

Assign team identifiers by increasing team salary. The lowest salary that forms a team receives `team_id = 1`, the next repeated salary receives `team_id = 2`, and so on without gaps. Unique salaries do not participate in this ranking. Return every team member with their original employee data and team identifier, ordered first by `team_id` and then by `employee_id`, both ascending.
