# Pizza With 3n Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1388 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/pizza-with-3n-slices/) |

## Problem Description

### Goal

A circular pizza is divided into $3n$ slices of possibly different sizes. In each round, Alice chooses any remaining slice. Bob then takes the next remaining slice counterclockwise from Alice's choice, and Charlie takes the next remaining slice clockwise. The process repeats until no slices remain.

Alice therefore receives exactly $n$ slices, and no two slices she originally chooses can be adjacent in the circle. Given the slice sizes in circular order, maximize the total size Alice can obtain.

### Function Contract

**Inputs**

- `slices`: a circular array of positive sizes with length $L$, where $L$ is divisible by $3$.
- Let $C = L / 3$ be the exact number of slices Alice receives.

**Return value**

- The maximum sum of exactly $C$ pairwise nonadjacent circular slices.

### Examples

**Example 1**

- Input: `slices = [1,2,3,4,5,6]`
- Output: `10`

**Example 2**

- Input: `slices = [8,9,8,6,1,1]`
- Output: `16`

**Example 3**

- Input: `slices = [4,1,2,5,8,3]`
- Output: `12`
