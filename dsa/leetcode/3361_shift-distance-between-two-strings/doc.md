# Shift Distance Between Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3361 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shift-distance-between-two-strings/) |

## Problem Description

### Goal

You receive lowercase strings `s` and `t` of the same length. A character of `s` may be shifted one letter forward or one letter backward in the alphabet per operation. Both directions are circular: the next letter after `z` is `a`, and the previous letter before `a` is `z`.

The price of a step depends on the letter being left. Moving forward from alphabet index $j$ costs `nextCost[j]`, while moving backward from that same index costs `previousCost[j]`. Operations at different string positions are independent, and any number of steps may be used. Return the minimum total cost needed to make every character of `s` equal the corresponding character of `t`.

### Function Contract

**Inputs**

- `s`: The source lowercase string.
- `t`: The target lowercase string, with the same length as `s`.
- `nextCost`: The 26 nonnegative costs for leaving each letter in the forward direction.
- `previousCost`: The 26 nonnegative costs for leaving each letter in the backward direction.

The common string length $n$ satisfies $1\le n\le10^5$. Both cost arrays have length 26, and every cost is between $0$ and $10^9$, inclusive.

**Return value**

- The minimum total shift cost as an integer.

### Examples

#### Example 1

- **Input:** `s = "abab"`, `t = "baba"`, `nextCost = [100, 0, ..., 0]`, `previousCost = [1, 100, 0, ..., 0]`
- **Output:** `2`
- **Explanation:** Each `a` moves backward around the alphabet for cost 1, while each `b` moves forward around the alphabet at zero cost.

#### Example 2

- **Input:** `s = "leet"`, `t = "code"`, with every entry of both cost arrays equal to 1
- **Output:** `31`
- **Explanation:** The cheapest per-position shift counts are $9$, $10$, $1$, and $11$.
