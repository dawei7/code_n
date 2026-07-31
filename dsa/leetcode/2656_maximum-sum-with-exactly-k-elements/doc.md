# Maximum Sum With Exactly K Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2656 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. Perform exactly `k` operations while maximizing a score that begins at zero. In one operation, choose any current array element `m`, remove that occurrence, insert `m + 1`, and add `m` to the score.

Return the greatest score attainable after all `k` operations. The inserted value is available to later operations, so choosing one element can create an increasing sequence of future choices; equal values in the original array remain separate occurrences.

### Function Contract

**Inputs**

- `nums`: A non-empty integer array, where $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums[i]} \le 100$.
- `k`: The exact number of operations, where $1 \le k \le 100$.

**Return value**

- Return the maximum total score obtainable after exactly `k` operations.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5], k = 3`
- Output: `18`
- Explanation: Select `5`, then the inserted `6`, then the inserted `7`, contributing `5 + 6 + 7`.

**Example 2**

- Input: `nums = [5,5,5], k = 2`
- Output: `11`
- Explanation: Select one `5`, then select the `6` created by the first operation.
