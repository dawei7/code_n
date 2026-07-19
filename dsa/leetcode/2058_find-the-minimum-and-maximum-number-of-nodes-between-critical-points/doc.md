# Find the Minimum and Maximum Number of Nodes Between Critical Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2058 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) |

## Problem Description

### Goal

A critical point in a singly linked list is an internal node that is either a strict local maximum or a strict local minimum. Its value must be strictly greater than both neighboring values or strictly less than both. The head and tail cannot be critical because each lacks one neighbor.

Among all distinct critical-point pairs, find the minimum and maximum distances between their zero-based list positions. Return `[minDistance, maxDistance]`. If the list contains fewer than two critical points, neither distance exists, so return `[-1, -1]`.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list containing $n$ nodes, where $2 \le n \le 10^5$ and every node value is from $1$ through $10^5$.

**Return value**

- Return the minimum and maximum index differences among pairs of critical points.
- Return `[-1, -1]` when fewer than two critical points exist.

### Examples

**Example 1**

- Input: `head = [3,1]`
- Output: `[-1,-1]`
- Explanation: Neither endpoint can be critical.

**Example 2**

- Input: `head = [5,3,1,2,5,1,2]`
- Output: `[1,3]`
- Explanation: Critical positions are `2`, `4`, and `5`.

**Example 3**

- Input: `head = [1,3,2,2,3,2,2,2,7]`
- Output: `[3,3]`
- Explanation: The two critical positions are `1` and `4`.
