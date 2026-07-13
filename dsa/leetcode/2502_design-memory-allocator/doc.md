# Design Memory Allocator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2502 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-memory-allocator](https://leetcode.com/problems/design-memory-allocator/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-memory-allocator/).

### Goal
Implement a memory management system that simulates a contiguous block of memory of a fixed size. The system must support allocating a specific number of free contiguous units to a unique process ID and freeing all memory units currently assigned to a specific process ID.

### Function Contract
**Inputs**
- `n` (int): The total number of memory units available (indexed 0 to n-1).
- `allocate(size, mID)`: Requests `size` contiguous units for process `mID`. Returns the starting index of the block if successful, or -1 if no such block exists.
- `freeMemory(mID)`: Releases all memory units currently held by process `mID`. Returns the total number of units freed.

**Return value**
- `allocate`: Returns the starting index (int) or -1.
- `freeMemory`: Returns the count of freed units (int).

### Examples
**Example 1**
- Input: `["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]`
  `[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]`
- Output: `[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]`

**Example 2**
- Input: `["Allocator", "allocate", "freeMemory", "allocate"]`
  `[[5], [2, 1], [1], [3, 2]]`
- Output: `[null, 0, 2, 0]`

**Example 3**
- Input: `["Allocator", "allocate", "freeMemory", "allocate", "freeMemory"]`
  `[[10], [5, 1], [1], [5, 2], [2]]`
- Output: `[null, 0, 5, 0, 5]`

---

## Solution
### Approach
The system uses a linear array to represent memory, where each index stores the `mID` of the process occupying it (or 0 if free). Allocation is performed via a linear scan to find the first available contiguous segment of the requested size. Deallocation is performed by iterating through the entire array and resetting all indices matching the target `mID`.

### Complexity Analysis
- **Time Complexity**:
  - `allocate`: O(n), where n is the total memory size, as we perform a linear scan to find contiguous blocks.
  - `free`: O(n), as we must traverse the entire memory array to identify and clear the target process's blocks.
- **Space Complexity**: O(n) to store the state of the memory array.

### Reference Implementations
<details>
<summary>python</summary>

```python
class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n
        self.size = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.size):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    start_index = i - size + 1
                    for j in range(start_index, i + 1):
                        self.memory[j] = mID
                    return start_index
            else:
                count = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed_count = 0
        for i in range(self.size):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed_count += 1
        return freed_count

def solve(commands, inputs):
    results = []
    allocator = None
    for cmd, args in zip(commands, inputs):
        if cmd == "Allocator":
            allocator = Allocator(args[0])
            results.append(None)
        elif cmd == "allocate":
            results.append(allocator.allocate(args[0], args[1]))
        elif cmd in {"freeMemory", "free"}:
            results.append(allocator.freeMemory(args[0]))
    return results
```
</details>
