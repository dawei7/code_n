## General

**Separate future tasks from currently available tasks.** At any CPU decision time, tasks fall into two groups. Future tasks have an enqueue time greater than the current time and cannot be selected. Available tasks have already arrived, and the CPU must choose the one with smallest processing time, breaking ties by original index.

The solution represents those groups with two ordered structures:

- The mutated and sorted `tasks` list supplies future tasks in enqueue-time order.
- The min-heap `q` stores available tasks as pairs `(processing_time, original_index)`.

This separation is essential. Sorting only by processing time would risk selecting a short task that has not arrived. Sorting only by enqueue time would fail to choose the shortest among several tasks already waiting. The sorted list answers when a task becomes eligible; the heap answers which eligible task the CPU must run.

**Attach original indices before sorting.** The initial loop appends `i` to each task, changing `[enqueueTime, processingTime]` into `[enqueueTime, processingTime, i]`. The subsequent `tasks.sort()` is lexicographic, primarily ordering by enqueue time. Processing time and index break ties between equally enqueued tasks, but that secondary order does not decide execution directly; all tasks available by the current time will enter the heap, where the required processing-time and index priorities take over.

The original index must be saved before sorting because the return value refers to the input labels, not positions in the sorted list.

**Meaning of the simulation variables.** `i` is the position of the next sorted task not yet inserted into the heap. `t` is the current CPU time. `ans` records completed task indices in execution order. The main loop continues while either an available task remains in `q` or some future task remains at position `i`.

**Jump across idle time.** If the heap is empty, the CPU has nothing available to run. The next possible event is the enqueue time of `tasks[i]`. The update

`t = max(t, tasks[i][0])`

moves time directly to that event if it lies in the future. The maximum also prevents time from moving backward. Incrementing one time unit at a time would be disastrous because enqueue times can reach one billion and long idle gaps carry no decisions.

The code accesses `tasks[i]` only when `q` is empty inside a loop known to have remaining work. If no future tasks remained, both `q` and the remaining-task condition would be false and the outer loop would already have ended.

**Move every newly available task into the heap.** The inner while loop inserts tasks while `tasks[i][0] <= t`. Each heap entry is

`(tasks[i][1], tasks[i][2])`,

namely processing time followed by original index. Python compares tuples lexicographically, so `heappop` returns the smallest processing time. When processing times tie, it returns the smallest index. This exactly matches the scheduling rule.

It is important to insert all tasks available at time `t` before popping. If the code inserted only the first one, it could start a longer task without noticing a shorter task that arrived at the same or an earlier time.

**Run one task to completion.** The pop gives `pt` and `j`. The index `j` is appended to `ans`, then `t += pt` advances time to completion. No task can interrupt this interval because scheduling is non-preemptive. Tasks that arrive while the CPU is busy remain in the sorted future segment; on the next outer iteration, the inner loop moves every one whose enqueue time is now at most `t` into the heap.

**Trace the first sample.** After indices are attached and tasks are sorted, time jumps from zero to one. Task zero enters the heap and runs for two units, so `t` becomes three and `ans` begins with zero. Tasks one and two are now available; their processing times are four and two, so the heap selects task two. It completes at time five. Task three, which arrived at four, is then inserted. Its processing time one beats task one’s processing time four, so task three runs next. Task one is last, yielding `[0, 2, 3, 1]`.

When all tasks arrive at the same time, they all enter the heap together. The heap then orders them by processing time and index exactly as the second sample requires.

**Why the simulation is correct.** Maintain two invariants at each selection point. First, every unprocessed task with enqueue time at most `t` is in `q`, and no task with a later enqueue time is in `q`. The sorted list and insertion loop establish this availability invariant. Second, the heap root is the available task with the required smallest pair of processing time and index. Popping it therefore makes exactly the CPU’s mandated decision.

Advancing `t` by the full processing time models non-preemption. If no task is available, jumping to the next enqueue event models the required idle interval without skipping any possible decision. By induction, each appended index matches the real CPU’s next task, so the complete returned order is correct.

**The exact code mutates `tasks`.** It appends an index to every inner list and sorts the outer list in place. After the call, the caller’s input is no longer a two-column array in original order. This mutation is accepted by the judge but is a material implementation behavior. A non-mutating variant would build separate triples.

## Complexity detail

Let `n = tasks.length`. Appending indices takes `O(n)` time. Sorting the task triples takes `O(n log n)`. Every task is pushed into the heap once and popped once; each heap operation costs `O(log n)` in the worst case. The total running time is therefore `O(n log n)`.

The heap can hold `O(n)` tasks, and `ans` contains `n` output indices. Python’s sort may also use temporary memory. Thus total additional storage is `O(n)`. The exact solution reuses and enlarges the input task rows rather than allocating a separate sorted triple list, but that mutation does not eliminate the heap, output, or sorting storage.

The current time may grow to the sum of many processing times plus an enqueue offset, potentially beyond 32-bit range. Python integers expand safely; fixed-width implementations should use a 64-bit type.

## Alternatives and edge cases

- **Repeatedly scan all tasks:** At each decision, searching all unprocessed tasks for eligible minimum work can take `O(n^2)` time.
- **Sort the available list after every completion:** This models the policy but repeatedly sorts overlapping collections. A heap maintains the next minimum incrementally.
- **Build non-mutating triples:** Creating `(enqueue, processing, index)` tuples preserves the caller’s input and has the same `O(n log n)` time and `O(n)` space.
- **Long idle gap:** When `q` is empty, time jumps directly to the next enqueue time rather than advancing unit by unit.
- **Several tasks enqueue together:** The insertion loop pushes all of them before selection, so processing time and index decide correctly.
- **Equal processing times:** Tuple ordering uses original index as the second key, satisfying the required tie-break.
- **Task arrives exactly when another finishes:** Its enqueue time is `<= t`, so it enters the heap before the next selection.
- **Task arrives during execution:** Non-preemption means it waits until completion; the next insertion pass then makes it available.
- **One task:** Time jumps to its enqueue time, it is pushed and popped once, and its index is returned.
- **All tasks already available:** The heap receives them together and drains according to the scheduling priority.
- **Large accumulated time:** Python avoids overflow, while other languages should not store `t` in a 32-bit integer.
- **Input mutation:** Every inner list gains an index and the outer list is sorted. Callers requiring preservation must pass a copy or use a separate triple list.
