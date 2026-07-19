# Minimum Number of Days to Make m Bouquets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1482 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) |

## Problem Description
### Goal

A garden contains $N$ flowers in a fixed left-to-right order. The flower at index `i` blooms on day `bloomDay[i]`; from that day onward it is available for use. Each flower may belong to exactly one bouquet.

Make `m` bouquets, each from `k` adjacent flowers. The flowers of one bouquet must occupy consecutive garden positions, and bouquets cannot reuse flowers. Return the minimum day by which such a selection is possible. If the garden can never supply all `m` bouquets, return `-1`.

### Function Contract
**Inputs**

Let $N$ be the length of `bloomDay`, and define the inclusive bloom-day range

$$
D = \max(\texttt{bloomDay}) - \min(\texttt{bloomDay}) + 1.
$$

- `bloomDay`: an integer array of length $N$, with $1 \le N \le 10^5$.
- Every entry satisfies $1 \le \texttt{bloomDay[i]} \le 10^9$.
- `m`: the required number of bouquets, with $1 \le m \le 10^6$.
- `k`: the number of adjacent flowers per bouquet, with $1 \le k \le N$.
- In the app-local `solve` contract, the corresponding parameter name is `bloom_day`.

**Return value**

Return the smallest day on which at least `m` pairwise disjoint groups of `k` adjacent bloomed flowers can be formed, or `-1` when this is impossible.

### Examples
**Example 1**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 1`
- Output: `3`
- Explanation: By day three, the flowers at positions zero, two, and four have bloomed, providing three one-flower bouquets.

**Example 2**

- Input: `bloomDay = [1,10,3,10,2], m = 3, k = 2`
- Output: `-1`
- Explanation: Three bouquets would require six distinct flowers, but the garden contains only five.

**Example 3**

- Input: `bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3`
- Output: `12`
- Explanation: On day seven, the unbloomed middle flower separates the garden into runs of lengths four and two, enough for only one bouquet. On day twelve, all seven positions are available and two disjoint groups of three can be selected.
