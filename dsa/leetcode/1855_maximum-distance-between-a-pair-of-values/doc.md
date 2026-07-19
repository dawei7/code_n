# Maximum Distance Between a Pair of Values

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) |
| Frontend ID | 1855 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two integer arrays `nums1` and `nums2` are each sorted in non-increasing order. Choose an index `i` from the first array and an index `j` from the second array. The pair is valid only when $i\le j$ and `nums1[i] <= nums2[j]`.

The distance of a valid pair is $j-i$. Return the largest distance over all valid pairs. A zero-distance pair may be the best available choice, and the answer is also zero when no pair with positive distance satisfies both the index and value conditions.

### Function Contract

**Inputs**

- `nums1`: a non-increasing list of $n$ integers.
- `nums2`: a non-increasing list of $m$ integers.
- $1\le n,m\le10^5$.
- Every value lies between 1 and $10^5$, inclusive.

**Return value**

- Return $\max(j-i)$ over indices satisfying $0\le i<n$, $0\le j<m$, $i\le j$, and $\texttt{nums1[i]}\le\texttt{nums2[j]}$.
- Return 0 when no positive distance is valid.

### Examples

**Example 1**

- Input: `nums1 = [55, 30, 5, 4, 2]`, `nums2 = [100, 20, 10, 10, 5]`
- Output: `2`

Indices `(2, 4)` form a valid pair because $5\le5$.

**Example 2**

- Input: `nums1 = [2, 2, 2]`, `nums2 = [10, 10, 1]`
- Output: `1`

**Example 3**

- Input: `nums1 = [30, 29, 19, 5]`, `nums2 = [25, 25, 25, 25, 25]`
- Output: `2`

### Required Complexity

- **Time:** $O(n+m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Scan `nums2` from left to right with index `j`, while maintaining the smallest not-yet-discarded index `i` in `nums1`. If `nums1[i] > nums2[j]`, that `i` cannot pair with the current `j` or any later position of `nums2`, because later values are no larger. Advance `i` until its value is small enough or the first array is exhausted.

When `nums1[i] <= nums2[j]`, this `i` is the earliest remaining first-array index that can satisfy the value condition. If $i\le j$, it therefore gives the greatest distance ending at this `j`; update the answer with $j-i$.

Neither pointer moves backward. Discarded first-array indices are permanently impossible for all future second-array values, while every feasible current endpoint is paired with its farthest eligible start. Taking the maximum of those candidates yields the global optimum.

#### Complexity detail

The `j` scan visits all $m$ entries of `nums2` at most once, and `i` advances through at most $n$ entries of `nums1`. The total time is $O(n+m)$. The two indices and running answer use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all index pairs:** Directly checks the definition but costs $O(nm)$ time.
- **Binary search for every `i`:** Find the last qualifying `j` in the non-increasing second array for $O(n\log m)$ time.
- **Index condition:** A value-compatible pair with $i>j$ is invalid and must not produce a negative or reversed distance.
- **Equal values:** The comparison is non-strict, so equality is valid.
- **No positive distance:** The initialized answer 0 is correct.
- **Unequal lengths:** Either array may finish first; indices always belong to their own arrays.
- **Repeated plateaus:** Pointer monotonicity remains valid when many adjacent values are equal.
- **Exhausted first array:** Once every `nums1` value is too large, later smaller `nums2` values cannot recover a valid pair.

</details>
