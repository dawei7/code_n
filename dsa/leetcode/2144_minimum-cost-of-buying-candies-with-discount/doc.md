# Minimum Cost of Buying Candies With Discount

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2144 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-cost-of-buying-candies-with-discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) |

## Problem Description

### Goal

A candy shop offers one free candy for every two candies purchased. The
customer may choose any remaining candy as the free one, but its cost must be
less than or equal to the cheaper of the two purchased candies.

For example, buying candies costing `2` and `3` permits a candy costing `1` to
be free, but does not permit one costing `4`. Discounts may be applied
repeatedly until every candy has been obtained.

Given the cost of each candy, return the minimum total amount that must be paid
to obtain all of them.

### Function Contract

**Inputs**

- `cost`: A 0-indexed list of candy prices. Its length is between $1$ and
  $100$, inclusive, and every price is between $1$ and $100$, inclusive.

**Return value**

Return the smallest sum of prices that must be paid after assigning every
valid free candy.

### Examples

#### Example 1

- **Input:** `cost = [1,2,3]`
- **Output:** `5`
- **Explanation:** Pay for costs `3` and `2`, then take cost `1` for free.

#### Example 2

- **Input:** `cost = [6,5,7,9,2,2]`
- **Output:** `23`
- **Explanation:** Pay for `9` and `7` to receive `6` free, then pay for `5` and
  `2` to receive the remaining `2` free.

#### Example 3

- **Input:** `cost = [5,5]`
- **Output:** `10`
- **Explanation:** Fewer than three candies means neither candy can be free.
