# Maximum Square Area by Removing Fences From a Field

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2975 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-square-area-by-removing-fences-from-a-field](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/).

### Goal
Given a rectangular field defined by dimensions `m` and `n`, and sets of horizontal and vertical fence coordinates, determine the largest possible square area that can be formed by removing a subset of these fences. The boundaries of the field (1, m) and (1, n) are implicitly included as fences.

### Function Contract
**Inputs**

- `m`: An integer representing the total height of the field.
- `n`: An integer representing the total width of the field.
- `hFences`: A list of integers representing the coordinates of horizontal fences.
- `vFences`: A list of integers representing the coordinates of vertical fences.

**Return value**

- An integer representing the maximum area of a square formed by the remaining fences, or -1 if no square can be formed. The result should be returned modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `m = 4, n = 3, hFences = [2, 3], vFences = [2]`
- Output: `4`

**Example 2**

- Input: `m = 6, n = 7, hFences = [2], vFences = [4]`
- Output: `4`

**Example 3**

- Input: `m = 3, n = 9, hFences = [2], vFences = [8, 5, 6, 7]`
- Output: `1`

---

## Solution
### Approach
The problem relies on the observation that any square formed by fences must have a side length equal to the distance between two horizontal fences and simultaneously equal to the distance between two vertical fences. By calculating all possible distances between every pair of horizontal fences (including boundaries 1 and m) and storing them in a hash set, we can then iterate through all possible distances between vertical fences (including boundaries 1 and n). If a vertical distance exists in the horizontal distance set, it represents a valid square side length. We track the maximum such side length and return its square modulo 10^9 + 7.

### Complexity Analysis
- **Time Complexity**: O(H^2 + V^2), where H is the number of horizontal fences and V is the number of vertical fences. We generate all pairs of distances for both sets.
- **Space Complexity**: O(H^2), to store the set of all possible horizontal distances.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
    MOD = 10**9 + 7

    # Include the boundaries of the field
    h_coords = sorted([1] + hFences + [m])
    v_coords = sorted([1] + vFences + [n])

    # Calculate all possible distances between any two horizontal fences
    h_distances = set()
    for i in range(len(h_coords)):
        for j in range(i + 1, len(h_coords)):
            h_distances.add(h_coords[j] - h_coords[i])

    # Calculate all possible distances between any two vertical fences
    # and check if they exist in the horizontal distances set
    max_side = -1
    for i in range(len(v_coords)):
        for j in range(i + 1, len(v_coords)):
            dist = v_coords[j] - v_coords[i]
            if dist in h_distances:
                if dist > max_side:
                    max_side = dist

    if max_side == -1:
        return -1

    return (max_side * max_side) % MOD
```
</details>
