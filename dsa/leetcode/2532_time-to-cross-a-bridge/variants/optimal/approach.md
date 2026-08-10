## General

**Model workers in four off-bridge states**

At any moment, a worker is in exactly one of these collections:

- `wait_in_left`: ready on the left to cross right and fetch a box;
- `work_in_right`: picking up a box, unavailable until a completion time;
- `wait_in_right`: ready on the right with a box and waiting to cross left;
- `work_in_left`: putting down a returned box, unavailable until completion.

The bridge itself is simulated by advancing current time `cur` whenever one chosen worker crosses. Since crossings are never simultaneous, no separate bridge-occupancy structure is needed.

**Turn worker indices into efficiency ranks**

The code sorts `time` by `right_i+left_i` in ascending order. Python's sort is stable, so equal crossing sums remain in original worker-index order.

After sorting:

- a larger sorted index has a larger crossing sum, or the same sum and a larger original index;
- therefore, a larger sorted index means a less efficient worker under the problem's exact ordering.

The simulation can use these sorted indices as efficiency ranks. It does not need original IDs because the answer asks only for elapsed time.

**Waiting heaps choose the least efficient worker**

Python heaps return the smallest key. Waiting heaps store `-i`, so the most negative key corresponds to the largest sorted index and hence the least efficient waiting worker.

All workers begin on the left, and indices 0 through `k-1` are inserted into `wait_in_left`.

There are separate waiting heaps per side because right-side workers always receive bridge priority over left-side workers.

**Working heaps are ordered by completion time**

`work_in_right` stores `(pick_finish_time,i)`. `work_in_left` stores `(put_finish_time,i)`. Their smallest tuples expose the next worker to finish off-bridge work.

At the beginning of every simulation cycle, both completion heaps release all workers whose finish time is at most `cur` into the corresponding waiting heap.

Releasing all of them before selecting a bridge user is essential: bridge priority must compare every worker actually ready at that time, not just the first completion event.

**Decide which direction crosses next**

`right_to_go` is true whenever a worker waits on the right. Such a worker has already picked up a box and receives unconditional priority.

`left_to_go` is true only when:

- at least one undispatched box remains, `n>0`;
- a worker waits on the left.

If enough workers have already been sent to account for all boxes, `n==0` prevents dispatching another left-side worker.

When both directions are possible, the code checks `right_to_go` first, enforcing the rule that a box-carrying right worker crosses before any left worker.

**Dispatch a worker from the left**

Pop the least efficient left waiter. Crossing right takes `time[i][0]`, so add it to `cur`.

One box is now assigned to this worker, so decrement `n` immediately. The worker will finish picking at

`cur+time[i][1]`,

which is pushed into `work_in_right`.

Decrementing on dispatch, rather than pickup completion, correctly enforces “no more workers once enough have been dispatched.”

**Return a worker from the right**

Pop the least efficient right waiter and add `time[i][2]` for the right-to-left crossing. At this instant, that worker and its box reach the left side.

If `n==0` and both right-side heaps are now empty, every box has been dispatched and the just-returned box is the last outstanding one. The function returns `cur` immediately.

It intentionally does not wait for this worker's put time, because the requested moment is when the last box reaches the left side of the bridge.

If more boxes remain in transit or waiting, schedule this worker's put completion at `cur+time[i][3]` in `work_in_left`. Only after putting the box down may the worker wait on the left again.

**Jump when the bridge has nobody ready**

If neither side has an eligible waiter, no bridge event can occur at current time. The next meaningful time is the earliest pick or put completion.

The code takes the minimum finish time at the tops of `work_in_left` and `work_in_right` and assigns it to `cur`. The next loop then releases every worker completing at that time.

This event jump avoids simulating empty minutes one by one.

**Why the event simulation is faithful**

Before each bridge decision, the four heaps contain exactly the workers in their four states, and all completions through `cur` have been released. The direction checks implement right priority and the dispatch limit. Negative rank heaps implement least-efficiency priority within a side.

Each crossing advances time by its exact duration and schedules the worker's next state at its exact finish time. Induction over events proves the simulated schedule is exactly the mandatory schedule from the statement.

The terminating right crossing is exactly when the final box arrives on the left, so the returned time matches the requested endpoint.

## Complexity detail

Sorting `k` workers costs $O(k\log k)$. Each dispatched box causes one left-to-right and one right-to-left crossing. Workers enter and leave work heaps a constant number of times per carried box, and every heap operation costs $O(\log k)$.

Total time is $O((n+k)\log k)$. Event jumps add only constant work per completion.

Across the four heaps, at most `k` workers are stored at once. Auxiliary space is $O(k)$. Sorting mutates the input `time` order.

## Alternatives and edge cases

- **Minute-by-minute simulation:** It wastes time across long pick or put intervals; completion heaps allow jumps.
- **One waiting heap:** It cannot enforce unconditional right-side priority cleanly.
- **Efficiency ties:** Stable sorting preserves original index order, so larger sorted rank remains less efficient.
- **Several simultaneous completions:** Release all before choosing the least efficient waiter.
- **No boxes left to dispatch:** Do not send another left worker even if one waits.
- **Final box:** Return after its left crossing without waiting for put time.
- **One worker:** The same worker cycles through all four stages for every box.
- **Right-side priority:** It is checked before left dispatch whenever both wait.
- **Idle bridge:** Advance to the earliest work completion.
- **Input mutation:** Sorting reorders worker rows into efficiency rank order.
