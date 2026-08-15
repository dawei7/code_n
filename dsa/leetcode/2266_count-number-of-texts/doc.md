# Count Number of Texts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2266 |
| Difficulty | Medium |
| Topics | Hash Table, Math, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-texts/) |

## Problem Description

### Goal

Alice types letters with a traditional telephone keypad. Each digit from `2`
through `9` represents its printed letters in order: pressing a key once
selects its first letter, twice selects its second, and so on. Keys `2` through
`6` and key `8` each have three letters, while `7` and `9` each have four.
Digits `0` and `1` do not represent letters and are never used.

During transmission, Bob receives only the consecutive key presses rather than
the letter boundaries. For example, the message `"bob"` produces
`"2266622"`. Equal adjacent key presses can therefore be divided into letter
groups in several valid ways, provided no group exceeds the number of letters
on that key.

Given the received string `pressedKeys`, count all text messages that could
have produced exactly those presses. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `pressedKeys`: A string of $n$ digits, each between `2` and `9`.

The length satisfies $1\le n\le10^5$.

**Return value**

Return the number of valid ways to partition the presses into letters, modulo
$10^9+7$. A letter group must contain equal digits and may have length at most
three, except groups of `7` or `9`, which may have length at most four.

### Examples

#### Example 1

- **Input:** `pressedKeys = "22233"`
- **Output:** `8`

The run `"222"` has four valid divisions and `"33"` has two, giving
$4\cdot2=8$ possible messages.

#### Example 2

- **Input:** `pressedKeys = "222222222222222222222222222222222222"`
- **Output:** `82876089`

The unmodded count is `2082876103`; reducing it modulo $10^9+7$ gives the
reported result.
