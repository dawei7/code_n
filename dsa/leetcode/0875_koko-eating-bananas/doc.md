# Koko Eating Bananas

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 875 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) |

## Problem Description
### Goal
Koko has $n$ piles of bananas, with `piles[i]` bananas in the $i$th pile. The guards are away for exactly `h` hours. Before eating, Koko chooses one integer bananas-per-hour speed `k` that remains fixed throughout that time.

During each hour, she selects one pile and eats `k` bananas from it. If fewer than `k` bananas remain in that pile, she finishes the pile but does not begin another pile during the same hour. Koko wants to eat as slowly as possible while still finishing every pile before the guards return. Find the minimum integer speed `k` that lets her finish within `h` hours.

### Function Contract
**Inputs**

- `piles`: an array of $n$ positive pile sizes, where $1 \leq n \leq 10^4$ and $1 \leq \texttt{piles[i]} \leq 10^9$.
- `h`: the available number of hours, where $n \leq \texttt{h} \leq 10^9$.
- Let $M=\max(\texttt{piles})$.

**Return value**

Return the smallest positive integer `k` for which all piles can be consumed in at most `h` hours.

### Examples
**Example 1**

- Input: `piles = [3,6,7,11], h = 8`
- Output: `4`

**Example 2**

- Input: `piles = [30,11,23,4,20], h = 5`
- Output: `30`

With only one hour per pile, the speed must cover the largest pile.

**Example 3**

- Input: `piles = [30,11,23,4,20], h = 6`
- Output: `23`

One extra hour permits a smaller speed than in Example 2.
