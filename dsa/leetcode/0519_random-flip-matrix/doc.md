# Random Flip Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 519 |
| Difficulty | Medium |
| Topics | Hash Table, Math, Reservoir Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-flip-matrix/) |

## Problem Description
### Goal
Design an $m \times n$ binary matrix whose cells all start at `0`. Each `flip()` call chooses an index `[i, j]` whose current value is zero, changes it to one, and returns its coordinates. Every zero cell must be equally likely, and at least one free cell is guaranteed whenever `flip()` is called.

`reset()` changes every cell back to zero so future flips again sample the full matrix. Preserve state between calls and never return an already flipped cell before a reset. Minimize calls to the language's built-in random function as well as time and space, rather than materializing and reshuffling every remaining coordinate after each operation.

### Function Contract
**Inputs**

- `rows`, `cols`: the matrix dimensions
- `random_values`, `operations`: the app adapter uses a repeatable uniform-value stream and a chronological list of `"flip"` and `"reset"` calls

**Return value**

- The app adapter returns one coordinate for each flip and `null` for each reset; native LeetCode invokes the object methods directly

### Examples
**Example 1**

- Input: `rows = 2, cols = 2, operations = ["flip", "flip", "reset", "flip"]`
- Output: one valid trace is `[[0,0], [1,1], null, [0,0]]`

**Example 2**

- Input: `rows = 1, cols = 1, operations = ["flip", "reset", "flip"]`
- Output: `[[0,0], null, [0,0]]`

**Example 3**

- Input: `rows = 1, cols = 3, operations = ["flip", "flip"]`
- Output: any two distinct coordinates in that row
