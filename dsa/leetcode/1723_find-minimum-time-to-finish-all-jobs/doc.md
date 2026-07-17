# Find Minimum Time to Finish All Jobs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1723 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/) |

## Problem Description

### Goal

Each positive integer in `jobs` is the time required to finish one job. Assign every job to exactly one of `k` workers. A worker may receive any number of jobs, and that worker's working time is the sum of the assigned durations.

For an assignment, consider the largest working time among all workers. Return the minimum possible value of that maximum over every complete assignment of jobs to workers.

### Function Contract

**Inputs**

- `jobs`: an array of $n$ positive durations, where $1 \le n \le 12$ and $1 \le \texttt{jobs[i]} \le 10^7$.
- `k`: the number of workers, with $1 \le k \le n$.

**Return value**

- Return the smallest achievable maximum worker workload.

### Examples

**Example 1**

- Input: `jobs = [3,2,3], k = 3`
- Output: `3`
- Explanation: Assigning one job to each worker makes the largest workload $3$.

**Example 2**

- Input: `jobs = [1,2,4,7,8], k = 2`
- Output: `11`
- Explanation: Workloads $1+2+8=11$ and $4+7=11$ attain the optimum.

**Example 3**

- Input: `jobs = [5,5,4,4,4], k = 2`
- Output: `12`
- Explanation: One worker can receive the two fives while the other receives the three fours.

### Required Complexity

- **Time:** $O(k^n)$
- **Space:** $O(k+n)$

<details>
<summary>Approach</summary>

#### General

**Schedule restrictive jobs first**

Sort job durations in descending order. Assigning a long job early raises worker loads sooner, making an already noncompetitive branch easier to recognize. Maintain an array of the current loads and a global best maximum, initially the sum of all durations.

**Explore every distinct worker-load state**

For the next job, try adding it to each worker. Recursively schedule the remaining jobs, then undo the addition. At a complete assignment, the maximum entry in the load array is a feasible makespan and can lower the current best. Since every job chooses one worker, this search includes every assignment that could be optimal.

**Prune loads that cannot improve the answer**

Skip a placement when the receiving worker's new load is already at least the best known makespan: every later duration is positive, so that branch cannot improve the answer. At one recursion level, workers with equal current loads are interchangeable; trying the job on more than one of them produces states that differ only by worker labels. Record seen loads and explore one representative.

**Collapse equivalent empty workers**

After trying the current job on one empty worker and backtracking, stop trying other empty workers. Those branches are identical up to renaming unused workers. These symmetry reductions remove redundant work without removing any distinct multiset of worker workloads, so the smallest complete makespan remains reachable.

#### Complexity detail

Without pruning, each of the $n$ jobs can choose any of $k$ workers, giving the worst-case bound $O(k^n)$. Sorting costs $O(n\log n)$ and is dominated by the search. The workload array and recursion stack require $O(k+n)$ space.

#### Alternatives and edge cases

- **Binary search plus feasibility backtracking:** Search between the largest job and total duration, checking whether jobs fit under each candidate limit; this adds a logarithmic number of pruned searches.
- **Subset dynamic programming:** Precompute subset sums and distribute subsets among workers in roughly $O(k3^n)$ time with $O(k2^n)$ state, trading memory for a deterministic exact bound.
- **Unpruned labeled assignment:** Enumerating all worker choices is correct but repeats assignments that differ only by worker names and reaches the same $O(k^n)$ worst-case class with much larger constants.
- **One worker:** Every job belongs to that worker, so the answer is the total duration.
- **One worker per job:** No worker needs more than one job, so the answer is the largest duration.
- **Equal durations:** Seen-load and empty-worker pruning are especially important because many assignments are symmetric.

</details>
