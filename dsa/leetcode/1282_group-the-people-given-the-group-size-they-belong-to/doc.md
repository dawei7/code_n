# Group the People Given the Group Size They Belong To

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1282 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [group-the-people-given-the-group-size-they-belong-to](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/).

### Goal
Partition people into groups so that person `i` belongs to a group of size `groupSizes[i]`.

### Function Contract
**Inputs**

- `groupSizes`: required group size for each person index.

**Return value**

Any valid grouping of all indices.

### Examples
**Example 1**

- Input: `groupSizes = [3,3,3,3,3,1,3]`
- Output: `[[5],[0,1,2],[3,4,6]]`

**Example 2**

- Input: `groupSizes = [2,1,3,3,3,2]`
- Output: `[[1],[0,5],[2,3,4]]`

**Example 3**

- Input: `groupSizes = [1,1,1]`
- Output: `[[0],[1],[2]]`

---

## Solution
### Approach
Greedy bucket filling.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(group_sizes):
    buckets = defaultdict(list)
    answer = []
    for i, size in enumerate(group_sizes):
        buckets[size].append(i)
        if len(buckets[size]) == size:
            answer.append(buckets[size])
            buckets[size] = []
    return answer
```
</details>
