# Maximize the Profit as the Salesman

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2830 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-the-profit-as-the-salesman](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/).

### Goal
Given a set of potential sales offers, each defined by a start house, an end house, and a gold profit, determine the maximum total gold you can earn. You can only accept offers that do not overlap; specifically, if you accept an offer ending at house `i`, the next offer must start at house `i + 1` or later.

### Function Contract
**Inputs**

- `n` (int): The total number of houses, indexed from 0 to n-1.
- `offers` (List[List[int]]): A list of offers where each offer is represented as `[start, end, gold]`.

**Return value**

- `int`: The maximum possible gold profit achievable.

### Examples
**Example 1**

- Input: `n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]`
- Output: `3`

**Example 2**

- Input: `n = 5, offers = [[0,0,1],[1,2,2],[2,4,3],[3,5,2]]`
- Output: `6`

**Example 3**

- Input: `n = 1, offers = [[0,0,1]]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with Sorting and Binary Search. We define `dp[i]` as the maximum profit achievable using houses up to index `i`. For each house, we have two choices: either skip the house (inheriting the profit from `dp[i-1]`) or accept an offer that ends at `i`. To efficiently find the best previous state when accepting an offer `[start, end, gold]`, we sort offers by their end house and use binary search to find the optimal profit from `dp[start - 1]`.

### Complexity Analysis
- **Time Complexity**: `O(M log M + M log N)`, where `M` is the number of offers and `N` is the number of houses. Sorting the offers takes `O(M log M)`, and iterating through the offers while performing binary search takes `O(M log M)`.
- **Space Complexity**: `O(N + M)` to store the DP array and the grouped offers.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List
import bisect

def solve(n: int, offers: List[List[int]]) -> int:
    # Group offers by their end house for efficient lookup
    # end_map[end_house] = list of (start, gold)
    end_map = {}
    for start, end, gold in offers:
        if end not in end_map:
            end_map[end] = []
        end_map[end].append((start, gold))

    # dp[i] will store the max profit using houses up to index i-1
    # dp[0] = 0 (no houses)
    dp = [0] * (n + 1)

    # Iterate through each house index
    for i in range(1, n + 1):
        # Option 1: Don't include any offer ending at house i-1
        dp[i] = dp[i-1]

        # Option 2: Consider all offers that end exactly at house i-1
        if (i - 1) in end_map:
            for start, gold in end_map[i - 1]:
                # If we take this offer, we add its gold to the max profit
                # achievable up to the house before the offer started
                current_profit = dp[start] + gold
                if current_profit > dp[i]:
                    dp[i] = current_profit

    return dp[n]
```
</details>
