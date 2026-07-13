# Maximum Number of Alloys

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2861 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-alloys](https://leetcode.com/problems/maximum-number-of-alloys/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-alloys/).

### Goal
Given a set of metal compositions (alloys) and a supply of base metals, determine the maximum number of identical alloys you can produce. You have a budget to purchase additional base metals at specified costs. Each alloy type requires a specific ratio of base metals, and you are provided with the current inventory and the cost per unit for each base metal.

### Function Contract
**Inputs**

- `n`: An integer representing the number of different base metals.
- `k`: An integer representing the number of different alloy compositions available.
- `budget`: An integer representing the total money available to buy additional base metals.
- `composition`: A 2D list of integers where `composition[i][j]` is the amount of metal `j` required for one unit of alloy `i`.
- `stock`: A list of integers where `stock[j]` is the amount of metal `j` currently in inventory.
- `cost`: A list of integers where `cost[j]` is the price to purchase one unit of metal `j`.

**Return value**

- An integer representing the maximum number of alloys of any single type that can be produced.

### Examples
**Example 1**

- Input: `n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]`
- Output: `5`

**Example 3**

- Input: `n = 2, k = 1, budget = 10, composition = [[2,1]], stock = [1,1], cost = [5,5]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the number of alloys produced is monotonic (if we can produce $X$ alloys, we can produce any number less than $X$), we can binary search for the maximum possible count. For each candidate count, we check if it is feasible within the given budget for at least one alloy composition.

### Complexity Analysis
- **Time Complexity**: $O(k \cdot n \cdot \log(\text{max\_possible\_alloys}))$, where $k$ is the number of compositions, $n$ is the number of metals, and the search space is bounded by $2 \cdot 10^9$.
- **Space Complexity**: $O(1)$, as we only use a few variables for calculations during the binary search.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    def can_produce(alloy_idx: int, count: int) -> bool:
        needed_budget = 0
        for j in range(n):
            required = composition[alloy_idx][j] * count
            if required > stock[j]:
                needed_budget += (required - stock[j]) * cost[j]
            if needed_budget > budget:
                return False
        return needed_budget <= budget

    max_alloys = 0
    # The upper bound is budget + max(stock) because even if cost is 1,
    # we can't exceed total resources. 2*10^9 is a safe upper bound.
    low = 0
    high = 2 * 10**9

    ans = 0
    for i in range(k):
        l, r = 0, high
        best_for_alloy = 0
        while l <= r:
            mid = (l + r) // 2
            if can_produce(i, mid):
                best_for_alloy = mid
                l = mid + 1
            else:
                r = mid - 1
        ans = max(ans, best_for_alloy)

    return ans
```
</details>
