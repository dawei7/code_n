# Merge Operations for Minimum Travel Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3538 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-operations-for-minimum-travel-time/) |

## Problem Description

### Goal

A straight road runs from kilometer `0` to kilometer `l`. There are `n` signs at the strictly increasing positions in `position`, including a sign at each endpoint. For every $i<n-1$, `time[i]` is the number of minutes needed to travel one kilometer after passing `position[i]` and before reaching `position[i + 1]`.

Perform exactly `k` merge operations. In one operation, choose two currently adjacent signs at indices `i` and `i + 1`, where the first sign is not the road's starting sign and the second is not beyond the ending sign. Add the first sign's time to the second sign's time, then remove the first sign and its position. Consequently, removing several consecutive original signs accumulates their times into the next sign that remains.

After all merges, each interval between consecutive remaining signs uses the time stored at its left endpoint. Return the minimum possible total minutes required to travel from `0` to `l` after exactly `k` merges.

### Function Contract

**Inputs**

- `l`: The road length in kilometers, where $1 \le l \le 10^5$.
- `n`: The number of signs, equal to both array lengths, where $2 \le n \le \min(l+1,50)$.
- `k`: The exact number of merges, where $0 \le k \le \min(n-2,10)$.
- `position`: Strictly increasing sign positions with `position[0] = 0` and `position[n - 1] = l`.
- `time`: Positive per-kilometer travel times, each at most $100$, whose total is at most $100$.

**Return value**

- The minimum total travel time in minutes after exactly `k` valid merges.

### Examples

**Example 1**

- Input: `l = 10, n = 4, k = 1, position = [0,3,8,10], time = [5,8,3,6]`
- Output: `62`
- Explanation: Removing the sign at kilometer `3` changes the time at kilometer `8` to `11`. The remaining intervals cost `8 * 5 + 2 * 11 = 62` minutes.

**Example 2**

- Input: `l = 5, n = 5, k = 1, position = [0,1,2,3,5], time = [8,3,9,3,3]`
- Output: `34`
- Explanation: Merging the signs originally at kilometers `1` and `2` leaves interval costs `2 * 8`, `1 * 12`, and `2 * 3`.
