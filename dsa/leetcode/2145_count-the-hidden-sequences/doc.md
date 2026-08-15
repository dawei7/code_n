# Count the Hidden Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2145 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-the-hidden-sequences](https://leetcode.com/problems/count-the-hidden-sequences/) |

## Problem Description

### Goal

A 0-indexed array `differences` of length $n$ describes a hidden integer
sequence of length $n+1$. For every index `i`, the consecutive values must
satisfy `differences[i] = hidden[i + 1] - hidden[i]`.

Every value in the hidden sequence must lie in the inclusive interval
`[lower, upper]`. The first value is not given, but once it is chosen, all
remaining values are fixed by the required differences.

Return the number of possible hidden sequences. Return `0` if no starting value
keeps the complete sequence within the permitted interval.

### Function Contract

**Inputs**

- `differences`: The required changes between consecutive hidden values. Its
  length is between $1$ and $10^5$, inclusive, and each change lies between
  $-10^5$ and $10^5$.
- `lower`: The inclusive minimum hidden value.
- `upper`: The inclusive maximum hidden value, with
  $-10^5 \leq \texttt{lower} \leq \texttt{upper} \leq 10^5$.

**Return value**

Return the number of integer starting values that generate a sequence wholly
inside `[lower, upper]`.

### Examples

#### Example 1

- **Input:** `differences = [1,-3,4], lower = 1, upper = 6`
- **Output:** `2`
- **Explanation:** The valid sequences are `[3,4,1,5]` and `[4,5,2,6]`.

#### Example 2

- **Input:** `differences = [3,-4,5,1,-2], lower = -4, upper = 5`
- **Output:** `4`

#### Example 3

- **Input:** `differences = [4,-7,2], lower = 3, upper = 6`
- **Output:** `0`
