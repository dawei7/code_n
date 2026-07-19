## General
**Separate future tasks from currently available tasks**

Attach each task's original index and sort the triples by enqueue time. A pointer divides this ordered list: earlier entries have already been made available, while later entries remain in the future.

Store available tasks in a min-heap keyed by `(processingTime, index)`. This key exactly matches the CPU rule: the root has the shortest duration, and tuple ordering chooses the smaller index when durations tie.

**Advance simulated time only through meaningful events**

If the heap is empty, no available work exists. Jump the clock directly to the next enqueue time instead of advancing it one unit at a time. Then push every task whose enqueue time is at most the current clock.

Pop the heap root, append its original index, and increase the clock by its full processing time. This models non-preemption. Before the next selection, push all tasks that arrived during that interval, including tasks enqueued exactly at the completion time.

**Why every heap choice matches the CPU**

At each selection event, the sorted-list pointer has moved past exactly the tasks with enqueue time at most the current clock, so the heap contains all and only unfinished available tasks. Its lexicographically smallest key implements both required priority rules. Running that task to completion and adding newly arrived tasks reconstructs the same state for the next event. Induction over the $n$ selections proves that the reported order is the CPU's order.

## Complexity detail
Sorting $n$ indexed tasks takes $O(n\log n)$ time. Each task enters and leaves the heap once, adding another $O(n\log n)$ time. The sorted triples, heap, and returned order each hold at most $n$ entries, so space is $O(n)$.

## Alternatives and edge cases
- **Scan all waiting tasks per selection:** It can apply the same priority rule but may inspect $\Theta(n)$ candidates for each of $n$ tasks, taking $O(n^2)$ time.
- **Advance time one unit at a time:** This is infeasible when enqueue times are near $10^9$; jump directly to the next arrival.
- **Sort only by processing time:** Future tasks are not eligible, so a single static processing-time ordering is incorrect.
- **Equal processing times:** Choose the smaller original task index, not the earlier position in the enqueue-time sort.
- **Equal enqueue times:** Add every task from that timestamp before selecting one.
- **Arrival during processing:** The running task is never interrupted; the arrival waits in the heap.
- **Arrival at completion:** It is eligible for the immediately following selection.
- **Idle gaps:** An empty heap requires a clock jump before attempting to pop.
- **Large cumulative time:** The total clock may exceed individual $10^9$ bounds, so use an integer type capable of holding the sum.
- **Single task:** Jump to its enqueue time, run it, and return index 0.
