## General

**Binary-search a sum threshold.** Instead of generating all $n(n+1)/2$ sums, define predicate `f(s)`: at least `k` subarrays have sum at most `s`. As `s` grows, that count never decreases. The first threshold making the predicate true is exactly the $k$-th smallest sum, including duplicate sums as separate subarray occurrences.

**Count bounded-sum subarrays with a sliding window.** Every `nums` value is positive. Variables `j` and `i` delimit a window, and `t` is its sum. On adding `nums[i]`, the loop removes values from the left while `t > s`. When it stops, `nums[j:i+1]` is the longest valid suffix ending at `i`.

Every subarray ending at `i` and starting at `j, j+1, ..., i` has sum at most `s` because removing positive values cannot increase a sum. Any earlier start is invalid because `j` was advanced until the bound held. Therefore exactly `i - j + 1` valid subarrays end at `i`, and the source adds that number to `cnt`.

**Why positivity is essential.** With negative values, removing the leftmost element could increase the sum, and valid starts would not necessarily form one contiguous suffix. The stated positive constraint supplies the monotonic window behavior.

**Turn the count into a Boolean.** After scanning every right endpoint, `f` returns `cnt >= k`. It could stop early once the threshold is reached, but the exact source completes the full scan. Counts include equal sums separately because each start/end pair contributes once.

**Choose complete numeric bounds.** The smallest nonempty subarray sum is at least `min(nums)` and is achieved by its one-element subarray. The largest is `sum(nums)` because all values are positive and the full array includes every value. The answer lies in this inclusive range.

**Understand the keyed bisect call.** `range(l, r + 1)` is a lazy sequence of every candidate sum. `bisect_left(..., True, key=f)` conceptually applies `f` at probed candidates. Boolean keys are ordered `False < True`, and monotonicity makes them a run of false values followed by true values. Bisect returns the offset of the first true key. Adding `l` converts that zero-based range offset back to the actual sum.

**Trace `[2,1,3]` at threshold three.** Sliding counting finds one valid ending at index zero, two at index one, and one at index two, totaling four subarrays with sum at most three. Thus `f(3)` is true for `k=4`. At threshold two, only sums one and two qualify, so the predicate is false. The first true threshold is three.

**Why first true equals order statistic.** If fewer than `k` sums are at most `s`, the $k$-th smallest must exceed `s`. Once at least `k` are at most `s`, the $k$-th smallest is no greater than `s`. The boundary between these cases is exactly its value.

**Why the window counts each subarray once.** Every nonempty subarray has one unique right endpoint. On the iteration for that endpoint, it is counted through exactly one start position if its sum is within the threshold. It cannot appear during another iteration, and invalid starts before `j` are excluded. Summing window lengths therefore counts occurrences rather than distinct numeric sums, which is essential for the order statistic.

**Why the pointer never moves backward.** Adding another positive number can only make earlier starts less likely to fit. Once start index `j` has been rejected for one right endpoint because its window is too large, extending the right side cannot make that same start valid again. This monotonicity makes all inner-loop movements linear across one predicate call.

## Complexity detail

Let $N$ be array length and $S=\sum nums-\min nums+1$ the numeric search span. One predicate call moves each window pointer forward at most $N$ times, so it is $O(N)$. Binary search performs $O(\log S)$ calls, giving $O(N\log S)$ time.

The range is lazy, the window uses scalar variables, and no prefix array is built. Auxiliary space is $O(1)$, matching the manifest. The sum/count may require 64-bit arithmetic outside Python.

## Alternatives and edge cases

- **Generate and sort all sums:** Requires $O(N^2)$ storage and at least quadratic work, infeasible for $N=20000$.
- **Prefix sums plus two pointers:** Equivalent counting can use prefixes, but positive values let the exact source maintain the running sum directly.
- **Early predicate exit:** Returning once `cnt >= k` can improve constants without changing the bound.
- **Single element:** Both numeric bounds equal that element, and bisect returns it.
- **Duplicate sums:** They represent different subarrays and are counted separately through start positions.
- **`k = 1`:** The boundary is the smallest one-element value.
- **Maximum `k`:** The answer is full-array sum, the largest positive subarray sum.
- **No zero candidate:** Inputs are positive, so starting at `min(nums)` excludes impossible smaller sums safely.
- **Keyed bisect semantics:** The returned value is an offset into `range`, so adding `l` is required.
- **Large answer span:** Binary search depends logarithmically on total sum, not on the number of subarrays, so a huge quadratic candidate count is never materialized.
- **Strict versus non-strict threshold:** Predicate counts sums `<= s`. Using `< s` would shift the first-true boundary past the correct repeated value.
