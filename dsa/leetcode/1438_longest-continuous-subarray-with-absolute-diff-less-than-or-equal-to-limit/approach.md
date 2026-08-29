## General

**Only the window minimum and maximum determine validity**

For any set of numbers, the largest absolute difference between a pair is:

$$
\max-\min.
$$

If that extreme difference is at most `limit`, every other pair is also within the limit. If it exceeds the limit, the minimum and maximum themselves form a violating pair.

The algorithm therefore maintains a sliding window and a sorted multiset `sl` containing exactly its elements. The first sorted value is its minimum and the last is its maximum.

**What the two boundaries mean**

`j` is the left endpoint of the current window. The outer loop's index `i` is its right endpoint. After adding `nums[i]` and shrinking as needed, the window is `nums[j:i+1]`.

`ans` stores the longest valid window length observed.

**A sorted multiset is required, not a plain set**

`SortedList` keeps values in nondecreasing order and allows duplicates. Duplicate support matters: if the current window contains three copies of 2, removing one leftmost 2 must leave the other two present.

For each new value:

```python
sl.add(x)
```

inserts it into sorted position. Then `sl[0]` is the current minimum and `sl[-1]` is the current maximum.

**Shrink until the extreme difference is legal**

After expansion:

```python
while sl[-1] - sl[0] > limit:
    sl.remove(nums[j])
    j += 1
```

removes the actual value at the left boundary and advances that boundary. `SortedList.remove` deletes one occurrence, matching the removal of one array position.

The loop may need several removals because the newly added value can be far from the existing range. It stops at the first left boundary that makes the window valid.

The multiset never becomes empty during the condition check. A one-element window has maximum minus minimum zero, and `limit` is nonnegative, so shrinking must stop by the time only `nums[i]` remains.

**Why a single forward-moving left pointer is enough**

For a fixed right endpoint `i`, if window `[j,i]` is invalid, every window `[j',i]` with `j'<j` contains all its elements plus more and cannot repair the current extreme pair merely by adding elements. The left endpoint must move right.

Once a left endpoint is discarded, it never needs to return for a later right endpoint. Future windows ending farther right would still include the elements that already caused invalidity unless the left boundary stays beyond them.

This monotonicity is the basis of sliding windows.

**Record the longest valid ending at `i`**

When the while loop stops:

```python
ans = max(ans, i - j + 1)
```

The current window is valid. Because `j` was advanced only while invalid, it is the earliest valid left boundary still possible for this right endpoint. Therefore, `i-j+1` is the longest valid subarray ending at `i`.

Taking the maximum over all right endpoints finds the global longest subarray.

**Trace `[8,2,4,7]` with limit 4**

- Add 8: multiset `[8]`, difference 0, length 1.
- Add 2: multiset `[2,8]`, difference 6. Remove leftmost 8, leaving `[2]` and moving `j` to 1.
- Add 4: multiset `[2,4]`, difference 2, length 2.
- Add 7: multiset `[2,4,7]`, difference 5. Remove leftmost 2, leaving `[4,7]`, difference 3, length 2.

The maximum length is two.

**Why removal follows array order rather than value order**

When a window is invalid, the algorithm cannot simply remove the minimum or maximum value unless that value is at the left boundary. A subarray must remain contiguous, so shrinking means removing `nums[j]` specifically. The sorted multiset supplies the extreme test while `j` enforces contiguity.

**Why the algorithm is correct**

The multiset invariant holds because each expansion inserts the new right value and each contraction removes exactly the departing left value. Thus its extremes always describe the current window.

The contraction loop ends exactly when max minus min is within the limit, which is equivalent to all pair differences being valid. It chooses the earliest valid left boundary for each right endpoint, so the recorded length is the best ending there. Maximizing those values returns the overall optimum.

## Complexity detail

Let $n$ be the array length. Each element is inserted into `SortedList` once and removed at most once. Balanced sorted-container insertion and removal cost $O(\log n)$, while reading either endpoint is $O(1)$. Total time for the exact stored implementation is $O(n\log n)$.

The multiset can hold $O(n)$ values, so space is $O(n)$.

The manifest advertises $O(n)$ time and $O(n)$ space. Linear time requires two monotonic deques, one tracking maximum candidates and one tracking minimum candidates. The protected source uses `SortedList`, so its true time is logarithmic per update rather than linear overall.

## Alternatives and edge cases

- **Two monotonic deques:** Maintain decreasing maximum candidates and increasing minimum candidates. Each index enters and leaves each deque once, realizing $O(n)$ time.
- **Two heaps with lazy deletion:** Track minimum and maximum with indices. It is correct but uses logarithmic operations and more stale-entry handling.
- **Balanced frequency map:** A sorted dictionary from values to counts implements the same multiset idea as SortedList.
- **Brute-force subarrays:** Recomputing extremes for every range can take quadratic or cubic time.
- **`limit = 0`:** A valid window can contain only equal values; duplicate-aware removal is essential.
- **All equal values:** The window never shrinks and the answer is $n$.
- **One element:** Difference is zero, so the result is one.
- **Duplicate minimum or maximum:** Removing one occurrence must not erase the others; SortedList handles multiplicity.
- **Large new outlier:** The while loop may remove many left elements, but each array position is removed only once overall.
- **Contiguity:** Shrinking always removes `nums[j]`, not an arbitrary extreme value.
