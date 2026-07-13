# Maximum Candies You Can Get from Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1298 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-candies-you-can-get-from-boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/).

### Goal
Starting with some boxes, collect the maximum candies possible. A box can be opened if it is already open or if you have found its key. Opened boxes may contain candies, keys, and more boxes.

### Function Contract
**Inputs**

- `status`: `status[i]` is `1` if box `i` is open initially, else `0`.
- `candies`: candies inside each box.
- `keys`: `keys[i]` lists keys found inside box `i`.
- `containedBoxes`: `containedBoxes[i]` lists boxes found inside box `i`.
- `initialBoxes`: boxes available at the start.

**Return value**

The maximum candies collectable.

### Examples
**Example 1**

- Input: `status = [1,0,1,0]`, `candies = [7,5,4,100]`, `keys = [[],[],[1],[]]`, `containedBoxes = [[1,2],[3],[],[]]`, `initialBoxes = [0]`
- Output: `16`

**Example 2**

- Input: `status = [1,0,0,0,0,0]`, `candies = [1,1,1,1,1,1]`, `keys = [[1,2,3,4,5],[],[],[],[],[]]`, `containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]`, `initialBoxes = [0]`
- Output: `6`

**Example 3**

- Input: `status = [1,1,1]`, `candies = [10,20,30]`, `keys = [[],[],[]]`, `containedBoxes = [[],[],[]]`, `initialBoxes = [1]`
- Output: `20`

---

## Solution
### Approach
Graph traversal with gated nodes.

### Complexity Analysis
- **Time Complexity**: `O(n + total_keys + total_contained_boxes)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(status, candies, keys, contained_boxes, initial_boxes):
    owned = set(initial_boxes)
    opened = set()
    queue = deque(box for box in initial_boxes if status[box] == 1)
    total = 0

    while queue:
        box = queue.popleft()
        if box in opened or status[box] == 0:
            continue
        opened.add(box)
        total += candies[box]
        for key in keys[box]:
            if status[key] == 0:
                status[key] = 1
                if key in owned and key not in opened:
                    queue.append(key)
        for child in contained_boxes[box]:
            owned.add(child)
            if status[child] == 1 and child not in opened:
                queue.append(child)
    return total
```
</details>
