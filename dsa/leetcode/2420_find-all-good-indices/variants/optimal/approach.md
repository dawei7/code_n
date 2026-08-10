## General

**Replace repeated range checks with reusable run lengths**

For a candidate index `i`, the problem asks about two blocks that do not include `nums[i]` itself. The $k$ positions immediately before it are

`nums[i-k], ..., nums[i-1]`,

and they must be non-increasing. The $k$ positions immediately after it are

`nums[i+1], ..., nums[i+k]`,

and they must be non-decreasing. Checking both blocks from scratch for every candidate would inspect up to $2k$ adjacent pairs per index, leading to $O(nk)$ time in the worst case.

The solution instead precomputes the length of the relevant monotone run on each side of every possible center. A long run automatically certifies all shorter windows contained at its end or beginning.

**Meaning of the left-side array**

The list `decr` is initialized with ones. For a center-like position `i`, `decr[i]` represents the length of the non-increasing run ending at `nums[i - 1]`. The shifted index is important: the center is excluded, so the left block ends one position before `i`.

For `i` from 2 through `n - 2`, the code compares `nums[i - 1]` with `nums[i - 2]`. If

`nums[i - 1] <= nums[i - 2]`,

then moving from left to right has not increased, so the run ending at `i - 2` can be extended by `nums[i - 1]`. The assignment `decr[i] = decr[i - 1] + 1` records that extension. If the comparison fails, the initial value 1 remains, representing a new run containing only `nums[i - 1]`.

For $k=1$, a one-element block is automatically non-increasing, so the default values are already sufficient. The extra array position from allocating `n + 1` entries is not logically necessary, but it is harmless and remains unused by the returned comprehension.

**Meaning of the right-side array**

The list `incr` is also initialized with ones. Here `incr[i]` represents the length of the non-decreasing run starting at `nums[i + 1]`. Again, the offset excludes the candidate center.

This information must be built from right to left because the run starting at one position depends on the run starting at the next. For `i` from `n - 3` down to 0, the comparison

`nums[i + 1] <= nums[i + 2]`

checks whether the first two values on the right are in non-decreasing order. If so, `nums[i + 1]` can be placed before the already known run beginning at `nums[i + 2]`, and `incr[i] = incr[i + 1] + 1`. Otherwise, the run starting immediately after `i` has length 1.

Equality is accepted on both sides. “Non-increasing” allows adjacent equal values because it forbids only an increase; “non-decreasing” likewise permits equality because it forbids only a decrease.

**Select exactly the legal centers**

The comprehension considers `range(k, n - k)`. This is precisely the legal interval $k \le i < n-k$: there must be at least $k$ elements before and at least $k$ elements after `i`.

The condition `decr[i] >= k` says that the non-increasing run ending just before `i` is long enough to cover all $k$ required left elements. The condition `incr[i] >= k` says that the non-decreasing run starting just after `i` is long enough to cover all $k$ required right elements. Both must hold.

Because Python's `range` emits indices in increasing order, the result automatically satisfies the required output order. No final sort is needed.

For `nums = [2, 1, 1, 1, 3, 4, 1]` and $k=2$, consider `i=2`. The two left values `[2, 1]` form a non-increasing run of length at least 2, and the two right values `[1, 3]` form a non-decreasing run of length at least 2. Both precomputed tests pass. At `i=4`, the right block `[4, 1]` breaks the required direction, so `incr[4]` is only 1 and the index is rejected.

**Why the two tests are sufficient and necessary**

If `decr[i] >= k`, the last $k$ elements in that run are exactly the $k$ elements immediately before `i`, so every adjacent pair in the required block follows non-increasing order. Conversely, if that block is non-increasing, it forms a run of length at least $k$ ending at `i-1`, so the recurrence must produce `decr[i] >= k`. The same two-way argument applies to `incr[i]` and the block after `i`.

Therefore an index passes the comprehension if and only if both conditions in the definition of a good index hold. The candidate range excludes precisely the indices without enough surrounding elements, completing the correctness argument.

## Complexity detail

Let $n$ be the length of `nums`. The forward loop performs at most $n$ constant-time comparisons and assignments. The backward loop does the same. The result comprehension considers at most $n$ centers and performs two constant-time run-length comparisons for each. The total time is therefore $O(n)$.

The `decr` and `incr` arrays each contain $n+1$ integers, so auxiliary space is $O(n)$. The returned list can itself contain $O(n)$ indices. Excluding output space does not change the auxiliary bound because the two run arrays remain linear.

The approach avoids any dependence on $k$ in the running-time factor. Even when $k$ is near $n/2$, each adjacent relationship is processed only once per direction rather than once for every overlapping window.

## Alternatives and edge cases

- **Check every candidate window directly:** Scan the $k$ values on both sides of each center. This is straightforward but can take $O(nk)$ time because neighboring candidates repeat nearly all the same comparisons.
- **Prefix arrays of violations:** Mark each adjacent increase and decrease, then use prefix sums to ask whether a window contains a forbidden pair. This also gives $O(n)$ time and $O(n)$ space, but run lengths express the exact condition more directly.
- **Streaming with queues:** Sliding-window counts of left and right violations can produce the answer in linear time. It requires careful synchronization of two windows around a skipped center and is easier to get off by one.
- **One-sided memory reduction:** It is possible to precompute only one direction and maintain the other direction while scanning candidates, reducing some storage. The two-array form is clearer and already fits the constraints.
- **$k=1$:** Every single-element left or right block is monotone, so every legal index from 1 through $n-2$ is good. The arrays' initial value 1 handles this automatically.
- **Equal adjacent values:** Equality satisfies both non-increasing and non-decreasing order. The code's `<=` comparisons correctly extend both kinds of run.
- **Exactly $2k$ elements:** The legal range can be empty because a center also occupies a position. `range(k, n-k)` correctly returns no candidates when its endpoints meet.
- **Center value is irrelevant:** Neither recurrence compares the center with its neighbors for the final test. Only the $k$ elements strictly before and strictly after matter.
- **Output ordering:** Candidate indices are visited from small to large, so appending through the comprehension already produces increasing order.
