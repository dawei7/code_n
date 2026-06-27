# Buy Two Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2706 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting |
| Official Link | [buy-two-chocolates](https://leetcode.com/problems/buy-two-chocolates/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The core of this problem involves identifying the two smallest elements within a given array. This can be achieved through a few common approaches:

1.  **Sorting:** Sort the entire `prices` array in ascending order. The two cheapest chocolates will then be the first two elements of the sorted array.
2.  **Single Pass Iteration:** Iterate through the `prices` array once, keeping track of the two smallest prices encountered so far. This approach avoids a full sort and is generally more efficient for finding a fixed number of smallest elements.

After finding the two cheapest prices, their sum is compared against the available `money` to determine the final return value.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`
  * The optimal approach involves a single pass through the `prices` list to find the two smallest elements. This takes linear time proportional to the number of chocolates, N.
  * A sorting-based approach would typically be `O(N log N)`.
- **Space Complexity**: `O(1)`
  * The optimal approach only requires a few constant-space variables to store the two smallest prices found so far.
  * A sorting-based approach might use `O(N)` space depending on the sorting algorithm's implementation (e.g., Python's Timsort uses `O(N)` in the worst case for temporary storage), but can be `O(1)` for in-place sorts.
