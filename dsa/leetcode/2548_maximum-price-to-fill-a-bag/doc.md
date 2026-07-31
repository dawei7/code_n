# Maximum Price to Fill a Bag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2548 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-price-to-fill-a-bag](https://leetcode.com/problems/maximum-price-to-fill-a-bag/) |

## Problem Description

### Goal

Each row `items[i] = [price_i, weight_i]` describes an item with a total price and weight. An item may be divided in any proportions whose fractions sum to 1; each resulting portion keeps the same fraction of both the original weight and the original price.

Given a positive bag `capacity`, choose whole items or fractional portions whose weights total exactly that capacity. Return the maximum total price obtainable. If all available weight is insufficient to fill the bag exactly, return `-1`. A floating-point result within $10^{-5}$ of the optimum is accepted.

### Function Contract

**Inputs**

- `items`: A list of `[price, weight]` pairs for divisible items.
- `capacity`: The exact positive weight that the bag must contain.

There are at most $10^5$ items; every price and weight is between 1 and $10^4$, and `capacity` is at most $10^9$.

**Return value**

Return the maximum price of an exact-capacity selection as a floating-point number, or `-1` when the total available weight is smaller than `capacity`.

### Examples

**Example 1**

- Input: `items = [[50,1],[10,8]], capacity = 5`
- Output: `55.00000`
- Explanation: Take the first item and four eighths of the second item.

**Example 2**

- Input: `items = [[100,30]], capacity = 50`
- Output: `-1.00000`
- Explanation: Only 30 units of weight are available, so the bag cannot be filled.
