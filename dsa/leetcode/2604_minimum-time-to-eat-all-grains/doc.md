# Minimum Time to Eat All Grains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2604 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-eat-all-grains/) |

## Problem Description

### Goal

There are $n$ hens and $m$ grains placed at integer positions on a line. The arrays `hens` and `grains` give their respective starting positions. A hen immediately eats any grain at its current position and may eat any number of grains.

During one second, each hen may move one unit left or right. All hens move simultaneously and independently.

Determine the minimum time in which the hens can eat every grain when their movements are chosen optimally.

### Function Contract

**Inputs**

- `hens`: A list of $n$ integer positions of hens.
- `grains`: A list of $m$ integer positions of grains.

The constraints are $1 \leq n,m \leq 2 \cdot 10^4$ and $0 \leq \texttt{hens[i]}, \texttt{grains[j]} \leq 10^9$.

Let $C = 2 \cdot 10^9 + 1$, the size of the inclusive search range used for a guaranteed upper bound.

**Return value**

- The minimum number of seconds needed to eat every grain.

### Examples

**Example 1**

- Input: `hens = [3,6,7], grains = [2,4,7,9]`
- Output: `2`

In two seconds, the three hens can cover the grains near positions $3$, $6$, and $7$ concurrently. No assignment can cover every grain in less time.

**Example 2**

- Input: `hens = [4,6,109,111,213,215], grains = [5,110,214]`
- Output: `1`

Three hens each move one unit to a grain while the others remain still.
