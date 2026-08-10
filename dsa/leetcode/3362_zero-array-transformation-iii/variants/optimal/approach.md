## General

**Reframe maximum removals as minimum retained queries.** A retained query `[l,r]` supplies one unit of decrement capacity independently at every covered index. Index $i$ needs at least `nums[i]` retained queries covering it. Once a smallest sufficient set is retained, every other query can be removed, so maximizing removals is equivalent to selecting as few intervals as possible.

**Sweep indices from left to right.** When processing index `i`, every earlier index is already permanently satisfied. Variable `s` is the number of previously selected queries that are still active at `i`. Difference array `d` schedules when those selected queries stop contributing: selecting an interval ending at `r` records `d[r + 1] -= 1`.

At the beginning of an index, `s += d[i]` removes selections whose right endpoint was `i-1`. It therefore restores the invariant that `s` is exactly the current selected coverage.

**Make every newly available query a candidate.** The source sorts `queries` lexicographically, primarily by left endpoint. Pointer `j` advances while `queries[j][0] <= i` and inserts each query's negated right endpoint into `pq`.

Python's heap is a min-heap, so storing `-r` makes the smallest heap item correspond to the largest real right endpoint. The heap contains queries whose left endpoints have been reached but that have not been selected. Some expired unselected intervals may remain, which is safe because the maximum right endpoint is examined before any selection.

**Select a query only when current coverage is deficient.** If `s < nums[i]`, more retained queries covering `i` are mandatory; no future query with left endpoint greater than `i` can repair this position. The source repeatedly pops an available interval while the largest right endpoint still reaches `i`.

Every pop increases current coverage by one and schedules its expiration just after its right endpoint. The loop stops as soon as `s` meets the current demand, so it never retains a query without an already-proven need.

**Choose the farthest-reaching available interval.** Among all candidates covering the current deficient index, an interval with a larger right endpoint dominates one with a smaller endpoint. Both contribute equally at `i`, but the farther interval remains useful at every future position where the shorter one could help, and possibly more.

An exchange argument makes the greedy choice safe. Suppose some optimal retained set uses a shorter available query when the greedy method chooses a longer one. Replace the shorter query with the longer query. All already processed positions are covered by both because their left endpoints are at most the current index, current coverage is unchanged, and future coverage cannot decrease. The retained-set size stays the same. Repeating this exchange yields an optimal solution consistent with every greedy selection.

**Detect impossibility immediately.** If coverage is deficient and the heap is empty, no started unselected query exists. If the heap's largest right endpoint is below `i`, every heap query has expired. Future queries start too late. In either situation, index `i` can never receive enough retained capacity, so the source returns `-1`.

After the selection loop, the separate `if s < x` handles both failure forms uniformly.

**Why stale heap entries do not break the method.** Since the heap exposes the largest right endpoint, if its top has expired then every other stored endpoint is no larger and has expired too. If at least one unexpired query exists, the top is unexpired. Stale entries can therefore remain until the end without blocking a useful interval.

**Count removable queries from the heap.** Selected queries are popped and never reinserted. Unselected queries remain in `pq`, including harmless expired ones. By the time the sweep reaches the final index, every legal query has left endpoint at most that index and has been pushed. Therefore `len(pq)` is exactly the number never selected, which is the maximum removable count.

**Trace the first example.** At index zero, demand is two and two intervals `[0,2]` are available; the greedy loop must retain both. They stay active through index two. Query `[1,1]` enters the heap later but is never needed because the middle demand is zero and the endpoint demand is already covered. It remains in the heap, so the returned removable count is one.

**Independent decrement amounts make coverage sufficient.** A retained query does not have to decrement every covered element. Once each index has at least its demanded number of retained covering queries, choose that index in exactly `nums[i]` of them and choose decrement zero in the rest. Thus the interval-coverage problem precisely matches zero-array feasibility.

**Why the final set is minimum.** At every index, the algorithm selects only the exact number of additional intervals forced by the deficit. The farthest-end exchange argument ensures those forced choices are at least as useful as the choices in any optimum. Induction across the sweep shows an optimal retained set can always be transformed to include the greedy selections without growing. Hence no solution retains fewer queries, and all remaining heap entries are safely removable.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. Sorting costs $O(q\log q)$. Every query is pushed once, and each selected query is popped once; each heap operation costs $O(\log q)$. The array sweep and difference updates cost $O(n+q)$ outside the heap.

Total time is $O(n+q\log q)$. The difference array uses $O(n)$ space and the heap can hold $O(q)$ endpoints, so auxiliary space is $O(n+q)$.

The source sorts `queries` in place. The space bound counts the heap and difference array but not implementation-specific temporary storage used internally by Python's sort.

## Alternatives and edge cases

- **Select shortest-reaching intervals:** This can satisfy the current index but waste future coverage and force additional retained queries later.
- **Check every removal subset:** There are $2^q$ subsets and no feasible exhaustive approach at the given limit.
- **Difference-array feasibility after each deletion:** Repeated checking is far slower and does not identify the greedy dominance relation.
- **Zero-demand index:** No new interval is selected, but queries whose left endpoint has arrived are still inserted for possible future use.
- **Impossible current deficit:** If no available interval reaches `i`, future-starting intervals cannot help and `-1` is final.
- **Duplicate queries:** They are distinct capacity units and are pushed separately.
- **Single-index query:** It expires through `d[i+1]` immediately after its only useful position.
- **Query ending at the last index:** Its expiration event is stored safely in the extra difference cell.
- **Expired unselected query:** It remains removable and may stay in the heap.
- **Expired heap top:** Because the top has the maximum right endpoint, all heap entries are then expired.
- **All queries needed:** Every query is popped, the heap ends empty, and zero removals are returned.
- **No queries needed:** When `nums` is all zero, no query is popped and all $q$ are removable.
- **Independent per-index choice:** Retaining an interval creates capacity at all covered positions without forcing unwanted decrements.
- **Inclusive range:** A selected query contributes through `r` and expires at `r+1`.
- **Input mutation:** `queries.sort()` changes the caller-visible query order, although it does not change interval contents.
- **Lexicographic sort:** Only left-endpoint order is required; the secondary right-endpoint order does not affect correctness because the heap reorders by right endpoint.
- **Heap sign convention:** Negated endpoints turn Python's min-heap into a max-right-endpoint structure.
