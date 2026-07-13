# Maximum Number of Tasks You Can Assign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2071 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Queue, Sorting, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-tasks-you-can-assign](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/).

### Goal
Assign as many tasks as possible to workers. A worker can do one task if their strength is high enough, and a limited number of pills can temporarily increase worker strength by `strength`.

### Function Contract
**Inputs**

- `tasks`: required strengths for tasks.
- `workers`: worker strengths.
- `pills`: number of available pills.
- `strength`: strength gained from one pill.

**Return value**

Return the maximum number of tasks that can be completed.

### Examples
**Example 1**

- Input: `tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1`
- Output: `3`

**Example 2**

- Input: `tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5`
- Output: `1`

**Example 3**

- Input: `tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10`
- Output: `2`

---

## Solution
### Approach
Binary search the number of tasks `x`. To test feasibility, consider the `x` easiest tasks and the `x` strongest workers. Assign from hardest task downward: use a worker who can already handle it when possible; otherwise spend a pill on the weakest worker who can reach the requirement after the boost.

### Complexity Analysis
- **Time Complexity**: `O((n + m) log(n + m) + log(min(n,m)) * x log x)` for feasibility with an ordered multiset/deque.
- **Space Complexity**: `O(x)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
