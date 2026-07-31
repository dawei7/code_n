# Number of Stable Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3686 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-stable-subsequences/) |

## Problem Description
### Goal

Count the nonempty subsequences of `nums` that are stable. A subsequence retains the original order of its chosen positions, although it may omit any number of elements. Different choices of positions count separately even when they produce the same values.

A subsequence is stable when no three consecutive elements within that subsequence all have the same parity. The restriction concerns adjacency after the omitted elements have been removed, not adjacency in the original array. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers, with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and every value at most $10^5$.

**Return value**

Return the number of nonempty stable subsequences modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 3, 5]`
- Output: `6`

Every nonempty subsequence except the one containing all three odd elements is stable.

**Example 2**

- Input: `nums = [2, 3, 4, 2]`
- Output: `14`

Among the 15 nonempty subsequences, only `[2, 4, 2]` contains three consecutive even elements.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `10`

Only subsequences of length one or two can be stable when every value is odd.
