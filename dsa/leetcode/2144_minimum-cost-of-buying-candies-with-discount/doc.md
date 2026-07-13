# Minimum Cost of Buying Candies With Discount

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2144 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-of-buying-candies-with-discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/).

### Goal
Buy every candy under a discount that makes one candy free whenever two candies are purchased, provided the free candy costs no more than the cheaper purchased candy. Find the minimum total payment.

### Function Contract
**Inputs**

- `cost`: the price of each candy.

**Return value**

The minimum amount needed to obtain all candies.

### Examples
**Example 1**

- Input: `cost = [1, 2, 3]`
- Output: `5`

**Example 2**

- Input: `cost = [6, 5, 7, 9, 2, 2]`
- Output: `23`

**Example 3**

- Input: `cost = [5, 5]`
- Output: `10`

---

## Solution
### Approach
Sort prices from highest to lowest. In each consecutive group of three, pay for the first two and take the third for free. Assigning the largest eligible unpaid candy to each discount minimizes the sum paid.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
