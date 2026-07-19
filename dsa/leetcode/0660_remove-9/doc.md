# Remove 9

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 660 |
| Difficulty | Hard |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-9/) |

## Problem Description
### Goal
Consider the positive integers in increasing numerical order after removing every integer whose decimal representation contains the digit `9`. The remaining sequence begins with the ordinary one-digit values `1` through `8` and then continues with larger numbers that also avoid `9` in every position.

Given a positive one-based index `n`, return the `n`th integer in this filtered sequence. The index counts valid integers rather than decimal digits, and an otherwise valid number is excluded if `9` appears anywhere in its representation.

### Function Contract
**Inputs**

- `n`: a positive 1-based position in the filtered integer sequence

**Return value**

- The integer at position `n` among positive decimal integers that do not contain `9`

### Examples
**Example 1**

- Input: `n = 9`
- Output: `10`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 18`
- Output: `20`
