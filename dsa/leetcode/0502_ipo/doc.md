# IPO

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 502 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/ipo/) |

## Problem Description
### Goal
You begin with capital `w` and are given parallel arrays `profits` and `capital` describing distinct projects. Project `i` may be started only when current capital is at least `capital[i]`; after completion, its nonnegative `profits[i]` is added immediately to the available capital.

Choose and complete at most `k` distinct projects to maximize final capital, using each project no more than once. A project made affordable by an earlier profit may be selected later, while an unaffordable project cannot be chosen in anticipation of future gains. Return the greatest capital reachable after the allowed completions, not the selected project indices or total profit alone.

### Function Contract
**Inputs**

- `k`: the maximum number of projects that may be completed
- `w`: the initial capital
- `profits`: the profit earned by each project
- `capital`: the minimum capital required by the corresponding project

**Return value**

- The maximum capital achievable after at most `k` selections

### Examples
**Example 1**

- Input: `k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]`
- Output: `4`

**Example 2**

- Input: `k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]`
- Output: `6`

**Example 3**

- Input: `k = 1, w = 2, profits = [1,2], capital = [2,3]`
- Output: `3`
