# Largest Combination With Bitwise AND Greater Than Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/) |

## Problem Description
### Goal
The bitwise AND of an array is obtained by applying the AND operator across
all its values. A bit remains set in that result only when the same bit is set
in every selected value. For instance, the bitwise AND of `[1, 5, 3]` is
`1 & 5 & 3 = 1`, while the result for the one-element array `[7]` is `7`.

You are given an array `candidates` of positive integers. Consider every
nonempty combination of its elements, where equal values at different indices
remain distinct selectable elements. Among the combinations whose bitwise AND
is greater than zero, find the largest possible number of selected elements.

Return that maximum combination size. More than one combination may attain
the same maximum; only its size is required.

### Function Contract
**Inputs**

- `candidates`: a nonempty list of at most $10^5$ positive integers, each at
  most $10^7$

Let $n=\lvert\texttt{candidates}\rvert$ and
$M=\max(\texttt{candidates})$.

**Return value**

The greatest number of elements that can be chosen while keeping their
combined bitwise AND greater than zero.

### Examples
**Example 1**

- Input: `candidates = [16, 17, 71, 62, 12, 24, 14]`
- Output: `4`

For example, `[16, 17, 62, 24]` has bitwise AND `16`.

**Example 2**

- Input: `candidates = [8, 8]`
- Output: `2`

Both occurrences can be selected, and their bitwise AND remains `8`.

**Example 3**

- Input: `candidates = [1, 2, 4]`
- Output: `1`

No two values share a set bit, but every individual positive value is valid.
