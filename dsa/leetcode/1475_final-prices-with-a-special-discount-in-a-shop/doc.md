# Final Prices With a Special Discount in a Shop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1475 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [final-prices-with-a-special-discount-in-a-shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/).

### Goal
For each item, subtract the price of the first later item whose price is less than or equal to it. If no such later item exists, the price stays unchanged.

### Function Contract
**Inputs**

- `prices`: item prices in order.

**Return value**

The final discounted prices.

### Examples
**Example 1**

- Input: `prices = [8,4,6,2,3]`
- Output: `[4,2,4,2,3]`

**Example 2**

- Input: `prices = [1,2,3,4,5]`
- Output: `[1,2,3,4,5]`

**Example 3**

- Input: `prices = [10,1,1,6]`
- Output: `[9,0,1,6]`

---

## Solution
### Approach
Monotonic stack. Scan left to right, keeping indices whose discount has not been found; when a new price is small enough, resolve all waiting higher-or-equal prices.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(prices):
    result = list(prices)
    stack = []
    for index, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
            result[stack.pop()] -= price
        stack.append(index)
    return result
```
</details>
