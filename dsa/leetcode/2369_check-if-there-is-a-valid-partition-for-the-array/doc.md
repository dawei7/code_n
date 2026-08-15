# Check if There is a Valid Partition For The Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2369 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, partition the entire array into one or more contiguous subarrays. Every element must belong to exactly one part, and the order of the elements cannot change.

A partition is valid only when every part has one of three exact forms: two equal elements; three equal elements; or three consecutive increasing elements whose adjacent differences are both $1$. Return `true` when at least one valid partition exists, and return `false` otherwise.

### Function Contract

**Inputs**

- `nums`: An integer array with $2 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- Return `true` if all of `nums` can be divided into valid contiguous parts; otherwise, return `false`.

**Partition rules**

- A two-element part is valid exactly when its two values are equal.
- A three-element part is valid when all three values are equal.
- A three-element part is also valid when its values are consecutive increasing, such as `[3,4,5]`. A merely increasing triple such as `[1,3,5]` is not valid.

### Examples

#### Example 1

- **Input:** `nums = [4,4,4,5,6]`
- **Output:** `true`
- **Explanation:** The parts `[4,4]` and `[4,5,6]` are valid: the first is an equal pair, and the second is a consecutive increasing triple.

#### Example 2

- **Input:** `nums = [1,1,1,2]`
- **Output:** `false`
- **Explanation:** No sequence of allowed two- or three-element parts covers the whole array.
