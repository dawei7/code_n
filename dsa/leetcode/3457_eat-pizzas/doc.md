# Eat Pizzas!

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3457 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [eat-pizzas](https://leetcode.com/problems/eat-pizzas/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/eat-pizzas/).

### Goal
You are given a collection of pizzas, each with a specific weight. You must consume all pizzas by forming groups of 4. In each group, you eat one pizza of your choice, and the remaining three are consumed by your friends. To maximize the total weight of the pizzas you eat, you must strategically pair the heaviest pizzas with the lightest ones to satisfy the group constraints while ensuring you get the highest possible sum.

### Function Contract
**Inputs**

- `pizzas`: A list of integers representing the weights of the available pizzas. The length of the list is guaranteed to be a multiple of 4.

**Return value**

- An integer representing the maximum total weight you can obtain by eating one pizza from each group of 4.

### Examples
**Example 1**

- Input: `pizzas = [1, 2, 3, 4, 5, 6, 7, 8]`
- Output: `10`
- Explanation: You can form two groups: (8, 1, 2, 3) and (7, 4, 5, 6). You eat 8 and 7. Total = 15? No, wait: (8, 1, 2, 3) and (6, 4, 5, 7) -> 8+6=14. Actually, the optimal is 8 and 2.

**Example 2**

- Input: `pizzas = [2, 1, 1, 1, 1, 1, 1, 1]`
- Output: `3`

**Example 3**

- Input: `pizzas = [5, 5, 5, 5]`
- Output: `5`

---

## Solution
### Approach
The problem is solved using a **Greedy approach** combined with **Sorting**. Since we need to form $N/4$ groups, we should prioritize eating the largest available pizzas. However, each group requires 3 "filler" pizzas. To maximize the count of large pizzas we can claim, we use the smallest available pizzas to satisfy the filler requirements for the largest pizzas, and use the second-largest available pizzas to satisfy the filler requirements for the remaining groups.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ due to the sorting of the input array, where $N$ is the number of pizzas.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(pizzas: list[int]) -> int:
    pizzas.sort()
    days = len(pizzas) // 4
    odd_days = (days + 1) // 2
    even_days = days // 2

    total = 0
    index = len(pizzas) - 1
    for _ in range(odd_days):
        total += pizzas[index]
        index -= 1

    for _ in range(even_days):
        index -= 1
        total += pizzas[index]
        index -= 1

    return total
```
</details>
