## General

Two requirements pull in different directions. Updates need direct access by `taskId`, while `execTop` needs the globally greatest `(priority, taskId)` pair. Use one structure for each role:

- `tasks` maps every active task ID to its current `(userId, priority)` record.
- `heap` stores `(-priority, -taskId)` so Python's min-heap exposes the required maximum rank.

Construction and `add` write the authoritative map entry and push its rank. `edit` changes only the map's priority and pushes the new rank. `rmv` deletes only the map entry. None of these operations searches the heap or removes an arbitrary heap element.

This intentionally leaves obsolete ranks in the heap. During `execTop`, pop ranks until the map still contains that task and its recorded priority equals the popped priority. A missing task was removed or previously executed; a different priority was superseded by an edit. Once a valid entry is found, its heap rank is maximal among all remaining ranks. Every active task has a current rank somewhere in the heap, so no active task can outrank it. Delete the map entry and return its current owner.

Task-ID reuse is safe even when an old and new task share the same priority. Both heap entries encode the same rank, and either can represent the one current logical task; ownership is always read from the authoritative map. After execution deletes that map entry, every duplicate becomes stale.

## Complexity detail

Let $t$ be the number of initial tasks and $q$ the number of later method calls. Each initialization, addition, or edit creates one heap entry. A heap entry is pushed once and popped at most once, including stale entries. Thus construction and the complete call sequence take $O((t+q)\log(t+q))$ time and use $O(t+q)$ space.

Individually, `add` and `edit` take $O(\log(t+q))$, while `rmv` takes expected $O(1)$ map time. One `execTop` can discard many stale entries, but those costs cannot recur; its amortized cost is $O(\log(t+q))$ per popped entry across the trace.

The benchmark defines `size` as the number of initial tasks and subsequent executions. Its legal 10-, 20-, and 40-task tiers span 4x and execute every task in rank order. The accepted heap implementation stays within the required near-linear-logarithmic trace bound. A correct manager that scans all active tasks for every execution takes quadratic total work and fails only the scaling verdict.

## Alternatives and edge cases

- **Scan the task map in `execTop`:** Updates are simple, but executing all tasks requires $O(t^2)$ total comparisons.
- **Remove old heap entries eagerly:** Finding an arbitrary task inside a binary heap is linear, destroying the intended update bound.
- **Balanced ordered set:** A tree keyed by `(priority, taskId)` supports eager deletion and logarithmic operations, but Python's standard library provides no built-in ordered set.
- **Equal priorities:** Negating both tuple fields makes the greater task ID win the heap tie.
- **Edited tasks:** The former heap rank must be rejected unless its priority still matches the map.
- **Removed or executed tasks:** Their map entries disappear immediately; any later heap copies are ignored.
- **Reused task IDs:** Validate against the current map record and read the current owner rather than storing an owner in the heap rank.
- **Empty manager:** Once all heap entries are exhausted or stale, `execTop` returns `-1`.
- **Zero values:** Zero is a valid user ID, task ID, and priority; presence must be tested with `is not None`, not truthiness.
