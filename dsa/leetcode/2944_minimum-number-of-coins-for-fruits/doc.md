# Minimum Number of Coins for Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2944 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/) |

## Problem Description
### Goal
A 0-indexed array `prices` gives the purchase cost of the fruits in market
order: `prices[i]` is the number of coins charged for the $(i+1)$-th fruit.
Purchasing the $(i+1)$-th fruit allows any number of the next $i+1$ fruits to
be taken for free.

A fruit that is currently eligible to be taken for free may instead be
purchased at its listed price. Paying for it activates that fruit's own reward,
which can make a later acquisition cheaper. Determine the minimum total number
of coins required to acquire every fruit.

### Function Contract
**Inputs**

- `prices`: the positive purchase prices in fruit order

Let $N=\lvert\texttt{prices}\rvert$. The contract guarantees
$1\le N\le1000$ and $1\le\texttt{prices[i]}\le10^5$.

**Return value**

The minimum total purchase cost that acquires all $N$ fruits.

### Examples
**Example 1**

- Input: `prices = [3,1,2]`
- Output: `4`
- Explanation: Buy the first fruit, then buy the second even though it is free;
  the second purchase covers the third fruit.

**Example 2**

- Input: `prices = [1,10,1,1]`
- Output: `2`
- Explanation: Buy fruits `1` and `3`; their rewards cover fruits `2` and
  `4`.

**Example 3**

- Input: `prices = [26,18,6,12,49,7,45,45]`
- Output: `39`
- Explanation: Buying fruits `1`, `3`, and `6` costs
  `26 + 6 + 7 = 39` and covers every remaining fruit.
