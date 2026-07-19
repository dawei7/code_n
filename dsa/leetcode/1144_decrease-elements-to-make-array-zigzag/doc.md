# Decrease Elements To Make Array Zigzag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1144 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/) |

## Problem Description

### Goal

An array `nums` is zigzag when its adjacent comparisons alternate in one of two strict patterns. It may begin with a peak, so `nums[0] > nums[1] < nums[2] > nums[3] ...`, or it may begin with a valley, so `nums[0] < nums[1] > nums[2] < nums[3] ...`. Equal adjacent values do not satisfy either pattern.

One move chooses any element of `nums` and decrements it by exactly `1`. An element may be chosen repeatedly, and no move can increase a value. Return the minimum number of moves needed to make the whole array zigzag in either of the two permitted patterns.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

The minimum total number of single-unit decrements that produces either valid zigzag pattern.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`
- Explanation: Decrementing `nums[2]` twice gives `[1, 2, 1]`, which follows the valley-peak-valley pattern.

**Example 2**

- Input: `nums = [9, 6, 1, 6, 2]`
- Output: `4`
- Explanation: Four decrements can make the even-indexed positions the peaks of a valid zigzag array.
