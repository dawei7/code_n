# Set Mismatch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 645 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/set-mismatch/) |

## Problem Description
### Goal
A set originally contained every integer from `1` through `n` exactly once. After an error, one number was duplicated in place of another, causing one value to occur twice and a different value to disappear. The array `nums` represents the set after this corruption.

Find both affected values and return them as `[duplicate, missing]` in that order. Exactly one number is repeated and exactly one number from the original range is absent; equal array entries identify the repeated value, not two independent missing positions.

### Function Contract
**Inputs**

- `nums`: a length-`n` list whose original values were exactly `1` through `n`, but one value appears twice and one other value is absent

**Return value**

- `[duplicate, missing]` in that order

### Examples
**Example 1**

- Input: `nums = [1,2,2,4]`
- Output: `[2,3]`

**Example 2**

- Input: `nums = [1,1]`
- Output: `[1,2]`

**Example 3**

- Input: `nums = [2,2]`
- Output: `[2,1]`
