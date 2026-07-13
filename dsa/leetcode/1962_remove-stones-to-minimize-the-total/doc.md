# Remove Stones to Minimize the Total

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1962 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-stones-to-minimize-the-total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-stones-to-minimize-the-total/).

### Goal
Perform `k` operations on piles of stones. Each operation chooses one pile and removes `floor(pile / 2)` stones. Minimize the total stones left.

### Function Contract
**Inputs**

- `piles`: stone counts in each pile.
- `k`: number of operations.

**Return value**

Return the minimum possible total remaining stones.

### Examples
**Example 1**

- Input: `piles = [5,4,9], k = 2`
- Output: `12`

**Example 2**

- Input: `piles = [4,3,6,7], k = 3`
- Output: `12`

**Example 3**

- Input: `piles = [1], k = 1`
- Output: `1`

---

## Solution
### Approach
Always reduce the current largest pile, because halving a larger pile removes at least as many stones as halving a smaller one. Use a max-heap and push the reduced pile back after each operation.

### Complexity Analysis
- **Time Complexity**: `O((n + k) log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
