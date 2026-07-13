# Clumsy Factorial

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1006 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [clumsy-factorial](https://leetcode.com/problems/clumsy-factorial/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/clumsy-factorial/).

### Goal
Compute a modified factorial expression for `n` where the operators cycle through multiplication, division, addition, and subtraction. Division truncates toward zero, and normal arithmetic precedence still applies.

### Function Contract
**Inputs**

- `n`: Positive integer.

**Return value**

Integer value of the clumsy factorial expression for `n`.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `7`

**Example 2**

- Input: `n = 10`
- Output: `12`

**Example 3**

- Input: `n = 1`
- Output: `1`

---

## Solution
### Approach
The operator pattern quickly becomes periodic after the first few values. Handle the small cases directly:

- `n = 1` gives `1`
- `n = 2` gives `2`
- `n = 3` gives `6`
- `n = 4` gives `7`

For larger `n`, the leading term dominates and every following group of four numbers contributes a predictable correction. The result depends only on `n % 4`:

- `0`: return `n + 1`
- `1`: return `n + 2`
- `2`: return `n + 2`
- `3`: return `n - 1`

A stack simulation is useful for deriving the pattern, but the periodic formula gives the optimal constant-time solution.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
