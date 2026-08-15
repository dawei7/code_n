# Maximum Running Time of N Computers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2141 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-running-time-of-n-computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/) |

## Problem Description

### Goal

There are `n` computers and a 0-indexed list `batteries`; battery `i` can
power one computer for `batteries[i]` minutes. All `n` computers must run
simultaneously.

Initially, at most one battery may be placed in each computer. At any integer
time, a battery may be removed and another inserted. Replacements take no time,
may use an unused battery or one moved from another computer, and may be
performed any number of times. A battery can power only one computer at a time,
and spent energy cannot be recharged.

Return the maximum whole number of minutes for which all `n` computers can
remain running together.

### Function Contract

**Inputs**

- `n`: The number of computers, with
  $1 \leq n \leq \lvert\texttt{batteries}\rvert$.
- `batteries`: Battery capacities in minutes. The list has at most $10^5$
  elements, and each capacity is between $1$ and $10^9$, inclusive.

**Return value**

Return the greatest integer duration during which every computer can be
continuously powered under the replacement rules.

### Examples

#### Example 1

- **Input:** `n = 2, batteries = [3,3,3]`
- **Output:** `4`
- **Explanation:** Swapping the three batteries between two computers uses eight
  of their nine total minutes over four simultaneous minutes.

#### Example 2

- **Input:** `n = 2, batteries = [1,1,1,1]`
- **Output:** `2`
- **Explanation:** Two batteries power the computers for the first minute and the
  other two power them for the second.
