# Minimum Number of Coins for Fruits II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2969 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/) |

## Problem Description
### Goal
A fruit market displays fruits in positions numbered from `1` through $N$.
The 1-indexed value `prices[i]` is the number of coins required to purchase
fruit `i`.

Purchasing fruit `i` grants the next `i` fruits for free, covering positions
`i + 1` through `2 * i` that exist. A fruit currently available for free may
still be purchased at its listed price; doing so starts its own offer and can
extend free coverage farther into the market.

Return the minimum number of coins needed to acquire every fruit.

### Function Contract
**Inputs**

- `prices`: the purchase prices in 1-indexed market order

Let $N=\lvert\texttt{prices}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{prices[i]}\le10^5$.

**Return value**

The minimum total purchase price of a strategy that obtains all fruits using
the stated free-fruit offers.

### Examples
**Example 1**

- Input: `prices = [3,1,2]`
- Output: `4`
- Explanation: Buy fruit `1`, then buy fruit `2` despite its free eligibility so its offer covers fruit `3`.

**Example 2**

- Input: `prices = [1,10,1,1]`
- Output: `2`
- Explanation: Buy fruit `1`, take fruit `2` free, buy fruit `3`, and take fruit `4` free.
