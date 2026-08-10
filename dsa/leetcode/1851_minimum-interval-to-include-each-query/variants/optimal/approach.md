## General

**Sweep queries from left to right.** For a query value `x`, an interval contains it when its left endpoint has started, `left <= x`, and its right endpoint has not expired, `right >= x`. Processing queries in ascending order lets the algorithm add intervals when they start and lazily remove them when they end.

The solution sorts `intervals` by left endpoint and replaces local `queries` with sorted pairs `(value, original_index)`. `ans` is initialized to minus one for every original query position.

**Add every interval that could contain the current query.** Pointer `i` tracks the next interval not yet inserted. While `intervals[i][0] <= x`, the code pushes

`(right - left + 1, right)`

into min-heap `pq`. The first tuple field is interval size, so the heap prioritizes the smallest interval. The right endpoint is stored so expired intervals can be recognized. The left endpoint need not be stored because insertion itself proves it is at most the current and every later query.

Inclusive size uses `right - left + 1`. Omitting the one would measure coordinate difference rather than number of contained integers.

**Remove expired heap leaders.** After additions, the code pops while `pq[0][1] < x`. A right endpoint equal to `x` remains valid because intervals are inclusive.

Some expired interval may remain deeper in the heap when a smaller-size valid interval is on top. That is harmless: it cannot affect the current answer while it is not the minimum. If it later reaches the root, the same loop removes it before an answer is read. This is lazy deletion.

**Read the minimum valid size.** Once the expiration loop stops, an existing heap root has:

- a left endpoint no greater than `x` because it was inserted,
- a right endpoint at least `x` because expired roots were removed.

It therefore contains `x`. Since the heap is ordered first by size, its first field is the smallest size among all active intervals. The method writes that size to `ans[j]`. If the heap is empty, no inserted unexpired interval exists and the prefilled minus one remains.

**Restore original query order.** Queries are processed by value for the sweep, but `j` stores each original position. Writing `ans[j]` ensures the returned list follows the caller’s query order, including repeated query values.

**Trace the first sample around query four.** By the time `x = 4` is processed, intervals beginning at one, two, three, and four have all entered the heap. None ending at four is expired because equality is included. Interval `[4, 4]` has size one and becomes the heap root, so the answer is one. At query five, intervals ending at four are popped when they reach the root, and `[3, 6]` supplies size four.

**Why each interval is handled only once.** Sorted starts and monotonically increasing queries mean pointer `i` never moves backward. Every interval is pushed exactly once. Once an interval’s right endpoint lies before the current query, it can never contain a later query, so popping it permanently is safe.
Before answering `x`, the heap has received every interval with `left <= x`. The cleanup guarantees its root, if any, also has `right >= x`. Any containing interval is therefore either present and valid or was never removed; no valid interval can have expired earlier. Heap priority chooses the smallest size among them. This proves each recorded answer is correct.

**Exact input behavior.** `intervals.sort()` mutates the caller’s interval order. The original query list is not mutated because the name `queries` is rebound to a new sorted list of pairs.

## Complexity detail

Let `n` be the number of intervals and `q` the number of queries. Sorting costs `O(n log n + q log q)`. Every interval is pushed once and popped at most once, with heap cost `O(log n)` each. Query processing otherwise does constant work, so total time is `O((n + q) log(n + q))`.

The heap can hold `O(n)` intervals. Sorted query pairs and the answer use `O(q)` storage, and sorting may need temporary space. Total auxiliary and output storage is `O(n + q)`.

## Alternatives and edge cases

- **Scan every interval per query:** It follows the definition but costs `O(nq)`.
- **Segment tree over coordinates:** Coordinate compression can support range updates and point queries, but selecting minimum interval size is more involved than the offline heap sweep.
- **Equal query values:** They are adjacent after sorting and receive the same active-interval state, while original indices preserve duplicate outputs.
- **Point interval `[x, x]`:** Its inclusive size is one and it contains exactly query `x`.
- **Right endpoint equals query:** It is valid because expiration uses `right < x`, not `<=`.
- **No containing interval:** The heap is empty after cleanup and answer stays minus one.
- **Expired interval below the root:** Lazy deletion is safe because only the heap root can determine the minimum answer.
- **Many intervals start together:** All enter before the answer, ensuring the shortest is considered.
- **Nested intervals:** Heap size priority selects the shortest containing one regardless of start order.
- **Repeated interval sizes:** Either root gives the same requested size; no interval identity tie-break is needed.
- **Input mutation:** Intervals are sorted in place, while the caller’s query list remains unchanged.
- **Original output order:** Stored indices undo the offline query sorting.
