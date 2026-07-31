# Maximum Good Subtree Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3575 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-good-subtree-score/) |

## Problem Description

### Goal

An undirected tree is rooted at node `0`. Array `par` identifies each non-root node's parent, and `vals[i]` is the positive integer written at node `i`.

Within any rooted subtree, a selected subset of nodes is good when the decimal representations of all selected values use every digit from `0` through `9` at most once in total. Thus, a value containing a repeated digit cannot itself be selected, and two individually valid values cannot be selected together if they share a digit. The subset's score is the sum of its selected node values; the empty subset has score zero.

For every node `u`, find the maximum score of a good subset drawn from the entire subtree rooted at `u`. Return the sum of these `n` maxima modulo $10^9+7$.

### Function Contract

**Inputs**

- `vals`: An integer array of length $n$, where $1\le n\le500$ and $1\le\texttt{vals[i]}\le10^9$.
- `par`: A length-$n$ parent array describing a valid tree rooted at `0`; `par[0] = -1`, and $0\le\texttt{par[i]}<n$ for every non-root node.

Let $D=10$ be the number of decimal digits.

**Return value**

Return the sum of the maximum good-subset score for every rooted subtree, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `vals = [2,3], par = [-1,0]`
- Output: `8`
- Explanation: The root subtree can select both values for score `5`, while node `1` contributes `3`.

**Example 2**

- Input: `vals = [1,5,2], par = [-1,0,0]`
- Output: `15`
- Explanation: The root selects all three distinct digits for score `8`; the two leaf maxima are `5` and `2`.

**Example 3**

- Input: `vals = [34,1,2], par = [-1,0,1]`
- Output: `42`
- Explanation: The three subtree maxima are `37`, `3`, and `2` because the digits `3`, `4`, `1`, and `2` do not conflict.

---
