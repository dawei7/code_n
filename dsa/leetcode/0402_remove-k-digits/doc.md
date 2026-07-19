# Remove K Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 402 |
| Difficulty | Medium |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-k-digits/) |

## Problem Description
### Goal
Given the normalized decimal string `num` and an integer `k`, delete exactly `k` digit occurrences. The digits that remain must preserve their original relative order, so they form a subsequence rather than an arbitrary rearrangement.

Return the numerically smallest value obtainable, written as a normalized decimal string. Remove leading zeroes from the retained sequence, and return exactly `"0"` when all digits are deleted or only zeroes remain. A locally large earlier digit may need removal to expose a smaller prefix, while any unused deletion quota must still be applied from the remaining digits. Do not parse the full number into a fixed-width integer.

### Function Contract
**Inputs**

- `num`: the original decimal representation without a leading zero
- `k`: the exact number of digits to delete

**Return value**

- Return the smallest remaining value as a normalized decimal string: remove leading zeroes and return `"0"` if no nonzero digit remains.

### Examples
**Example 1**

- Input: `num = "1432219", k = 3`
- Output: `"1219"`

**Example 2**

- Input: `num = "10200", k = 1`
- Output: `"200"`

**Example 3**

- Input: `num = "10", k = 2`
- Output: `"0"`
