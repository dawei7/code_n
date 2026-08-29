## General

**Build the senior cheapest prefix**

The hiring rule explicitly chooses the cheapest remaining senior until the next senior no longer fits. CTE `s` filters seniors and computes `SUM(salary) OVER (ORDER BY salary)`.

Because every salary is guaranteed unique in this version, the ordering identifies candidates one by one without peer ties. `cur` is intended to be the total cost of hiring that senior and every cheaper senior.

Rows with `cur <= 70000` are exactly the senior IDs accepted by the greedy rule.

**Carry senior spending into junior prefixes**

The scalar query inside CTE `j` intends to find the greatest affordable senior cumulative total. If no senior fits, `COALESCE` intends to use zero.

Junior salaries are independently accumulated in ascending order. Adding senior spending to each junior prefix total gives the total company spending after hiring the fixed senior prefix and that many cheapest juniors.

Filtering junior rows at 70000 selects exactly the affordable junior prefix.

**Why cheapest-first implements the criteria**

For any desired count $q$ within one experience group, the $q$ cheapest salaries have the smallest possible total. If their sum does not fit the available budget, no other $q$ candidates can fit. If it does, that count is achievable.

The maximum affordable senior prefix therefore implements the first priority. Freezing its cost and applying the same argument to juniors implements the second.

Unique salaries also make the chosen employee IDs unambiguous at every step.

**Trace the intended spending flow**

With senior salaries 16000, 20000, and 50000, cumulative totals are 16000, 36000, and 86000. The first two IDs qualify, so senior spending is 36000 and remaining budget is 34000. Junior salaries 10000, 15000, and 40000 produce combined totals 46000, 61000, and 101000. The first two junior IDs qualify. This is exactly the example's procedural sequence encoded as two window prefixes.

**Combine hired IDs**

The first final query returns accepted senior `employee_id` values. The second returns accepted juniors. `UNION` combines them.

Employee IDs are unique across the entire table, so no senior and junior branch can return the same ID. `UNION ALL` would produce the same rows with less duplicate-removal work, but `UNION` is semantically harmless.

The contract permits any output order.

**The exact SQL has a parse error**

As in ID 2004, the source writes a `SELECT` directly as an argument of `COALESCE`:

`COALESCE(SELECT MAX(cur) FROM s ..., 0)`.

MySQL requires a scalar subquery expression to have its own parentheses:

`COALESCE((SELECT MAX(cur) FROM s WHERE cur <= 70000), 0)`.

Without that inner pair, the exact `solution.sql` is syntactically invalid and cannot run. The approach describes the intended data flow, but the file cannot truthfully be called an executable correct solution.

**Why ID 2004's salary-tie issue does not apply here**

This statement guarantees every candidate salary is unique. Therefore `ORDER BY salary` has no peers, and the default window frame advances one candidate at a time.

After repairing the scalar-subquery syntax, the cumulative values correctly represent individual greedy prefixes without an explicit `ROWS` frame or employee-ID tie-breaker. The syntax defect remains; the peer-frame semantic defect does not.


Each accepted senior row belongs to the longest affordable sorted senior prefix. The scalar senior cost is exactly its total, or zero when empty. Each accepted junior row then belongs to the longest affordable junior prefix under the remaining budget.

No excluded candidate of the same group can be added after the prefix fails, because all later salaries are larger. Thus the returned IDs match the procedural rules exactly, assuming the missing scalar-subquery parentheses are repaired.

## Complexity detail

Let $R$ be the number of candidates. Window functions sort senior and junior partitions by salary, giving $O(R\log R)$ time. Filtering, scalar aggregation, and final combination add linear work.

Window processing and possible materialized CTEs can use $O(R)$ space. A real database plan may use temporary tables or indexes. The exact text fails during parsing before runtime complexity is realized.

## Alternatives and edge cases

- **Correct the scalar subquery:** Use `COALESCE((SELECT MAX(cur) ...), 0)`; this is mandatory for valid MySQL.
- **Procedural two-pass hiring:** Sort seniors and consume budget, then juniors; it mirrors the stated rules directly.
- **Recursive CTE:** Can model sequential hiring but is more complex than cumulative sums.
- **No affordable senior:** Senior cost becomes zero and juniors use the entire budget.
- **No affordable junior:** Only senior IDs are returned.
- **No candidates in one category:** Its CTE is empty without affecting the other category.
- **Salary exactly fits:** Included because cumulative cost uses `<= 70000`.
- **Unique salaries:** Eliminate window peer ambiguity and make selected IDs deterministic.
- **Senior priority:** Juniors cannot consume money until the maximum senior prefix is fixed.
- **`UNION` versus `UNION ALL`:** IDs are globally unique, so duplicate elimination is unnecessary but harmless.
- **Invalid exact source:** Missing scalar-subquery parentheses prevent execution.
- **Any result order:** No final ordering is required.
