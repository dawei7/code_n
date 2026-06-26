# Next Special Palindrome Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3646 |
| Difficulty | Hard |
| Topics | Backtracking, Bit Manipulation |
| Official Link | [next-special-palindrome-number](https://leetcode.com/problems/next-special-palindrome-number/) |

## Problem Description & Examples
### Goal
Return the smallest integer strictly greater than `n` that is a palindrome and whose used digits obey this rule: every digit `k` that appears in the number appears exactly `k` times.

### Function Contract
**Inputs**

- `n`: int lower bound

**Return value**

int - the next special palindrome greater than `n`

### Examples
**Example 1**

- Input: `n = 2`
- Output: `22`

**Example 2**

- Input: `n = 33`
- Output: `212`

**Example 3**

- Input: `n = 3000`
- Output: `4444`

---

## Underlying Base Algorithm(s)
Subset enumeration of digit counts plus backtracking over palindrome halves.

---

## Complexity Analysis
- **Time Complexity**: bounded by a small constant for normal integer constraints, since only digit subsets `1..9` are considered
- **Space Complexity**: `O(1)` relative to `n`
