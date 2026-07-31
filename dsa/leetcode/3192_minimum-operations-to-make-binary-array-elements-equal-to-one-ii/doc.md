# Minimum Operations to Make Binary Array Elements Equal to One II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3192 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/) |

## Problem Description
### Goal
You are given a binary array `nums`. An operation chooses any index `i` and
flips every element from `i` through the end of the array. Flipping changes a
`0` to `1` and a `1` to `0`.

You may apply this operation any number of times, including zero. Return the
minimum number of operations needed to make every element of `nums` equal to
`1`.

### Function Contract
**Inputs**

- `nums`: A binary integer array of length $n$, where $1 \le n \le 10^5$.

Every value of `nums` is either `0` or `1`.

**Return value**

The minimum number of suffix-flip operations that makes every array element
equal to `1`.

### Examples
**Example 1**

- Input: `nums = [0, 1, 1, 0, 1]`
- Output: `4`

One minimum sequence flips suffixes beginning at indices `1`, `0`, `4`, and
`3`.

**Example 2**

- Input: `nums = [1, 0, 0, 0]`
- Output: `1`

Flipping the suffix beginning at index `1` changes all three trailing zeros
to ones.
