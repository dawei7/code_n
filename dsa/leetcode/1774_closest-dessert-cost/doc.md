# Closest Dessert Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1774 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [closest-dessert-cost](https://leetcode.com/problems/closest-dessert-cost/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/closest-dessert-cost/).

### Goal
Choose exactly one base cost and zero, one, or two of each topping cost. Find the total cost closest to `target`, breaking ties toward the smaller total.

### Function Contract
**Inputs**

- `baseCosts`: possible base dessert costs.
- `toppingCosts`: costs of topping types.
- `target`: desired total cost.

**Return value**

Return the closest achievable dessert cost.

### Examples
**Example 1**

- Input: `baseCosts = [1,7], toppingCosts = [3,4], target = 10`
- Output: `10`

**Example 2**

- Input: `baseCosts = [2,3], toppingCosts = [4,5,100], target = 18`
- Output: `17`

**Example 3**

- Input: `baseCosts = [3,10], toppingCosts = [2,5], target = 9`
- Output: `8`

---

## Solution
### Approach
Enumerate topping sums with DFS or iterative set expansion, where each topping contributes `0`, `1`, or `2` copies. Combine every topping sum with every base cost and keep the total with smallest absolute distance to `target`, using the smaller cost on ties.

### Complexity Analysis
- **Time Complexity**: `O(B * 3^T)` in direct enumeration
- **Space Complexity**: `O(3^T)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
