## General
**Why sorting turns the assignment into contiguous groups**

Sort the house positions. In an optimal solution, houses served by one mailbox can be taken as a contiguous interval of this order. If two houses $a<c$ use one mailbox while an intermediate house $b$ uses a different mailbox, assigning $b$ consistently across the boundary cannot increase the one-dimensional nearest-distance optimum; optimal service regions are separated by ordered breakpoints.

The problem therefore becomes partitioning the sorted houses into exactly $k$ nonempty contiguous groups and placing one optimal mailbox for each group.

**The median minimizes one group's distance**

For a sorted interval from index `left` through `right`, the sum of absolute distances is minimized at a median position. Pair the outermost houses. Wherever a mailbox lies between their positions, that pair contributes at least

$$
\texttt{houses[right]}-\texttt{houses[left]}.
$$

Removing the pair leaves the same problem for the inner interval. Hence its optimal one-mailbox cost satisfies

$$
C[\texttt{left}][\texttt{right}]
=
C[\texttt{left}+1][\texttt{right}-1]
+
\texttt{houses[right]}-\texttt{houses[left]}.
$$

Empty and one-house inner intervals cost zero. Filling intervals by increasing length computes every $C$ entry in constant time after sorting, for quadratic preprocessing rather than re-summing every interval.

**Partitioning prefixes among mailboxes**

Let `previous[i]` be the minimum distance for the first `i` sorted houses using one fewer mailbox layer, with `previous[0] = 0` before any groups. For each number of mailboxes `boxes`, compute `current[end]`, the optimum for the first `end` houses.

Choose `start` as the number of houses handled by earlier mailboxes. The final mailbox serves indices `start` through `end - 1`, so

$$
\texttt{current[end]}
=
\min_{\texttt{start}}
\left(
\texttt{previous[start]}
+
C[\texttt{start}][\texttt{end}-1]
\right).
$$

Require at least `boxes - 1` houses before the final group and at least one house in it. Rolling the mailbox layers retains only two length-$N+1$ arrays.

**Why the dynamic program gives the global optimum**

Every feasible allocation induces $k$ ordered, nonempty service groups after sorting. Its last group begins at some `start`; the earlier groups have cost at least the stored optimum for that prefix, and the last group costs at least its median cost $C$. Thus the transition considers a value no larger than the allocation's cost.

Conversely, every transition combines an optimal partition of a prefix with one median-served contiguous suffix, producing a valid allocation with the recorded cost. Minimizing over all split positions therefore yields exactly the optimal $k$-mailbox allocation.

## Complexity detail
Sorting costs $O(N\log N)$. The interval recurrence fills $O(N^2)$ entries. The partition DP has $k$ layers, $N$ prefix endpoints, and up to $N$ split positions per state, for $O(kN^2)$ time, which dominates because $k\ge1$.

The interval-cost table uses $O(N^2)$ space. Two rolling DP arrays use $O(N)$ additional space, so total space is $O(N^2)$.

## Alternatives and edge cases
- **Re-sum every interval around its median:** This computes correct group costs but adds an inner interval traversal, taking $O(N^3)$ preprocessing time.
- **Top-down partition memoization:** Memoizing house index and mailboxes remaining explores the same $O(kN)$ states, but each state still tries split endpoints and recursion adds stack overhead.
- **Try mailbox coordinates directly:** The street coordinate range is not the useful search space; medians prove that only group partitions need consideration.
- **Prefix sums for interval cost:** Median distance can also be computed in $O(1)$ from prefix sums after sorting. It matches the recurrence's asymptotic bounds but uses more algebra.
- **One mailbox:** The answer is the total distance to a median of all sorted houses.
- **One mailbox per house:** When `k == N`, place a mailbox at every house and return zero.
- **Unsorted input:** Sorting is essential before assuming contiguous service groups or using median indices.
- **Even group size:** Any position between the two middle houses minimizes the group cost; either median index yields the same sum.
- **Widely separated clusters:** The DP naturally places partition boundaries across large gaps when mailbox count permits.
- **Distinct positions:** Equal coordinates do not occur, but the median and recurrence would remain valid if they did.
