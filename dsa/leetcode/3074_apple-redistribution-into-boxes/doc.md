# Apple Redistribution into Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3074 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apple-redistribution-into-boxes/) |

## Problem Description

### Goal

You are given $n$ packs of apples and $m$ empty boxes. Pack $i$ contains `apple[i]` apples, while box $i$ can hold at most `capacity[i]` apples.

Choose the minimum number of boxes whose combined capacity can hold every apple from all $n$ packs. Apples may be redistributed freely: a single pack can be split across several boxes, and a box may receive apples from different packs. Consequently, only the total number of apples and the selected boxes' total capacity determine feasibility.

The input guarantees that all apples can be redistributed among the available boxes.

### Function Contract

**Inputs**

- `apple`: A list of $n$ positive integers giving the apple count in each pack.
- `capacity`: A list of $m$ positive integers giving each box's capacity.

Both $n$ and $m$ lie from $1$ through $50$, and every value in both lists lies from $1$ through $50$. The sum of `capacity` is at least the sum of `apple`.

**Return value**

- The minimum number of boxes whose combined capacity is at least the total number of apples.

### Examples

**Example 1**

- Input: `apple = [1, 3, 2]`, `capacity = [4, 3, 1, 5, 2]`
- Output: `2`
- Explanation: There are six apples, and the boxes of capacities `5` and `4` hold them using two boxes. No single box has enough capacity.

**Example 2**

- Input: `apple = [5, 5, 5]`, `capacity = [2, 4, 2, 7]`
- Output: `4`
- Explanation: All four boxes are necessary because their combined capacity is exactly fifteen.
