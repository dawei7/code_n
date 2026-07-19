# Count Pairs in Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-in-two-arrays/) |
| Frontend ID | 1885 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, have the same length $N$. Choose two distinct positions in increasing index order, $(i,j)$ with $i<j$, and compare the sum of the two values selected from `nums1` with the sum at those same positions in `nums2`.

Count how many index pairs satisfy the strict inequality

$$
\texttt{nums1[i]}+\texttt{nums1[j]} >
\texttt{nums2[i]}+\texttt{nums2[j]}.
$$

Pairs whose two sums are equal do not count. Return the total over all possible index pairs.

### Function Contract

**Inputs**

- `nums1`: a length-$N$ array of positive integers.
- `nums2`: a length-$N$ array of positive integers corresponding position by position with `nums1`.
- $1 \le N \le 10^5$, and every array value lies between $1$ and $10^5$, inclusive.

**Return value**

- Return the number of pairs $(i,j)$ with $i<j$ whose `nums1` sum is strictly larger than the corresponding `nums2` sum.

### Examples

**Example 1**

- Input: `nums1 = [2,1,2,1], nums2 = [1,2,1,2]`
- Output: `1`

Only pair `(0,2)` satisfies the required inequality.

**Example 2**

- Input: `nums1 = [1,10,6,2], nums2 = [1,4,1,5]`
- Output: `5`

Every pair except `(0,3)` has a strictly positive combined difference.

**Example 3**

- Input: `nums1 = [5,1], nums2 = [3,3]`
- Output: `0`

The two sides are equal, so the strict comparison rejects the pair.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Transform the pair inequality**

For each position define

$$
d_i=\texttt{nums1[i]}-\texttt{nums2[i]}.
$$

Moving the `nums2` terms to the left shows that a pair is valid exactly when $d_i+d_j>0$. The original positions no longer affect validity beyond requiring two distinct elements, so the difference array may be sorted.

**Count a whole block at once**

Sort the differences and place pointers at the smallest and largest remaining values. If `differences[left] + differences[right] > 0`, then every value from `left` through `right - 1` also forms a positive sum with the current right value. Add `right - left` pairs and decrement `right`.

If that smallest-plus-largest sum is nonpositive, the left value cannot pair successfully with any remaining value, because `right` is already the largest. Increment `left` and discard it. Continue until the pointers meet.

**Why every pair is counted exactly once**

Each successful step counts all still-unprocessed pairs whose larger sorted endpoint is `right`, then removes that endpoint. Each unsuccessful step proves that no pair using `left` can qualify before removing it. Thus no valid pair is missed, invalid pairs are never added, and no endpoint pair can be counted twice.

#### Complexity detail

Building the $N$ differences takes $O(N)$ time. Sorting costs $O(N\log N)$, and the two pointers move inward at most $N-1$ times, so total time is $O(N\log N)$. The difference array occupies $O(N)$ auxiliary space. The result may be as large as $\binom{N}{2}$, so implementations must use a sufficiently wide integer type where necessary.

#### Alternatives and edge cases

- **All index pairs:** Directly testing every $(i,j)$ is correct but takes $O(N^2)$ time.
- **Binary search per endpoint:** After sorting, search for the first partner greater than $-d_j$ for each $j$; this also takes $O(N\log N)$ time.
- **One element:** No pair exists, so return `0`.
- **Strict inequality:** A difference sum of exactly zero must not be counted.
- **All positive differences:** Every one of the $\binom{N}{2}$ pairs qualifies.
- **All nonpositive differences:** No pair can qualify.
- **Duplicate differences:** They remain separate indexed elements and contribute with their full multiplicity.

</details>
