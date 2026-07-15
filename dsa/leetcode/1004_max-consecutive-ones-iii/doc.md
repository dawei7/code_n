# Max Consecutive Ones III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1004 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/max-consecutive-ones-iii/) |

## Problem Description

### Goal

You are given a binary array `nums` and an integer `k`. You may flip at most `k` entries whose value is `0`, changing each selected entry to `1`.

Return the maximum number of consecutive `1`s that can appear after those flips. Because the chosen positions must contribute to one contiguous run, the task is equivalently to find the longest subarray containing at most `k` zeroes; every zero in that subarray can be flipped, while its existing ones remain unchanged.

### Function Contract

**Inputs**

- `nums`: a binary array of length $N$, where $1\le N\le10^5$ and every element is either `0` or `1`.
- `k`: the maximum number of zeroes that may be flipped, where $0\le k\le N$.

**Return value**

- The maximum length of a contiguous run of `1`s obtainable by flipping at most `k` zeroes.

### Examples

**Example 1**

- Input: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- Output: `6`
- Explanation: Flipping the zero at index `5` and the final zero creates a consecutive run of six ones from indices `5` through `10`.

**Example 2**

- Input: `nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3`
- Output: `10`
- Explanation: The subarray from indices `2` through `11` contains exactly three zeroes, so all ten of its entries can become `1`.

**Example 3**

- Input: `nums = [1, 1, 1], k = 0`
- Output: `3`
- Explanation: No flip is needed because the entire array is already one consecutive run of ones.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn flips into a window condition:** A subarray can be changed entirely to ones precisely when it contains at most `k` zeroes. Its existing ones cost nothing, and each zero consumes one permitted flip. This converts the requested run into the longest contiguous window satisfying a simple zero-count constraint.

**Grow the right boundary and repair violations:** Maintain a left boundary, a zero counter, and the best valid length. Move the right boundary across `nums`, incrementing the counter whenever `nums[right] == 0`. If the count exceeds `k`, advance `left` until enough departing zeroes have been removed and the window is valid again. Once repaired, update the best length with `right - left + 1`.

**Why discarding the prefix is safe:** For a fixed right boundary, after shrinking stops, `left` is the earliest boundary that leaves at most `k` zeroes in the window. Any earlier boundary is invalid, so no longer valid window ending at this position was skipped. Boundaries only move to the right; therefore every possible right endpoint is considered and the longest feasible subarray is recorded.

#### Complexity detail

The right boundary visits each of the $N$ entries once. The left boundary also advances at most $N$ times over the entire run, so the total work is $O(N)$ rather than one complete scan per window. The two boundaries, the zero counter, and the best length use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix sums plus binary search:** Prefix zero counts can test a window quickly, and binary searching each left boundary gives $O(N\log N)$ time and $O(N)$ space, but it is less direct than the linear window.
- **Try every starting position:** Extending a fresh window from every index is correct, but an array with no zeroes forces $\Theta(N^2)$ inspections.
- **Zero flip allowance:** When `k == 0`, the window reduces to the longest run already containing only ones.
- **Allowance covers every zero:** If the array has at most `k` zeroes, the entire array is feasible and the answer is $N$.
- **All zeroes:** The result is $\min(N,k)$, including `0` when `k == 0`.

</details>
