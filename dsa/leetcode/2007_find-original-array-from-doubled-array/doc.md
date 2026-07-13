# Find Original Array From Doubled Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2007 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-original-array-from-doubled-array](https://leetcode.com/problems/find-original-array-from-doubled-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-original-array-from-doubled-array/).

### Goal
An array was doubled by appending twice every original value and shuffling. Recover one possible original array or report that none exists.

### Function Contract
**Inputs**

- `changed`: the shuffled doubled array.

**Return value**

Return the original array if possible, otherwise an empty array.

### Examples
**Example 1**

- Input: `changed = [1,3,4,2,6,8]`
- Output: `[1,3,4]`

**Example 2**

- Input: `changed = [6,3,0,1]`
- Output: `[]`

**Example 3**

- Input: `changed = [0,0,0,0]`
- Output: `[0,0]`

---

## Solution
### Approach
If the length is odd, recovery is impossible. Count values and process them in ascending absolute value so each number is paired with its double before the double is consumed for another role. Zeros must have an even count.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
