## General

**Process queries in increasing `nums1` order.** For index $i$, eligible indices $j$ are exactly those with

$$
\texttt{nums1}[j] < \texttt{nums1}[i].
$$

If the current `nums1` threshold increases, the eligible set only grows. This monotonicity allows one sorted sweep instead of independently scanning all $n$ indices for every answer.

The source builds tuples `(nums1 value, original index)` in `arr` and sorts them. The original index is retained because answers must be written in the input's order, not sorted order.

**Maintain the best \(k\) values from the eligible prefix.** `pq` is a min-heap containing the largest at most $k$ eligible `nums2` values seen so far. `s` stores their sum.

Whenever one newly eligible index is introduced, its `nums2` value `y` is pushed and added to `s`. If the heap grows beyond $k$, the smallest retained value is popped and subtracted. After this correction, the heap again contains the largest $k$ values among all eligible values, or all eligible values when fewer than $k$ exist.

A min-heap is the correct orientation even though the goal is to keep large values: when there are too many candidates, the one that must be discarded is the smallest, and the heap exposes that value in $O(\log k)$ time.

**Use a second pointer to enforce strict inequality.** At sorted position `h` with threshold `x`, pointer `j` marks the earliest sorted tuple not yet inserted into the heap. The loop advances while both

`j < h` and `arr[j][0] < x`.

The second comparison is essential. Elements with equal `nums1` values are not eligible for one another because the condition is strictly less, not less than or equal.

Suppose a group of several tuples all has value $x$. For each tuple in that group, `j` stops before the group, so every member receives the same heap sum based only on smaller values. When the sweep later reaches a larger threshold, the while loop consumes all members of the $x$ group. This delayed group insertion implements strict inequality without building explicit groups.

After all newly smaller tuples have been inserted, `ans[i] = s` stores the maximum allowed sum for the tuple's original index.

For the first example, sorted `nums1` values are $1,2,3,4,5$. At threshold one, the heap is empty and the answer is zero. Before threshold two, value $30$ associated with `nums1=1` becomes eligible, giving $30$. Before threshold three, profit $20$ is added, so the top two sum is $50$. At threshold four, profit $50$ enters; the heap discards $20$ and keeps $30+50=80$. Threshold five also introduces profit $10$, but the same top two remain, so its answer is $80$.

For all-equal `nums1`, the strict comparison never admits an earlier tuple in the equal group. The heap remains empty for all answers, producing zeros as required.

**Why selecting exactly the heap contents is optimal.** Every `nums2` value is positive under the constraints. Therefore, when at least $k$ indices are eligible, an optimum chooses exactly the $k$ largest values. When fewer than $k$ are eligible, choosing all of them is optimal. The bounded heap stores exactly this set.

Even without positivity, the problem says “at most $k$,” so negative values would need exclusion rather than automatic retention. The declared positive range is what makes the source's always-push policy correct.

**Heap invariant and overall correctness.** Before answering a sorted tuple with threshold $x$, the pointer loop has inserted every tuple with smaller `nums1` and no tuple with equal or larger `nums1`. Inductively, after every insertion and optional pop, `pq` contains the largest at most $k$ `nums2` values among inserted tuples, and `s` equals their sum. Consequently, `s` is exactly the requested maximum for that threshold. Restoring it to `ans` at the saved original index makes every output position correct.

Each input tuple is inserted only when it first becomes eligible for a later threshold. The sweep shares that work across all queries.

## Complexity detail

Building `arr` costs $O(n)$ and sorting it costs $O(n\log n)$. Pointer `j` advances from zero to at most $n$ over the entire sweep, so there are $O(n)$ heap pushes and at most $O(n)$ pops. Each heap operation costs $O(\log k)$ because the heap retains at most $k+1$ values.

Total time is

$$
O(n\log n+n\log k)=O(n\log n),
$$

matching the manifest.

`arr` and `ans` each use $O(n)$ space, while `pq` uses $O(k)$. Auxiliary space is $O(n)$ overall. The running sum uses a Python integer; in fixed-width languages, up to $k\cdot10^6$ may require a 64-bit type.

## Alternatives and edge cases

- **Scan every index for every answer:** This directly follows the definition but costs $O(n^2)$.
- **Sort `nums2` candidates per query:** Repeated sorting is even more expensive and discards the monotone-threshold structure.
- **Use a max-heap:** It exposes the largest value, while maintenance needs to evict the smallest; a bounded min-heap is the natural choice.
- **Insert equal `nums1` values immediately:** That would incorrectly treat equality as eligibility. The `arr[j][0] < x` guard delays the entire equal group.
- **\(k=n\):** No eligible set can exceed $n-1$, so the heap retains all eligible values and returns their sum.
- **Fewer than \(k\) eligible indices:** The heap contains all of them and no pop occurs.
- **Smallest `nums1` value:** Its eligible set is empty, so its answer is zero.
- **Duplicate `nums2` values:** The heap stores occurrences, not unique values, so separate indices may both be selected.
- **Positive-value guarantee:** Taking as many eligible values as allowed is optimal; a negative-value variant would require skipping harmful candidates.
- **Original order:** Saving index `i` in each sorted tuple is necessary to place the result back correctly.
- **Running-sum synchronization:** Every push adds to `s` and every pop subtracts from it, so no separate $O(k)$ heap summation is needed per query.
- **Input preservation:** Neither input array is mutated; sorted tuples and answers are stored separately.
