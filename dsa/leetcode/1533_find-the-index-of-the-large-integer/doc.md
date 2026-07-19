# Find the Index of the Large Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1533 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-index-of-the-large-integer/) |

## Problem Description
### Goal

An inaccessible integer array contains equal values at every position except one, whose value is strictly larger. Locate the index of that unique larger integer without reading individual elements directly.

The supplied `ArrayReader` reports the array length and compares the sums of two inclusive subarrays. `compareSub(l, r, x, y)` returns 1, 0, or -1 according to whether the first sum is greater than, equal to, or less than the second. Use at most 20 sum-comparison calls and return the large value's index.

### Function Contract
**Inputs**

- `reader`: A read-only `ArrayReader` for an array of length $n$, where $2 \leq n \leq 5\cdot10^5$.
- Every hidden value lies from 1 through 100; exactly one is larger and all remaining values are equal.
- `reader.length()` returns $n$ in $O(1)$ time.
- `reader.compareSub(l, r, x, y)` compares two valid inclusive subarray sums in $O(1)$ time.

**Return value**

Return the zero-based index of the unique larger value while making at most 20 calls to `compareSub`.

### Examples
**Example 1**

- Hidden array: `[7, 7, 7, 7, 10, 7, 7, 7]`
- Output: `4`
- Explanation: Equal-length half comparisons isolate the half containing 10.

**Example 2**

- Hidden array: `[6, 6, 12]`
- Output: `2`
- Explanation: Comparing the first two singleton candidates gives equal sums, so the unpaired final index is larger.

**Example 3**

- Hidden array: `[9, 12]`
- Output: `1`
- Explanation: One singleton comparison identifies the larger side.
