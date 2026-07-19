# Minimum Elements to Add to Form a Given Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/) |
| Frontend ID | 1785 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` and integers `limit` and `goal`. Every existing array value satisfies $\lvert\texttt{nums[i]}\rvert \le \texttt{limit}$.

You may add any integers to the array, but each new value must preserve the same absolute-value bound. Find the minimum number of elements that must be added so that the sum of the resulting array equals `goal`. Added values may be positive, negative, or zero as long as their absolute values do not exceed `limit`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and every value is between `-limit` and `limit`, inclusive.
- `limit`: the positive maximum absolute value of any array element, where $1 \le \texttt{limit} \le 10^6$.
- `goal`: the desired final sum, where $-10^9 \le \texttt{goal} \le 10^9$.

**Return value**

- Return the minimum number of bounded integers that must be appended to make the final array sum equal `goal`.

### Examples

**Example 1**

- Input: `nums = [1,-1,1], limit = 3, goal = -4`
- Output: `2`

The current sum is `1`. Adding `-2` and `-3` supplies the missing `-5`.

**Example 2**

- Input: `nums = [1,-10,9,1], limit = 100, goal = 0`
- Output: `1`

The current sum is `1`, so one added value `-1` is sufficient.

**Example 3**

- Input: `nums = [4,-7,3], limit = 5, goal = 0`
- Output: `0`

The array already has the requested sum.
