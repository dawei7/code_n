# Find the Maximum Number of Elements in Subset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3020 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Select a nonempty subset of its occurrences and rearrange the selected values into a symmetric square chain.

For some positive integer $x$, the arrangement must begin with repeated squaring,

$$
x, x^2, x^4, ldots,
$$

reach one central value, and then mirror the preceding values in reverse order. Examples include `[3]`, `[3, 9, 3]`, and `[2, 4, 16, 4, 2]`. By contrast, `[2, 4, 8, 4, 2]` is invalid because $8\ne4^2$.

Every noncentral value therefore needs two copies in the selected subset, while the center needs one. Return the maximum number of selected elements that can form such a pattern.

### Function Contract

**Inputs**

- `nums`: A list of positive integers; duplicate occurrences may occupy symmetric positions.

The source constraints guarantee $2 \le N \le 10^5$, $1 \le \texttt{nums}[i] \le 10^9$, where $N=\lvert\texttt{nums}\rvert$.

**Return value**

- The maximum odd length of a subset that can be rearranged into a symmetric square chain.

### Examples

**Example 1**

- Input: `nums = [5, 4, 1, 2, 2]`
- Output: `3`
- Explanation: Select two copies of `2` and one `4`, then arrange them as `[2, 4, 2]`.

**Example 2**

- Input: `nums = [1, 3, 2, 4]`
- Output: `1`
- Explanation: No value has the duplicate needed for a noncentral layer, so any single value is optimal.

**Example 3**

- Input: `nums = [2, 2, 4, 4, 16]`
- Output: `5`
- Explanation: All five values form `[2, 4, 16, 4, 2]`.
