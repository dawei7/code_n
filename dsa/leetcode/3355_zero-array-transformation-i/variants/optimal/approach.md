## General

**Interpret each query as one unit of capacity at every covered index.** Query `[l,r]` lets us choose any subset of indices in that interval and decrement each chosen value by one. Therefore, for a fixed index $i$, every query covering $i$ can contribute at most one decrement there.

If $c_i$ queries cover index $i$, its total available decrement capacity is $c_i$. Turning `nums[i]` into zero is possible exactly when

$$
\texttt{nums}[i]\le c_i.
$$

This condition is independent for each index. A single query may include any subset, so using it at one covered index does not prevent using the same query at other covered indices. There is no shared budget that couples their choices.

**Why having extra capacity is harmless.** The operation says to select a subset, not every index. Once an element has received exactly `nums[i]` decrements, later covering queries can simply omit that index. Thus the algorithm needs at least the required capacity, not capacity exactly equal to the original value.

Sequential processing also creates no obstacle. For each index, choose any `nums[i]` of its covering queries and include that index in those queries' subsets. Since the choices for different indices are independent inside every query, all these per-index schedules can be combined into valid query subsets without making any element negative.

**Accumulate interval coverage with a difference array.** Explicitly incrementing every position in every query can cost $O(nq)$. The source instead creates `d` of length `n + 1`. For query `[l,r]`:

- `d[l] += 1` begins one additional active covering query;
- `d[r + 1] -= 1` removes it immediately after the inclusive right endpoint.

The extra sentinel cell makes `r + 1` valid even when `r` is the last real index.

**Recover capacity through a prefix sum.** Variable `s` is the running sum of difference events. Before checking index $i$, adding `d[i]` makes `s` equal the number of intervals whose left endpoint is at most $i$ and whose right endpoint is at least $i$. That is exactly $c_i$.

The loop uses `zip(nums, d)`. Because `nums` has only $n$ values, `zip` stops after the first $n$ cells of `d`; the sentinel event at `d[n]` does not correspond to a real element and need not be processed.

If `x > s` at any position, even selecting that index in every covering query supplies too few decrements. The source immediately returns false. If no position violates the inequality, every element has enough independent capacity and the method returns true.

**Trace overlapping queries.** For `nums = [1,0,1]` and query `[0,2]`, the events are plus one at zero and minus one at three. The running coverage is one at all three indices. Values one, zero, and one each fit within capacity, so the first and third indices are selected and the middle is omitted.

For two queries `[1,3]` and `[0,2]`, coverage may be one at the outer indices and two in their overlap. An element initially four at index zero still fails because its local capacity is only one, even if other positions have unused capacity. Capacity cannot move between indices.

**Why the test is both necessary and sufficient.** Necessity follows because a query can decrement a given index no more than once. For sufficiency, independently select each index in exactly as many covering queries as its value demands. The subset rule permits all these choices simultaneously. The difference scan calculates each coverage exactly, so returning true is equivalent to the existence of a complete zeroing schedule.

**The input itself is never transformed.** The algorithm answers an existence question. It does not need to construct the subsets or modify `nums`, because the coverage inequalities already guarantee that such choices can be made.

## Complexity detail

Let $n$ be the number of elements and $q$ the number of queries. Building two difference events per query takes $O(q)$ time. The prefix scan takes $O(n)$ time, for total $O(n+q)$.

The difference array has $n+1$ integers, so auxiliary space is $O(n)$. The running sum uses constant additional space, and neither input list is modified.

## Alternatives and edge cases

- **Apply each query across its range:** Directly increasing coverage for every covered index can take $O(nq)$ time in the worst case.
- **Fenwick tree:** Range additions and point queries can solve the same task in $O((n+q)\log n)$ time, but the offline difference array is simpler and faster.
- **Construct explicit subsets:** It is unnecessary for the Boolean result; per-index capacity proves a combined construction exists.
- **Zero-valued element:** It requires no capacity and always satisfies `0 <= s`.
- **No query covers a positive index:** Its coverage is zero and the method correctly fails.
- **More queries than needed:** Extra capacity can be ignored by omitting the index from later subsets.
- **Overlapping queries:** Their contributions add in the prefix sum.
- **Duplicate queries:** Each is a separate operation and adds another unit of capacity.
- **Single-index query:** Events at `l` and `l+1` cover exactly that one element.
- **Query ending at `n-1`:** The $n+1$ array safely stores its removal event at sentinel index $n$.
- **Inclusive endpoints:** Subtraction must occur at `r+1`, not `r`.
- **Sequential wording:** Query order does not affect feasibility because decrements at different indices are independently optional.
- **Avoiding negative values:** Select an index in exactly its required number of covering queries and omit it afterward.
- **Early false return:** Once one index lacks capacity, no choices at other indices can compensate for it.
- **Input preservation:** Only the separate difference array is changed.
