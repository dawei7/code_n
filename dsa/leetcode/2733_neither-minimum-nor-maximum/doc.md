# Neither Minimum nor Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2733 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/neither-minimum-nor-maximum/) |

## Problem Description

### Goal

An array contains distinct positive integers. Return any array value that is neither the smallest nor the largest value in the complete array.

When no such value exists, return `-1`. Because any qualifying value is accepted, the result does not have to follow the input order or choose a particular interior value when several are available. The selected integer must occur in `nums`.

### Function Contract

**Inputs**

- `nums`: An array of distinct integers with $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums}[i] \le 100$.

**Return value**

Return any value strictly between the global minimum and maximum of `nums`, or `-1` if no such element exists.

### Examples

#### Example 1

- **Input:** `nums = [3,2,1,4]`
- **Output:** `2`
- **Explanation:** The global extremes are `1` and `4`, so either `2` or `3` is valid.

#### Example 2

- **Input:** `nums = [1,2]`
- **Output:** `-1`
- **Explanation:** With two distinct elements, one is the minimum and the other is the maximum.

#### Example 3

- **Input:** `nums = [2,1,3]`
- **Output:** `2`
- **Explanation:** `2` is the only value strictly between `1` and `3`.
