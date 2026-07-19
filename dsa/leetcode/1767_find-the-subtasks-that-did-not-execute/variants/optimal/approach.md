## General
**Generate each task's complete subtask domain**

Begin a recursive common table expression with subtask `1` for every row of `Tasks`. Retain `subtasks_count` in the recursive state, then repeatedly increment `subtask_id` while it remains below that task's count. Each task therefore produces exactly its legal identifiers and cannot cross into another task's range.

**Let all task sequences advance independently**

The recursive member operates on every current row of the common table expression. A task with a small count stops when it reaches its own limit, while larger tasks continue producing rows. After recursion finishes, the relation contains each of the $T$ possible `(task_id, subtask_id)` pairs once.

**Exclude pairs that have execution evidence**

For each generated pair, use `NOT EXISTS` to test for a matching row in `Executed` on both columns. A composite-key lookup succeeds precisely for executed work, so retaining only failed lookups yields exactly the missing subtasks. This form also expresses the anti-join directly without relying on nullable data columns.

**Specify the requested output order**

Sort the remaining rows by `task_id` and `subtask_id`. Recursive production order is an implementation detail and cannot replace an explicit `ORDER BY`.

Every output row comes from a task's inclusive range and lacks a matching execution record, so it is a valid missing subtask. Conversely, recursion generates every valid pair, and any pair not executed survives the anti-join; therefore no required row is omitted.

## Complexity detail
The recursive relation creates exactly $T$ rows. With the unique executed-pair key, each anti-join probe takes constant expected or indexed time, so enumeration and filtering take $O(T)$ time. The recursive intermediate relation and result can contain $O(T)$ rows, giving $O(T)$ space. Since every executed row represents one of these valid pairs, its count is at most $T$.

## Alternatives and edge cases
- **Fixed numbers table:** Joining `Tasks` to a permanent sequence table is efficient and avoids recursion, but assumes that auxiliary table exists in the submission environment.
- **Hard-coded union of integers:** This only works for a known small maximum and is brittle when the supported subtask bound changes.
- **Left anti-join:** A `LEFT JOIN` followed by a null check on the executed key is equivalent when the key columns are non-null.
- **Task with no executions:** Every generated subtask for that task must appear.
- **Task fully executed:** All of its generated pairs are removed, contributing no rows.
- **Gaps between executed IDs:** Missing identifiers need not form one interval; each absent pair is returned independently.
- **Several tasks:** Subtask identifiers restart at `1` for every task.
- **Unsorted source rows:** Input storage order does not affect the explicitly sorted result.
