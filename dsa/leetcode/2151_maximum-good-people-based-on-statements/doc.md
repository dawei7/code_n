# Maximum Good People Based on Statements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2151 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-good-people-based-on-statements](https://leetcode.com/problems/maximum-good-people-based-on-statements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-good-people-based-on-statements/).

### Goal
Assign each person as good or bad while respecting all statements made by good people. A good person's statements are truthful, while a bad person's statements may be either true or false. Find the maximum possible number of good people.

### Function Contract
**Inputs**

- `statements`: a square matrix where `0` says a person is bad, `1` says good, and `2` means no statement; row `i` contains person `i`'s claims.

**Return value**

The largest number of people who can consistently be classified as good.

### Examples
**Example 1**

- Input: `statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]`
- Output: `2`

**Example 2**

- Input: `statements = [[2, 0], [0, 2]]`
- Output: `1`

**Example 3**

- Input: `statements = [[2]]`
- Output: `1`

---

## Solution
### Approach
Enumerate all `2^n` assignments as bitmasks. For every person marked good, verify each non-unknown statement against the corresponding bit in the assignment. Among masks with no contradiction, maximize the number of set bits. Statements from people marked bad are ignored.

### Complexity Analysis
- **Time Complexity**: `O(2^n * n^2)`
- **Space Complexity**: `O(1)` auxiliary space

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
