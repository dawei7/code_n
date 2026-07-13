# Implement Router

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3508 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Design, Queue, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [implement-router](https://leetcode.com/problems/implement-router/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/implement-router/).

### Goal
Design a routing system that manages a collection of network paths. The system must support registering specific URL patterns (which may include wildcards) and resolving incoming request URLs to the most specific matching registered path. If multiple patterns match, the system should prioritize the longest or most specific match.

### Function Contract
**Inputs**

- `add_route(pattern: str, handler: str)`: Registers a URL pattern to a specific handler.
- `resolve(url: str) -> str`: Returns the handler associated with the best-matching pattern for the given URL, or an empty string if no match exists.

**Return value**

- `resolve` returns the `handler` string associated with the matched pattern.

### Examples
**Example 1**

- Input: `add_route("/api/v1/*", "v1_handler"), resolve("/api/v1/users")`
- Output: `"v1_handler"`

**Example 2**

- Input: `add_route("/static/*", "static_handler"), add_route("/static/images/*", "img_handler"), resolve("/static/images/logo.png")`
- Output: `"img_handler"`

**Example 3**

- Input: `add_route("/home", "home_handler"), resolve("/about")`
- Output: `""`

---

## Solution
### Approach
The optimal approach utilizes a **Trie (Prefix Tree)** data structure. Each node in the Trie represents a segment of the URL path (split by '/'). Wildcards are handled by storing a special node type that matches any segment but carries a lower priority than exact matches during the traversal.

### Complexity Analysis
- **Time Complexity**: `O(L)` for both `add_route` and `resolve`, where `L` is the number of segments in the URL path.
- **Space Complexity**: `O(N * L)` where `N` is the number of registered routes and `L` is the average length of the routes.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue: deque[tuple[int, int, int]] = deque()
        self.packets: set[tuple[int, int, int]] = set()
        self.timestamps: dict[int, list[int]] = defaultdict(list)
        self.left_index: dict[int, int] = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False
        if len(self.queue) == self.limit:
            self._remove_oldest()
        self.queue.append(packet)
        self.packets.add(packet)
        self.timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self._remove_oldest()
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        values = self.timestamps.get(destination, [])
        left = self.left_index.get(destination, 0)
        return bisect_right(values, endTime, lo=left) - bisect_left(values, startTime, lo=left)

    def _remove_oldest(self) -> tuple[int, int, int]:
        packet = self.queue.popleft()
        self.packets.remove(packet)
        self.left_index[packet[1]] += 1
        return packet


def solve(operations: list[str], arguments: list[list[int]]) -> list[object]:
    router: Router | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "Router":
            router = Router(args[0])
            output.append(None)
        elif operation == "addPacket":
            assert router is not None
            output.append(router.addPacket(args[0], args[1], args[2]))
        elif operation == "forwardPacket":
            assert router is not None
            output.append(router.forwardPacket())
        elif operation == "getCount":
            assert router is not None
            output.append(router.getCount(args[0], args[1], args[2]))
    return output
```
</details>
