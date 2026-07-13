# Jump Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1306 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [jump-game-iii](https://leetcode.com/problems/jump-game-iii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/jump-game-iii/).

### Goal
Starting at index `start`, repeatedly jump left or right by the value at the current index. Decide whether some sequence of jumps can reach an index whose value is `0`.

### Function Contract
**Inputs**

- `arr`: non-negative integer array.
- `start`: starting index.

**Return value**

`true` if a zero-valued index is reachable, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 5`
- Output: `true`

**Example 2**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 0`
- Output: `true`

**Example 3**

- Input: `arr = [3,0,2,1,2]`, `start = 2`
- Output: `false`

---

## Solution
### Approach
Graph search on array indices.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(arr, start):
    queue = deque([start])
    seen = {start}
    while queue:
        i = queue.popleft()
        if arr[i] == 0:
            return True
        for nxt in (i + arr[i], i - arr[i]):
            if 0 <= nxt < len(arr) and nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False
```
</details>
