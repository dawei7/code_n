# The Earliest Moment When Everyone Become Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) |

## Problem Description

### Goal

A social group contains `n` people labeled from `0` through `n - 1`. Each entry `logs[i] = [timestamp_i, x_i, y_i]` says that two different people become friends at that timestamp. Friendship is symmetric.

Two people are acquainted when they are direct friends or connected through a chain of friendships. Return the earliest timestamp at which every person is acquainted with every other person. If the events never connect the entire group, return `-1`. All timestamps are unique, and each friendship pair occurs at most once.

### Function Contract

**Inputs**

- `logs`: a list of $m$ triples `[timestamp, x, y]`, where $1 \leq m \leq 10^4$, $0 \leq \texttt{timestamp} \leq 10^9$, and `x` and `y` are distinct labels in $[0,n-1]`. Timestamps and unordered friendship pairs are unique.
- `n`: the number of people, where $2 \leq n \leq 100$.

**Return value**

The earliest timestamp when the friendship graph is connected, or `-1` if it never becomes connected.

### Examples

**Example 1**

- Input: `logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6`
- Output: `20190301`

At that event, the components containing `{0,1,5}` and `{2,3,4}` merge.

**Example 2**

- Input: `logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4`
- Output: `3`
