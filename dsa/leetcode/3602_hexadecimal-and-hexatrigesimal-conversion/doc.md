# Hexadecimal and Hexatrigesimal Conversion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3602 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/) |

## Problem Description
### Goal
Given a positive integer `n`, calculate both its square $n^2$ and its cube $n^3$. Express the square in hexadecimal, the base-$16$ numeral system whose digit symbols are `0` through `9` followed by uppercase `A` through `F` for values $10$ through $15$.

Express the cube in hexatrigesimal, the base-$36$ numeral system whose symbols are `0` through `9` followed by uppercase `A` through `Z` for values $10$ through $35$. Concatenate the hexadecimal representation of $n^2$ directly with the base-$36$ representation of $n^3$, without a separator, and return that combined string.

### Function Contract
**Inputs**

- `n`: an integer satisfying $1 \le n \le 1000$

**Return value**

The uppercase base-$16$ representation of $n^2$ followed immediately by the uppercase base-$36$ representation of $n^3$.

### Examples
**Example 1**

- Input: `n = 13`
- Output: `"A91P1"`

The square is $169$, written as `A9` in base $16$. The cube is $2197$, written as `1P1` in base $36$.

**Example 2**

- Input: `n = 36`
- Output: `"5101000"`

The square $1296$ becomes `510` in hexadecimal, and the cube $46656$ becomes `1000` in base $36$.

**Example 3**

- Input: `n = 1`
- Output: `"11"`

Both the square and cube equal $1$, so each representation contains the single digit `1`.
