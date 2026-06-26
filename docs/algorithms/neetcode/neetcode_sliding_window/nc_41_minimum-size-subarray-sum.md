## Problem Description & Examples
### Goal
Given an array of integers `temperatures` representing daily temperatures, return an array `answer` where `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature. If no future day is warmer, `answer[i] = 0`.

### Function Contract
**Inputs**

- `temperatures`: List[int]

**Return value**

List[int] - days to wait for a warmer day

### Examples
**Example 1**

- Input: `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
- Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

**Example 2**

- Input: `temperatures = [79, 83]`
- Output: `[1, 0]`

**Example 3**

- Input: `temperatures = [47, 38]`
- Output: `[0, 0]`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
