# Delivering Boxes from Storage to Ports

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1687 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Segment Tree, Queue, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [delivering-boxes-from-storage-to-ports](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/).

### Goal
Boxes must be delivered in order. Each box has a destination port and a weight, and one trip can carry at most `maxBoxes` boxes and `maxWeight` total weight. A trip starts at storage, visits ports as needed for its carried boxes, and returns to storage. Minimize total trips between locations.

### Function Contract
**Inputs**

- `boxes`: a list of `[port, weight]` pairs in delivery order.
- `portsCount`: the number of possible ports.
- `maxBoxes`: maximum boxes per trip.
- `maxWeight`: maximum total weight per trip.

**Return value**

Return the minimum number of location-to-location moves needed to deliver all boxes.

### Examples
**Example 1**

- Input: `boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3`
- Output: `4`

**Example 2**

- Input: `boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6`
- Output: `6`

**Example 3**

- Input: `boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7`
- Output: `6`

---

## Solution
### Approach
Use dynamic programming with a sliding feasible window. Prefix sums track weight and the number of port changes, so the cost of delivering a consecutive segment can be computed quickly. A monotonic deque stores the best previous split value for starts that still satisfy both capacity limits, giving the next `dp` value in amortized constant time.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
