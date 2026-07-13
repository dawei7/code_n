# Average Waiting Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1701 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [average-waiting-time](https://leetcode.com/problems/average-waiting-time/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/average-waiting-time/).

### Goal
A single chef handles customers in arrival order. Each customer has an arrival time and preparation time. Compute the average time from a customer's arrival until their order is finished.

### Function Contract
**Inputs**

- `customers`: a list of `[arrival, preparation]` pairs sorted by arrival time.

**Return value**

Return the average waiting time as a floating-point value.

### Examples
**Example 1**

- Input: `customers = [[1,2],[2,5],[4,3]]`
- Output: `5.00000`

**Example 2**

- Input: `customers = [[5,2],[5,4],[10,3],[20,1]]`
- Output: `3.25000`

**Example 3**

- Input: `customers = [[1,1],[2,2],[3,3]]`
- Output: `3.00000`

---

## Solution
### Approach
Simulate the chef's current finish time. For each customer, service starts at `max(current_time, arrival)`, finishes after the preparation time, and contributes `finish - arrival` to the total wait.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
