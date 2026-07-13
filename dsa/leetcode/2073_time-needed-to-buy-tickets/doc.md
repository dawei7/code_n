# Time Needed to Buy Tickets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2073 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [time-needed-to-buy-tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/time-needed-to-buy-tickets/).

### Goal
People buy one ticket per turn from left to right and rejoin the line if they still need tickets. Find when person `k` finishes.

### Function Contract
**Inputs**

- `tickets`: number of tickets each person wants.
- `k`: index of the person to track.

**Return value**

Return the number of seconds until person `k` has bought all tickets.

### Examples
**Example 1**

- Input: `tickets = [2,3,2], k = 2`
- Output: `6`

**Example 2**

- Input: `tickets = [5,1,1,1], k = 0`
- Output: `8`

**Example 3**

- Input: `tickets = [1], k = 0`
- Output: `1`

---

## Solution
### Approach
Person `i` contributes `min(tickets[i], tickets[k])` turns if `i <= k`, and `min(tickets[i], tickets[k] - 1)` turns if `i > k`, because the process stops immediately when person `k` buys their last ticket.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
