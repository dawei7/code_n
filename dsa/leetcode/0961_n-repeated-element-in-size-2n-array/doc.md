# N-Repeated Element in Size 2N Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 961 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [n-repeated-element-in-size-2n-array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) |

## Problem Description

### Goal

An integer array `nums` has length $2N$ and contains exactly $N+1$ distinct values. Of those values, $N$ occur exactly once, while one remaining value occurs exactly $N$ times.

The entries may appear in any order, so the repeated copies do not have to be adjacent. No singleton value appears a second time, and the input always satisfies the stated frequency guarantee; there is no invalid-input case to report.

Identify and return the value that is repeated $N$ times. The requested result is the value itself, not its frequency or the indices where its copies occur.

### Function Contract

**Inputs**

- `nums`: an integer array of length $2N$, where $2 \le N \le 5000$.
- Every value is between $0$ and $10^4$, inclusive.
- The promised frequency structure always holds: one value occurs $N$ times and every other value occurs once.

**Return value**

Return the unique value whose frequency is $N$.

### Examples

**Example 1**

- Input: `nums = [1,2,3,3]`
- Output: `3`

**Example 2**

- Input: `nums = [2,1,2,5,3,2]`
- Output: `2`

**Example 3**

- Input: `nums = [5,1,5,2,5,3,5,4]`
- Output: `5`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Stop at the first duplicate.** Scan `nums` from left to right while storing every previously visited value in a set. If the current value is already present, return it immediately.

**Why that duplicate is the answer.** The contract says that every value except one occurs exactly once. Consequently, the first value encountered twice cannot be one of the singleton values; it must be the value that appears $N$ times. The promised repeated value necessarily produces such an encounter, so the scan always returns before it finishes.

#### Complexity detail

At most $2N$ values are processed, and average-case set lookup and insertion take constant time, giving $O(N)$ time. The set may hold $N+1$ distinct values, so it uses $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Constant-distance comparison:** The frequency guarantee implies that two copies of the answer occur within distance three. Comparing each value with the previous three positions yields $O(N)$ time and $O(1)$ space, but its pigeonhole argument is less direct.
- **Frequency table:** Count every value and return the one with count $N$. This is also linear but performs a full scan even after the answer has repeated.
- **Repeated full-array counting:** For each candidate, scan the entire array to count it. This is correct but takes $O(N^2)$ time.
- **Minimum size:** When $N=2$, the four-element array still contains one value twice and two singleton values.
- **Zero as the answer:** A repeated value of `0` is valid and must not be confused with a sentinel.
- **Adjacent copies:** The repeated value may appear consecutively, so the second copy should be returned immediately.

</details>
