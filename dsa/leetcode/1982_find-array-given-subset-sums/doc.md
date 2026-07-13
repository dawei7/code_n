# Find Array Given Subset Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1982 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-array-given-subset-sums](https://leetcode.com/problems/find-array-given-subset-sums/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-array-given-subset-sums/).

### Goal
Recover one possible integer array of length `n` from the multiset of all `2^n` subset sums.

### Function Contract
**Inputs**

- `n`: length of the original array.
- `sums`: all subset sums, in any order.

**Return value**

Return any array whose subset sums match `sums`.

### Examples
**Example 1**

- Input: `n = 3, sums = [-3,-2,-1,0,0,1,2,3]`
- Output: `[1,2,-3]`

**Example 2**

- Input: `n = 2, sums = [0,0,0,0]`
- Output: `[0,0]`

**Example 3**

- Input: `n = 1, sums = [0,5]`
- Output: `[5]`

---

## Solution
### Approach
Sort the sums. The difference between the two smallest remaining sums gives the absolute value of one original number. Split the multiset into sums without and with that value; whichever group contains `0` determines the sign. Repeat until all numbers are recovered.

### Complexity Analysis
- **Time Complexity**: `O(n * 2^n)`
- **Space Complexity**: `O(2^n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
