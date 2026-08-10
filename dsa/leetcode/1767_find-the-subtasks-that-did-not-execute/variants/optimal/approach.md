## General

**Generate the complete expected subtask relation**

`Tasks` stores only a count, not one row per valid subtask. Before missing rows can be found, the query must expand each task into identifiers one through `subtasks_count`.

The recursive common table expression `T(task_id, subtask_id)` performs that expansion. Its anchor member selects:

`task_id, subtasks_count`

from every task. This creates the highest valid subtask identifier for each task.

The recursive member then selects the same `task_id` with `subtask_id - 1` while `subtask_id > 1`. Repeated recursion therefore generates the descending sequence from the count down to one.

**Why every valid pair appears exactly once**

For a task with count $c$, the anchor emits `(task_id, c)`. The recursion emits `c-1`, then `c-2`, continuing until the row with identifier one. The condition prevents a zero row.

`task_id` is unique in `Tasks`, and each descending numeric step is unique for that task. `UNION ALL` is therefore safe: it preserves all generated rows without paying for unnecessary duplicate elimination.

The constraint `subtasks_count >= 2` is not required for the recursion's correctness; even a count of one would produce its one anchor row and no recursive child.

**Compare expected pairs with executed pairs**

After expansion, `T` contains the universe of valid task-subtask pairs. The query left-joins `Executed` using both `task_id` and `subtask_id`.

A matching execution row is attached when that exact pair executed successfully. When no match exists, columns from `Executed` are null because a left join preserves every row from `T`.

The filter:

`WHERE Executed.subtask_id IS NULL`

keeps only unmatched expected rows. Since valid `Executed.subtask_id` values are real integer identifiers and the key pair is unique, null here is an unambiguous no-match signal.

**Why joining on both columns matters**

Joining only on `task_id` would treat any executed subtask for a task as evidence that all of its subtasks ran. Joining only on `subtask_id` could match the same number from a different task.

The composite pair uniquely identifies one execution and exactly matches the membership question being asked.

**Project the recursive pair**

`SELECT T.*` returns the two CTE columns in declared order: `task_id` and `subtask_id`. No count or execution column is included.

A task with all subtasks executed has all of its generated rows matched and contributes nothing. A task with no executed rows has every generated pair unmatched and contributes its full identifier range.

**Trace the example**

Task one with count three generates `(1,3)`, `(1,2)`, and `(1,1)`. The executed table contains only `(1,2)`, so the left join leaves identifiers one and three unmatched.

Task two generates `(2,2)` and `(2,1)`. It has no executions, so both survive.

Task three generates four pairs and all four match, so none survives. The result contains exactly the four missing pairs described.

**Any-order behavior of the exact query**

The main problem description permits any output order, and the exact SQL has no `ORDER BY`. Recursive generation happens from high subtask identifiers downward, but SQL does not guarantee that this internal production order becomes result order.

The local function-contract text additionally asks for ascending task and subtask order. The exact query does not guarantee that stricter presentation requirement. Adding `ORDER BY task_id, subtask_id` would be required if sorted output is treated as mandatory.

This ordering detail does not affect which pairs the query returns.

**Why the result set is correct**

The recursive CTE generates every valid subtask pair and no invalid identifier. The left join marks exactly those generated pairs present in `Executed`. Filtering for a null execution retains precisely the set difference:

$$
\text{all valid subtasks}\setminus\text{executed subtasks}.
$$

Therefore every returned row is missing, and every missing valid subtask is returned.

## Complexity detail

Let $T=\sum \texttt{subtasks_count}$ be the total number of valid task-subtask pairs. The recursive CTE generates exactly $T$ rows, taking $O(T)$ logical work and $O(T)$ CTE storage.

Let $E$ be the number of executed rows. The guarantees imply $E \le T$. With an index or hash lookup on the unique pair, matching all generated rows takes expected $O(T+E)=O(T)$ time. The output and recursive relation use $O(T)$ space, matching the manifest.

A database may choose a different physical join, materialization, or temporary-index plan. Without a useful lookup strategy, physical execution can be worse; SQL describes the relational result rather than mandating one algorithm.

Adding the optional ascending `ORDER BY` would introduce sorting work, typically $O(M\log M)$ for $M$ missing rows unless an order can be produced through an index.

## Alternatives and edge cases

- **Numbers helper table:** Join each task to preexisting integers from one through `subtasks_count`. It avoids recursion when such a table is available.
- **Recursive sequence upward:** Anchor at one and increment while below the task count. It is equally correct and naturally describes ascending identifiers.
- **NOT EXISTS:** Generate candidates, then retain those for which no matching execution row exists. It expresses the anti-join directly.
- **NOT IN:** Null semantics can be troublesome in general; a composite `NOT EXISTS` or left anti-join is safer.
- **No executions for a task:** Every generated subtask survives.
- **All executions present:** No row for that task survives.
- **Some executions present:** Only exact unmatched composite pairs are returned.
- **Different tasks share subtask numbers:** Composite joining keeps them separate.
- **Maximum count twenty:** Recursion depth per task is small.
- **UNION ALL:** Generated pairs are inherently unique, so duplicate removal is unnecessary.
- **Stop at one:** `WHERE subtask_id > 1` prevents invalid identifier zero.
- **Executed uniqueness:** A successful pair cannot duplicate the result through multiple matches.
- **Any-order main contract:** The exact query satisfies membership but promises no ordering.
- **Ascending-order stricter contract:** Add an explicit `ORDER BY` if that local requirement must be enforced.
- **Empty missing set:** The query naturally returns no rows when everything executed.
