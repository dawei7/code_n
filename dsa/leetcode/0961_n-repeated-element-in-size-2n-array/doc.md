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
