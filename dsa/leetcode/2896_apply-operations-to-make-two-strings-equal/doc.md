# Apply Operations to Make Two Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2896 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/) |

## Problem Description

### Goal

You are given two 0-indexed binary strings, `s1` and `s2`, of the same length $n$, together with a positive integer `x`. You may modify only `s1`, applying either operation any number of times:

- Choose any two indices and flip both characters, paying a cost of `x`.
- Choose an index $i<n-1$ and flip the adjacent characters at indices $i$ and $i+1$, paying a cost of $1$.

Flipping changes `0` to `1` or `1` to `0`. Return the minimum total cost needed to make `s1` equal to `s2`. If no sequence of allowed operations can do so, return `-1`.

### Function Contract

**Inputs**

- `s1`: The binary string to modify.
- `s2`: The target binary string, with the same length as `s1`.
- `x`: The cost of flipping an arbitrary pair of indices.

The shared bounds are $1 \le n \le 500$, $1 \le x \le 500$, and $n=\lvert\texttt{s1}\rvert=\lvert\texttt{s2}\rvert$.

**Return value**

Return the minimum achievable total cost, or `-1` when equality is impossible.

### Examples

#### Example 1

- **Input:** `s1 = "1100011000", s2 = "0101001010", x = 2`
- **Output:** `4`
- **Explanation:** Two adjacent-pair operations and one arbitrary-pair operation can resolve all mismatches for total cost $1+1+2=4$.

#### Example 2

- **Input:** `s1 = "10110", s2 = "00011", x = 4`
- **Output:** `-1`
- **Explanation:** The strings differ at an odd number of positions, while every operation flips exactly two positions.
