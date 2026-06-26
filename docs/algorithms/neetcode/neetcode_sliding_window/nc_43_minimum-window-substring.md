## Problem Description & Examples
### Goal
Given an integer array `asteroids`, represent asteroids in a row. Positive = moving right, negative = moving left. When two asteroids meet (moving toward each other), the smaller explodes; equal-size both explode. Return the state after all collisions.

### Function Contract
**Inputs**

- `asteroids`: List[int]

**Return value**

List[int] - surviving asteroids

### Examples
**Example 1**

- Input: `asteroids = [5, 10, -5]`
- Output: `[5, 10]`

**Example 2**

- Input: `asteroids = [-13, 14]`
- Output: `[-13, 14]`

**Example 3**

- Input: `asteroids = [-5, 3]`
- Output: `[-5, 3]`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
