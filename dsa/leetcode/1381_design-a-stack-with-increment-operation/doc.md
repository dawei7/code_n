# Design a Stack With Increment Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-a-stack-with-increment-operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-a-stack-with-increment-operation/).

### Goal
Design a bounded stack that supports pushing, popping, and incrementing the bottom `k` stored values by a given amount.

### Function Contract
**Inputs**

- `max_size`: stack capacity passed to the constructor.
- `operations`: method calls after construction, written as `[method, args]` pairs using `push`, `pop`, and `increment`.

**Return value**

List of method results. `push` and `increment` return `None`; `pop` returns the removed value or `-1`.

### Examples
**Example 1**

- Input: `max_size = 2, operations = [["push", [1]], ["push", [2]], ["pop", []]]`
- Output: `[null, null, 2]`

**Example 2**

- Input: `max_size = 3, operations = [["push", [1]], ["push", [2]], ["increment", [2, 5]], ["pop", []]]`
- Output: `[null, null, null, 7]`

**Example 3**

- Input: `max_size = 1, operations = [["pop", []]]`
- Output: `[-1]`

---

## Solution
### Approach
Array-backed stack. The direct approach updates the bottom `min(k, size)` entries during `increment`; an optimized lazy approach stores pending increments by depth and pushes them downward when popping.

### Complexity Analysis
- **Time Complexity**: `O(1)` for `push` and `pop`; `O(k)` per direct `increment`, or `O(1)` with lazy increments.
- **Space Complexity**: `O(maxSize)`

### Reference Implementations
<details>
<summary>python</summary>

```python
class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack: list[int] = []
        self.increments: list[int] = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        increment = self.increments.pop()
        if index > 0:
            self.increments[index - 1] += increment
        return self.stack.pop() + increment

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            index = min(k, len(self.stack)) - 1
            self.increments[index] += val


def solve(max_size: int, operations: list[tuple[str, tuple[int, ...]]]) -> list[int | None]:
    stack = CustomStack(max_size)
    outputs: list[int | None] = []
    for operation, args in operations:
        if operation == "push":
            outputs.append(stack.push(args[0]))
        elif operation == "pop":
            outputs.append(stack.pop())
        elif operation == "increment":
            outputs.append(stack.increment(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return outputs
```
</details>
