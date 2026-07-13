# Building H2O

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1117 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [building-h2o](https://leetcode.com/problems/building-h2o/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/building-h2o/).

### Goal
Several threads call either a hydrogen action or an oxygen action. Coordinate them so output is released in complete water groups: exactly two hydrogen actions and one oxygen action may pass for each molecule, with no partial group leaking into the next one.

### Function Contract
**Inputs**

- `releaseHydrogen`: callable that emits one hydrogen marker
- `releaseOxygen`: callable that emits one oxygen marker

**Return value**

None - synchronization controls the order and grouping of side effects

### Examples
**Example 1**

- Input: `arrival = "HOH"`
- Output: `"HHO"` or `"HOH"`

**Example 2**

- Input: `arrival = "OOHHHH"`
- Output: `"HHOHHO"` or any grouping where each 3-character block contains two `H` and one `O`

**Example 3**

- Input: `arrival = "HHOOHH"`
- Output: `"HHOHHO"` or any valid pair of complete water groups

---

## Solution
### Approach
Semaphore permits plus a reusable barrier for fixed-size thread groups.

### Complexity Analysis
- **Time Complexity**: `O(1)` synchronization work per arriving thread
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
