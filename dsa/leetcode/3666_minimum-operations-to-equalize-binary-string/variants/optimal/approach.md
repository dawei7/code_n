## General

**Compress an entire string into its zero count**

An operation may choose any `k` distinct indices. Positions do not otherwise matter: among the chosen indices, only the number currently holding zero determines how the total zero count changes.

If two strings have the same length and the same number of zeros, they have the same possible next zero counts. Any selection described by “choose `c` zeros and `k - c` ones” can be made in either string.

The source therefore treats each integer from zero through `n` as a state. State `m` means the current string has exactly `m` zeros. The starting state is `s.count('0')`, and the target is zero.

This reduces a graph of up to `2^n` binary strings to only `n + 1` count states.

**Derive how many zeros may be selected**

Suppose the current state has `cur` zeros and `n - cur` ones. In one operation, choose `c` zeros and `k - c` ones.

There are two availability constraints:

`0 <= c <= min(cur, k)`

because we cannot choose more zeros than exist or more than all `k` selected positions, and

`k - c <= n - cur`

because enough ones must exist for the other selections.

Rearranging the second inequality gives

`c >= k - n + cur`.

Combining it with non-negativity, the feasible range is

`max(k - n + cur, 0) <= c <= min(cur, k)`.

Every integer `c` in this interval is achievable by choosing arbitrary occurrences of the required two types.

**Compute the resulting zero count**

Of the original `cur` zeros, the selected `c` flip to ones, leaving `cur - c` zeros.

The selected `k - c` ones flip to zeros, adding that many. The new zero count is

`cur - c + (k - c) = cur + k - 2c`.

As `c` increases by one, the result decreases by two. Therefore all one-operation destinations form an inclusive numeric interval with one fixed parity.

The smallest destination uses the largest feasible `c = min(cur, k)`:

`l = cur + k - 2 * min(cur, k)`.

The largest uses the smallest feasible `c = max(k - n + cur, 0)`:

`r = cur + k - 2 * max(k - n + cur, 0)`.

Reachable values are

`l, l + 2, l + 4, ..., r`.

They all have parity `l % 2`, equivalently `(cur + k) % 2`.

**Use breadth-first search for the minimum operation count**

Every graph edge represents exactly one operation and has equal cost. Breadth-first search is therefore the correct shortest-path method.

The queue initially contains the starting zero count. Variable `ans` is the number of operations used to reach every state currently in the queue’s layer.

Before expanding the layer, the source records its current queue length and processes exactly those entries. Newly discovered states go to the back for the next layer. If state zero is removed, `ans` is the minimum possible operation count because BFS visits states in non-decreasing distance.

**Why scanning every interval repeatedly would be quadratic**

One state may reach `Theta(n)` other counts. Iterating over all same-parity values in `[l, r]` every time could reconsider states many times and cost `O(n^2)`.

The source stores unvisited states in two ordered sets:

- `ts[0]` contains unvisited even counts.
- `ts[1]` contains unvisited odd counts.

The start is removed immediately so it cannot be enqueued again.

For current interval `[l, r]`, only set `ts[l % 2]` can contain reachable states. `bisect_left(l)` finds the first unvisited state not below `l`. While that state remains at most `r`, the method enqueues and removes it.

After removal, the next ordered-set element shifts into the same logical index `j`, so the loop deliberately does not increment `j`.

**Each state is processed at most once**

As soon as a zero count is discovered, it is removed from its parity set. No later interval can discover it again.

Thus, although many reachability intervals overlap, every integer state is extracted from an ordered set at most once and enqueued at most once. The sets provide an efficient way to enumerate only new nodes within each arithmetic-progression interval.

This is the central optimization: BFS still explores the exact graph, but it never scans already-visited destinations repeatedly.

**Trace `s = "0101", k = 3`**

The start has two zeros, so `cur = 2` and `n = 4`.

The maximum selected zeros is two, producing

`l = 2 + 3 - 2 * 2 = 1`.

The minimum selected zeros is `max(3 - 4 + 2, 0) = 1`, producing

`r = 2 + 3 - 2 * 1 = 3`.

After one operation, reachable zero counts are one and three. From state one, selecting its one zero and two ones produces zero zeros after another operation. BFS reaches target at depth two.

**Trace the impossible example**

For `"101"` with `k = 2`, the start has one zero. Since `k` is even, every transition preserves zero-count parity:

`new = cur + even - 2c`.

Starting odd, the BFS can reach only odd states and never zero. Its reachable component is exhausted and the method returns `-1`.

**Parity is useful but not the whole problem**

When `k` is even, parity immediately rules out an odd starting zero count. When `k` is odd, parity alternates on every operation.

However, parity alone does not determine reachability or the minimum number of operations. Availability constraints can narrow `[l, r]`, especially near zero or `n`. The BFS handles both parity and capacity exactly.

**The exact source differs from the manifest**

The manifest claims an `O(n)`-time, `O(1)`-space arithmetic method. The stored `solution.py` instead implements the ordered-set BFS described above.

It allocates all `n + 1` states, a queue, and two `SortedSet` instances. Its actual bounds are `O(n log n)` time and `O(n)` space, matching the local editorial’s BFS rather than the manifest summary.

The approach documents the code that actually runs. A closed-form derivation, if independently established and implemented, would be a separate alternative.

## Complexity detail

Initializing the two ordered sets with all counts zero through `n` performs `n + 1` insertions. In the exact loop-based source, this costs `O(n log n)`.

Each state is removed at most once. Every interval expansion performs one binary search plus ordered-set indexing and removal operations, each logarithmic under `SortedSet`. Across all states, BFS work is `O(n log n)`.

Counting initial zeros takes `O(n)`, so total time remains `O(n log n)`.

The two sets collectively hold at most `n + 1` integers. The queue can also hold `O(n)` states. Auxiliary space is `O(n)`.

These are the exact source bounds, not the manifest’s `O(n)` time and `O(1)` space.

## Alternatives and edge cases

- **Closed-form parity/capacity analysis:** The manifest describes deriving the smallest feasible operation count arithmetically. That would avoid BFS if fully proven, but it is not the stored implementation.
- **BFS over complete strings:** It has up to `2^n` states and is infeasible.
- **BFS over zero counts with ordinary interval loops:** It has only `n + 1` states but can rescan the same destinations quadratically.
- **Disjoint-set “next unvisited” structure:** Successor pointers can enumerate and delete interval states in near-linear time without a third-party ordered set.
- **Ignore the parity step:** Reachable counts differ by two, not one. Scanning the other parity invents impossible transitions.
- **Already all ones:** The start state is zero, so BFS returns zero operations immediately.
- **`k = 1`:** Each operation can flip one zero to one; the minimum is the initial zero count, which BFS discovers layer by layer.
- **`k = n`:** Every operation flips the whole string, so the zero count alternates between `cur` and `n - cur`. Only those states are reachable.
- **Even `k` and odd zero count:** Parity never changes, making target zero unreachable.
- **Choose fewer than `k` indices:** Not allowed. The transition derivation always selects exactly `c + (k-c) = k` distinct positions.
- **Index identities:** They do not matter once the counts of zeros and ones are known because any subset of the required sizes can be selected.
- **Removing while iterating:** The source keeps the same ordered-set index after deletion so the shifted successor is examined next.
- **Input preservation:** The string is immutable and only its zero count is stored.
- **Missing imports/dependency:** The stored source uses `SortedSet` and `deque` without imports. It requires the appropriate ordered-set package and `collections.deque` in a standalone environment.
