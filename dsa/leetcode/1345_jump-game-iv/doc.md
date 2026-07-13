# Jump Game IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1345 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [jump-game-iv](https://leetcode.com/problems/jump-game-iv/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/jump-game-iv/).

### Goal
Starting at index `0`, reach the last index in the fewest jumps. From index `i`, you may move to `i - 1`, `i + 1`, or any other index with the same value.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The minimum number of jumps needed to reach index `len(arr) - 1`.

### Examples
**Example 1**

- Input: `arr = [100,-23,-23,404,100,23,23,23,3,404]`
- Output: `3`

**Example 2**

- Input: `arr = [7]`
- Output: `0`

**Example 3**

- Input: `arr = [7,6,9,6,9,6,9,7]`
- Output: `1`

---

## Solution
### Approach
Breadth-first search with value buckets.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict, deque


def solve(arr):
    if len(arr) <= 1:
        return 0
    positions = defaultdict(list)
    for i, value in enumerate(arr):
        positions[value].append(i)

    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        i, steps = queue.popleft()
        for nxt in positions[arr[i]] + [i - 1, i + 1]:
            if nxt == len(arr) - 1:
                return steps + 1
            if 0 <= nxt < len(arr) and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))
        positions[arr[i]].clear()
    return -1
```
</details>
