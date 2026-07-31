# Length of the Longest Subsequence That Sums to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2915 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) |

## Problem Description

### Goal

Choose a subsequence from the zero-indexed positive-integer array `nums`. A
subsequence retains the relative order of the selected positions but may delete
any number of other elements. Different occurrences of the same value remain
separate choices because each array position can be selected at most once.

Among all subsequences whose elements sum to exactly `target`, return the
greatest possible number of selected elements. The goal is length rather than
the number of different solutions or the fewest elements. If no subsequence
has the required sum, return `-1`.

### Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers, where $1\le n\le1000$ and $1\le\texttt{nums[i]}\le1000$.
- `target`: The required subsequence sum, where $1\le\texttt{target}\le1000$.

**Return value**

Return the maximum length of a subsequence whose sum is exactly `target`, or
`-1` when the target is unreachable.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], target = 9`
- Output: `3`
- Explanation: `[1, 3, 5]` and `[2, 3, 4]` have length three, longer than `[4, 5]`.

**Example 2**

- Input: `nums = [4, 1, 3, 2, 1, 5], target = 7`
- Output: `4`
- Explanation: The subsequence `[1, 3, 2, 1]` reaches seven using four positions.

**Example 3**

- Input: `nums = [1, 1, 5, 4, 5], target = 3`
- Output: `-1`
- Explanation: No selection of positions sums to three.
