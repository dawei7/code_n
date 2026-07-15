# Longest Turbulent Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 978 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-turbulent-subarray/) |

## Problem Description

### Goal

Given an integer array `arr`, find the maximum length of a turbulent subarray. A subarray is contiguous, and it is turbulent when the comparison sign between adjacent elements flips at every step.

More formally, for a range `arr[i], ..., arr[j]`, one valid orientation requires `arr[k] > arr[k + 1]` at odd indices `k` and `arr[k] < arr[k + 1]` at even indices; the other orientation reverses those two signs. Either orientation is acceptable throughout the range. Equal adjacent values satisfy neither strict comparison and therefore stop a turbulent range. Return the length of the longest qualifying contiguous range; a single element is turbulent vacuously.

### Function Contract

**Inputs**

- `arr`: a list of $N$ integers, where $1 \le N \le 4\cdot10^4$ and $0 \le \texttt{arr[i]} \le 10^9$.

**Return value**

- The maximum number of elements in a contiguous subarray whose adjacent comparison signs strictly alternate.

### Examples

**Example 1**

- Input: `arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]`
- Output: `5`
- Explanation: `[4, 2, 10, 7, 8]` follows $4>2<10>7<8$.

**Example 2**

- Input: `arr = [4, 8, 12, 16]`
- Output: `2`
- Explanation: consecutive increases cannot both belong to a longer turbulent range.

**Example 3**

- Input: `arr = [100]`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the required final comparison:** Let `up` be the length of the longest turbulent subarray ending at the current position whose final comparison is an increase. Let `down` mean the same when the final comparison is a decrease. Both start at one because a single element needs no comparison.

**Extend only the opposite state:** If `arr[i] > arr[i - 1]`, an increasing comparison can extend exactly a range whose previous final comparison was decreasing, so set `up = down + 1` and reset `down = 1`. If the current comparison decreases, apply the symmetric update `down = up + 1` and reset `up = 1`. Equality resets both states to one because neither strict sign is available.

Every turbulent range ending at `i` must have one of these two final signs. The alternating requirement uniquely determines which state at `i - 1` it may extend, so the recurrence neither misses a longer range nor accepts two identical consecutive signs. Taking the maximum state over the scan yields the global longest length.

#### Complexity detail

The algorithm visits each of the $N$ elements once and performs constant work per adjacent comparison, giving $O(N)$ time. It stores only `up`, `down`, and the best length, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Start a scan at every index:** Extending each candidate range independently is correct but takes $O(N^2)$ time on an array that remains turbulent throughout.
- **Comparison-array sliding window:** Converting adjacent pairs to signs and finding the longest alternating nonzero sign window also runs in $O(N)$ time, but explicitly storing all signs uses $O(N)$ space unnecessarily.
- **Equal neighbors:** Equality terminates every turbulent range crossing that pair and resets both state lengths to one.
- **Monotone arrays:** Any two unequal adjacent elements form a turbulent range of length two, but a second comparison with the same sign cannot extend it.
- **Single element:** With no adjacent comparison to violate the rule, the answer is one.

</details>
