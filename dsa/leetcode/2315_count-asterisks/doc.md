# Count Asterisks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2315 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/count-asterisks/) |

## Problem Description

### Goal

The vertical bars in `s` occur an even number of times. Reading from left to
right, the first and second bars form one pair, the third and fourth form the
next pair, and so on. Each pair encloses one region of the string, and every
bar belongs to exactly one such pair.

Count the `'*'` characters that lie outside all paired regions. Asterisks after
an opening bar and before its matching closing bar must be ignored, while
asterisks before the first pair, between two pairs, or after the last pair
contribute to the result.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters, vertical bars `'|'`, and
  asterisks `'*'`.

The length of `s` is from 1 through 1000, and the number of vertical bars is
even.

**Return value**

The number of asterisks outside the regions delimited by consecutive bar
pairs.

### Examples

#### Example 1

- **Input:** `s = "l|*e*et|c**o|*de|"`
- **Output:** `2`
- **Explanation:** Only the two asterisks in `c**o` are outside paired bars.

#### Example 2

- **Input:** `s = "iamprogrammer"`
- **Output:** `0`

#### Example 3

- **Input:** `s = "yo|uar|e**|b|e***au|tifu|l"`
- **Output:** `5`
