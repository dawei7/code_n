# Pairs of Songs With Total Durations Divisible by 60

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1010 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) |

## Problem Description

### Goal

You are given a list of songs where `time[i]` is the duration, in seconds, of song `i`.

Return the number of index pairs `i`, `j` with $i<j$ whose total duration is divisible by `60`. Equivalently, count every pair satisfying `(time[i] + time[j]) % 60 == 0`; pairs are distinguished by their indices even when durations are equal, and the same song cannot be used twice.

### Function Contract

**Inputs**

- `time`: an array of $N$ song durations, where $1\le N\le6\cdot10^4$ and $1\le\texttt{time[i]}\le500$.

**Return value**

- The number of index pairs whose two durations sum to a multiple of `60`.

### Examples

**Example 1**

- Input: `time = [30, 20, 150, 100, 40]`
- Output: `3`
- Explanation: The valid index pairs have duration sums `180`, `120`, and `60`.

**Example 2**

- Input: `time = [60, 60, 60]`
- Output: `3`
- Explanation: Each of the three index pairs totals `120` seconds.

**Example 3**

- Input: `time = [10, 50, 90, 30]`
- Output: `2`
- Explanation: Remainders `10` and `50` pair, and the two remainder-`30` songs pair.
