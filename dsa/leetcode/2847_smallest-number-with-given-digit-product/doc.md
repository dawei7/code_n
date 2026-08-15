# Smallest Number With Given Digit Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2847 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-number-with-given-digit-product/) |

## Problem Description

### Goal

You are given a positive integer `n`. Find the smallest positive integer whose decimal digits have product exactly `n`, and return that integer as a string.

Every digit of the returned number participates in the product. If no decimal integer can have the required digit product, return `"-1"` instead. The comparison is by ordinary numeric value, so a valid answer with fewer digits is smaller than any valid answer with more digits; among answers of equal length, their left-to-right digit order decides which is smallest.

### Function Contract

**Inputs**

- `n`: The required product of the answer's decimal digits.

The constraint is $1\le n\le10^{18}$.

**Return value**

- A string containing the smallest positive integer whose digit product is `n`, or `"-1"` when no such integer exists.

### Examples

#### Example 1

- **Input:** `n = 105`
- **Output:** `"357"`
- **Explanation:** The digits multiply to $3\cdot5\cdot7=105$, and no smaller positive integer has that digit product.

#### Example 2

- **Input:** `n = 7`
- **Output:** `"7"`
- **Explanation:** The one-digit number already has the required product and is the smallest possible answer.

#### Example 3

- **Input:** `n = 44`
- **Output:** `"-1"`
- **Explanation:** The prime factor $11$ cannot be supplied by any decimal digit, so no valid integer exists.
