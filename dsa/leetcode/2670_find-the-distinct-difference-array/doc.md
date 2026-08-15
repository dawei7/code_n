# Find the Distinct Difference Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2670 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-distinct-difference-array/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` of length $n$. Construct an equally long array `diff`. For every index `i`, count the distinct values in the inclusive prefix `nums[0:i + 1]` and subtract the number of distinct values in the suffix `nums[i + 1:n]`.

The suffix after the last element is empty and therefore contains zero distinct values. Repeated values contribute only once to either side's distinct count, even when they occur many times within that prefix or suffix. Return all $n$ differences in index order.

### Function Contract

**Inputs**

- `nums`: An integer array with $1 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 50$.

**Return value**

- Return `diff`, where `diff[i]` equals the prefix distinct count through `i` minus the suffix distinct count strictly after `i`.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `[-3,-1,1,3,5]`
- **Explanation:** Every value is unique, so the prefix count grows by one while the suffix count shrinks by one.

#### Example 2

- **Input:** `nums = [3,2,3,4,2]`
- **Output:** `[-2,-1,0,2,3]`
- **Explanation:** Repetitions keep some distinct counts unchanged as the dividing point moves.
