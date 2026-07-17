# Closest Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1755 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Bit Manipulation, Sorting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-subsequence-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `goal`. A subsequence may be formed by deleting any number of elements, including all of them, without changing the order of those retained. Its sum is the total of its selected elements.

Among every possible subsequence of `nums`, find one whose sum is closest to `goal`. Return the minimum possible absolute difference between that subsequence sum and `goal`. The selected subsequence need not be contiguous, and the empty subsequence contributes a sum of zero.

### Function Contract

**Inputs**

- `nums`: an integer array with $1 \le n \le 40$, where $n=\lvert\texttt{nums}\rvert$ and each value lies between $-10^7$ and $10^7$, inclusive.
- `goal`: an integer satisfying $-10^9 \le \texttt{goal} \le 10^9$.

**Return value**

- Return $\min\lvert\texttt{goal}-x\rvert$ over all sums $x$ of subsequences of `nums`.

### Examples

**Example 1**

- Input: `nums = [5, -7, 3, 5], goal = 6`
- Output: `0`
- Explanation: Selecting `5`, `-7`, `3`, and `5` gives a sum of `6`, exactly matching the goal.

**Example 2**

- Input: `nums = [7, -9, 15, -2], goal = -5`
- Output: `1`
- Explanation: A subsequence sum of `-6` is attainable, and no attainable sum is closer to `-5`.

**Example 3**

- Input: `nums = [1, 2, 3], goal = -7`
- Output: `7`
- Explanation: Every nonempty subsequence has a positive sum, so the empty subsequence with sum zero is closest.

### Required Complexity

- **Time:** $O(n2^{n/2})$
- **Space:** $O(2^{n/2})$

<details>
<summary>Approach</summary>

#### General

**Split the exponential search**

There are $2^n$ possible subsequences, which is too many when $n=40$. Divide `nums` near its midpoint. Each half then has at most 20 elements and therefore at most $2^{n/2}$ subset sums. Starting with the empty sum zero, process each value by adjoining that value to every sum already generated; this enumerates precisely the sums obtainable from that half.

**Turn a global choice into a complement search**

Every subsequence of the original array is uniquely the combination of a subset from the left half and one from the right half. If a left subset contributes $x$, the ideal right contribution is $\texttt{goal}-x$. Sort all right-half sums, then use binary search to locate where this ideal value would be inserted.

**Inspect both neighbors**

The insertion position is the smallest right sum not below the desired complement. The closest available value must be either that sum or its immediate predecessor: every earlier value is no larger than the predecessor, and every later value is no smaller than the insertion value. Checking both valid neighbors therefore finds the best completion for the current left sum.

Since every left sum is examined and its best possible right partner is considered, the minimum difference found covers every full-array subsequence. A difference of zero is globally optimal, so it may be returned immediately.

#### Complexity detail

Each half produces at most $2^{\lceil n/2\rceil}$ sums. Generating them takes exponential time, sorting the right sums and binary-searching once for every left sum add a factor of $O(n)$, giving $O(n2^{n/2})$ time. The two collections of subset sums occupy $O(2^{n/2})$ space.

#### Alternatives and edge cases

- **Enumerate every full-array subset:** Direct bitmask or recursive enumeration uses $O(2^n)$ time and becomes impractical at the maximum length.
- **Set-based reachable-sum dynamic programming:** Tracking every integer sum can work when the numeric range is small, but values up to $10^7$ make pseudo-polynomial state growth unsuitable here.
- **Sort both sum lists and use two pointers:** A descending/ascending sweep can replace the repeated binary searches after both lists are sorted, with the same meet-in-the-middle principle.
- **Empty subsequence:** Sum zero is always available and can be optimal, especially when `goal` is zero or all nonempty sums lie farther away.
- **Negative values:** Subset sums are not monotone in selection size; enumeration must retain both positive and negative totals.
- **Exact match:** Once a combined sum equals `goal`, the minimum difference is zero and no further search can improve it.
- **Duplicate sums:** Repeated values may generate identical subset sums, but duplicates do not affect correctness and need not be removed.
- **Insertion boundaries:** If the desired complement lies below or above every right sum, only the existing neighbor on that side is checked.
- **Large goal magnitude:** The answer can be as large as $10^9$, so the empty subsequence must be included when initializing the best difference.

</details>
