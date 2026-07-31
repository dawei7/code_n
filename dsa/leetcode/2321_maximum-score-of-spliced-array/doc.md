# Maximum Score of Spliced Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2321 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-of-spliced-array/) |

## Problem Description
### Goal
Two integer arrays `nums1` and `nums2` have the same length. At most once,
choose an inclusive interval `[left, right]` and exchange the elements at those
indices between the arrays. The chosen indices must be contiguous, and the
same interval is exchanged in both arrays.

After the optional swap, the score is the larger of the two complete array
sums. Find the greatest score attainable. Choosing no interval is allowed, so
the original larger sum always remains a candidate.

### Function Contract
**Inputs**

- `nums1`: The first length-$n$ array.
- `nums2`: The second length-$n$ array.

The common length satisfies $1\le n\le10^5$, and every value is from 1 through
$10^4$.

**Return value**

The maximum of the two array sums after zero or one equal-index contiguous
subarray swap.

### Examples
**Example 1**

- Input: `nums1 = [60,60,60]`, `nums2 = [10,90,10]`
- Output: `210`

**Example 2**

- Input: `nums1 = [20,40,20,70,30]`, `nums2 = [50,20,50,40,20]`
- Output: `220`

**Example 3**

- Input: `nums1 = [7,11,13]`, `nums2 = [1,1,1]`
- Output: `31`
- Explanation: Not swapping is optimal.
