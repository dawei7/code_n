## Description

The `employees` table records each employee's identifier, salary, and department. For every department, determine its second-highest **distinct** salary. Return every employee earning that salary; if several employees tie at the second level, none of them may be discarded.

A department contributes no row when it has fewer than two distinct salary values, even if it contains several employees tied at its only salary. Report only the employee identifier and department, and order the complete result by `emp_id` in ascending order across all departments.
