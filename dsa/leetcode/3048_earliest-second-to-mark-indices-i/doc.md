# Earliest Second to Mark Indices I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) |

## Problem Description

### Goal

You are given two 1-indexed integer arrays: `nums` contains `n` values, and `changeIndices` describes `m` consecutive seconds. Initially, none of the indices of `nums` are marked. The objective is to mark every index.

At second `s`, for $1 \le s \le m$, you may perform exactly one of three operations: choose any index `i` from `[1, n]` and decrement `nums[i]` by `1`; mark `changeIndices[s]` if its current value in `nums` is equal to `0`; or do nothing. Decrements may target any index and are not restricted by `changeIndices[s]`, while a marking operation is restricted to the index named at that second.

Return the earliest second in `[1, m]` by which all indices can be marked when the operations are chosen optimally. Return `-1` if the complete sequence does not make this possible.

### Function Contract

**Inputs**

- `nums`: `n` nonnegative integers; `nums[i]` is the initial value at 0-based position `i`, corresponding to the problem's 1-indexed index $i+1$.
- `changeIndices`: `m` 1-indexed positions; at second $s+1$, only `changeIndices[s]` is eligible for the marking operation.

The bounds are $1 \le n \le 2000$, $0 \le \texttt{nums[i]} \le 10^9$, $1 \le m \le 2000$, and $1 \le \texttt{changeIndices[s]} \le n$.

**Return value**

- The earliest 1-indexed second when every index can be marked, or `-1` if no prefix of `changeIndices` is sufficient.

### Examples

**Example 1**

- Input: `nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]`
- Output: `8`
- Explanation: Four early seconds can perform the two decrements required for each of indices `1` and `2`. Later eligible seconds mark indices `3`, `2`, and `1`; the last required mark occurs at second `8`.

**Example 2**

- Input: `nums = [1,3], changeIndices = [1,1,1,2,1,1,1]`
- Output: `6`
- Explanation: Use the first three seconds to reduce index `2` to zero, mark it at second `4`, decrement index `1` at second `5`, and mark index `1` at second `6`.

**Example 3**

- Input: `nums = [0,1], changeIndices = [2,2,2]`
- Output: `-1`
- Explanation: Index `1` never occurs in `changeIndices`, so no second permits it to be marked.
