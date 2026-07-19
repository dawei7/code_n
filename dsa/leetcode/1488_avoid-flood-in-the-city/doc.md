# Avoid Flood in The City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1488 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/avoid-flood-in-the-city/) |

## Problem Description
### Goal

Initially every lake is empty. On day `i`, a positive value `rains[i] = lake` means rain fills that lake. If rain reaches a lake that is already full, a flood occurs. A zero means no rain falls; on that day, exactly one lake must be selected for drying. Drying a full lake empties it, while drying an empty lake has no effect.

Produce one action for each day that prevents every flood. Rainy days must contain `-1`; zero days must contain a positive lake identifier to dry. Any flood-free schedule is acceptable. If no schedule can avoid flooding, return an empty array.

### Function Contract
**Inputs**

Let $N$ be the length of `rains`.

- `rains`: an integer array with $1 \le N \le 10^5$.
- Every entry satisfies $0 \le \texttt{rains[i]} \le 10^9$.
- A positive entry identifies the lake filled on that day.
- A zero entry provides one drying action for any chosen lake.

**Return value**

Return an integer array `ans` of length $N$ when a valid schedule exists:

- if `rains[i] > 0`, then `ans[i] = -1`;
- if `rains[i] = 0`, then `ans[i]` is a positive lake identifier dried that day;
- simulating the actions from an all-empty state never rains on a full lake.

Return `[]` if no valid schedule exists.

### Examples
**Example 1**

- Input: `rains = [1,2,3,4]`
- Output: `[-1,-1,-1,-1]`
- Explanation: Each lake receives rain only once, so no drying is needed.

**Example 2**

- Input: `rains = [1,2,0,0,2,1]`
- One valid output: `[-1,-1,2,1,-1,-1]`
- Explanation: Dry lake `2` before its second rain, then dry lake `1` before its second rain. Reversing those two dry choices is also valid.

**Example 3**

- Input: `rains = [1,2,0,1,2]`
- Output: `[]`
- Explanation: Both full lakes will receive rain again, but only one intervening dry day is available.
