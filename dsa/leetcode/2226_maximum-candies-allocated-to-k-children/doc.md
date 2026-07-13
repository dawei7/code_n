# Maximum Candies Allocated to K Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2226 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-candies-allocated-to-k-children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/).

### Goal
Give each of `k` children the same positive number of candies using portions split from existing piles. A child receives one portion from one pile, piles need not be fully used, and portions cannot combine candies from different piles. Maximize the candies per child.

### Function Contract
**Inputs**

- `candies`: sizes of the available piles.
- `k`: the number of children.

**Return value**

The greatest equal portion size possible, or `0` if no child can receive at least one candy.

### Examples
**Example 1**

- Input: `candies = [5, 8, 6]`, `k = 3`
- Output: `5`

**Example 2**

- Input: `candies = [2, 5]`, `k = 11`
- Output: `0`

**Example 3**

- Input: `candies = [10]`, `k = 2`
- Output: `5`

---

## Solution
### Approach
Binary-search a proposed portion size `x`. Pile `p` supplies `floor(p / x)` children, so `x` is feasible when the summed portions reach `k`. This predicate is monotonic, with search bounds from `1` through `sum(candies) / k`.

### Complexity Analysis
- **Time Complexity**: `O(n log(sum(candies) / k))`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
