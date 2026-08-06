## Description

The `Candidates` table records each applicant's unique `employee_id`,
experience category, and unique monthly salary. Experience is either `Senior`
or `Junior`.

The company has a salary budget of $70{,}000$. It first hires seniors in
ascending salary order until the next senior no longer fits. It then spends
the remaining budget on juniors, again taking the lowest salaries in order
until the next one is unaffordable. Return the employee IDs of every candidate
hired by this senior-first process. The result rows may appear in any order.
