## Function Contract

**Input**

- `Employees`: a table with one row per `employee_id`, together with the employee's `employee_name` and direct `manager_id`.

Manager relationships may form a hierarchy rooted at employee `1` or a separate hierarchy that does not report to employee `1`. A qualifying reporting path may contain one, two, or three manager links to the head.

**Output**

Return a one-column table named `employee_id`. It must contain each non-head employee whose direct-manager chain reaches employee `1`, whether immediately or indirectly. Result order is unrestricted.
