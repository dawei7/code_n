# Minimum Amount of Time to Collect Garbage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) |

## Problem Description

### Goal

Houses are arranged from index zero onward. At each house, a string lists units of metal (`'M'`), paper (`'P'`), and glass (`'G'`) garbage. Collecting any one unit takes one minute, and `travel[i]` gives the driving time from house `i` to house `i + 1`.

One truck handles each garbage type. Every truck starts at house zero, visits houses in order, and may stop after its last needed house. Because only one truck can drive or collect at a time, all pickup and travel durations add rather than overlap. Return the minimum total time to collect every unit.

### Function Contract

**Inputs**

- `garbage`: A list of $n$ nonempty strings over `'M'`, `'P'`, and `'G'`, where $2 \le n \le 10^5$ and each string has length at most 10.
- `travel`: A list of $n-1$ positive travel times, each at most 100.

**Return value**

- Return the minimum total serial time for all three trucks.

**Timing semantics**

- Every garbage character costs one pickup minute.
- A truck pays every road segment through the last house containing its type, once.
- Trucks cannot operate concurrently.

### Examples

**Example 1**

- Input: `garbage = ["G","P","GP","GG"], travel = [2,4,3]`
- Output: `21`

**Example 2**

- Input: `garbage = ["MMM","PGM","GP"], travel = [3,10]`
- Output: `37`
