# Largest Component Size by Common Factor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 952 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [largest-component-size-by-common-factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) |

## Problem Description

### Goal

Given an array `nums` of unique positive integers, form an undirected graph with one node for every array value. Two different values have an edge exactly when they share a common factor greater than 1.

Connectivity is transitive: values belong to the same connected component even when they do not share a factor directly, provided a path of qualifying edges joins them. Return the number of nodes in the largest connected component of this graph.

### Function Contract

Let $N$ be the length of `nums`, let $M = \max(\texttt{nums})$, and let $\alpha$ denote the inverse Ackermann function.

**Inputs**

- `nums`: a list of $N$ unique positive integers, where $1 \le N \le 2\cdot 10^4$ and `1 <= nums[i] <= 100000`.

**Return value**

Return the size of the largest component under the common-factor edge rule.

### Examples

**Example 1**

- Input: `nums = [4,6,15,35]`
- Output: `4`

**Example 2**

- Input: `nums = [20,50,9,63]`
- Output: `2`

**Example 3**

- Input: `nums = [2,3,6,7,4,12,21,39]`
- Output: `8`
