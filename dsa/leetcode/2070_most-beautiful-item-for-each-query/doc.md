# Most Beautiful Item for Each Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2070 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-beautiful-item-for-each-query](https://leetcode.com/problems/most-beautiful-item-for-each-query/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-beautiful-item-for-each-query/).

### Goal
For each query price, find the maximum beauty among items whose price is no more than that query.

### Function Contract
**Inputs**

- `items`: pairs `[price, beauty]`.
- `queries`: maximum affordable prices.

**Return value**

Return one best beauty value per query.

### Examples
**Example 1**

- Input: `items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]`
- Output: `[2,4,5,5,6,6]`

**Example 2**

- Input: `items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]`
- Output: `[4]`

**Example 3**

- Input: `items = [[10,1000]], queries = [5,10]`
- Output: `[0,1000]`

---

## Solution
### Approach
Sort items by price and build a prefix maximum of beauty. For each query, binary-search the last affordable item and read the corresponding prefix maximum.

### Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
