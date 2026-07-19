## General
**Schedule restrictive jobs first**

Sort job durations in descending order. Assigning a long job early raises worker loads sooner, making an already noncompetitive branch easier to recognize. Maintain an array of the current loads and a global best maximum, initially the sum of all durations.

**Explore every distinct worker-load state**

For the next job, try adding it to each worker. Recursively schedule the remaining jobs, then undo the addition. At a complete assignment, the maximum entry in the load array is a feasible makespan and can lower the current best. Since every job chooses one worker, this search includes every assignment that could be optimal.

**Prune loads that cannot improve the answer**

Skip a placement when the receiving worker's new load is already at least the best known makespan: every later duration is positive, so that branch cannot improve the answer. At one recursion level, workers with equal current loads are interchangeable; trying the job on more than one of them produces states that differ only by worker labels. Record seen loads and explore one representative.

**Collapse equivalent empty workers**

After trying the current job on one empty worker and backtracking, stop trying other empty workers. Those branches are identical up to renaming unused workers. These symmetry reductions remove redundant work without removing any distinct multiset of worker workloads, so the smallest complete makespan remains reachable.

## Complexity detail
Without pruning, each of the $n$ jobs can choose any of $k$ workers, giving the worst-case bound $O(k^n)$. Sorting costs $O(n\log n)$ and is dominated by the search. The workload array and recursion stack require $O(k+n)$ space.

## Alternatives and edge cases
- **Binary search plus feasibility backtracking:** Search between the largest job and total duration, checking whether jobs fit under each candidate limit; this adds a logarithmic number of pruned searches.
- **Subset dynamic programming:** Precompute subset sums and distribute subsets among workers in roughly $O(k3^n)$ time with $O(k2^n)$ state, trading memory for a deterministic exact bound.
- **Unpruned labeled assignment:** Enumerating all worker choices is correct but repeats assignments that differ only by worker names and reaches the same $O(k^n)$ worst-case class with much larger constants.
- **One worker:** Every job belongs to that worker, so the answer is the total duration.
- **One worker per job:** No worker needs more than one job, so the answer is the largest duration.
- **Equal durations:** Seen-load and empty-worker pruning are especially important because many assignments are symmetric.
