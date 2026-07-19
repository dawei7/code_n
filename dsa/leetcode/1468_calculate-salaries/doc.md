# Calculate Salaries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1468 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-salaries/) |

## Problem Description
### Goal

The `Salaries` table contains one row per employee within a company. Each row records the company identifier, employee identifier, employee name, and that employee's salary. The pair `(company_id, employee_id)` uniquely identifies a row.

Calculate an after-tax salary for every employee. A company uses a single tax rate determined by the greatest salary paid by that company: the rate is 0% when the maximum is less than `1000`, 24% when the maximum lies in the inclusive range `[1000, 10000]`, and 49% when the maximum is greater than `10000`. Apply that company-wide rate to every employee in the company and round each resulting salary to the nearest integer. Return the employee and company identifiers, employee name, and adjusted salary in any order.

### Function Contract
**Inputs**

- `Salaries(company_id, employee_id, employee_name, salary)`: the source table.
- `(company_id, employee_id)` is the primary key.
- Let $E$ be the number of employee rows and $C$ the number of distinct companies.

**Return value**

Return one row for every input employee with columns `company_id`, `employee_id`, `employee_name`, and `salary`. The returned `salary` is the original salary multiplied by the take-home fraction selected from the company's maximum salary, then rounded to the nearest integer. Row order is not constrained.

### Examples
**Example 1**

- Input: a company whose salaries are `2000`, `21300`, and `10800`.
- Output salaries: `1020`, `10863`, and `5508`.
- Explanation: The company maximum is `21300`, so all three employees retain 51% after the 49% tax.

**Example 2**

- Input: a company whose salaries are `300`, `450`, and `700`.
- Output salaries: `300`, `450`, and `700`.
- Explanation: Its maximum is below `1000`, so the company tax rate is 0%.

**Example 3**

- Input: a company with maximum salary `7777`.
- Output for that employee: `5911`.
- Explanation: The maximum belongs to the inclusive 24% bracket, and `7777 * 0.76 = 5910.52`, which rounds to `5911`.
