# Letter Combinations of a Phone Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_133` |
| Frontend ID | 17 |
| Difficulty | Medium |
| Topics | Hash Table, String, Backtracking |
| Official Link | [letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |

## Problem Description & Examples
### Goal
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given.

### Function Contract
**Inputs**

- `digits`: str

**Return value**

List[str] - combinations

### Examples
**Example 1**

- Input: `digits = "23"`
- Output: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

**Example 2**

- Input: `digits = '8'`
- Output: `['t', 'u', 'v']`

**Example 3**

- Input: `digits = '38'`
- Output: `['dt', 'du', 'dv', 'et', 'eu', 'ev', 'ft', 'fu', ...]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
