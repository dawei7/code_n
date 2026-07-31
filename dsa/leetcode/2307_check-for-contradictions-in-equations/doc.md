# Check for Contradictions in Equations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2307 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-for-contradictions-in-equations/) |

## Problem Description

### Goal

You are given equations between positive variables. For every index $i$, the pair `equations[i] = [A_i, B_i]` and the corresponding number `values[i]` assert that $A_i / B_i = \texttt{values[i]}$.

Determine whether the collection contains a contradiction. A contradiction exists when the stated ratios imply two incompatible values for the same relationship. Two computed values are considered equal when their absolute difference is less than $10^{-5}$; ordinary double-precision arithmetic is sufficient.

### Function Contract

**Inputs**

- `equations`: A list of variable-name pairs. Each name contains one to five lowercase English letters.
- `values`: A positive floating-point value for each equation, in matching order.

There are between $1$ and $100$ equations. Each value is at most $10$ and has no more than two digits after the decimal point.

**Return value**

Return `true` if at least one equation conflicts with the relationships implied by the others; otherwise, return `false`.

### Examples

**Example 1**

- Input: `equations = [["a","b"],["b","c"],["a","c"]], values = [3.0,0.5,1.5]`
- Output: `false`

The first two equations imply $a/c = 3 \cdot 0.5 = 1.5$, which agrees with the third equation.

**Example 2**

- Input: `equations = [["le","et"],["le","code"],["code","et"]], values = [2.0,5.0,0.5]`
- Output: `true`

The first two equations imply $\texttt{code}/\texttt{et} = 2/5 = 0.4$, which contradicts the stated value $0.5$.
