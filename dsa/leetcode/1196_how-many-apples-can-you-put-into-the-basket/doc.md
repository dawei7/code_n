# How Many Apples Can You Put into the Basket

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1196 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [how-many-apples-can-you-put-into-the-basket](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/).

### Goal
Given apple weights and a basket capacity of `5000`, return the maximum number of apples that can fit in the basket.

### Function Contract
**Inputs**

- `weight`: List of apple weights.

**Return value**

Maximum number of apples whose total weight is at most `5000`.

### Examples
**Example 1**

- Input: `weight = [100,200,150,1000]`
- Output: `4`

**Example 2**

- Input: `weight = [900,950,800,1000,700,800]`
- Output: `5`

**Example 3**

- Input: `weight = [5000,1,1]`
- Output: `2`

---

## Solution
### Approach
To maximize the count, always take lighter apples first. Sort the weights ascending and add apples until the next one would exceed capacity.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra if sorting in place, otherwise `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
