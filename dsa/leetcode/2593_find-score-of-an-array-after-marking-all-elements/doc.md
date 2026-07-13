# Find Score of an Array After Marking All Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2593 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-score-of-an-array-after-marking-all-elements](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/).

### Goal
The objective is to calculate a total score by iteratively selecting the smallest available number in an array. When a number is selected, it is added to the score, and that number along with its immediate left and right neighbors are "marked" (rendered unavailable for future selection). This process continues until all elements in the array are marked.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- `score`: A 64-bit integer representing the total sum of the selected elements.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 4, 5, 2]`
- Output: `7`
- Explanation: Select 1 (index 1), mark indices 0, 1, 2. Remaining: [4, 5, 2]. Select 2 (index 5), mark indices 4, 5. Remaining: [4]. Select 4 (index 3), mark index 3. Total: 1 + 2 + 4 = 7.

**Example 2**

- Input: `nums = [2, 3, 5, 1, 3, 2]`
- Output: `5`
- Explanation: Select 1 (index 3), mark indices 2, 3, 4. Remaining: [2, 3, 2]. Select 2 (index 0), mark indices 0, 1. Remaining: [2]. Select 2 (index 5), mark index 5. Total: 1 + 2 + 2 = 5.

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy** combined with **Sorting** or a **Min-Heap**. By sorting the elements based on their values (and indices for tie-breaking), we ensure that we always process the smallest available element first. A boolean array is used to track the "marked" status of each index to ensure $O(1)$ lookup time during the simulation.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of the array. This is dominated by the sorting step. The subsequent linear scan through the sorted elements takes $O(N)$.
- **Space Complexity**: $O(N)$ to store the indexed elements and the boolean array tracking marked indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    # Create a list of (value, index) tuples to keep track of original positions
    indexed_nums = []
    for i in range(n):
        indexed_nums.append((nums[i], i))

    # Sort primarily by value, secondarily by index
    indexed_nums.sort()

    marked = [False] * n
    total_score = 0

    for val, idx in indexed_nums:
        # If the current element is already marked, skip it
        if marked[idx]:
            continue

        # Add to score and mark the current index and its neighbors
        total_score += val
        marked[idx] = True
        if idx > 0:
            marked[idx - 1] = True
        if idx < n - 1:
            marked[idx + 1] = True

    return total_score
```
</details>
