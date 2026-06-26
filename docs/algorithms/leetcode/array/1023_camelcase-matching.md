# Camelcase Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1023 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, String, Trie |
| Official Link | [camelcase-matching](https://leetcode.com/problems/camelcase-matching/) |

## Problem Description & Examples
### Goal
For each query string, decide whether it can match a pattern after inserting any number of lowercase letters into the pattern. Extra uppercase letters are not allowed.

### Function Contract
**Inputs**

- `queries`: List[str]
- `pattern`: str

**Return value**

List[bool] - match result for each query

### Examples
**Example 1**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FB"`
- Output: `[True, False, True, True, False]`

**Example 2**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBa"`
- Output: `[True, False, True, False, False]`

**Example 3**

- Input: `queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"], pattern = "CooP"`
- Output: `[False, False, True]`

---

## Underlying Base Algorithm(s)
Two-pointer subsequence matching with uppercase constraints.

---

## Complexity Analysis
- **Time Complexity**: `O(total query characters)`
- **Space Complexity**: `O(1)` auxiliary space excluding output
