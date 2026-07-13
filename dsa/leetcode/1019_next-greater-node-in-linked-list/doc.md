# Next Greater Node In Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1019 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [next-greater-node-in-linked-list](https://leetcode.com/problems/next-greater-node-in-linked-list/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/next-greater-node-in-linked-list/).

### Goal
For each node in a singly linked list, find the value of the next node to its right with a strictly larger value. Use `0` when no greater value exists.

### Function Contract
**Inputs**

- `head`: ListNode

**Return value**

List[int] - next greater value for each node position

### Examples
**Example 1**

- Input: `head = [2, 1, 5]`
- Output: `[5, 5, 0]`

**Example 2**

- Input: `head = [2, 7, 4, 3, 5]`
- Output: `[7, 0, 5, 5, 0]`

**Example 3**

- Input: `head = [1, 7, 5, 1, 9, 2, 5, 1]`
- Output: `[7, 9, 9, 9, 0, 5, 0, 0]`

---

## Solution
### Approach
Monotonic decreasing stack over list positions.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1019: Next Greater Node In Linked List."""

from __future__ import annotations

from typing import Any


def solve(head: Any | None) -> list[int]:
    values: list[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next

    answer = [0] * len(values)
    stack: list[int] = []
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(i)
    return answer
```
</details>
