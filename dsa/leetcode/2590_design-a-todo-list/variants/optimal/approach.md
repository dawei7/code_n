## General

Assign each addition the next global integer ID and store its owner, description, due date, tag set, and completion flag in a dictionary keyed by that ID. This makes completion lookup direct: change the flag only when the record exists, its owner matches `userId`, and it is not already complete.

For either retrieval operation, scan the stored records and keep only unfinished tasks owned by the requested user. The tag-specific operation adds one constant-time set-membership test. Sort the surviving records by due date and return only their descriptions. Due dates are globally unique, so no tie-breaking rule is needed.

The filters exactly encode the visibility contract: records from other users and completed records never enter the result, while a tag query retains precisely the owned unfinished records containing that tag. Sorting after filtering establishes the required order without changing membership. The app-local adapter constructs one object and invokes all commands sequentially, preserving state and returning `null` for construction and completion operations.

## Complexity detail

Let $q$ be the number of method calls, $a \leq q$ the number of stored tasks, and $S$ the total stored tag associations. Addition takes $O(g)$ time for its $g$ supplied tags, completion takes expected $O(1)$ time, and a retrieval takes $O(a + p \log p)$ time for $p$ matching pending tasks. Across an arbitrary sequence, this is $O(q^2 \log q)$ time in the worst case. Stored records and tag sets use $O(q+S)$ space, excluding returned output lists.

## Alternatives and edge cases

- **Per-user and per-tag indexes:** Maintaining extra indexes reduces irrelevant scanning but complicates completion filtering and still must emit every matching description.
- **Due-date array:** Because legal due dates are globally unique integers from `1` through `100`, a fixed array can avoid sorting, at the cost of coupling the design to that small domain.
- **Wrong owner or missing task:** `completeTask` must leave all state unchanged.
- **Repeated completion:** Completing an already completed task is also a no-op.
- **Empty tag list:** The task remains visible to `getAllTasks` but cannot match any tag query.
- **Global IDs:** The counter is shared across users; each user's first task does not restart at ID `1`.
