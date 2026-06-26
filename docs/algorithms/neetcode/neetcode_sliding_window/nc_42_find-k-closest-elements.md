## Problem Description & Examples
### Goal
There are `n` cars at various positions on a single-lane road of length `target`. Each car has a position and a speed. Faster cars that catch up to slower ones form a fleet. Return the number of car fleets that reach the destination.

### Function Contract
**Inputs**

- `target`: int - destination
- `position`: List[int]
- `speed`: List[int]

**Return value**

int - number of car fleets

### Examples
**Example 1**

- Input: `target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]`
- Output: `3`

**Example 2**

- Input: `target = 59, position = [48, 56], speed = [7, 1]`
- Output: `1`

**Example 3**

- Input: `target = 27, position = [18, 25], speed = [2, 5]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
