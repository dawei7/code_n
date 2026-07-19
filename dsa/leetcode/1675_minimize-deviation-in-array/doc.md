# Minimize Deviation in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1675 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-deviation-in-array/) |

## Problem Description
### Goal
The deviation of an array is the difference between its maximum and minimum values. Starting from an array of positive integers, operations may be applied to any element any number of times: an even value may be divided by two, while an odd value may be multiplied by two.

Choose any legal sequence of these operations and return the smallest deviation that can be achieved. Each element evolves independently, but the objective depends on the common range containing one reachable value from every element.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers.

Let $M=\max(\texttt{nums})$.

**Return value**

Return the minimum possible difference between the largest and smallest array values after any number of legal operations.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `1`

**Example 2**

- Input: `nums = [4,1,5,20,3]`
- Output: `3`

**Example 3**

- Input: `nums = [2,10,8]`
- Output: `3`
