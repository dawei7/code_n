# Count Special Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2376 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-special-integers/) |

## Problem Description

### Goal

A positive integer is called special when every decimal digit in its usual representation is distinct. Repetition anywhere in the representation makes the integer non-special; for example, `22`, `114`, and `131` are not special.

Given a positive integer `n`, count how many special integers belong to the inclusive interval from $1$ through `n`. The number `0` is not part of the interval and must not be counted as a one-digit special integer.

### Function Contract

**Inputs**

- `n`: A positive integer with $1 \le \texttt{n} \le 2 \cdot 10^9$.

Let $d$ be the number of decimal digits in `n`.

**Return value**

- Return the number of integers $x$ satisfying $1 \le x \le \texttt{n}$ whose decimal digits are pairwise distinct.

**Digit semantics**

- Leading zeroes are not part of an integer's decimal representation.
- The digit zero may occur once after the first position.
- An integer with one digit is always special.

### Examples

#### Example 1

- **Input:** `n = 20`
- **Output:** `19`
- **Explanation:** Every positive integer through `20` is special except `11`.

#### Example 2

- **Input:** `n = 5`
- **Output:** `5`
- **Explanation:** All five positive integers in the interval have one digit.

#### Example 3

- **Input:** `n = 135`
- **Output:** `110`
- **Explanation:** Exactly 110 integers in the interval have no repeated decimal digit.
