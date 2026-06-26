# Median of Two Sorted Arrays

| | |
|---|---|
| **ID** | `dc_09` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(log(min(M, N)$)) Time, $O(1)$ Space |
| **Difficulty** | 10/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

## Problem statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.
The overall run time complexity should be $O(log(m+n)$).

**Input:** Two sorted integer arrays `nums1` and `nums2`.
**Output:** A floating point number representing the exact median.

## When to use it

- Widely considered one of the hardest standard technical interview questions.
- It tests your ability to abstract Binary Search away from searching for a *value*, and instead Binary Searching for a *structural partition boundary*.

## Approach

**1. The Meaning of Median:**
If we merged both arrays into a single massive array `A` of size `M + N`, the median would split `A` perfectly in half.
- **Left Half:** Contains exactly (M + N + 1) // 2 elements. Every element here is smaller than every element in the right half.
- **Right Half:** Contains the rest.
If `M + N` is odd, the median is the largest element in the Left Half.
If `M + N` is even, the median is the average of the largest element in the Left Half and the smallest element in the Right Half.

**2. Partitioning Instead of Merging:**
We DO NOT want to physically merge the arrays! (That takes $O(M+N)$ time).
Instead, we want to draw a virtual dividing line through `nums1` and a virtual dividing line through `nums2` such that:
`len(nums1_left) + len(nums2_left) == (M + N + 1) // 2`.
This means if we pick a partition point `partitionX` in `nums1`, the partition point `partitionY` in `nums2` is mathematically FORCED!
`partitionY = (M + N + 1) // 2 - partitionX`.

**3. Binary Search for the Perfect Partition:**
We binary search for `partitionX` only on the smaller array (let's say `nums1`, so the search space is $O(log(\min(M, N)$))).
At any given `partitionX`, we check if it is VALID.
It is valid IF AND ONLY IF:
- `maxLeftX <= minRightY` (The largest element on the left of X is smaller than the smallest on the right of Y).
- `maxLeftY <= minRightX` (The largest element on the left of Y is smaller than the smallest on the right of X).

If `maxLeftX > minRightY`: We partitioned too far right in `X`. We must move our binary search `high` pointer to the left!
If `maxLeftY > minRightX`: We partitioned too far left in `X`. We must move our binary search `low` pointer to the right!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_09: Median of Two Sorted Arrays.

Given two sorted arrays `a` (length m) and `b`
"""


def solve(a, b, m, n):
    """Median of two sorted arrays in O(log(min(m, n)))."""
    if m > n:
        return solve(b, a, n, m)
    lo, hi = 0, m
    half = (m + n + 1) // 2
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        if i > 0 and a[i - 1] > b[j]:
            hi = i - 1
        elif i < m and j > 0 and b[j - 1] > a[i]:
            lo = i + 1
        else:
            # Found the right partition.
            if i == 0:
                left_max = b[j - 1]
            elif j == 0:
                left_max = a[i - 1]
            else:
                left_max = max(a[i - 1], b[j - 1])
            if (m + n) % 2 == 1:
                return float(left_max)
            if i == m:
                right_min = b[j]
            elif j == n:
                right_min = a[i]
            else:
                right_min = min(a[i], b[j])
            return (left_max + right_min) / 2
```

</details>

## Walk-through

`nums1 = [1, 3, 8, 9, 15]`. `X = 5`.
`nums2 = [7, 11, 18, 19, 21, 25]`. `Y = 6`.
Total elements = 11 (Odd). Target left half size = (5 + 6 + 1) // 2 = 6.

1. **Binary Search 1:**
   - `low = 0, high = 5`. `partitionX = 2`. (Take 2 from nums1).
   - `partitionY = 6 - 2 = 4`. (Take 4 from nums2).
   - `maxLeftX = nums1[1] = 3`. `minRightX = nums1[2] = 8`.
   - `maxLeftY = nums2[3] = 19`. `minRightY = nums2[4] = 21`.
   - Check: `3 <= 21` (True). `19 <= 8` (FALSE!).
   - Since `maxLeftY > minRightX` (`19 > 8`), we need MORE from `nums1` to push out the big `19`! `low = partitionX + 1 = 3`.
2. **Binary Search 2:**
   - `low = 3, high = 5`. `partitionX = 4`. (Take 4 from nums1).
   - `partitionY = 6 - 4 = 2`. (Take 2 from nums2).
   - `maxLeftX = nums1[3] = 9`. `minRightX = nums1[4] = 15`.
   - `maxLeftY = nums2[1] = 11`. `minRightY = nums2[2] = 18`.
   - Check: `9 <= 18` (True). `11 <= 15` (True!).
   - MATCH FOUND!
3. **Calculate Median:**
   - Total is odd. Median is `max(maxLeftX, maxLeftY)`.
   - `max(9, 11) = 11`.

Result is `11.0`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(log(min(M, N)$)) | $O(1)$ |
| **Worst** | $O(log(min(M, N)$)) | $O(1)$ |

We only perform binary search on the smaller array. Thus the search space is bounded by \min(M, N), resulting in exactly $O(log(\min(M, N)$)) time complexity.
No new arrays or recursion stacks are created. Space complexity is strictly $O(1)$.

## Variants & optimizations

- **K-th Element of Two Sorted Arrays:** Finding the median is literally just finding the K-th element where K = (M+N)/2. You can use this exact identical partition algorithm to find the K-th smallest element of two sorted arrays just by modifying the target left half size to be exactly `K`.

## Real-world applications

- **Distributed Databases (Sharding):** When an index is sharded and sorted across two physically different database nodes, you can query for the global median without transferring the entirety of either shard over the network! You only need to ping back and forth $O(\log N)$ times to establish the partition boundary.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The core foundational algorithm mechanism.
- **[dc_03 - Kth Smallest Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Finding the median/k-th element of a single UNSORTED array in $O(N)$ time.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
