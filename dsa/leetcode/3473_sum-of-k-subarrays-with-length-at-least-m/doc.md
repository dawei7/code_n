# Sum of K Subarrays With Length at Least M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3473 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/) |

## Problem Description

### Goal

You are given an integer array `nums`, a required number of selections `k`, and a minimum length `m`. Select exactly `k` contiguous subarrays. Every selected subarray must contain at least `m` elements, and no array position may belong to more than one selection. Separate selections may have unused elements between them, or they may be adjacent as long as they do not overlap.

Maximize the sum of all elements contained in the selected subarrays and return that maximum total. Values may be negative, so all `k` subarrays must still be selected even when doing so lowers the total; choosing fewer subarrays or empty subarrays is not permitted. The input guarantee ensures that at least `k * m` positions exist.

### Function Contract

**Inputs**

- `nums`: The integer array from which the subarrays are selected.
- `k`: The exact number of non-overlapping subarrays to select.
- `m`: The minimum permitted length of every selected subarray.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le2000$, $-10^4\le\texttt{nums[i]}\le10^4$, $1\le m\le3$, and $1\le k\le\lfloor n/m\rfloor$.

**Return value**

Return the maximum possible combined sum of exactly `k` valid non-overlapping subarrays.

### Examples

#### Example 1

- **Input:** `nums = [1,2,-1,3,3,4], k = 2, m = 2`
- **Output:** `13`

Selecting `[1,2]` and `[3,3,4]` gives sums `3` and `10`.

#### Example 2

- **Input:** `nums = [-10,3,-1,-2], k = 4, m = 1`
- **Output:** `-10`

Four singleton subarrays are required, so every element must be selected despite the negative total.

#### Example 3

- **Input:** `nums = [5,-10,6,7,-2,8], k = 2, m = 1`
- **Output:** `24`

The singleton `[5]` and the later subarray `[6,7,-2,8]` achieve the maximum total.
