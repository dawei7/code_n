# Meeting Scheduler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1229 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-scheduler/) |

## Problem Description

### Goal

Two people each provide a list of time slots during which they are available. A slot `[start, end]` can host a meeting beginning no earlier than `start` and finishing no later than `end`. Within either person's list, the slots do not overlap one another.

Given `slots1`, `slots2`, and a positive meeting `duration`, return the earliest time interval that lasts exactly `duration` and lies within one slot from each person. If no common availability is long enough, return an empty list.

### Function Contract

**Inputs**

- `slots1`: The first person's $n$ nonoverlapping availability intervals, where $1\le n\le10^4$.
- `slots2`: The second person's $m$ nonoverlapping availability intervals, where $1\le m\le10^4$.
- Every slot has two endpoints satisfying $0\le\texttt{start}<\texttt{end}\le10^9$.
- `duration`: The required meeting length, where $1\le\texttt{duration}\le10^6$.

**Return value**

- `[start, start + duration]` for the earliest feasible meeting, or `[]` when none exists.

### Examples

**Example 1**

- Input: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 8`
- Output: `[60,68]`

The first overlap lasts from `10` through `15`, which is too short. The overlap beginning at `60` can host eight time units.

**Example 2**

- Input: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 12`
- Output: `[]`

No shared interval lasts twelve time units.

**Example 3**

- Input: `slots1 = [[1,2]]`, `slots2 = [[3,4]]`, `duration = 1`
- Output: `[]`
