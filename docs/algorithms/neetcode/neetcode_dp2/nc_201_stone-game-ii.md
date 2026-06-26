## Problem Description & Examples
### Goal
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, each pile having a positive integer number of stones `piles[i]`.

Alice and Bob take turns, with Alice starting first. Initially, `M = 1`. On each player's turn, that player can take all the stones in the first `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken. Return the maximum number of stones Alice can get.

### Function Contract
**Inputs**

- `piles`: List[int]

**Return value**

int - maximum stones Alice can get

### Examples
**Example 1**

- Input: `piles = [2, 7, 9, 4, 4]`
- Output: `10`

**Example 2**

- Input: `piles = [14, 2, 9]`
- Output: `16`

**Example 3**

- Input: `piles = [19, 3]`
- Output: `22`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
