## General

The reporting structure is a hierarchy rooted at the CEO. Direct reports are one edge below the CEO, their reports are two edges below, and so on. An ordinary self-join can find one fixed depth, but the maximum depth is not known in advance. A recursive common table expression is designed for exactly this kind of parent-to-child traversal.

The first CTE, `T`, represents all employees reached from the root together with their depth. Its non-recursive anchor selects the row whose `manager_id IS NULL`. That row is the CEO according to the table contract. The anchor copies the CEO's identifier, name, manager, and salary, and assigns `hierarchy_level = 0`. Level zero is useful internally even though the CEO must not appear in the final output.

The recursive member joins the rows already in `T`, aliased as `t`, to `Employees`, aliased as `e`, using

`t.employee_id = e.manager_id`.

This equality says that `e` is a direct report of the already reached employee `t`. The child row carries its own identifier, name, manager, and salary, while its hierarchy level is `t.hierarchy_level + 1`. MySQL repeatedly evaluates this recursive member for newly produced rows until an iteration discovers no more descendants.

**Why every subordinate receives the correct level.** The CEO is placed at distance zero. If a reached manager is at distance $d$ from the CEO, every employee whose `manager_id` equals that manager's `employee_id` is exactly one reporting edge farther away, so the recursive query labels that employee $d+1$. By induction on the number of reporting edges, every direct or indirect subordinate is produced with its correct depth. Employees not descended from the CEO cannot satisfy a chain of these joins starting at the root and are not produced.

The query uses `UNION ALL` rather than `UNION`. In a valid employee hierarchy, each employee has one manager and therefore one path from the CEO, so the same employee should not be generated through multiple parents. Duplicate elimination is unnecessary. Avoiding it also saves the work that `UNION` would spend comparing recursive rows.

The second CTE, `P`, selects the salary of the row whose manager is null. It isolates the CEO salary so that every recursively discovered row can be compared with the same reference value. In the final query, `T t JOIN P p` has no join condition. In MySQL this acts as a cross join. Because the contract describes one CEO, `P` contains one row, so every `T` row is paired with exactly that one salary.

The selected result renames `employee_id` to `subordinate_id` and `employee_name` to `subordinate_name`. The expression `t.salary - p.salary` is the requested salary difference. The order of subtraction matters: a subordinate earning less than the CEO receives a negative value, as in the examples. It is not an absolute difference and it is not CEO salary minus subordinate salary.

The filter `WHERE hierarchy_level != 0` removes the anchor row. Every actual subordinate has a positive level, so no descendant is lost. Finally, `ORDER BY 3, 1` uses select-list positions: column three is `hierarchy_level` and column one is `subordinate_id`. It therefore implements ascending hierarchy level followed by ascending subordinate identifier. Ascending is MySQL's default when no `DESC` modifier is supplied.

For the example, Alice enters `T` at level zero. The first recursive expansion joins Bob and Charlie because their `manager_id` is Alice's identifier, assigning level one. The next expansion reaches David, Eve, Frank, and Grace at level two. Helen is reached from Eve in the following expansion and receives level three. `P` supplies Alice's `150000` salary to every output calculation, and the final sort groups the rows by those levels.

**Assumptions embedded in the exact query.** The statement refers to one CEO and a hierarchy, so the query expects one `manager_id IS NULL` row and no reachable management cycle. If several root rows existed, `T` would anchor all of them and `P` would also contain all of their salaries; the conditionless final join would multiply each reached employee by every root salary. That is not meaningful for a single-CEO problem. Likewise, malformed cyclic reporting data is outside the intended hierarchy contract and can cause problematic recursion. Under the stated model, the traversal is exact.

The recursive CTE finds the transitive closure of the “manages” relationship from the CEO. The separate root-salary CTE supplies a constant comparison value, and the final projection removes the root and formats the requested answer. Each part has one focused responsibility.

## Complexity detail

Let $e$ be the number of employees reachable in the CEO's hierarchy. The recursive CTE materializes $O(e)$ rows. With an index on `manager_id`, finding each manager's children is efficient; the final ordering of the $e-1$ subordinate rows costs $O(e\log e)$ in the general case. This sorting cost supports the stated overall $O(e\log e)$ bound.

Actual SQL runtime is plan- and index-dependent. Without a useful index, a database engine may repeatedly scan `Employees` during recursive expansion, making the join work worse than linear before sorting. Complexity notation for a SQL solution describes the intended relational work, not a guaranteed physical plan across all schemas and engines.

The recursive result and final sort can hold $O(e)$ rows, so auxiliary working space is $O(e)$. The recursion depth equals the height of the reporting tree, at most $e$ in a chain. Database recursion limits and temporary-table choices are operational considerations for exceptionally deep data.

## Alternatives and edge cases

- **Fixed self-joins:** Joining `Employees` to itself once finds direct reports, twice finds second-level reports, and so forth. This cannot handle an unknown hierarchy depth without hard-coding a maximum.
- **Application-side traversal:** Fetching rows and running BFS or DFS in application code can compute levels in $O(e)$ after building child lists, but the task asks for a SQL result and the recursive CTE keeps traversal close to the data.
- **Carry CEO salary inside `T`:** The anchor could add a `ceo_salary` column and propagate it unchanged through recursion. That would remove CTE `P` and its cross join while producing the same calculation.
- **Explicit `CROSS JOIN`:** Writing `CROSS JOIN P p` would communicate the intended one-row Cartesian product more clearly than `JOIN P p` without an `ON` clause. The exact MySQL query relies on their equivalent behavior here.
- **Only the CEO exists:** `T` contains the level-zero anchor, the final filter removes it, and the correct result is empty.
- **A deep chain:** Each employee is reached one recursive iteration after their manager, and the level equals their position in the chain. Very deep chains may encounter the database's configured recursive-CTE depth limit.
- **Multiple employees at one level:** `ORDER BY 3, 1` deterministically sorts them by identifier, regardless of the order in which recursive evaluation discovered them.
- **Higher-paid subordinate:** `t.salary - p.salary` becomes positive. A lower salary becomes negative and an equal salary becomes zero; all three signs are meaningful.
- **Multiple null managers:** The query would cross every traversed row with every root salary and duplicate output. Correctness depends on the single-CEO hierarchy promised by the problem.
- **Cycles or multiple-parent data:** A valid `manager_id` hierarchy gives each employee one parent and has no cycle reachable from the CEO. `UNION ALL` performs no cycle elimination, so malformed cyclic input is not protected against.
