## General

**Store each user's tasks in due-date order**

`self.tasks` is a `defaultdict(SortedList)`. Accessing a user ID that has not appeared creates an empty sorted collection automatically.

Each task record is stored as:

`[dueDate, taskDescription, set(tags), taskId, False]`.

Placing `dueDate` first makes the SortedList order records by due date. Due dates are globally unique under the constraints, so later fields never need to break a due-date tie.

The final boolean is the completion flag. False means pending and true means completed.

**Generate global sequential IDs**

`self.i` begins at one. `addTask` saves the current value as `taskId`, increments the counter, inserts the record under the specified user, and returns the saved ID.

Because the counter belongs to the whole TodoList rather than one user, task IDs increase globally across users exactly in call order.

Converting `tags` to a set makes later membership tests such as `tag in x[2]` expected constant time and removes duplicate tags without changing their yes-or-no meaning.

**Why sorting at insertion answers queries in order**

SortedList inserts each new record at its due-date position. Iterating `self.tasks[userId]` therefore visits all that user's records in ascending due date.

`getAllTasks` filters out records whose completion flag is true and projects field one, the description. Filtering does not disturb the relative order of surviving records, so the returned descriptions remain due-date ordered.

`getTasksForTag` applies both pending and tag-membership conditions before projecting the description. It likewise preserves iteration order.

No query-time sort is needed.

**Completion keeps the record but changes its visibility**

`completeTask` scans only the specified user's collection. If it finds a record whose task ID matches, it sets its final field to true and stops.

If the user has no such task, the loop ends with no effect. A task belonging to another user is invisible because it resides in a different collection. Completing an already completed task sets true to true and produces no observable change, consistent with doing nothing further.

Completed records are not deleted. Both query methods exclude them through `not x[4]`, preserving history and making completion a simple flag update.

**Why mutating the flag does not break sort order**

Mutating an item stored in an ordered container is generally dangerous if the changed field affects comparisons. Here, due date is the first field and all due dates are unique. Changing only field four cannot alter any record's ordering relative to another record because their comparison is already decided by distinct first fields.

Thus the SortedList remains correctly ordered after completion.

**Trace the example state**

Adding Task1 at due date 50 and Task2 at 100 stores them in that order. Querying user one returns both descriptions. Querying unseen user five creates or observes an empty list and returns no tasks.

Adding Task3 with due date 30 inserts it before both existing records. A tag-P1 query scans in order and returns Task3 then Task2. Completing Task2 sets its flag; later tag and all-task queries skip it while retaining Task3 before Task1 by due date.

An attempted completion by user five cannot reach user one's Task1 and changes nothing.


After every add, exactly one record with the new ID exists under the requested user, carrying the exact description, due date, tag set, and pending state. SortedList preserves due-date order.

Completion changes exactly the matching record under the requested user, if present. Query comprehensions select exactly records satisfying the stated pending and optional-tag predicates, then emit descriptions in maintained order.

These representation facts directly imply every method contract.

**Exact operation costs**

Let $u$ be one user's stored task count. SortedList insertion is $O(\log u)$ for locating a block and has library-specific amortized movement costs. Building the tag set costs proportional to the supplied tags.

Both retrieval methods scan all $u$ records, even if few qualify. Completion also scans up to $u$ records because there is no direct task-ID index. Over $Q$ calls, repeated full scans can total $O(Q^2)$ in the worst case.

The manifest's aggregate $O(q^2\log q)$ is a conservative upper description, but individual behavior is more informative: add is ordered insertion, while read and completion operations are linear in that user's stored records.

## Complexity detail

For a user with $u$ tasks and a new tag list of size $z$, `addTask` uses $O(z)$ set construction plus SortedList insertion, conventionally $O(\log u)$ search with container insertion overhead. `getAllTasks` costs $O(u)$ plus output. `getTasksForTag` costs expected $O(u)$ because each set lookup is expected constant time. `completeTask` costs $O(u)$ worst case.

Across $Q$ tasks, records use $O(Q)$ space and tag sets use $O(S)$ total tag storage. Completed tasks remain stored, so space is $O(Q+S)$.

## Alternatives and edge cases

- **Task-ID index:** A dictionary from task ID to record and owner would make completion expected $O(1)$ while keeping per-user ordering separately.
- **Sort on every query:** Plain per-user lists simplify insertion but make each retrieval $O(u\log u)$; SortedList pays ordering cost incrementally.
- **Delete completed tasks:** Removal would shrink scans but loses stored history and requires locating the record in the ordered container.
- **Unknown user:** Defaultdict supplies an empty SortedList, and query methods return an empty list.
- **Wrong owner completion:** Searching only that user's records ensures another user's task cannot be completed.
- **Repeated completion:** The flag is already true, so observable state does not change.
- **Empty tags:** The stored set is empty and no tag query can match it.
- **Unique due dates:** They guarantee record ordering never depends on mutable later fields.
- **Global task IDs:** One shared counter, not a per-user counter, satisfies sequential creation order.
- **Completed filtering:** Records remain ordered and stored but never appear in either pending-task query.
