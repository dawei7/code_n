# Reduction Operations to Make the Array Elements Equal

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) |
| Frontend ID | 1887 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given an integer array `nums`, repeatedly reduce one of its largest elements until every element has the same value. In one operation, find the largest value currently present. If that value occurs more than once, choose its smallest array index. Replace only that chosen element with the next-largest distinct value currently in the array.

For example, if the current array is `[5,1,3]`, the first operation changes `5` to `3`, because `3` is the greatest value strictly smaller than `5`. The array becomes `[3,1,3]`; subsequent operations continue under the same rule. Return the total number of operations required before all entries are equal.

### Function Contract

**Inputs**

- `nums`: an array of $N$ positive integers.
- $1 \le N \le 5 \cdot 10^4$.
- Each value lies between $1$ and $5 \cdot 10^4$, inclusive.

**Return value**

- Return the number of single-element reduction operations needed to make all values equal.

### Examples

**Example 1**

- Input: `nums = [5,1,3]`
- Output: `3`

The reductions are `[5,1,3]` to `[3,1,3]`, then `[1,1,3]`, then `[1,1,1]`.

**Example 2**

- Input: `nums = [1,1,1]`
- Output: `0`

The values are already equal.

**Example 3**

- Input: `nums = [1,1,2,2,3]`
- Output: `4`

The `3` crosses two distinct lower levels, while each `2` crosses one.
