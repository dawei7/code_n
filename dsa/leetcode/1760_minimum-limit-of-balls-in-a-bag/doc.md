# Minimum Limit of Balls in a Bag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1760 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) |

## Problem Description

### Goal

You are given several bags, where `nums[i]` is the positive number of balls in the $i$-th bag. In one operation, choose one bag and split all of its balls between two new nonempty bags. The original bag is replaced, and the total number of balls is preserved.

You may perform at most `maxOperations` such splits. The penalty of the final arrangement is the largest number of balls in any remaining bag. Choose the operations to make this penalty as small as possible, and return that minimum achievable value.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive bag sizes, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `maxOperations`: the maximum allowed number of splits, with $1 \le \texttt{maxOperations} \le 10^9$.

Let $M=\max(\texttt{nums})$.

**Return value**

- Return the smallest possible maximum bag size after performing no more than `maxOperations` legal splits.

### Examples

**Example 1**

- Input: `nums = [9], maxOperations = 2`
- Output: `3`
- Explanation: Split nine balls into three bags of three using two operations.

**Example 2**

- Input: `nums = [2, 4, 8, 2], maxOperations = 4`
- Output: `2`
- Explanation: The bags of four and eight can be divided until every bag contains at most two balls.

**Example 3**

- Input: `nums = [7, 17], maxOperations = 2`
- Output: `7`
- Explanation: Split seventeen into parts no larger than seven; a penalty below seven would require too many total splits.
