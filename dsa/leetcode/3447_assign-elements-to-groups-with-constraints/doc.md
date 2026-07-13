# Assign Elements to Groups with Constraints

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3447 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [assign-elements-to-groups-with-constraints](https://leetcode.com/problems/assign-elements-to-groups-with-constraints/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/assign-elements-to-groups-with-constraints/).

### Goal
Given a list of groups where each group contains integers, and a list of elements, assign each group an index from the elements list. A group can be assigned an element if at least one number in the group is divisible by that element. If multiple elements satisfy this, choose the one with the smallest index in the elements list. If no element satisfies the condition for a group, assign -1.

### Function Contract
**Inputs**

- `groups`: A list of lists of integers, where each sublist represents a group.
- `elements`: A list of integers representing the available elements to assign.

**Return value**

- A list of integers where the $i$-th integer is the smallest index $j$ such that `elements[j]` divides at least one number in `groups[i]`. If no such element exists, the value is -1.

### Examples
**Example 1**

- Input: `groups = [[10, 21], [5, 7]], elements = [2, 3, 4, 5]`
- Output: `[0, 0]`
- Explanation: For group 0, 10 is divisible by 2 (index 0). For group 1, 5 is divisible by 5 (index 3) and 7 is not. Wait, 5 is divisible by 5 (index 3), but 2 (index 0) doesn't divide 5 or 7. Actually, 10 is divisible by 2 (index 0).

**Example 2**

- Input: `groups = [[10, 21], [30]], elements = [8, 6, 4, 2]`
- Output: `[3, 1]`

**Example 3**

- Input: `groups = [[2, 3, 5], [7]], elements = [10]`
- Output: `[-1, -1]`

---

## Solution
### Approach
The problem is solved using a pre-computation strategy similar to the Sieve of Eratosthenes. We map each element to its first occurrence index. Then, for every possible value up to the maximum value found in the groups, we determine the smallest index of an element that divides it. This is done by iterating through multiples of each element and updating the minimum index for those multiples.

### Complexity Analysis
- **Time Complexity**: $O(M \log M + N \cdot K)$, where $M$ is the maximum value in `groups`, $N$ is the number of groups, and $K$ is the average size of a group. The sieve-like pre-computation takes $O(M \log M)$.
- **Space Complexity**: $O(M + E)$, where $M$ is the maximum value in `groups` and $E$ is the number of unique elements, used to store the mapping of divisors to their minimum indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(groups: list[int], elements: list[int]) -> list[int]:
    max_group = max(groups)
    first_index = {}
    for index, value in enumerate(elements):
        if value <= max_group and value not in first_index:
            first_index[value] = index

    best_for_value = [10**9] * (max_group + 1)
    for value, index in first_index.items():
        for multiple in range(value, max_group + 1, value):
            if index < best_for_value[multiple]:
                best_for_value[multiple] = index

    return [-1 if best_for_value[group] == 10**9 else best_for_value[group] for group in groups]
```
</details>
