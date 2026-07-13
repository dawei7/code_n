# Rearranging Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2561 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [rearranging-fruits](https://leetcode.com/problems/rearranging-fruits/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/rearranging-fruits/).

### Goal
Given two baskets of fruits represented by integer arrays, determine the minimum cost to make both baskets identical. A swap operation between two fruits (one from each basket) costs the minimum value of the two fruits being swapped. If it is impossible to make the baskets identical, return -1.

### Function Contract
**Inputs**

- `basket1`: A list of integers representing the fruits in the first basket.
- `basket2`: A list of integers representing the fruits in the second basket.

**Return value**

- An integer representing the minimum cost to equalize the baskets, or -1 if equalization is impossible.

### Examples
**Example 1**

- Input: `basket1 = [4,2,2,2], basket2 = [1,4,1,2]`
- Output: `1`

**Example 2**

- Input: `basket1 = [2,3,4,1], basket2 = [3,2,5,1]`
- Output: `-1`

**Example 3**

- Input: `basket1 = [8,4,5,3], basket2 = [3,2,5,1]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a **Greedy approach** combined with **Frequency Counting**. First, we calculate the total frequency of each fruit across both baskets. If the total count of any fruit is odd, it is impossible to distribute them equally, so we return -1. We then identify the "excess" fruits in each basket (those that appear more than half the total count). We collect these excess fruits, sort them, and pair them up to minimize the swap cost. The cost of swapping two fruits is the minimum of the two, so we also consider swapping with the global minimum fruit available in either basket to potentially reduce costs.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of fruits in each basket, primarily due to sorting the excess fruits.
- **Space Complexity**: `O(N)` to store the frequency maps and the lists of excess fruits.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(basket1: list[int], basket2: list[int]) -> int:
    n = len(basket1)
    count1 = Counter(basket1)
    count2 = Counter(basket2)

    # Total count of each fruit across both baskets
    total_counts = Counter(basket1) + Counter(basket2)

    # If any fruit has an odd total count, we cannot split them equally
    for fruit in total_counts:
        if total_counts[fruit] % 2 != 0:
            return -1

    # Identify the global minimum fruit value to use as a "cheaper" swap option
    min_val = min(min(basket1), min(basket2))

    # Find excess fruits in each basket
    excess1 = []
    excess2 = []

    for fruit in total_counts:
        target = total_counts[fruit] // 2
        if count1[fruit] > target:
            excess1.extend([fruit] * (count1[fruit] - target))
        elif count2[fruit] > target:
            excess2.extend([fruit] * (count2[fruit] - target))

    # Sort excess fruits to pair the smallest ones together
    excess1.sort()
    excess2.sort(reverse=True)

    # The number of excess fruits must be equal in both baskets
    # We pair them up. For each pair, we can either swap them directly
    # or use the global minimum to swap them if it's cheaper.
    total_cost = 0
    for i in range(len(excess1)):
        total_cost += min(min(excess1[i], excess2[i]), 2 * min_val)

    return total_cost
```
</details>
