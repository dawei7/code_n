# Snapshot Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1146 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [snapshot-array](https://leetcode.com/problems/snapshot-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/snapshot-array/).

### Goal
Design an array that supports point updates, immutable snapshots, and historical reads by snapshot id.

### Function Contract
**Inputs**

- `length`: array length passed to the constructor.
- `operations`: method calls after construction, written as `[method, args]` pairs using `set`, `snap`, and `get`.

**Return value**

List of method results. `set` returns `None`, `snap` returns a snapshot id, and `get` returns a historical value.

### Examples
**Example 1**

- Input: `length = 3, operations = [["set", [0, 5]], ["snap", []], ["set", [0, 6]], ["get", [0, 0]]]`
- Output: `[null, 0, null, 5]`

**Example 2**

- Input: `length = 1, operations = [["snap", []], ["snap", []], ["get", [0, 1]]]`
- Output: `[0, 1, 0]`

**Example 3**

- Input: `length = 2, operations = [["set", [1, 7]], ["set", [1, 8]], ["snap", []], ["get", [1, 0]]]`
- Output: `[null, null, 0, 8]`

---

## Solution
### Approach
Sparse version history with binary search.

### Complexity Analysis
- **Time Complexity**: `set` is `O(1)`, `snap` is `O(1)`, and `get` is `O(log u)` for `u` updates at that index.
- **Space Complexity**: `O(length + number_of_sets)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.histories[index]
        if history[-1][0] == self.snap_id:
            history[-1][1] = val
        else:
            history.append([self.snap_id, val])

    def snap(self) -> int:
        current = self.snap_id
        self.snap_id += 1
        return current

    def get(self, index: int, snap_id: int) -> int:
        history = self.histories[index]
        pos = bisect_right(history, [snap_id, 10**18]) - 1
        return history[pos][1]


def solve(length, operations):
    snapshot = SnapshotArray(length)
    output = []
    for operation, args in operations:
        if operation == "set":
            output.append(snapshot.set(args[0], args[1]))
        elif operation == "snap":
            output.append(snapshot.snap())
        elif operation == "get":
            output.append(snapshot.get(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
```
</details>
