# Sort the People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2418 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-the-people](https://leetcode.com/problems/sort-the-people/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-the-people/).

### Goal
Given two parallel arrays representing names and heights of individuals, return a list of names sorted in descending order based on their corresponding heights.

### Function Contract
**Inputs**

- `names`: A list of strings where `names[i]` is the name of the i-th person.
- `heights`: A list of integers where `heights[i]` is the height of the i-th person.

**Return value**

- A list of strings containing the names sorted by height from tallest to shortest.

### Examples
**Example 1**

- Input: `names = ["Mary","John","Emma"], heights = [180,165,170]`
- Output: `["Mary","Emma","John"]`

**Example 2**

- Input: `names = ["Alice","Bob","Bob"], heights = [155,185,150]`
- Output: `["Bob","Alice","Bob"]`

**Example 3**

- Input: `names = ["Alex"], heights = [100]`
- Output: `["Alex"]`

---

## Solution
### Approach
The problem is solved by creating pairs of (height, name) and applying a sorting algorithm. Since we need to sort by height in descending order, we can use Python's built-in Timsort (via `sort` or `sorted`), which provides an efficient $O(N \log N)$ performance.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of people, due to the sorting operation.
- **Space Complexity**: $O(N)$ to store the zipped list of pairs and the resulting list of names.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(names: List[str], heights: List[int]) -> List[str]:
    """
    Sorts names based on heights in descending order.

    Args:
        names: List of strings representing names.
        heights: List of integers representing heights.

    Returns:
        A list of names sorted by height descending.
    """
    # Combine names and heights into pairs
    people = list(zip(heights, names))

    # Sort the list of tuples based on height (the first element) in descending order
    people.sort(key=lambda x: x[0], reverse=True)

    # Extract the names from the sorted list
    return [person[1] for person in people]
```
</details>
