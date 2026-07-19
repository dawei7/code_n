# Video Stitching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1024 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/video-stitching/) |

## Problem Description

### Goal

A sporting event lasts `time` seconds, and you are given video clips that may overlap and have different lengths. Clip `i` covers the interval from `clips[i][0]` through `clips[i][1]`.

You may cut any clip freely into smaller segments. Return the minimum number of original clips needed to cover the entire event interval `[0, time]` without a gap. If the available clips cannot provide complete coverage, return `-1`; using several segments from one original clip still counts as one clip.

### Function Contract

**Inputs**

- `clips`: an array of $N$ intervals `[start, end]`, where $1\le N\le100$ and $0\le\texttt{start}\le\texttt{end}\le100$.
- `time`: the target endpoint $T$, where $1\le T\le100$.

**Return value**

- The minimum number of clips whose cuttable coverage spans `[0, T]`, or `-1` if impossible.

### Examples

**Example 1**

- Input: `clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10`
- Output: `3`
- Explanation: Clips `[0,2]`, `[1,9]`, and `[8,10]` can be cut and combined to cover the full event.

**Example 2**

- Input: `clips = [[0,1],[1,2]], time = 5`
- Output: `-1`
- Explanation: No clip covers any time after `2`.

**Example 3**

- Input: `clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9`
- Output: `3`
- Explanation: Clips `[0,4]`, `[4,7]`, and `[6,9]` suffice.
