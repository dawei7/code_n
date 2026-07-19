# Final Prices With a Special Discount in a Shop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1475 |
| Difficulty | Easy |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) |

## Problem Description
### Goal

The integer array `prices` lists shop items in their displayed order. When buying item `i`, inspect only items to its right. Its discount is the price at the smallest index `j` satisfying both $j>i$ and `prices[j] <= prices[i]`.

Subtract that first qualifying later price from `prices[i]`. If no later price is less than or equal to the current price, the item receives no discount and retains its original price. Return the final price for every item without changing which later occurrence supplies each discount.

### Function Contract
**Inputs**

Let $N$ be the number of shop items.

- `prices`: an integer array with $1 \le N \le 500$.
- Every item price lies in the inclusive range $[1,1000]$.

**Return value**

Return an integer array `answer` of length $N$. For each index $i$, if $j$ is the first later index with `prices[j] <= prices[i]`, then `answer[i] = prices[i] - prices[j]`; otherwise, `answer[i] = prices[i]`.

### Examples
**Example 1**

- Input: `prices = [8,4,6,2,3]`
- Output: `[4,2,4,2,3]`
- Explanation: Prices `8`, `4`, and `6` use their first qualifying later discounts `4`, `2`, and `2`. Neither of the final two items has a qualifying later price.

**Example 2**

- Input: `prices = [1,2,3,4,5]`
- Output: `[1,2,3,4,5]`
- Explanation: Every later price is larger than the current one, so no discount applies.

**Example 3**

- Input: `prices = [10,1,1,6]`
- Output: `[9,0,1,6]`
- Explanation: The first `1` discounts `10`, and the second `1` discounts the first `1` because equality qualifies.
