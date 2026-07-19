# Minimum Absolute Sum Difference

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-absolute-sum-difference/) |
| Frontend ID | 1818 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two positive-integer arrays `nums1` and `nums2` have the same length. Their absolute sum difference is obtained by adding $\lvert\texttt{nums1[i]}-\texttt{nums2[i]}\rvert$ over every corresponding index.

You may change at most one position of `nums1`. If you make a change, the replacement value must equal some value that occurs anywhere in the original `nums1`; choosing the value from another position does not remove or alter that source position. Minimize the absolute sum difference after this optional replacement and return the minimum modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums1`: an array of $n$ positive integers, each between 1 and $10^5$.
- `nums2`: an array of the same length, with values in the same range.
- The common length satisfies $1 \le n \le 10^5$.

**Return value**

- Return the smallest attainable sum of corresponding absolute differences after at most one permitted replacement in `nums1`, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums1 = [1,7,5], nums2 = [2,3,5]`
- Output: `3`

Replacing `7` with either `1` or `5` reduces its difference from 4 to 2.

**Example 2**

- Input: `nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]`
- Output: `0`

The arrays already match, so the optional replacement is unnecessary.

**Example 3**

- Input: `nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]`
- Output: `20`

Replacing the first value `1` with the available value `10` gives the optimal reduction.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate the original total from the best possible improvement**

First accumulate every original difference. A replacement affects only one index, so its benefit is the old difference at that index minus the smallest difference obtainable there using a value from `nums1`. The globally optimal operation is therefore the single largest nonnegative benefit among all indices. If every benefit is zero, making no replacement is optimal.

**Find the nearest permitted value efficiently**

Sort a copy of `nums1`. For a target `nums2[i]`, the replacement minimizing absolute difference is its nearest value in this ordered copy. Binary search for the insertion position; only the value at that position and its predecessor can be nearest. Compare both existing candidates with the original difference and retain the largest reduction seen.

**Why subtracting the maximum reduction is optimal**

For each index, binary search considers the closest original value on both sides of its target, so it computes the minimum attainable difference at that index. Each resulting reduction describes the best replacement whose sole changed position is that index. Because the rules permit at most one change, no valid outcome can combine reductions from different indices. Subtracting the maximum individual reduction from the unchanged total therefore gives the global minimum.

#### Complexity detail

Sorting the $n$ values costs $O(n\log n)$. The second pass performs $n$ binary searches, each taking $O(\log n)$, so total time remains $O(n\log n)$. The sorted copy uses $O(n)$ space. Keep the unreduced total and best reduction until the end, then apply the modulus; reducing intermediate differences could corrupt their ordering.

#### Alternatives and edge cases

- **Try every replacement at every index:** Scanning all values of `nums1` for each target is correct but takes $O(n^2)$ time.
- **Balanced ordered set:** It supports predecessor and successor queries in $O(\log n)$ without a sorted copy, but is more machinery than a one-time sort.
- **Already equal arrays:** Every original difference and every possible reduction is zero, so return zero.
- **Duplicate values:** Duplicates do not create new replacement choices; retaining them in the sorted copy is harmless.
- **One-element arrays:** The only available replacement is the existing value, so the original difference cannot improve.
- **Nearest value at an endpoint:** The insertion position may be zero or $n$; inspect only candidates whose indices exist.
- **Modulo handling:** Select the best reduction using exact totals and apply $10^9+7$ only to the final minimized sum.

</details>
