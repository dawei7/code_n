# Find the Highest Altitude

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1732 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-highest-altitude](https://leetcode.com/problems/find-the-highest-altitude/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-highest-altitude/).

### Goal
Starting at altitude `0`, apply each net gain in order and find the highest altitude reached.

### Function Contract
**Inputs**

- `gain`: a list of altitude changes between consecutive points.

**Return value**

Return the maximum running altitude.

### Examples
**Example 1**

- Input: `gain = [-5,1,5,0,-7]`
- Output: `1`

**Example 2**

- Input: `gain = [-4,-3,-2,-1,4,3,2]`
- Output: `0`

**Example 3**

- Input: `gain = [3,-1,2,-2]`
- Output: `4`

---

## Solution
### Approach
Maintain a running altitude initialized to `0` and a best altitude initialized to `0`. Add each gain to the running altitude and update the best value.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
