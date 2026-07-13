# Find Good Days to Rob the Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-good-days-to-rob-the-bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-good-days-to-rob-the-bank/).

### Goal
A day is suitable when security has been non-increasing for `time` days through that day and non-decreasing for `time` days starting from that day.

### Function Contract
**Inputs**

- `security`: guards present each day.
- `time`: required days on each side.

**Return value**

Return all suitable day indices.

### Examples
**Example 1**

- Input: `security = [5,3,3,3,5,6,2], time = 2`
- Output: `[2,3]`

**Example 2**

- Input: `security = [1,1,1,1,1], time = 0`
- Output: `[0,1,2,3,4]`

**Example 3**

- Input: `security = [1,2,3,4,5,6], time = 2`
- Output: `[]`

---

## Solution
### Approach
Compute for each index the length of the non-increasing run ending there and the non-decreasing run starting there. An index is good when both lengths cover at least `time` transitions.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
