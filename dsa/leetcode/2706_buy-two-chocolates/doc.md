# Buy Two Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2706 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [buy-two-chocolates](https://leetcode.com/problems/buy-two-chocolates/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/buy-two-chocolates/).

### Goal
Given a list of chocolate prices and an initial amount of money, determine if it's possible to purchase the two cheapest chocolates available. If the combined cost of the two cheapest chocolates is less than or equal to your initial money, return the amount of money you would have left after the purchase. Otherwise, if you cannot afford both of the two cheapest chocolates, return your original amount of money.

### Function Contract
**Inputs**

- `prices`: A list of integers, where `prices[i]` represents the price of the i-th chocolate.
- `money`: An integer representing the initial amount of money you have.

**Return value**

An integer representing the money left after buying the two cheapest chocolates, or the original money if they cannot be afforded.

### Examples
**Example 1**

- Input: `prices = [1,2,2]`, `money = 3`
- Output: `0`
  * Explanation: The two cheapest chocolates cost 1 and 2, totaling 3. Since 3 <= 3, you buy them and have 3 - 3 = 0 money left.

**Example 2**

- Input: `prices = [3,2,3]`, `money = 3`
- Output: `3`
  * Explanation: The two cheapest chocolates cost 2 and 3, totaling 5. Since 5 > 3, you cannot afford them. You return your original money, which is 3.

**Example 3**

- Input: `prices = [6,4,1,2]`, `money = 10`
- Output: `7`
  * Explanation: The two cheapest chocolates cost 1 and 2, totaling 3. Since 3 <= 10, you buy them and have 10 - 3 = 7 money left.

---

## Solution
### Approach
The core of this problem involves identifying the two smallest elements within a given array. This can be achieved through a few common approaches:

1.  **Sorting:** Sort the entire `prices` array in ascending order. The two cheapest chocolates will then be the first two elements of the sorted array.
2.  **Single Pass Iteration:** Iterate through the `prices` array once, keeping track of the two smallest prices encountered so far. This approach avoids a full sort and is generally more efficient for finding a fixed number of smallest elements.

After finding the two cheapest prices, their sum is compared against the available `money` to determine the final return value.

### Complexity Analysis
- **Time Complexity**: `O(N)`
  * The optimal approach involves a single pass through the `prices` list to find the two smallest elements. This takes linear time proportional to the number of chocolates, N.
  * A sorting-based approach would typically be `O(N log N)`.
- **Space Complexity**: `O(1)`
  * The optimal approach only requires a few constant-space variables to store the two smallest prices found so far.
  * A sorting-based approach might use `O(N)` space depending on the sorting algorithm's implementation (e.g., Python's Timsort uses `O(N)` in the worst case for temporary storage), but can be `O(1)` for in-place sorts.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(prices: list[int], money: int) -> int:
    """
    Determines if two cheapest chocolates can be bought and returns the remaining money,
    or the original money if not affordable.

    Args:
        prices: A list of integers representing the prices of chocolates.
        money: An integer representing the initial amount of money.

    Returns:
        An integer representing the money left after buying the two cheapest chocolates,
        or the original money if they cannot be afforded.
    """
    # Initialize min1 and min2 to positive infinity to ensure any price will be smaller.
    # min1 will store the smallest price found.
    # min2 will store the second smallest price found.
    min1 = math.inf
    min2 = math.inf

    # Iterate through the prices to find the two smallest values
    for price in prices:
        if price < min1:
            # If current price is smaller than the current smallest (min1),
            # then min1 becomes the new second smallest (min2),
            # and current price becomes the new smallest (min1).
            min2 = min1
            min1 = price
        elif price < min2:
            # If current price is not smaller than min1, but is smaller than min2,
            # then it becomes the new second smallest (min2).
            min2 = price

    # Calculate the total cost of the two cheapest chocolates
    total_cost = min1 + min2

    # Check if the total cost is within the available money
    if total_cost <= money:
        # If affordable, return the money left
        return money - total_cost
    else:
        # If not affordable, return the original money
        return money
```
</details>
