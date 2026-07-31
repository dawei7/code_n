## General

Let $R$ be the number of robots and $F$ the number of factories. Sort both groups by position. There is an optimal assignment with no crossing pairs: if robots $a\le b$ are sent to factories $y\le x$ respectively, swapping their destinations to $x$ and $y$ cannot increase the sum of absolute distances. Consequently, each factory repairs a contiguous block of the sorted robots, possibly an empty block.

After processing some factories, let `previous[i]` be the minimum cost to repair the first $i$ robots. For the next factory at position $p$ with capacity $c$, define

$$
P_i=\sum_{q=0}^{i-1}\lvert\texttt{robots[q]}-p\rvert.
$$

If this factory receives robots with sorted indices $j$ through $i-1$, their cost is $P_i-P_j$ and capacity requires $i-c\le j\le i$. Therefore

$$
\texttt{current[i]}=P_i+\min_{\max(0,i-c)\le j\le i}\bigl(\texttt{previous[j]}-P_j\bigr).
$$

**Sliding transition minimum.** As $i$ increases, the allowed $j$ interval slides one step right. Maintain candidate indices in a deque whose corresponding values `previous[j] - prefix[j]` increase from front to back. Before evaluating state $i$, remove dominated values from the back, append $i$, and discard indices smaller than $i-c$ from the front. The front then gives exactly the minimum required by the recurrence in amortized constant time.

The initial row is zero for no robots and infinity for every positive count. Processing every factory yields the minimum cost for all robots in the final state. The noncrossing property proves the recurrence covers an optimal assignment, and every transition respects the selected factory's capacity.

## Complexity detail

Sorting costs $O(R\log R+F\log F)$. For each of $F$ factories, constructing its distance prefix array and scanning all $R+1$ states takes $O(R)$ time. Every state enters and leaves the deque at most once per factory, so total time is $O(R\log R+F\log F+RF)$.

The previous row, current row, prefix distances, and deque each contain $O(R)$ entries. The implementation also makes sorted copies of both inputs, so total auxiliary space is $O(R+F)$.

## Alternatives and edge cases

- **Capacity-enumerating DP:** Trying every block length from zero through a factory's capacity is direct and correct, but takes $O(FR^2)$ time in the worst case.
- **Expanded factory slots:** Repeating each factory position according to capacity gives a simpler assignment DP, but total capacity can be $RF$, producing a larger state space.
- **Min-cost flow:** Robots, factories, and capacities form a transportation problem, but a general flow algorithm ignores the one-dimensional noncrossing structure and is substantially heavier.
- **Zero-capacity factory:** Its transition can only keep the same robot count; the deque window naturally has width one.
- **Robot at a factory:** Its contribution is zero and is handled by the absolute-distance prefix sum.
- **Negative coordinates:** Sorting and absolute differences work unchanged on either side of the origin.
- **Unused capacity:** The recurrence permits a factory to repair any number from zero through its limit; capacity need not be filled.
- **Large coordinates:** Total distance can exceed 32-bit range, so the implementation uses arbitrary-precision integers and a safely large sentinel.
