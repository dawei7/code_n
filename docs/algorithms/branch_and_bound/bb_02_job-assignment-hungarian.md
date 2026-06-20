# Job Assignment (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_02` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(N!)$ Worst Case |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Assignment problem](https://en.wikipedia.org/wiki/Assignment_problem) |

## Problem statement

Given N workers and N jobs, and a 2D cost matrix where `cost[i][j]` is the cost of assigning worker `i` to job `j`.
Each worker must be assigned exactly one job, and each job must be assigned to exactly one worker.
Find the assignment that minimizes the total cost.

While the famous Hungarian Algorithm solves this exactly in $O(N^3)$ time, you must demonstrate how to solve it using a generic **Branch and Bound** state-space search.

**Input:** An N x N integer matrix `cost`.
**Output:** The minimum possible total cost.

## When to use it

- To learn how to construct lower bounds for matrix-based combinatorial optimization problems.
- Branch and Bound is highly adaptable: if you add complex non-linear constraints (e.g., "Worker A cannot work on Tuesday if Worker B does Job 3"), the Hungarian algorithm completely breaks, but B&B can still solve it by simply discarding invalid states!

## Approach

We can view this as a decision tree.
Level 0 assigns a job to Worker 0. Level 1 assigns a job to Worker 1, etc.
At Level 0, Worker 0 has N choices. This creates N branches.
If we explore all branches, we check N! permutations.

**Branch and Bound Pruning:**
We need to calculate a **Lower Bound** for any partial assignment. If we have assigned the first 2 workers, what is the absolute *minimum* possible cost for the remaining N-2 workers?
Since we are minimizing, if this `lower_bound` is **greater than or equal to** our global `min_cost` found so far, we prune the branch!

**How to calculate the Lower Bound?**
A very simple and fast lower bound: For every unassigned worker, look at the available unassigned jobs, and pretend they can just take the absolute cheapest one independently (ignoring conflicts where two workers might want the same cheap job).
`bound = current_accumulated_cost + sum(min(available jobs) for each unassigned worker)`.
This bound is mathematically guaranteed to be \le the true cost of completing the assignment, making it safe for pruning.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_02: Job Assignment.

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum-cost assignment. Brute-force
enumerate all n! permutations of jobs. Setup keeps n small
(n <= 6) so this is tractable.
"""


def solve(cost, n):
    if n == 0:
        return 0
    jobs = list(range(n))
    best = float("inf")

    def helper(worker, used, current):
        nonlocal best
        if worker == n:
            if current < best:
                best = current
            return
        for job in jobs:
            if not used[job]:
                used[job] = True
                helper(worker + 1, used, current + cost[worker][job])
                used[job] = False

    helper(0, [False] * n, 0)
    return best
```

</details>

## Walk-through

*(Conceptual)*
`Cost Matrix:`
```text
W0: [9, 2, 7]
W1: [6, 4, 3]
W2: [5, 8, 1]
```

1. **Root (No assignments):** Bound = W0 min(2) + W1 min(3) + W2 min(1) = 6. Push to Heap.
2. **Pop Root. Branch W0:**
   - W0 takes J0 (cost 9). Bound = 9 + W1 min(3) + W2 min(1) = 13.
   - W0 takes J1 (cost 2). Bound = 2 + W1 min(3) + W2 min(1) = 6.
   - W0 takes J2 (cost 7). Bound = 7 + W1 min(4) + W2 min(5) = 16. *(Notice min changed because J2 is taken!)*
3. **Heap State:** `[6 (J1), 13 (J0), 16 (J2)]`.
4. **Pop J1 Branch (Best First). Branch W1:**
   - W1 takes J0 (cost 6). Total = 2+6=8. Bound = 8 + W2 min(1) = 9.
   - W1 takes J2 (cost 3). Total = 2+3=5. Bound = 5 + W2 min(5) = 10.
5. **Deepest Level:** The heap prioritizes expanding the `Bound 9` path. W2 is forced to take J2 (cost 1). Total cost = 9.
   - `min_final_cost = 9`.
6. Now the heap looks at the `Bound 13` and `Bound 16` paths from W0. Since 13 \ge 9, it completely PRUNES them and terminates! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^3)$ | $O(N)$ |
| **Average** | Much faster than N! | $O(2^N)$ |
| **Worst** | $O(N!)$ | $O(N!)$ |

In the absolute worst case where the bound never prunes anything, the tree generates N! leaves, taking factorial time. The Priority Queue also explodes to hold factorial elements in memory. However, the Best-First Search heuristic causes it to find the optimal solution almost immediately in standard datasets, pruning the vast majority of the tree.

## Variants & optimizations

- **Hungarian Algorithm ($O(N^3)$):** The exact, deterministic DP/combinatorial solution. It creates a bipartite graph and manipulates the matrix rows and columns to find zero-cost perfect matchings. It is strictly mathematically superior to B&B for the pure Job Assignment problem.

## Real-world applications

- **Ride-Sharing:** Uber/Lyft matching N drivers to N riders simultaneously to minimize total global wait time.

## Related algorithms in cOde(n)

- **[flow_03 - Bipartite Matching](../flow/flow_03_bipartite-matching.md)** — The unweighted, pure structural version of the assignment problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
