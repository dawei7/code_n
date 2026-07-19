# Maximum Number of Weeks for Which You Can Work

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1953 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/) |

## Problem Description
### Goal
There are $N$ projects, and `milestones[i]` is the number of milestones
remaining in project $i$. During each week you must complete exactly one
milestone, so there are no idle weeks while work continues.

You may not work on the same project in two consecutive weeks. Work stops
after every milestone is finished or when every remaining milestone belongs
to the project used in the preceding week. Some milestones may therefore
remain unfinished. Return the maximum number of weeks that can be scheduled
without violating the consecutive-project rule.

### Function Contract
**Inputs**

- `milestones`: an array of length $N$, where $1 \le N \le 10^5$ and every
  count is between 1 and $10^9$.

**Return value**

- The greatest number of consecutive working weeks achievable while completing
  one milestone per week and never choosing the same project twice in a row.

### Examples
**Example 1**

- Input: `milestones = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `milestones = [5, 2, 1]`
- Output: `7`
- Explanation: One milestone from the largest project cannot be scheduled.

**Example 3**

- Input: `milestones = [5, 2, 2]`
- Output: `9`
- Explanation: The four other milestones can separate all five largest-project
  milestones.
