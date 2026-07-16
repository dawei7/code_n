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

### Required Complexity
- **Time:** $O(E+C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Why the rate is a company-level property**

The bracket is not chosen independently from each employee's own salary. First compute `MAX(salary)` for each `company_id`; that single maximum determines the rate applied to every row in the group. An employee earning `100` can therefore pay 49% when another employee in the same company earns more than `10000`.

A grouped relation with one row per company captures this dependency directly. Alongside `company_id`, store a take-home percentage: `100` for a maximum below `1000`, `76` for a maximum at most `10000` after the first condition has failed, and `51` otherwise.

**Joining the bracket back to every employee**

Join the company-level relation to `Salaries` on `company_id`. Each employee row matches exactly one aggregate row because grouping produces one row per company. This restores all employee columns while attaching the rate derived from the correct company maximum.

The output salary can then be expressed as `ROUND(salary * take_home_percent / 100.0)`. Using the take-home percentage avoids subtracting a separately rounded tax amount; the problem requires rounding the final after-tax salary itself.

**Handling the threshold boundaries exactly**

The first condition is strictly `company_max < 1000`. Therefore a maximum of exactly `1000` enters the 24% bracket. That middle bracket remains active through exactly `10000`, while `10001` enters the 49% bracket. A `CASE` expression ordered as `< 1000`, `<= 10000`, and `ELSE` encodes all three disjoint ranges without gaps or overlaps.

**Why the query produces the required relation**

Grouping by `company_id` computes the true maximum over all and only the employees of each company. The bracket conditions map that maximum to exactly one source-defined tax rate. The equality join attaches the resulting rate to every employee in that same company and no employee in another company. Finally, the arithmetic applies the rate once and rounds the adjusted value, while the projection preserves the required identity and name columns. Hence every output row has precisely the salary mandated by its company's maximum.

#### Complexity detail

Under the standard hash-aggregation and hash-join execution model, the grouped scan reads all $E$ salary rows once and stores $C$ company aggregates. Joining those aggregates back to the $E$ employee rows and computing the projection takes another linear pass. Total expected time is $O(E+C)$, which simplifies to $O(E)$ because $C\le E$.

The company aggregate contains one entry per distinct company, so its auxiliary space is $O(C)$. The returned $E$ rows are required output and are not counted as auxiliary storage. A database engine may choose a sort-based grouping or join instead, but the relational plan admits the stated bounds.

#### Alternatives and edge cases

- **Window maximum:** `MAX(salary) OVER (PARTITION BY company_id)` places the company maximum directly on every employee row and avoids an explicit join. It is equally expressive, though its physical partitioning plan may sort rows and not every target SQL version supports window functions.
- **Correlated maximum subquery:** Looking up `MAX(salary)` separately for every employee is concise but can rescan the same company repeatedly and degrade to $O(E^2)$ without optimizer decorrelation or a suitable index.
- **Self-join with pairwise comparisons:** Comparing every employee with every colleague can derive company maxima but generates unnecessary row pairs and complicates retaining one output row per employee.
- **Maximum exactly `1000`:** It receives the 24% rate, not 0%, because the zero-tax condition is strictly below `1000`.
- **Maximum exactly `10000`:** It remains in the inclusive 24% bracket; only values greater than `10000` receive the 49% rate.
- **Low-paid employee in a high-bracket company:** Apply the company's rate, even when that employee's own salary would fall into another bracket.
- **Rounding stage:** Round the final after-tax salary, not the tax amount and not the company maximum. Premature rounding can change the result by one.
- **One-employee company:** That employee's salary is also the company maximum, so the same grouped logic applies without a special case.
- **Result order:** The source accepts rows in any order. An `ORDER BY` may be added for display but is not part of the required relation and can introduce an avoidable sorting cost.

</details>
