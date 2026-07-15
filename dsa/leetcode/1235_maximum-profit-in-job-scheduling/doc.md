# Maximum Profit in Job Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1235 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) |

## Problem Description

### Goal

There are $n$ jobs. Job $i$ runs from `start_time[i]` until `end_time[i]` and earns `profit[i]` when selected. Choose any subset of the jobs, but do not choose two jobs whose time ranges overlap.

A job ending at time $X$ is compatible with another job starting at exactly time $X$; their shared endpoint is not an overlap. Return the maximum total profit obtainable from a compatible subset. Jobs need not be presented in chronological order, and selecting no unnecessary job does not incur a penalty.

### Function Contract

**Inputs**

- `start_time`: A list of $n$ job start times, where $1\le n\le5\cdot10^4$.
- `end_time`: A list of the corresponding end times, with $1\le\texttt{start_time[i]}<\texttt{end_time[i]}\le10^9$.
- `profit`: A list of corresponding positive profits, where $1\le\texttt{profit[i]}\le10^4$.

**Return value**

- The maximum sum of profits from jobs whose time ranges do not overlap.

### Examples

**Example 1**

- Input: `start_time = [1,2,3,3]`, `end_time = [3,4,5,6]`, `profit = [50,10,40,70]`
- Output: `120`

The jobs `[1,3]` and `[3,6]` touch at time $3$ and earn $50+70=120$.

**Example 2**

- Input: `start_time = [1,2,3,4,6]`, `end_time = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`
- Output: `150`

Selecting `[1,3]`, `[4,6]`, and `[6,9]` earns $20+70+60=150$.

**Example 3**

- Input: `start_time = [1,1,1]`, `end_time = [2,3,4]`, `profit = [5,6,4]`
- Output: `6`

Every pair overlaps, so the single job worth $6$ is optimal.

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Order jobs by their starting times.** Combine the three arrays into `(start, end, gain)` records and sort them by `start`. Let `dp[i]` be the maximum profit available using only jobs from sorted position `i` onward. The answer is `dp[0]`, and `dp[n] = 0` represents having no jobs left.

**Separate the skip and take choices.** At job `i`, skipping it leaves `dp[i + 1]`. Taking it earns its `gain` and forbids every later job starting before its end. Because the starts are sorted, `bisect_left(starts, end, i + 1)` finds the first compatible position `next_index`; using a lower-bound search deliberately permits a job whose start equals the current end. The take value is `gain + dp[next_index]`.

**Fill suffix states backward.** When computing `dp[i]`, both `dp[i + 1]` and `dp[next_index]` are already known. Store the larger of the skip and take values. Every compatible schedule either omits job `i`, or includes it and then uses only jobs at or after `next_index`; these disjoint choices cover all possibilities, so the recurrence preserves the optimal profit at every suffix.

#### Complexity detail

Sorting $n$ jobs takes $O(n\log n)$ time. Each of the $n$ dynamic-programming states performs one $O(\log n)$ binary search, so the total remains $O(n\log n)$. The sorted jobs, start-time list, and dynamic-programming array use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Quadratic weighted-interval dynamic programming:** Scanning every earlier job to find compatible predecessors is correct but takes $O(n^2)$ time.
- **Top-down recursion with memoization:** It uses the same binary-search recurrence, but recursion adds call overhead and may exceed Python's recursion depth.
- **Sweep line with a profit frontier:** Processing start and end events can also maintain the best completed profit, though equal-time event ordering must allow an ending job before a starting job.
- **Touching endpoints:** A job with `start == previous_end` is compatible, which is why the binary search uses a lower bound for the current end time.
- **Identical time ranges:** Such jobs mutually overlap; the recurrence can select only the most profitable useful choice.
- **Unsorted input:** Sorting combined records preserves the association among each job's start, end, and profit.
- **Single job:** Its positive profit is the answer.

</details>
