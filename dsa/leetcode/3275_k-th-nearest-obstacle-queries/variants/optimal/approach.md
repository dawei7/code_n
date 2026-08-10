## General

After each insertion, only the $k$ smallest distances matter. Among those retained distances, the largest is exactly the $k$-th nearest. The source implements a size-$k$ max-heap using Python's min-heap by storing negative distances.

For obstacle $(x,y)$, the required Manhattan distance is `abs(x) + abs(y)`. Pushing its negative means a larger real distance is a smaller negative number and rises to the min-heap root. Thus `-pq[0]` is the largest retained real distance.

Every new distance is pushed. Once query index `i` is at least `k`, there are `k+1` inserted candidates in the heap before removal, so `heappop` discards the most negative entry: the largest real distance. The heap returns to size $k$ and contains the $k$ smallest distances seen so far.

The condition uses `i >= k` because indices are zero-based. After processing index `k-1`, exactly $k$ obstacles exist and none should be removed. After index `k`, the $(k+1)$-st obstacle has arrived and one must be discarded.

If fewer than $k$ obstacles have been inserted, the answer is minus one. Otherwise, `-pq[0]` is the largest of the retained $k$ nearest distances, which is precisely the order statistic requested.

For distances three, seven, five, and three with `k=2`, the heap first cannot answer, then retains three and seven with root representing seven. After five arrives, seven is removed, leaving three and five. After the final three, five is removed, leaving two threes and answer three.

**Why discarded distances never become relevant later.** Obstacles are only added. A distance outside the $k$ smallest at one time cannot later move ahead of retained smaller distances, because none of those disappear. It may be safely forgotten forever.

Equal distances are all valid separate obstacles. The heap stores duplicate numeric entries, and the $k$-th distance is defined with multiplicity, so no coordinate or uniqueness field is needed in the heap.

The answer list receives one entry per query. Coordinates themselves are not retained after their distance has been evaluated.

## Complexity detail

Let $n$ be the number of queries. The heap never exceeds $k+1$ entries. Each push and possible pop costs $O(\log k)$, giving $O(n\log k)$ time.

The heap uses $O(k)$ auxiliary space. The required answer uses $O(n)$ output space. Manhattan arithmetic is constant time.

## Alternatives and edge cases

- **Store all distances and sort after every query:** This repeats sorting and can cost $O(n^2\log n)$.
- **Balanced ordered multiset:** It can maintain all distances and select the $k$-th, but uses $O(n)$ space rather than discarding irrelevant values.
- **Min-heap of all distances:** Its root gives the nearest, not the $k$-th nearest, unless elements are destructively removed.
- **Negated max-heap:** This is the exact source technique because Python's standard heap is a min-heap.
- **`k = 1`:** The heap retains only the smallest distance, and every output after the first is the nearest obstacle.
- **Fewer than `k` queries processed:** Minus one is required even though the heap has a root.
- **Equal distances:** Duplicates remain separate heap entries and count toward rank.
- **Negative coordinates:** Absolute values correctly compute Manhattan distance in every quadrant.
- **Obstacle at the origin:** Its distance is zero and it will always belong to the retained nearest set.
- **Very large coordinates:** The sum can reach $2\cdot10^9$, safely represented by Python integers.
- **Unique coordinates but duplicate distances:** Coordinate uniqueness does not imply distance uniqueness; the heap correctly ignores that distinction.
- **Heap size invariant:** Push occurs before pop, allowing the new candidate and current worst retained candidate to compete uniformly.
- **Why the root is the rank answer:** Exactly $k$ values remain, all no larger than every discarded value. Their largest element has exactly $k-1$ retained values no greater than it when multiplicity is considered, making it the $k$-th order statistic.
- **New distant obstacle:** It is pushed, immediately becomes the most negative heap entry, and is popped again. Existing nearest distances and the answer remain unchanged.
- **New close obstacle:** It remains in the heap and causes the previous largest retained distance to be removed, so the reported $k$-th distance can only stay equal or decrease over time.
- **Monotonic answers after availability:** Once at least $k$ obstacles exist, adding obstacles cannot increase the $k$-th nearest distance. The maintained heap exhibits this property directly.
- **Why indices are unnecessary:** Tie-breaking among obstacles at equal distance is irrelevant because the output is only the distance. Unlike an update problem, no obstacle later needs to be identified or modified.
- **`k` larger than total query count:** Every output is minus one. The heap may grow to all query distances but never exceeds `k`, which is still within the stated space bound.
- **Negating zero:** Distance zero remains zero, and `-pq[0]` returns zero correctly.
- **Streaming behavior:** Each answer is finalized using only previous obstacles and the current query. Future queries are never needed, making the method suitable for an online stream.
