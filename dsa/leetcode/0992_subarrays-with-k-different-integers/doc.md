# Subarrays with K Different Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 992 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subarrays-with-k-different-integers/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, count the good subarrays of `nums`. An array is good when it contains exactly `k` different integers; for instance, `[1, 2, 3, 1, 2]` contains the three different integers $1$, $2$, and $3$.

A subarray is a contiguous part of the original array, so equal value sequences occurring at different start or end positions count separately. Return the total number of contiguous subarrays whose number of different integers is exactly `k`.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le2\cdot10^4$ and $1\le\texttt{nums[i]}\le N$.
- `k`: the required number of different integers, where $1\le\texttt{k}\le N$.

**Return value**

- The number of contiguous subarrays containing exactly `k` different integers.

### Examples

**Example 1**

- Input: `nums = [1, 2, 1, 2, 3], k = 2`
- Output: `7`
- Explanation: Four length-two-or-more ranges ending before the final $3$, two shorter alternating ranges, and `[2, 3]` give seven qualifying subarrays.

**Example 2**

- Input: `nums = [1, 2, 1, 3, 4], k = 3`
- Output: `3`
- Explanation: The qualifying ranges are `[1, 2, 1, 3]`, `[2, 1, 3]`, and `[1, 3, 4]`.

**Example 3**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`
- Explanation: Every nonempty subarray contains exactly one different integer.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Convert exact counting into two monotone counts:** A sliding window naturally maintains an upper bound on the number of different values, but “exactly” is not monotone as the left endpoint moves. Let $A(m)$ be the number of subarrays containing at most $m$ different integers. Every subarray counted by $A(k)$ either has fewer than $k$ different integers or exactly $k$, while $A(k-1)$ contains precisely the former group. Therefore the requested count is $A(k)-A(k-1)$.

**Count all valid endings with one window:** For a fixed right endpoint, extend the window and update the new value's frequency. While the number of different integers exceeds the limit, move the left endpoint rightward, decrementing frequencies and removing a value from the distinct count when its frequency reaches zero. After shrinking, every start position from `left` through `right` forms a valid subarray ending at `right`, contributing `right - left + 1` to $A(m)$.

Both pointers only move forward, so each element enters and leaves a window at most once. Applying the helper with limits `k` and `k - 1` and subtracting the results counts every exactly-`k` subarray once.

#### Complexity detail

Each of the two sliding-window passes processes $N$ right endpoints and advances its left endpoint at most $N$ times, for $O(N)$ total time. Frequencies for values from $1$ through $N$ require $O(N)$ space.

#### Alternatives and edge cases

- **Enumerate every start and end:** Growing a distinct-value set from each start is straightforward but takes $O(N^2)$ time in the worst case.
- **One exact-`k` window without extra state:** A single left boundary loses how many removable duplicates precede the first essential value, so it cannot directly count every valid start.
- **All values equal:** With `k = 1`, all $N(N+1)/2$ nonempty subarrays qualify.
- **Too few different values:** If the entire array contains fewer than `k` different integers, the result is zero.
- **Limit zero:** The helper call $A(k-1)$ receives zero when `k = 1`; only the empty window is allowed, so it contributes no nonempty subarrays.

</details>
