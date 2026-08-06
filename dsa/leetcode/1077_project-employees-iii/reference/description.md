## Description

Projects may have different sets of assigned employees, and the same employee may work on more than one project. The `Project` table supplies those assignments, while `Employee` supplies the experience value associated with each employee. Comparisons must therefore be made separately within each project rather than across the workforce as a whole.

For every project represented by at least one assignment, report the employee or employees with the greatest number of experience years among that project's assignees. If several assigned employees share that maximum, include every tied employee. Return each qualifying `project_id` and `employee_id` pair; the result rows may appear in any order.
