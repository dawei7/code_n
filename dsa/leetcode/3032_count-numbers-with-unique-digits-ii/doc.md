# Count Numbers With Unique Digits II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3032 |
| Difficulty | Easy |
| Topics | Hash Table, Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-numbers-with-unique-digits-ii/) |

## Problem Description

### Goal

Two positive integers `a` and `b` define the inclusive interval $[a,b]$.

A number has unique digits when no decimal digit occurs more than once in its usual representation. For example, `102` qualifies because its three digits differ, while `101` does not because digit `1` appears twice.

Count how many integers in the complete inclusive interval have unique digits altogether.

### Function Contract

Let $R=b-a+1$ be the number of integers in the interval, and let $D$ be the maximum number of decimal digits in an examined integer.

**Inputs**

- `a`: The positive lower endpoint of the interval.
- `b`: The inclusive upper endpoint, where $1 \le a \le b \le 1000$.

**Return value**

Return the number of integers from `a` through `b`, inclusive, whose decimal digits are pairwise distinct.

### Examples

#### Example 1

- **Input:** `a = 1, b = 20`
- **Output:** `19`
- **Explanation:** Every number in the interval qualifies except `11`.

#### Example 2

- **Input:** `a = 9, b = 19`
- **Output:** `10`
- **Explanation:** The interval contains eleven numbers, and only `11` repeats a digit.

#### Example 3

- **Input:** `a = 80, b = 120`
- **Output:** `27`
- **Explanation:** Exactly 27 of the 41 integers in this inclusive interval have no repeated decimal digit.
