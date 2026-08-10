## General

**Represent a task group by a bit mask**

With at most 14 tasks, every subset can be represented by an integer mask. Bit `j` is one when task `j` belongs to that subset.

The final scheduling problem is a partition of the full task set into the fewest subsets whose total times do not exceed `sessionTime`. Task order inside a session is irrelevant because only the sum matters and every task fits individually by contract.

**Precompute which subsets fit in one session**

`ok[mask]` records whether all tasks selected by `mask` can be completed in a single session. For each nonempty mask, the source sums `tasks[j]` over its set bits and compares the result with `sessionTime`.

This prevents the later partition loop from recomputing a session's total every time the same submask appears inside a larger state.

The empty subset remains false, but the transition enumerates only nonempty submasks, so no empty session is ever added.

**Define the minimum-session state**

`f[mask]` is the minimum number of sessions needed to finish exactly the tasks selected in `mask`. `f[0] = 0` because no tasks require no sessions. All nonempty states begin at infinity.

For a target mask `i`, choose any nonempty submask `j` that fits in one session. Schedule those tasks together as one session, and optimally schedule the remaining tasks `i ^ j`. Since `j` is a subset of `i`, XOR clears exactly the selected bits and is equivalent to set difference.

The transition is

`f[i] = min(f[i], f[i ^ j] + 1)`.

**Enumerate every submask**

The standard update

`j = (j - 1) & i`

visits every nonempty submask of `i` exactly once. Subtracting one changes the low bits, and AND with `i` removes bits not available in the parent mask.

The loop starts at `j = i`, so it first considers placing all remaining tasks into one session. It eventually reaches the smallest submasks and stops after the next update produces zero.

**Why dependencies are already computed**

For every nonempty `j`, `i ^ j` contains fewer set bits and is numerically smaller than `i` because at least one set bit is cleared and no new bit is added. The outer loop processes masks in increasing integer order, so `f[i ^ j]` is available.

**Why the recurrence is correct**

Any feasible schedule for tasks in `i` has some one of its sessions containing a nonempty subset `j` with total time at most the limit. Removing that session leaves a valid schedule for `i ^ j`. Hence the optimal schedule has cost at least `f[i ^ j] + 1` for one transition considered by the loop.

Conversely, every transition combines a feasible one-session subset `j` with an optimal schedule for the disjoint remaining tasks. It produces a legal schedule covering each task exactly once. Taking the minimum over all feasible choices therefore equals the optimum.

The final mask `(1 << n) - 1` contains every task, so `f[-1]` is the requested answer.

**Trace a simple schedule**

For tasks `[1, 2, 3]` and session limit three, masks for subsets `{1,2}` and `{3}` are both feasible. The full mask cannot fit in one session. A transition choosing `{1,2}` adds one to the already computed cost for `{3}`, producing two sessions.

No one-session transition covers the full mask, so the DP correctly returns two.

**The exact time bound is not the manifest bound**

The feasibility table takes $O(N2^N)$ work with the source's from-scratch summation. However, the partition phase enumerates all submasks of all masks.

Across $N$ bit positions, each bit has three roles in a pair $(i,j)$: absent from `i`, present in `i` but absent from `j`, or present in both. Therefore the total number of mask-submask pairs is $3^N$. The exact runtime is dominated by $O(3^N)$, not the manifest's $O(N2^N)$.

## Complexity detail

Feasibility precomputation costs $O(N2^N)$ time. The DP examines $3^N-2^N$ nonempty mask-submask relationships in total, each with constant transition work, so overall exact time is $O(3^N+N2^N)=O(3^N)$.

The `ok` and `f` arrays each have $2^N$ entries, giving $O(2^N)$ space. Scalar masks and subset-sum generator state add at most $O(N)$ transient space.

## Alternatives and edge cases

- **DP storing sessions and current load:** For each mask, keep the best pair of completed-session count and current-session usage, then add one task at a time in $O(N2^N)$ time; this matches the manifest.
- **Backtracking with sorting and pruning:** Often fast for $N=14$ but has a less direct worst-case guarantee.
- **Greedy largest-first packing:** It can be a useful heuristic but does not always minimize the number of bins/sessions.
- **All tasks fit together:** `ok[full_mask]` is true and the answer becomes one.
- **Every task needs its own session:** Only singleton submasks fit, so the answer is $N$.
- **Task equals `sessionTime`:** It fits, but no positive-time companion can join it.
- **Repeated task times:** Tasks still have distinct bit positions and must each be scheduled.
- **Empty state:** `f[0]=0` anchors every partition.
- **No task exceeds the limit:** The contract guarantees at least singleton feasibility, so every DP state has a finite schedule.
- **XOR removal:** It is safe only because `j` is enumerated as a submask of `i`.
- **Exact-source bound:** All-submask enumeration is $O(3^N)$ even though the manifest reports $O(N2^N)$.
- **Input preservation:** The method reads task durations without sorting or modifying them.
