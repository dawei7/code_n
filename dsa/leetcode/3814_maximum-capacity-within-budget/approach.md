## General

**Discard machines that can never participate**

Every cost and capacity is positive. If one machine has `cost >= budget`, selecting it alone already violates the strict requirement, and adding a second positive-cost machine cannot help. The source therefore builds `arr` using only pairs `(cost, capacity)` whose cost is strictly below `budget`.

This filter is safe for both one-machine and two-machine choices. It also handles the zero-machine option implicitly: if `arr` is empty, no individual machine is affordable, so the best achievable capacity is 0.

The remaining tuples are sorted. Python sorts a pair first by cost and then by capacity, so costs are nondecreasing:

$$
a_0\le a_1\le\cdots\le a_{m-1},
$$

where $m$ is the number of individually affordable machines. The secondary capacity ordering among equal costs is not required for correctness, but it does not hurt.

**Keep the best capacity inside the currently feasible partner range**

For a fixed first machine at sorted index `i`, only later indices need to be considered as its partner. Any pair has one smaller sorted index, and the algorithm evaluates that pair when this smaller index becomes `i`. This prevents pairing a machine with itself and avoids reconsidering the same unordered pair from both directions.

Because costs are sorted, feasible later partners form a prefix of the later indices. If index `j` satisfies

$$
a_i+a_j<\texttt{budget},
$$

then every index $k$ with $i<k\le j$ is also feasible because $a_k\le a_j$. Conversely, once the largest remaining cost is too expensive, that index cannot partner with `i`.

The source maintains this changing set of candidates in `remain`, a `SortedList` of pairs `(capacity, sorted_index)`. Ordering by capacity first means `remain[-1][0]` is the maximum capacity among all currently stored candidates. The sorted index is included to make every entry unique even when two distinct machines have equal capacities.

Initially, `remain` contains every machine in `arr`. The right pointer `j` begins at the last sorted index. Before evaluating a fixed `i`, the source discards `(arr[i][1], i)` so that the machine cannot be selected twice.

It then checks the most expensive surviving endpoint. While `arr[i][0] + arr[j][0] >= budget`, index `j` is illegal because equality is forbidden as well as greater cost. That entry is discarded from `remain` and `j` moves left. When the loop stops with `i < j`, every remaining index from `i + 1` through `j` has a legal total cost with `i`.

At this point, `remain[-1]` does not identify the cheapest legal partner. It identifies the legal partner with greatest capacity, which is exactly what should be combined with `arr[i][1]`. Cost determines eligibility; among eligible machines, only capacity affects the objective.

**Why removed right endpoints never need to return**

As `i` moves right, `arr[i][0]` never decreases. Suppose a high-cost endpoint `j` is too expensive for the current `i`:

$$
a_i+a_j\ge\texttt{budget}.
$$

For any later first index $i'>i$, $a_{i'}\ge a_i$, so

$$
a_{i'}+a_j\ge a_i+a_j\ge\texttt{budget}.
$$

That endpoint is also illegal for every future iteration. It can be removed permanently, which is why `j` only moves left. This monotonicity prevents an $O(N^2)$ restart of the partner search.

After an iteration, `i` increases. At the beginning of the next iteration, its own entry is discarded. Inductively, `remain` contains exactly the later indices that have not been permanently rejected for excessive cost. Once the inner loop finishes, those are precisely the valid partners for the current first index.

Every legal pair is considered in the following sense: when its smaller sorted index is `i`, its larger index lies in the feasible range, and `remain` contains it. The algorithm need not calculate that particular pair if another feasible partner has higher capacity; using the maximum capacity can only produce an equal or better total for the same first machine.

**Preserve the at-most-two choice**

The answer is initialized as `remain[-1][0]` before any machine is removed. At that moment `remain` contains all individually affordable machines, so this is the largest valid one-machine capacity.

That baseline matters when no pair fits. For example, machines with costs 3 and 4 under budget 7 are each affordable but cost exactly 7 together, so the strict inequality rejects the pair. The result must still be the best individual capacity.

Each later update uses

`ans = max(ans, arr[i][1] + remain[-1][0])`

only when `remain` is nonempty. Since capacities are positive, a legal pair is better than either of its members alone, but the single-machine baseline is still necessary for instances with no legal pair. Choosing zero machines contributes 0 and cannot beat an affordable machine's positive capacity; it matters only when `arr` is empty.

**The exact source differs from the manifest summary**

The manifest describes “prefix maxima” and “binary-searching legal earlier partners.” That is a valid $O(N\log N)$ strategy, but it is not what this source implements. The exact source uses two monotone pointers plus a dynamically maintained `SortedList` of partner capacities. No prefix-maximum array is built, and no binary search appears in the function.

The approach must follow the executable source: `i` fixes the smaller-cost endpoint, `j` removes permanently unaffordable large endpoints, and `remain[-1]` supplies the largest capacity among the surviving later machines.

For the first example, sorting the affordable machines gives costs 3, 4, and 5 with capacities 7, 1, and 2; cost 8 is filtered out. With cost 3 fixed, cost 5 is rejected because $3+5=8$ is not strictly below 8. The surviving cost-4 machine has capacity 1, so the pair yields $7+1=8$. Later first costs have no valid distinct partner, and the answer stays 8.

## Complexity detail

Let $M\le N$ be the number of machines whose individual cost is below `budget`. Filtering costs $O(N)$ time. Sorting `arr` costs $O(M\log M)$. Inserting the $M$ entries into `SortedList` one at a time costs $O(M\log M)$ in the standard ordered-multiset complexity model.

The outer pointer advances at most $M$ times, and the right pointer retreats at most $M$ times total. Each entry is discarded only a constant number of times; `discard` also safely tolerates an entry that was previously removed as a right endpoint. Each ordered-list addition or removal is treated as $O(\log M)$, while retrieving `remain[-1]` is $O(1)$. The total time is therefore $O(N+M\log M)=O(N\log N)$.

The filtered array and ordered multiset each hold at most $M$ tuples, so auxiliary space is $O(M)$ and hence $O(N)$. The source assumes that the execution environment supplies `SortedList`; it is not a Python built-in.

## Alternatives and edge cases

- **Prefix maximum plus binary search:** Sort by cost, build the best capacity over every prefix, and for each machine binary-search the largest partner cost strictly below `budget - cost` while excluding the same index. This matches the manifest summary and also achieves $O(N\log N)$ time, but it is not the exact source's data flow.
- **Quadratic pair enumeration:** Testing every pair is straightforward and handles the strict inequality directly, but it costs $O(N^2)$ and is too slow for $N=10^5$.
- **Cost-indexed maximum table:** Since `budget <= 2 * 10^5`, capacities can be aggregated by cost and prefix maxima built over the numeric cost domain. Distinct-machine handling for two equal-cost selections still requires retaining the best two capacities at a cost.
- **No individually affordable machine:** Filtering produces an empty array and the function correctly returns 0.
- **Exactly equal to the budget:** A single cost equal to `budget` is filtered out, and a pair sum equal to `budget` is removed by the `>=` condition. Both reflect the exclusive bound.
- **Only one affordable machine:** `ans` is initialized from that machine, the `i < j` loop never runs, and its capacity is returned.
- **Equal costs:** Sorting may order them by capacity, but their distinct sorted indices keep them separate. Two equal-cost machines may be paired when twice the cost is strictly below the budget.
- **Equal capacities:** Including the sorted index in each `SortedList` tuple prevents two machines from collapsing into one multiset entry.
- **Best pair need not use the cheapest machine:** Every sorted index eventually serves as the smaller endpoint while a later partner exists, so a higher-cost, higher-capacity pair is still evaluated.
- **Positive capacities:** The largest affordable individual machine is always at least as good as selecting zero machines. If capacities could be negative, the zero-machine option would need explicit comparison, but the contract excludes that case.
- **External ordered-container dependency:** `SortedList` must be provided by the harness or imported from its supporting library. Replacing it with an ordinary list would make middle removals linear and could degrade the algorithm to quadratic time.
