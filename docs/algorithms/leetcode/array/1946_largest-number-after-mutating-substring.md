# Largest Number After Mutating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1946 |
| Difficulty | Medium |
| Topics | Array, String, Greedy |
| Official Link | [largest-number-after-mutating-substring](https://leetcode.com/problems/largest-number-after-mutating-substring/) |

## Problem Description & Examples
### Goal
Choose at most one contiguous substring of a decimal string and replace each digit `d` inside it with `change[d]`. Produce the lexicographically largest possible number.

### Function Contract
**Inputs**

- `num`: a string of digits.
- `change`: length-10 digit replacement table.

**Return value**

Return the best number string after zero or one mutation segment.

### Examples
**Example 1**

- Input: `num = "132", change = [9,8,5,0,3,6,4,2,6,8]`
- Output: `"832"`

**Example 2**

- Input: `num = "021", change = [9,4,3,5,7,2,1,9,0,6]`
- Output: `"934"`

**Example 3**

- Input: `num = "5", change = [1,4,7,5,3,2,5,6,9,4]`
- Output: `"5"`

---

## Underlying Base Algorithm(s)
Scan left to right until finding the first digit whose replacement is larger. Start mutating there, continue while replacements are at least as large as the original digits, and stop permanently at the first replacement that would shrink a digit.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the mutable result string.
