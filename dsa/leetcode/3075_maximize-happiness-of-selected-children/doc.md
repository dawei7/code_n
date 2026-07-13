# Maximize Happiness of Selected Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3075 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-happiness-of-selected-children](https://leetcode.com/problems/maximize-happiness-of-selected-children/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-happiness-of-selected-children/).

### Goal
Given an array representing the initial happiness levels of children and an integer representing the number of turns available, select children one by one to maximize the total happiness. Each time a child is selected, their happiness decreases by the number of children already chosen (starting from 0). If a child's happiness would drop below zero, it is treated as zero.

### Function Contract
**Inputs**

- `happiness`: A list of integers representing the initial happiness values of each child.
- `k`: An integer representing the total number of children to select.

**Return value**

- An integer representing the maximum possible sum of happiness values after selecting exactly `k` children.

### Examples
**Example 1**

- Input: `happiness = [1, 2, 3], k = 2`
- Output: `4`

**Example 2**

- Input: `happiness = [1, 1, 1, 1], k = 2`
- Output: `1`

**Example 3**

- Input: `happiness = [2, 3, 4, 5], k = 1`
- Output: `5`

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy**. By sorting the happiness values in descending order, we ensure that we always pick the children with the highest current potential happiness first. Since the penalty (the number of children already picked) increases linearly with each selection, picking the largest available values early minimizes the impact of the penalty.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` where `N` is the number of children, primarily due to the sorting step. The subsequent iteration takes `O(k)` time.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(N)`).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(happiness: List[int], k: int) -> int:
    """
    Calculates the maximum happiness by selecting k children greedily.
    """
    # Sort happiness in descending order to pick the largest values first
    sorted_happiness = sorted(happiness, reverse=True)

    total_happiness = 0
    for i in range(k):
        # The actual happiness is the initial value minus the number of children already picked
        # We use max(0, ...) because happiness cannot be negative
        current_val = sorted_happiness[i] - i
        if current_val > 0:
            total_happiness += current_val
        else:
            # Since the array is sorted, if current_val <= 0,
            # all subsequent values will also result in <= 0
            break

    return total_happiness
```
</details>
