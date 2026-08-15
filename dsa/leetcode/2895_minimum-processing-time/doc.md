# Minimum Processing Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2895 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-processing-time/) |

## Problem Description

### Goal

There are $n$ processors, and each processor has exactly four cores. The array `processorTime` gives the time when each processor becomes available. There are exactly $4n$ tasks, and `tasks` gives their individual execution durations.

Assign every task to a distinct core. Each core is used for exactly one task, so every processor receives four tasks. A task assigned to processor $i$ finishes after `processorTime[i] + taskDuration`, and the entire workload finishes when the last assigned task completes.

Return the minimum possible completion time over all valid assignments.

### Function Contract

**Inputs**

- `processorTime`: An array of $n$ processor availability times, where $1 \le n \le 25{,}000$ and $0 \le \texttt{processorTime[i]} \le 10^9$.
- `tasks`: An array of $4n$ task durations, where $1 \le \texttt{tasks[i]} \le 10^9$.

**Return value**

Return the smallest possible value of the latest task completion time.

### Examples

#### Example 1

- **Input:** `processorTime = [8, 10], tasks = [2, 2, 3, 1, 8, 7, 4, 5]`
- **Output:** `16`
- **Explanation:** Give durations $8,7,5,4$ to the processor available at time $8$, and give $3,2,2,1$ to the processor available at time $10$. Their finishing times are $16$ and $13$.

#### Example 2

- **Input:** `processorTime = [10, 20], tasks = [2, 3, 1, 2, 5, 8, 4, 3]`
- **Output:** `23`
- **Explanation:** The first processor can receive durations $8,5,4,3$, while the second receives $3,2,2,1$. The latest completion time is $23$.
