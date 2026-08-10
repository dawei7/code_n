## General

**Use the guaranteed depth bound to unroll the manager chain**

Each `Employees` row gives one employee and that person's direct manager. The hierarchy may include groups that do not lead to company head `1`. The problem guarantees that a qualifying reporting chain contains at most three manager links, so the exact query follows exactly three links with self-joins rather than using unbounded recursion.

Alias `e1` represents the employee being considered for output. The first join

`JOIN Employees AS e2 ON e1.manager_id = e2.employee_id`

makes `e2` the direct manager of `e1`. The second join

`JOIN Employees AS e3 ON e2.manager_id = e3.employee_id`

makes `e3` the manager of that direct manager. Finally, `e3.manager_id = 1` tests whether the next manager in the chain is the head.

Read from left to right, the tested chain is

`e1 -> e2 -> e3 -> 1`.

That directly covers an employee three links below the head.

**Why the same joins also cover shorter chains**

The head's row reports `manager_id = 1`, so once a chain reaches employee `1`, additional unrolled joins remain on that same row. This self-reference pads shorter chains.

For a direct report `e1 -> 1`, `e2` is the head row. Because that row's manager is also one, `e3` joins to the head row again, and `e3.manager_id = 1` passes.

For a two-link report `e1 -> manager -> 1`, `e2` is the intermediate manager and `e3` is the head. The final condition again passes.

For a three-link report, `e3` is the employee directly below the head, and its `manager_id` is one. Therefore one, two, and three manager links all satisfy the same fixed query.

This behavior is visible in the example. Employee `2` directly reports to one and qualifies through padded head joins. Employee `4` follows `4 -> 2 -> 1`. Employee `7` follows `7 -> 4 -> 2 -> 1`. All pass.

**Excluding the head**

Employee `1` would also satisfy the join chain because its manager relationship points back to itself. The condition `e1.employee_id != 1` explicitly removes it. The requested result contains people who report to the head, not the head personally.

No `DISTINCT` is necessary under the schema. `employee_id` is unique, and each employee row has one `manager_id`. Thus each `e1` can join to at most one `e2` and one `e3`, producing at most one output row for that employee.

Employees whose manager identifier does not match a row disappear at an inner join. In a valid hierarchy, manager references are expected to identify actual employees. Separate self-contained hierarchies remain in the joins but fail `e3.manager_id = 1` unless their chain reaches one within the allowed depth.

**Why the query is correct under the contract**

If the query returns an employee, the two join predicates and final filter establish a sequence of direct-manager links from that employee to `e2`, from `e2` to `e3`, and from `e3` to one. The employee is not the head because of the inequality. It therefore directly or indirectly reports to the head.

Conversely, take any non-head employee whose manager chain reaches one in at most three links. If the chain has three links, its first two managers fill `e2` and `e3` and the final link satisfies the filter. If it has one or two links, the head's self-manager row fills the unused join depth as described above. The joins therefore produce the employee, proving completeness.

The fixed-depth proof relies on both facts from the data model: qualifying chains are no deeper than three manager links, and the head row has manager identifier one. Without those guarantees, a recursive query would be needed.

The result has no `ORDER BY` because the statement allows any order. The selected expression is `e1.employee_id`, so MySQL uses the required column name `employee_id` without an extra alias.

## Complexity detail

Let $n$ be the number of employee rows. With an index or hash lookup on unique `employee_id`, scanning possible `e1` rows and resolving its two managers takes expected $O(n)$ time. The fixed number of joins does not grow with hierarchy depth because that depth is capped.

SQL performance depends on the optimizer and available indexes. Without efficient lookup support, a naive nested-loop execution could be slower, potentially quadratic for a join. The manifest's $O(n)$ time represents the natural indexed or hash-join plan supported by the unique employee identifier.

Hash-join structures or scanned intermediate rows may occupy $O(n)$ working space, matching the manifest. With index nested-loop joins, engine-side auxiliary memory can be smaller, excluding the database's stored indexes and the result. The output itself contains at most $n-1$ identifiers.

Because the query uses a constant three aliases, its logical query depth and per-row chain work are constant. It does not allocate a recursive table whose size grows with hierarchy depth.

## Alternatives and edge cases

- **Recursive common table expression:** Start from the head's direct reports and repeatedly join subordinates. This handles arbitrary depth and is more robust if the three-manager guarantee is removed, but is more machinery than the exact contract requires.
- **Three `OR` checks with fewer joins:** One could separately test direct, two-level, and three-level reporting. The padded self-loop formulation expresses all three with one chain and one final condition.
- **Only one join:** That finds direct reports but misses employees two or three links below the head.
- **Head employee:** The self-referential manager row would qualify, so `e1.employee_id != 1` is essential.
- **Direct report:** Repeated joins remain on the head row and correctly preserve qualification.
- **Separate self-managed hierarchy:** A row such as employee `3` managed by `3` keeps joining to itself and fails the final manager-one condition.
- **Chain longer than three links:** The fixed query would miss it; correctness depends on the stated maximum indirect depth.
- **Unique employee identifiers:** They ensure each alias lookup finds at most one manager row and prevent duplicate output paths.
- **Missing manager row:** Inner joins discard that broken chain, so it cannot be reported as reaching the head.
- **Any output order:** No sorting is necessary or promised.
- **Head self-reference assumption:** Padding shorter chains works because employee `1` has `manager_id = 1` in this data model.
