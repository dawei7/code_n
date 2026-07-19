# Minimum Time to Build Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1199 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-build-blocks/) |

## Problem Description

### Goal

Each entry `blocks[i] = t` describes a block that requires exactly one worker and $t$ time units to build. A worker may instead spend `split` time units splitting into two workers, increasing the available worker count by one. After building a block, that worker goes home.

Actions performed by different workers run in parallel, so simultaneous splits cost only `split` elapsed time rather than the sum of their costs. Starting with exactly one worker, determine the minimum elapsed time required to finish every block.

### Function Contract

**Inputs**

- `blocks`: A list of $n$ build times, where $1\le n\le1000$ and $1\le\texttt{blocks[i]}\le10^5$.
- `split`: The time for one worker to become two workers, where $1\le\texttt{split}\le100$.

**Return value**

- The minimum time by which all blocks can be completed from one initial worker.

### Examples

**Example 1**

- Input: `blocks = [1]`, `split = 1`
- Output: `1`

The initial worker builds the only block without splitting.

**Example 2**

- Input: `blocks = [1,2]`, `split = 5`
- Output: `7`

Split once, then build both blocks in parallel for a total of `5 + max(1,2)`.

**Example 3**

- Input: `blocks = [1,2,3]`, `split = 1`
- Output: `4`

One worker can take the longest block while the other splits again for the two shorter blocks.
