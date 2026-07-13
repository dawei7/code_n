# Find Missing Observations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2028 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-missing-observations](https://leetcode.com/problems/find-missing-observations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-missing-observations/).

### Goal
Some dice rolls are known and `n` rolls are missing. Fill the missing rolls so the average across all rolls equals `mean`.

### Function Contract
**Inputs**

- `rolls`: observed dice rolls.
- `mean`: target average over observed and missing rolls.
- `n`: number of missing rolls.

**Return value**

Return any valid list of missing rolls, or an empty list if impossible.

### Examples
**Example 1**

- Input: `rolls = [3,2,4,3], mean = 4, n = 2`
- Output: `[6,6]`

**Example 2**

- Input: `rolls = [1,5,6], mean = 3, n = 4`
- Output: `[2,3,2,2]`

**Example 3**

- Input: `rolls = [1,2,3,4], mean = 6, n = 4`
- Output: `[]`

---

## Solution
### Approach
Compute the required missing sum. It must lie between `n` and `6n`. Start every missing roll at `1`, then distribute the remaining sum with at most `5` extra per roll.

### Complexity Analysis
- **Time Complexity**: `O(n + m)` where `m = len(rolls)`.
- **Space Complexity**: `O(n)` for the returned rolls.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
