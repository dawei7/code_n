# Fair Candy Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 888 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/fair-candy-swap/) |

## Problem Description
### Goal
Alice and Bob each own boxes of candy, and the integer at each position of `aliceSizes` or `bobSizes` is the number of candies in that box. Their current total numbers of candies are different.

They will exchange exactly one box each. Return `[x, y]`, where Alice gives a box containing `x` candies and Bob gives a box containing `y` candies, so their totals are equal after the exchange. At least one valid swap is guaranteed; when several swaps work, return any one of them.

### Function Contract
Let $p=\lvert\texttt{aliceSizes}\rvert$ and $q=\lvert\texttt{bobSizes}\rvert$.

**Inputs**

- `aliceSizes`: Alice's box sizes, where $1 \leq p \leq 10^4$ and every size is between $1$ and $10^5$.
- `bobSizes`: Bob's box sizes, where $1 \leq q \leq 10^4$ and every size is between $1$ and $10^5$.

Alice's and Bob's initial totals differ, and the input guarantees at least one balancing exchange.

**Return value**

Return `[x, y]` for any valid exchange of Alice's `x`-candy box and Bob's `y`-candy box.

### Examples
**Example 1**

- Input: `aliceSizes = [1,1], bobSizes = [2,2]`
- Output: `[1,2]`

**Example 2**

- Input: `aliceSizes = [1,2], bobSizes = [2,3]`
- Output: `[1,2]`

**Example 3**

- Input: `aliceSizes = [2], bobSizes = [1,3]`
- Output: `[2,3]`
