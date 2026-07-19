# Most Profit Assigning Work

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 826 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-profit-assigning-work/) |

## Problem Description

### Goal

You have $n$ jobs and $m$ workers. For job $i$, `difficulty[i]` is the ability required to complete it and `profit[i]` is the profit earned from one completion. For worker $j$, `worker[j]` is that worker's ability, so the worker may complete only a job whose difficulty is at most `worker[j]`.

Each worker may be assigned at most one job. A job is reusable and may be completed by any number of workers, so assigning it once does not make it unavailable to anyone else. A worker who cannot complete any job contributes `0` profit. Choose an eligible job independently for every worker and return the maximum total profit across all assignments.

### Function Contract

**Inputs**

- `difficulty`: an array of $n$ job difficulties, where $1 \le n \le 10^4$ and $1 \le \texttt{difficulty}[i] \le 10^5$
- `profit`: an array of $n$ positive profits, where `profit[i]` belongs to the job described by `difficulty[i]` and $1 \le \texttt{profit}[i] \le 10^5$
- `worker`: an array of $m$ worker abilities, where $1 \le m \le 10^4$ and $1 \le \texttt{worker}[j] \le 10^5$

**Return value**

- The maximum sum of profit earned when each worker completes at most one eligible job

### Examples

**Example 1**

- Input: `difficulty = [2, 4, 6, 8, 10], profit = [10, 20, 30, 40, 50], worker = [4, 5, 6, 7]`
- Output: `100`
- Explanation: The workers can take jobs with difficulties `[4, 4, 6, 6]` and earn `[20, 20, 30, 30]`.

**Example 2**

- Input: `difficulty = [85, 47, 57], profit = [24, 66, 99], worker = [40, 25, 25]`
- Output: `0`
- Explanation: No worker has enough ability for any listed job.

**Example 3**

- Input: `difficulty = [2], profit = [10], worker = [1, 2, 2, 3]`
- Output: `30`
- Explanation: Three workers can independently complete the same job, while the worker with ability `1` earns nothing.
