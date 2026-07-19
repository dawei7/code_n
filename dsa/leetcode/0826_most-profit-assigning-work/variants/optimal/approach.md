## General
**Sort jobs without separating each difficulty from its profit**

Pair every `difficulty[i]` with `profit[i]`, then sort the pairs by difficulty. Also sort the worker abilities. Sorting creates a shared ascending order in which the set of jobs available to the next worker can only grow. Keeping each job as one pair is essential because the two input arrays describe corresponding properties, not independent multisets.

**Sweep once while remembering the best eligible profit**

Maintain a job pointer and `best_profit`. For each worker ability in ascending order, advance the pointer through every not-yet-processed job whose difficulty is at most that ability, updating `best_profit` with the largest profit encountered. Add the current best to the total; if no job has become eligible, the value remains `0`.

**Why the greedy choice is independent for every worker**

When a worker is processed, the pointer has visited exactly the jobs that worker can complete: all earlier jobs meet the difficulty bound, and the next job, if any, exceeds it. Therefore `best_profit` is the maximum profit available to that worker. Choosing it cannot reduce another worker's options because jobs may be completed multiple times. Taking the maximum independently for each worker consequently maximizes every term of the total, and their sum is globally optimal.

The job pointer never moves backward. A job examined for one worker stays represented by `best_profit` for all later, at-least-as-capable workers, so the sweep does not rescan earlier work.

## Complexity detail
Let $n$ be the number of jobs and $m$ the number of workers. Sorting the job pairs costs $O(n\log n)$ and sorting the worker abilities costs $O(m\log m)$. The two-pointer sweep visits every job and worker once in $O(n+m)$ time, leaving $O(n\log n+m\log m)$ overall. The sorted job pairs and worker copy use $O(n+m)$ auxiliary space.

## Alternatives and edge cases
- **Prefix maxima plus binary search:** Sort jobs, replace each profit with the best profit up to that difficulty, and binary-search for every worker. This takes $O(n\log n+m\log n)$ time and avoids sorting workers.
- **Ability-domain table:** Because values are at most $10^5$, a table of best profit at every ability can answer workers in $O(n+m+10^5)$ time with $O(10^5)$ space.
- **Scan every job per worker:** Selecting the best eligible job directly is correct but takes $O(nm)$ time.
- **Reusable jobs:** Multiple workers may choose the same most-profitable job; no capacity or removal step is allowed.
- **Dominated jobs:** A harder job may pay less than an easier one, so the current job's profit cannot replace the running maximum unconditionally.
- **Equal difficulties:** Retain the greatest profit among jobs at the same difficulty through the running maximum.
- **Underqualified worker:** If no job difficulty is within the worker's ability, that worker contributes `0`.
- **Input pairing:** Sorting `difficulty` and `profit` separately would destroy which profit belongs to which job.
