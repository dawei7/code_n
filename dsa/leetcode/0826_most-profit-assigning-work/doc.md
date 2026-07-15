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

### Required Complexity

- **Time:** $O(n \log n + m \log m)$
- **Space:** $O(n + m)$

<details>
<summary>Approach</summary>

#### General

**Sort jobs without separating each difficulty from its profit**

Pair every `difficulty[i]` with `profit[i]`, then sort the pairs by difficulty. Also sort the worker abilities. Sorting creates a shared ascending order in which the set of jobs available to the next worker can only grow. Keeping each job as one pair is essential because the two input arrays describe corresponding properties, not independent multisets.

**Sweep once while remembering the best eligible profit**

Maintain a job pointer and `best_profit`. For each worker ability in ascending order, advance the pointer through every not-yet-processed job whose difficulty is at most that ability, updating `best_profit` with the largest profit encountered. Add the current best to the total; if no job has become eligible, the value remains `0`.

**Why the greedy choice is independent for every worker**

When a worker is processed, the pointer has visited exactly the jobs that worker can complete: all earlier jobs meet the difficulty bound, and the next job, if any, exceeds it. Therefore `best_profit` is the maximum profit available to that worker. Choosing it cannot reduce another worker's options because jobs may be completed multiple times. Taking the maximum independently for each worker consequently maximizes every term of the total, and their sum is globally optimal.

The job pointer never moves backward. A job examined for one worker stays represented by `best_profit` for all later, at-least-as-capable workers, so the sweep does not rescan earlier work.

#### Complexity detail

Let $n$ be the number of jobs and $m$ the number of workers. Sorting the job pairs costs $O(n\log n)$ and sorting the worker abilities costs $O(m\log m)$. The two-pointer sweep visits every job and worker once in $O(n+m)$ time, leaving $O(n\log n+m\log m)$ overall. The sorted job pairs and worker copy use $O(n+m)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix maxima plus binary search:** Sort jobs, replace each profit with the best profit up to that difficulty, and binary-search for every worker. This takes $O(n\log n+m\log n)$ time and avoids sorting workers.
- **Ability-domain table:** Because values are at most $10^5$, a table of best profit at every ability can answer workers in $O(n+m+10^5)$ time with $O(10^5)$ space.
- **Scan every job per worker:** Selecting the best eligible job directly is correct but takes $O(nm)$ time.
- **Reusable jobs:** Multiple workers may choose the same most-profitable job; no capacity or removal step is allowed.
- **Dominated jobs:** A harder job may pay less than an easier one, so the current job's profit cannot replace the running maximum unconditionally.
- **Equal difficulties:** Retain the greatest profit among jobs at the same difficulty through the running maximum.
- **Underqualified worker:** If no job difficulty is within the worker's ability, that worker contributes `0`.
- **Input pairing:** Sorting `difficulty` and `profit` separately would destroy which profit belongs to which job.

</details>
