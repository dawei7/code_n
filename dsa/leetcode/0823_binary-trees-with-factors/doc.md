# Binary Trees With Factors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 823 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-trees-with-factors/) |

## Problem Description

### Goal

You are given an array `arr` of unique integers, each strictly greater than `1`. Construct binary trees whose node values are chosen from `arr`. A value may be used for any number of nodes and in any number of different trees; using it once does not remove it from the available choices. A single node is a valid tree.

Every non-leaf node must have two children, and its value must equal the product of its left child's value and its right child's value. Left and right positions are distinct, so exchanging two unequal children produces a different tree. Return the total number of valid binary trees, reduced modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `arr`: an array of $n$ unique integers in arbitrary order, where $1 \le n \le 1000$ and $2 \le \texttt{arr}[i] \le 10^9$

**Return value**

- The number of valid binary trees whose node values come from `arr`, modulo $10^9 + 7$

### Examples

**Example 1**

- Input: `arr = [2, 4]`
- Output: `3`
- Explanation: The single-node trees rooted at `2` and `4` are valid, as is the tree with root `4` and two children valued `2`.

**Example 2**

- Input: `arr = [2, 4, 5, 10]`
- Output: `7`
- Explanation: Besides the four single-node trees and the tree rooted at `4`, root `10` can have ordered children `(2, 5)` or `(5, 2)`.

**Example 3**

- Input: `arr = [2, 4, 8]`
- Output: `8`
- Explanation: There is one tree rooted at `2`, two rooted at `4`, and five rooted at `8`.
