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

### Required Complexity

- **Time:** $O(N+T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Compress clips by start time:** Build `farthest_from_start`, where each integer start stores the greatest endpoint among clips beginning there. Shorter clips with the same start can never improve a minimum solution.

**Treat coverage like minimum jumps:** Scan integer positions from `0` toward `T`. Maintain `farthest`, the greatest endpoint offered by any clip whose start has been scanned, and `current_end`, the endpoint reachable with the clips already committed.

**Commit only when existing coverage ends:** When the scan reaches `current_end`, choose one clip implicitly by extending `current_end` to `farthest`. This is the clip among all currently available choices that reaches farthest. If `farthest` does not pass the current position, a coverage gap makes the task impossible.

Choosing a shorter reachable endpoint can never expose a clip earlier than choosing the farthest endpoint, so the greedy extension cannot use more future clips than another feasible choice. Repeating this exchange argument at each committed boundary yields the minimum clip count.

#### Complexity detail

Compressing the $N$ clips costs $O(N)$, and scanning the $T$ integer positions costs $O(T)$, for $O(N+T)$ time. The farthest-end array has $T+1$ entries and uses $O(T)$ space.

#### Alternatives and edge cases

- **Sort intervals:** Sorting by start and greedily extending coverage takes $O(N\log N)$ time and is useful without bounded integer endpoints.
- **Dynamic programming:** Computing the minimum clips for every time from every interval costs $O(NT)$ time.
- **Gap at zero:** If no clip starting at zero extends coverage, return `-1`.
- **One covering clip:** A clip spanning `[0, T]` gives answer one even when many redundant clips exist.
- **Clips beyond time:** Endpoints past `T` are useful and may finish coverage immediately.

</details>
