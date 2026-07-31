# Keep Multiplying Found Values by Two

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2154 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [keep-multiplying-found-values-by-two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/) |

## Problem Description

### Goal

Given an integer array `nums` and a starting integer `original`, search for the
current value in the array. Whenever it is present, replace the current value
with twice itself and search again. Stop as soon as the current value is absent.

Return the value at which the process stops. Array occurrences are not
consumed: only whether a value appears at least once matters, so duplicates do
not create additional doublings.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 1000$ and
  $1 \leq \texttt{nums[i]} \leq 1000$.
- `original`: The initial integer, where $1 \leq \texttt{original} \leq 1000$.

**Return value**

Return the first value in the doubling sequence that does not appear in
`nums`.

### Examples

**Example 1**

- Input: `nums = [5, 3, 6, 1, 12]`, `original = 3`
- Output: `24`
- Explanation: The found values are `3`, `6`, and `12`; their successive
  doublings lead to absent value `24`.

**Example 2**

- Input: `nums = [2, 7, 9]`, `original = 4`
- Output: `4`
- Explanation: The starting value is absent, so no multiplication occurs.
