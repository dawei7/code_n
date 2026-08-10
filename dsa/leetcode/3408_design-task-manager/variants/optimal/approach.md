## General

**Each operation needs two different views of the same tasks.** Looking up a task by `taskId` is necessary for `edit` and `rmv`. Executing the globally best task requires ordering all live tasks by priority and, for equal priorities, by task ID. One data structure does not provide both views efficiently, so the source keeps them synchronized:

- `self.d` is a dictionary from `taskId` to `(userId, priority)`;
- `self.st` is a `SortedList` of `(-priority, -taskId)` pairs.

The dictionary is the direct identity view. It answers “who owns this task?” and “what is its current priority?” in expected constant time. The sorted list is the ranking view. It keeps every live task in the exact order needed by `execTop`.

**Why both fields in the sorted key are negative.** Python tuples are ordered lexicographically in ascending order. The smallest tuple in `self.st` is at index zero. Negating priority makes a larger original priority become a smaller stored number. If priorities tie, negating `taskId` makes a larger original task ID become the smaller second field. Therefore, `self.st[0]` always represents the task that the statement says to execute.

For example, priority-task pairs $(20,102)$, $(15,105)$, and $(15,103)$ become $(-20,-102)$, $(-15,-105)$, and $(-15,-103)$. Ascending order places $(-20,-102)$ first. If the priority-$20$ task is gone, $(-15,-105)$ precedes $(-15,-103)$, correctly choosing task $105$ over task $103$.

**Maintain one exact entry per live task.** A useful invariant after every public operation is:

1. every key in `self.d` identifies one live task;
2. `self.st` contains exactly one tuple `(-priority, -taskId)` for that live task;
3. no removed or outdated tuple remains in `self.st`.

The constructor starts from empty structures and calls `add` for every initial triple. Reusing the same method makes initialization obey the same invariant as later insertions.

`add(userId, taskId, priority)` records the owner and priority in the dictionary, then inserts the ranking tuple into the sorted list. The contract guarantees that `taskId` is new, so this cannot leave an older ranking entry behind.

`edit(taskId, newPriority)` first reads the current owner and priority. It removes the old tuple with `discard`, updates the dictionary value while preserving `userId`, and inserts the tuple for the new priority. Removing before inserting matters when the priority changes; otherwise two ranking entries would refer to one task. The contract guarantees that the task exists, so the dictionary lookup is valid. `discard` is tolerant if a tuple is absent, although the invariant says it should be present.

`rmv(taskId)` obtains the current priority, deletes the dictionary entry, and removes the exact ranking tuple. Here `remove` is used, so a broken synchronization invariant would raise an error instead of being silently ignored. Under valid operations, the tuple is always present.

`execTop()` first checks whether the sorted list is empty. If so, no live tasks exist and it returns `-1`. Otherwise, `pop(0)` removes the smallest stored tuple, which represents the highest priority and then highest task ID. The source negates the stored task ID to recover the original ID, looks up its user, removes the task from the dictionary, and returns that `userId`. Both structures have now forgotten the executed task, so execution cannot happen twice.

In the example, editing task $102$ from priority $20$ to $8$ removes $(-20,-102)$ and inserts $(-8,-102)$. Task $103$ at priority $15$ then occupies the front and `execTop` returns user $3$. Later task $105$ has priority $15$ and wins the next execution after the specified removal and insertion operations.

**This source is eager, not lazy.** The local editorial describes a heap plus lazy deletion: edits push a new entry while stale entries remain until a later execution skips them. The manifest summary also refers to a lazily validated max-heap. The protected Optimal source does something materially different. A `SortedList` supports removal of the exact old key, so edits and removals eagerly delete outdated ranking entries. `execTop` never needs a validation loop. The explanation must follow this exact two-structure invariant rather than claim that stale heap entries exist.

Correctness follows directly from the invariant. The dictionary always contains the current metadata for every live task, and the sorted list contains exactly their ranking keys. Tuple order makes its first entry precisely the required task. Every mutating operation restores the invariant, so `execTop` returns the correct owner and removes exactly that task.

## Complexity detail

Let $N$ be the number of live tasks immediately before an operation. Expected dictionary lookup, insertion, and deletion cost $O(1)$. A `SortedList` lookup/removal/insertion or indexed pop has $O(\log N)$ target-search cost and the library's block-based update cost is logarithmic or amortized sublinear; the standard problem-level bound treats each such ordered-set operation as $O(\log N)$.

The constructor calls `add` for $t$ initial tasks, costing $O(t\log t)$ in the usual aggregate bound. `add` is $O(\log N)$. `edit` performs one ordered removal and one ordered insertion, still $O(\log N)$. `rmv` performs one ordered removal, $O(\log N)$. `execTop` performs one front pop plus expected constant-time dictionary work, $O(\log N)$, and returns `-1` in $O(1)$ when empty.

Across $q$ later operations, $N\le t+q$, giving the manifest's safe total upper bound $O((t+q)\log(t+q))$. Unlike lazy deletion, the ranking structure holds only live tasks. The dictionary and sorted list each use $O(N)$ space, so peak space is $O(N)$, or $O(t+a)$ if $a$ is the number of successful additions before accounting for removals. The broader $O(t+q)$ manifest bound is valid but not tight for this eager implementation.

## Alternatives and edge cases

- **Heap with lazy deletion:** Keep current metadata in a dictionary, push a new heap item on each add or edit, and skip stale entries during execution. This is the editorial method, but it can retain $O(q)$ obsolete entries and is not the protected source.
- **Scan the dictionary on every execution:** Add, edit, and remove remain simple, but finding the best live task costs $O(N)$ per `execTop`, which is too slow for the operation limit.
- **Priority buckets:** Priorities reach $10^9$, so allocating a bucket for every possible priority is impractical; task-ID tie-breaking would still need an ordered structure.
- **Equal priorities:** The negative task ID in the second tuple field guarantees that the numerically largest `taskId` is executed first.
- **Priority zero:** Negation leaves zero unchanged, and tuple ordering still works. Zero-priority tasks remain executable if no higher priority exists.
- **Empty manager:** `execTop` checks `not self.st` and returns `-1` without touching the dictionary.
- **Multiple tasks for one user:** Tasks are keyed by `taskId`, not `userId`. A user can own any number of tasks without collisions.
- **Editing the owner:** `edit` changes only priority. The source reads and preserves the existing `userId`, matching the contract.
- **Uniqueness guarantees:** `add` assumes a new task ID, while `edit` and `rmv` assume an existing one. The implementation intentionally relies on those input guarantees rather than defining overwrite or missing-task behavior.
- **Synchronization failures:** Every change must update both structures. Forgetting to remove an old ranking tuple could make `execTop` access a missing dictionary task or execute an obsolete priority.
