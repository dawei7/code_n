## General

**Turn the missing-reference condition into an anti-join.** Begin with `Students`, because every student must remain available long enough to decide whether the recorded department exists. A left join on `d.id = s.department_id` either attaches the unique matching department or produces a null-extended department side when no match exists.

**Recognize an unmatched row unambiguously.** Keep only rows for which `d.id IS NULL`. `Departments.id` is a primary key, so an actual department row can never satisfy that predicate. The filter therefore accepts exactly the students whose recorded ID has no partner in `Departments`. Selecting `s.id` and `s.name` preserves the requested student identity even when names repeat.

Each student produces at most one joined row because the department join key is unique. A valid assignment is removed by the null filter, while an invalid assignment survives, which proves both that every returned student qualifies and that no qualifying student is omitted. The contract permits any result order, so no `ORDER BY` is required.

## Complexity detail

Let $D$ and $S$ be the table sizes and $N=D+S$. With the department primary-key index or a hash table, the engine can build or access the department lookup in $O(D)$ time and test all students in $O(S)$ time. The general indexed or hash-join model is therefore $O(N)$ time and $O(D)$ lookup space; a database may already own the index storage.

## Alternatives and edge cases

- **`NOT EXISTS` anti-subquery:** Testing for the absence of a matching department is equally robust and is commonly optimized to the same anti-join plan; a literal correlated rescan without key lookup can cost $O(DS)$.
- **`NOT IN` subquery:** This form is concise but participates in SQL three-valued logic. A null outer `department_id`, or a nullable value in a less constrained subquery, makes the predicate unknown rather than true; `NOT EXISTS` or the left anti-join states missing-match semantics more directly.
- **No invalid students:** Every join finds a department, so the filter returns an empty result.
- **No departments:** Every student receives a null-extended department side and is returned.
- **No students:** The left input is empty, so the result is empty without special handling.
- **Repeated student names:** Rows remain distinct through the student primary key; selecting from `Students` preserves every qualifying ID-name pair.
- **Input and output order:** Neither table order affects membership, and the result order is intentionally unrestricted.
