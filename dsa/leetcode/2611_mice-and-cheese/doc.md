# Mice and Cheese

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2611 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [mice-and-cheese](https://leetcode.com/problems/mice-and-cheese/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/mice-and-cheese/).

### Goal
Two mice are tasked with eating $n$ pieces of cheese. Each piece of cheese has a specific point value if eaten by the first mouse and a different point value if eaten by the second mouse. Given that the first mouse must eat exactly $k$ pieces of cheese, determine the maximum total points achievable by both mice combined.

### Function Contract
**Inputs**

- `reward1`: A list of integers representing the points gained if the first mouse eats the $i$-th piece of cheese.
- `reward2`: A list of integers representing the points gained if the second mouse eats the $i$-th piece of cheese.
- `k`: An integer representing the exact number of pieces the first mouse must consume.

**Return value**

- An integer representing the maximum total points possible.

### Examples
**Example 1**

- Input: `reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2`
- Output: `15`

**Example 2**

- Input: `reward1 = [1,1], reward2 = [1,1], k = 2`
- Output: `2`

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy**. We assume initially that the second mouse eats all $n$ pieces of cheese, yielding a base sum of all values in `reward2`. To satisfy the constraint that the first mouse eats exactly $k$ pieces, we calculate the "gain" of switching a piece from the second mouse to the first: `gain = reward1[i] - reward2[i]`. By selecting the $k$ pieces with the largest positive gains, we maximize the total score.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the sorting of the gain differences, where $n$ is the number of cheese pieces.
- **Space Complexity**: $O(n)$ to store the list of gain differences.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(reward1: List[int], reward2: List[int], k: int) -> int:
    """
    Calculates the maximum total points by greedily selecting the k pieces
    that provide the highest relative advantage for the first mouse.
    """
    n = len(reward1)

    # Calculate the net gain of choosing mouse 1 over mouse 2 for each piece
    gains = []
    for i in range(n):
        gains.append(reward1[i] - reward2[i])

    # Sort gains in descending order to pick the best k pieces for mouse 1
    gains.sort(reverse=True)

    # Start with the assumption that mouse 2 eats everything
    total_points = sum(reward2)

    # Add the top k gains to the base sum
    for i in range(k):
        total_points += gains[i]

    return total_points
```
</details>
