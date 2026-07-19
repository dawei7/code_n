# License Key Formatting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 482 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/license-key-formatting/) |

## Problem Description
### Goal
Given a license-key string `s` containing English letters, digits, and dashes, ignore the existing group boundaries by removing every dash. Convert all lowercase letters among the remaining alphanumeric characters to uppercase without changing any digit or character order.

Reformat the cleaned characters into groups separated by one dash. Every group except the first must contain exactly `k` characters; the first may be shorter than `k` but must contain at least one character. Return the reformatted key with no leading or trailing dash and no empty group.

### Function Contract
**Inputs**

- `s`: letters, digits, and dashes
- `k`: the required size of every group after the first

**Return value**

- The reformatted uppercase key with single dashes between groups

### Examples
**Example 1**

- Input: `s = "5F3Z-2e-9-w", k = 4`
- Output: `"5F3Z-2E9W"`

**Example 2**

- Input: `s = "2-5g-3-J", k = 2`
- Output: `"2-5G-3J"`

**Example 3**

- Input: `s = "---", k = 3`
- Output: `""`
