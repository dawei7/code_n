## General

**Model positions as an implicit unweighted graph**

Only the position of the single one matters. The surrounding zeroes are indistinguishable, so the full array never needs to be constructed.

Think of every non-banned index as a graph vertex. There is a directed move from current position $i$ to position $j$ when some length-$k$ subarray containing $i$ moves the one to $j$ after reversal. Every reversal costs one operation, so the requested minimum operation counts are shortest-path distances from starting vertex $p$.

This immediately suggests breadth-first search. The challenge is not BFS itself; it is enumerating all positions reachable from one index without trying every possible reversal repeatedly.

**Derive the destination of one reversal**

Suppose the reversed subarray starts at $l$ and ends at $l+k-1$. Within that interval, reversal maps position $i$ to

$$
j=l+(l+k-1-i)=2l+k-1-i.
$$

The chosen interval must both fit in the array and contain $i$. Therefore,

$$
\max(0,i-k+1)\le l\le\min(i,n-k).
$$

As $l$ increases by one, destination $j$ increases by two. All reachable destinations consequently have the same parity.

Substituting the smallest and largest legal $l$ values gives the inclusive destination range:

$$
\begin{aligned}
mi&=\max(i-k+1,\ k-i-1),\\
mx&=\min(i+k-1,\ 2n-k-i-1).
\end{aligned}
$$

These are exactly the formulas used by the solution. From position $i$, every index between `mi` and `mx` having parity `mi % 2` is reachable in one reversal, and no other index is.

**Why the range has no parity gaps**

Each legal start $l$ maps to one destination $2l+k-1-i$. Consecutive legal starts map to destinations differing by exactly two, so they fill the appropriate parity subsequence from `mi` through `mx`.

The mapping is also reversible: for a same-parity destination $j$ in that interval,

$$
l=\frac{i+j-k+1}{2}
$$

is an integer and lies between the legal start bounds. Thus the arithmetic range is not merely a safe superset; it describes the reachable positions exactly.

**Store only unvisited allowed positions**

The solution maintains two ordered sets:

- `ts[0]` contains unvisited allowed even indices;
- `ts[1]` contains unvisited allowed odd indices.

Initially every array index enters its parity set. The starting index $p$ is removed because its distance is already zero. Every banned index is removed because the one may never occupy it.

Separating parity is valuable because a BFS step needs only one parity. Within the selected set, all stored values already satisfy the step-of-two requirement, so the algorithm needs only an ordinary numeric interval query.

Each set also receives sentinel value $n$. Real destinations are at most $n-1$, so the sentinel can never be accepted. It guarantees that indexing the result of `bisect_left` is safe even when no real position remains at or above `mi`.

**Enumerate a reachable interval efficiently**

When BFS removes position `i` from the queue, it calculates `mi` and `mx` and selects `s = ts[mi % 2]`.

`s.bisect_left(mi)` finds the first still-unvisited allowed position not below `mi`. If that position is at most `mx`, it is a valid one-operation neighbor:

- append it to the queue;
- assign `ans[neighbor] = ans[i] + 1`;
- remove it from the ordered set.

The code then searches from `mi` again. Because the just-used position was removed, the new lower-bound query returns the next remaining candidate. The loop stops at the first value above `mx`, which may be the sentinel.

Removing a position at discovery time is essential. It prevents the same vertex from being generated from many earlier positions and bounds the total number of successful inner-loop iterations by $n$.

**Why BFS distances are minimal**

The queue begins with $p$ at distance zero. Whenever an unvisited position $j$ is discovered from $i$, the reversal formula proves there is a legal edge $i\to j$, so `ans[i] + 1` is a feasible operation count.

Breadth-first search processes vertices in nondecreasing distance order. Therefore, the first time $j$ is discovered, no shorter route to it can exist: every possible predecessor at a smaller distance would already have been processed. Removing $j$ after this first discovery is safe.

The ordered sets omit only three kinds of positions: the source, banned positions, and previously discovered positions. None needs rediscovery. Hence interval enumeration loses no unvisited legal neighbor, and ordinary BFS correctness gives the minimum operation count for every reachable index.

Positions never discovered retain the initial value `-1`, exactly representing impossibility.

**Trace the full-reversal example**

For $n=4$, $p=0$, and $k=4$, the only legal subarray is the whole array. At $i=0$,

$$
mi=mx=3.
$$

Index three is allowed, so BFS assigns distance one. Banned indices one and two were removed before the search and can never enter the queue. The answer becomes `[0,-1,-1,1]`.

When $k=1$, the formulas give `mi = mx = i`. The starting index has already been removed, and no other position can be reached. This matches the fact that reversing one element changes nothing.

**The exact data structure versus the manifest**

The manifest describes successor disjoint sets with almost-constant amortized removal, but the exact solution imports and uses `SortedSet`. The high-level idea is the same—enumerate each unvisited reachable index only once—but its operation costs are logarithmic. The complexity below follows the actual ordered-set implementation.

## Complexity detail

Let $n$ be the array length. Initial insertion of all indices into ordered sets costs $O(n\log n)$ with `SortedSet`, and removing banned indices costs at most $O(n\log n)$.

Every real index is appended to the BFS queue at most once and removed from its set at most once. Each successful enumeration performs ordered-set searches and a removal, each costing $O(\log n)$. There is also one final unsuccessful lower-bound lookup per processed BFS vertex. Total time is therefore $O(n\log n)$ for the exact code.

The manifest's $O(n\alpha(n))$ bound applies to the alternative successor-disjoint-set implementation, not `SortedSet`.

The answer, queue, and two sets collectively store $O(n)$ integers. The sentinels add constant space, so total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Successor disjoint set:** Maintain “next unvisited index” links separately by parity. Deleting an index unions it with its successor and yields $O(n\alpha(n))$ time, matching the manifest.
- **Balanced ordered sets:** The exact solution is easier to read and supports lower-bound queries directly, at the cost of $O(\log n)$ per discovery.
- **Try every reversal from every BFS state:** This can revisit the same destinations many times and degrade toward $O(n^2)$.
- **Banned starting position:** The contract guarantees $p$ is not banned, so its required distance zero is valid.
- **`k = 1`:** Reversal cannot move the one; only $p$ has a nonnegative answer.
- **`k = n`:** Each position has at most the single mirror destination $n-1-i$.
- **Parity restriction:** Only the parity determined by $k-1-i$ is reachable in one step; scanning both parity sets wastes work and risks invalid moves.
- **Unreachable allowed index:** It remains `-1` even though it was not banned.
- **Sentinel safety:** Since `mx <= n-1`, sentinel $n$ always terminates the interval loop and is never queued.
- **Removal timing:** A neighbor must leave its set when discovered, not later when dequeued, or multiple parents could enqueue it.
