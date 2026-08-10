## General

**Use one recursive CTE to walk upward from every employee.** The CTE named `level_cte` begins with one anchor row per employee:

`employee_id, manager_id, level = 1, salary`.

Its recursive term joins the current row's `manager_id` to that manager's employee record. It keeps the original `a.employee_id` and salary, replaces `manager_id` with the manager's own manager, and increments `level`.

Thus the CTE does not traverse downward from only the CEO. It independently follows every employee's manager chain upward. For an employee reporting directly to the CEO, it creates:

- an anchor row pointing to the CEO at temporary level one; and
- a recursive row whose `manager_id` is null at level two.

For the CEO, the anchor row already has null manager and level one. More deeply nested employees receive one row per ancestor step until the chain reaches null.

**Extract each employee's true hierarchy level at the top of their chain.** In `employee_with_level`, subquery `b` keeps only `level_cte` rows with `manager_id IS NULL`. Each employee has exactly one such terminal row in a valid tree rooted at the CEO, and its accumulated `level` is the required organizational level.

The query joins that terminal level back to `Employees` by `employee_id` to recover the employee name and own salary. Although the source uses a comma join plus a `WHERE` equality, it is logically an inner join.

For Alice, the terminal row is her anchor and level is one. Bob's anchor points to Alice; one recursive step reaches Alice's null manager, so Bob's terminal level is two. Hank's chain through David, Bob, and Alice reaches null at level four.

**The same CTE rows form the ancestor-descendant closure.** Consider any nonterminal `level_cte` row for original employee $e$. Its current `manager_id` is one of $e$'s ancestors. Grouping those rows by `manager_id` therefore collects every direct and indirect report under that ancestor.

The derived table `b` filters out rows whose manager is null and groups the rest:

`COUNT(*) AS team_size` counts one row for each descendant-ancestor relationship, so a manager's count is the number of employees below them.

`SUM(salary) AS budget` sums the original descendant employee's salary on each of those rows. Since a given descendant appears exactly once for each ancestor in its chain, each manager receives every descendant salary exactly once.

The grouped budget deliberately excludes the manager's own salary: an employee's upward-chain rows name their managers, not themselves. The outer select adds `a.salary` to the descendant sum, producing the requested controlled budget including self.

**Preserve employees with no reports.** `employee_with_level a` is left-joined to the aggregate by employee ID. A leaf employee has no group row because no other employee's chain names that leaf as manager. `COALESCE(b.team_size, 0)` gives zero, and `a.salary + COALESCE(b.budget, 0)` makes the budget equal to the leaf's own salary.

For Frank in the example, Ivy's and Judy's upward paths each contain a row whose manager ID is Frank. Frank's group therefore has count two and descendant salary sum $14{,}000$. Adding Frank's $9{,}000$ gives budget $23{,}000$.

For Alice, every other employee's chain contains Alice as a non-null manager before reaching the terminal null row. Her group counts nine descendants and sums all their salaries; adding her own salary yields the company-wide budget.

**Order using the computed output values.** The final `ORDER BY` sorts first by `level` ascending. Within a level, `budget DESC` puts larger controlled budgets first. Remaining ties use `employee_name` ascending. These references resolve to the selected aliases, matching the required ordering sequence.

**Why the result is correct.** For every employee, the upward recursion emits exactly one row for each successive ancestor boundary and terminates at the CEO's null manager. The terminal row's step count is therefore the employee's level. Every proper descendant contributes exactly one nonterminal row labeled with each ancestor's ID, so grouping counts the complete reporting subtree and sums its salaries without including the ancestor twice. The left join supplies zero aggregates to leaves, and adding the employee's own salary completes the budget definition. The final ordering applies the three requested keys in order.

The query assumes the described organization is an acyclic hierarchy whose manager links ultimately reach a null top-level manager. A management cycle would make recursive traversal invalid or unbounded, but it is outside the intended data model.

## Complexity detail

Let $n$ be the number of employees and let $a$ be the total number of employee-to-ancestor relationships materialized by the recursive CTE, including the upward chain rows. A shallow organization has $a=O(n)$, while a chain-shaped hierarchy can have $a=O(n^2)$.

Generating and aggregating the closure costs $O(a)$ logical row work, assuming indexed employee-ID joins. Joining the $n$ employee results and sorting them by level, budget, and name costs up to $O(n\log n)$. The total logical time bound is $O(a+n\log n)$, matching the manifest.

Materializing recursive rows and aggregates requires $O(a+n)$ workspace in a general plan, also matching the manifest. Exact execution, temporary-table use, and index access are controlled by MySQL's optimizer.

The query computes the ancestor closure once and reuses it for both terminal-level extraction and subtree aggregation, rather than issuing a separate recursive query per employee.

## Alternatives and edge cases

- **Recursive traversal once per manager:** It repeats subtree work and can be far more expensive than sharing one ancestor closure.
- **Start only from the CEO and traverse downward:** This also computes levels, but additional path information is needed to aggregate every manager's complete subtree.
- **Count only direct reports:** Grouping the base table by `manager_id` misses indirect descendants; recursive CTE rows supply all ancestor relationships.
- **Include the manager in `COUNT(*)`:** Team size excludes the manager, and the closure naturally counts descendants only.
- **Forget to add own salary:** The grouped sum contains reports' salaries, so `a.salary` is required for the full controlled budget.
- **Leaf employee:** The left join and `COALESCE` produce team size zero and budget equal to own salary.
- **CEO:** Their terminal level is one, and every other employee contributes to their descendant aggregate.
- **Several employees with equal level and budget:** `employee_name` ascending resolves the remaining order.
- **Duplicate employee names:** The requested keys may still tie completely; `employee_id` is not specified as a final ordering key.
- **Missing manager row:** The upward join would stop before a null terminal row and the employee could disappear from `employee_with_level`; the hierarchy model assumes valid manager references.
- **Management cycle:** Recursive expansion would not reach null; the organizational-tree contract implicitly excludes cycles.
- **Long chain:** The closure becomes quadratic in employee count, which is why complexity is expressed in terms of $a$ rather than only $n$.
- **Comma join syntax:** The `WHERE a.employee_id = b.employee_id` condition makes it an inner join despite the older notation.
