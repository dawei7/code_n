# Number of Flowers in Full Bloom

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2251 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-flowers-in-full-bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-flowers-in-full-bloom/).

### Goal
For each person's arrival time, count flowers whose inclusive blooming interval contains that time.

### Function Contract
**Inputs**

- `flowers`: inclusive intervals `[start, end]`.
- `people`: arrival times to query.

**Return value**

The number of flowers in bloom for each person, in the original query order.

### Examples
**Example 1**

- Input: `flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]`, `people = [2, 3, 7, 11]`
- Output: `[1, 2, 2, 2]`

**Example 2**

- Input: `flowers = [[1, 10], [3, 3]]`, `people = [3, 4]`
- Output: `[2, 1]`

**Example 3**

- Input: `flowers = [[5, 5]]`, `people = [4, 5, 6]`
- Output: `[0, 1, 0]`

---

## Solution
### Approach
Sort all start times and all end times separately. At time `t`, the active count is the number of starts at or before `t` minus the number of ends strictly before `t`. Obtain both counts with binary search, preserving interval inclusivity.

### Complexity Analysis
- **Time Complexity**: `O((F + P) log F)`
- **Space Complexity**: `O(F)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
