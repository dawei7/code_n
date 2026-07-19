# Split Array into Fibonacci Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 842 |
| Difficulty | Medium |
| Topics | String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) |

## Problem Description
### Goal
Given a digit string `num`, split all of its characters into a list of non-negative integers. The list must contain at least three values, every value must be smaller than $2^{31}$, and each value from the third onward must equal the sum of the previous two.

Each piece must use its ordinary decimal representation: it may be exactly `"0"`, but a multi-digit piece cannot begin with `0`. Return any Fibonacci-like sequence whose concatenated decimal pieces reproduce the entire input, or return `[]` when no such split exists.

### Function Contract
**Inputs**

- `num`: a string of digits with $1 \leq \lvert\texttt{num}\rvert \leq 200$.

**Return value**

Return any list `f` of at least three integers satisfying $0 \leq f_i < 2^{31}$ and

$$
f_i + f_{i+1} = f_{i+2}
$$

for every valid $i$, with the canonical decimal forms of all entries concatenating to `num`. Return `[]` if no valid list exists.

### Examples
**Example 1**

- Input: `num = "1101111"`
- Output: `[11, 0, 11, 11]`

`[110, 1, 111]` is another valid answer.

**Example 2**

- Input: `num = "112358130"`
- Output: `[]`

**Example 3**

- Input: `num = "0123"`
- Output: `[]`

The split `"01", "2", "3"` is forbidden because `"01"` has an extra leading zero.
