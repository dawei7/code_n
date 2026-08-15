# Strong Password Checker II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2299 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/strong-password-checker-ii/) |

## Problem Description

### Goal

Determine whether `password` satisfies every strong-password rule:

- its length is at least eight;
- it contains at least one lowercase English letter;
- it contains at least one uppercase English letter;
- it contains at least one digit;
- it contains at least one character from `"!@#$%^&*()-+"`; and
- no two adjacent characters are equal.

Return `true` only when all six requirements hold. A repeated character is
allowed at nonadjacent positions.

### Function Contract

**Inputs**

- `password`: A string made only from English letters, digits, and the allowed special-character set.

Its length is between 1 and 100, inclusive.

**Return value**

`true` if `password` meets every stated strength criterion; otherwise
`false`.

### Examples

#### Example 1

- **Input:** `password = "IloveLe3tcode!"`
- **Output:** `true`

#### Example 2

- **Input:** `password = "Me+You--IsMyDream"`
- **Output:** `false`

#### Example 3

- **Input:** `password = "1aB!"`
- **Output:** `false`
