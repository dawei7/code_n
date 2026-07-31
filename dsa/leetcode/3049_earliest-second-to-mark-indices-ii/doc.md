# Earliest Second to Mark Indices II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3049 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/earliest-second-to-mark-indices-ii/) |

## Problem Description

### Goal

You are given two 1-indexed integer arrays. The array `nums` contains `n` nonnegative values, and `changeIndices` assigns a particular index to each of `m` consecutive seconds. Initially, every index of `nums` is unmarked, and the goal is to mark them all.

At second `s`, for $1 \le s \le m$, you may perform exactly one operation. You may decrement any `nums[i]` by `1`; set `nums[changeIndices[s]]` to any non-negative value; mark any index `i` whose current value is equal to `0`; or do nothing. Only the set operation is tied to `changeIndices[s]`. Decrementing and marking may target any eligible index, and setting a value to zero does not mark it in the same second.

Return the earliest second in `[1, m]` by which every index can be marked under an optimal schedule. Return `-1` if even the entire sequence is insufficient.

### Function Contract

**Inputs**

- `nums`: `n` initial nonnegative values, represented with 0-based storage although the problem names their indices from `1` through `n`.
- `changeIndices`: `m` 1-indexed positions; at second $s+1$, `changeIndices[s]` is the only value eligible for the arbitrary non-negative assignment.

The bounds are $1 \le n \le 5000$, $0 \le \texttt{nums[i]} \le 10^9$, $1 \le m \le 5000$, and $1 \le \texttt{changeIndices[s]} \le n$.

**Return value**

- The smallest 1-indexed second at which all indices can be marked, or `-1` when no prefix permits a complete schedule.

### Examples

**Example 1**

- Input: `nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]`
- Output: `6`
- Explanation: Set each of the three designated values to zero during the first three seconds, then use seconds `4` through `6` to mark the three indices.

**Example 2**

- Input: `nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]`
- Output: `7`
- Explanation: Mark the two initially zero indices, use three seconds to decrement the remaining values to zero, and mark those two indices at seconds `6` and `7`.

**Example 3**

- Input: `nums = [1,2,3], changeIndices = [1,2,3]`
- Output: `-1`
- Explanation: Three seconds cannot perform enough value-changing work and also provide a separate mark for every index.
