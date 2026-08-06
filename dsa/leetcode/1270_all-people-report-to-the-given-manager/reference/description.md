## Description

The `Employees` table represents the reporting structure of a small company. Starting from any employee, following `manager_id` moves to that employee's direct manager. The company head is the employee whose `employee_id` is `1`.

Find the `employee_id` of every employee who reports to the company head, either directly or through a chain of managers. Do not include the head in the result. The indirect relationship is bounded so that a reporting chain passes through no more than three managers before reaching its destination.

Return the qualifying employee identifiers in any order.
