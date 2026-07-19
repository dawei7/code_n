# Kill Process

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 582 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/kill-process/) |

## Problem Description
### Goal
You are given a list of unique process identifiers `pid` and a parallel list `ppid`, where `ppid[i]` is the parent of `pid[i]` and parent identifier `0` denotes a root process. Killing one process also kills every process descended from it through any number of parent-child links.

Given the identifier `kill`, return that process together with all of its direct and indirect descendants. Do not include ancestors, siblings, or processes from another root, and return each affected process identifier once; the result may be in any order.

### Function Contract
**Inputs**

- `pid: list[int]`: unique process identifiers
- `ppid: list[int]`: corresponding parent identifiers, where `ppid[i]` is the parent of `pid[i]` and zero denotes no parent
- `kill: int`: identifier of the process to terminate

**Return value**

- A list containing `kill` and every direct or indirect descendant of `kill`
- The identifiers may be returned in any order

### Examples
**Example 1**

- Input: `pid = [1, 3, 10, 5]`, `ppid = [3, 0, 5, 3]`, `kill = 5`
- Output: `[5, 10]` in any order

**Example 2**

- Input: the same process tree with `kill = 3`
- Output: `[3, 1, 5, 10]` in any order

**Example 3**

- Input: `pid = [1]`, `ppid = [0]`, `kill = 1`
- Output: `[1]`
