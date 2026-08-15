# Unique 3-Digit Even Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3483 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Recursion, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/) |

## Problem Description

### Goal

The array `digits` supplies individual copies of decimal digits. Count how many distinct three-digit even integers can be assembled by choosing three different array positions.

The hundreds digit cannot be zero. A digit value may appear more than once in a number only when the input provides enough copies of that value, and any one copy can be used at most once within a number. Different selections that produce the same integer contribute only once.

### Function Contract

**Inputs**

- `digits`: A list of decimal digits, each between 0 and 9 inclusive.

The length $n$ satisfies $3\le n\le10$.

**Return value**

Return the number of distinct three-digit even integers constructible from the available digit copies without a leading zero.

### Examples

#### Example 1

- **Input:** `digits = [1, 2, 3, 4]`
- **Output:** `12`

There are twelve valid integers, including `124`, `132`, `214`, and `432`. The number `222` is unavailable because the input contains only one copy of 2.

#### Example 2

- **Input:** `digits = [0, 2, 2]`
- **Output:** `2`

The two valid integers are `202` and `220`; the repeated 2 is legal because two copies are supplied.

#### Example 3

- **Input:** `digits = [6, 6, 6]`
- **Output:** `1`

Only `666` can be formed.

#### Example 4

- **Input:** `digits = [1, 3, 5]`
- **Output:** `0`

No supplied digit can occupy the even units position.
