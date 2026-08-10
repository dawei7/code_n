## General

**Each worker can be optimized independently**

A job may be completed any number of times, so assigning a job to one worker does not consume it or prevent another worker from choosing it. Therefore, the globally maximum total is obtained by giving every worker the highest-profit job whose difficulty does not exceed that worker's ability.

The challenge is finding that best affordable profit efficiently for every worker. Checking all jobs for every worker would take `O(nm)`.

**Sort jobs and workers by their thresholds**

`jobs = sorted(zip(difficulty, profit))` creates `(difficulty, profit)` pairs and orders them by increasing difficulty. Pairing preserves which profit belongs to each job.

`worker.sort()` orders abilities increasingly. Once workers are processed in this order, the set of affordable jobs only grows: a later worker can perform every job an earlier worker could, plus possibly more difficult jobs.

This monotonicity permits one shared pointer through the sorted job list.

**Maintain the best profit among affordable jobs**

Variables begin as `ans = mx = i = 0`:

- `i` is the index of the first job not yet incorporated;
- `mx` is the greatest profit among all jobs before `i`;
- `ans` is the total assigned profit so far.

For a worker ability `w`, the while loop advances while `jobs[i][0] <= w`. Every newly affordable job updates

`mx = max(mx, jobs[i][1])`.

When the loop stops, every job with difficulty at most `w` has been considered, and every remaining job is too difficult. Thus, `mx` is exactly the highest obtainable profit for that worker.

The algorithm adds `mx` to `ans`. If no job is affordable, `mx` remains zero, correctly representing an unassigned worker.

**Why the pointer never moves backward**

The next worker has ability at least `w` because workers are sorted. Jobs already affordable remain affordable, so their best profit remains captured in `mx`. Only newly affordable jobs need examination.

Even if a newly considered harder job has lower profit, `max` preserves the better easier job. Ability is a ceiling, not a requirement to choose the hardest job.

Each job pointer advance happens once across the entire worker loop. This is the two-pointer efficiency: workers advance in the outer loop, while jobs advance monotonically in the inner loop.

**Trace the main example**

Sorted jobs are `(2,10), (4,20), (6,30), (8,40), (10,50)` and sorted abilities are 4, 5, 6, 7.

- Ability 4 incorporates difficulties 2 and 4, making `mx = 20`.
- Ability 5 incorporates no new job, so it also earns 20.
- Ability 6 incorporates difficulty 6, making `mx = 30`.
- Ability 7 incorporates no new job, so it earns 30.

The total is 100. Reusing difficulty-4 and difficulty-6 jobs is allowed, so no assignment conflict exists.

**Why the greedy choice is globally correct**

Fix one worker. At the moment that worker is processed, the invariant says `mx` is the maximum profit over exactly all feasible jobs. Choosing anything else cannot improve that worker's contribution.

Because jobs are reusable and workers have no coupling constraint, improving one worker never harms another. Summing each independent maximum is therefore the global optimum.

Sorting changes only processing order. The returned total does not associate results with original worker indices, so worker order is irrelevant.

## Complexity detail

Let `n` be the number of jobs and `m` the number of workers.

Sorting job pairs takes `O(n\log n)` time, and sorting workers takes `O(m\log m)`. The outer loop processes `m` workers. Across all its executions, the inner while loop advances `i` at most `n` times, so the sweep itself costs `O(n+m)`.

Total time is

$$
O(n\log n+m\log m).
$$

The `jobs` list stores `n` pairs. Python sorting may use linear temporary storage, and sorting `worker` is in place but can also use implementation workspace. The manifest's `O(n+m)` auxiliary bound safely covers the paired job list and sorting storage.

The growing input values do not affect loop count; only list sizes do.

## Alternatives and edge cases

- **Binary search per worker:** Sort jobs and preprocess prefix maximum profits, then binary-search the last affordable difficulty. This takes `O(n\log n+m\log n)` and avoids sorting workers, but the two-pointer sweep is simpler once both arrays are ordered.

- **Ability-indexed profit table:** With bounded abilities, store best profit at each difficulty and propagate prefix maxima. Here values reach `10^5`, so it is possible but allocates by value range rather than actual input size.

- **Check every job for every worker:** Correct but `O(nm)`, too slow at 10,000 by 10,000.

- **Choose the hardest affordable job:** Difficulty does not imply profit. `mx` must track maximum profit, not merely the most recently added job.

- **No affordable job:** The while loop adds nothing, `mx` stays zero, and that worker contributes zero.

- **Several jobs with the same difficulty:** Sorting places them together, and the loop considers each profit; `mx` retains the best.

- **Harder job with lower profit:** It cannot reduce `mx`, so later workers may still choose the more profitable easier job.

- **Several workers with equal ability:** The first incorporates all affordable jobs; later equal workers reuse the same `mx`, as job reuse permits.

- **All workers can do every job:** The first sufficiently capable worker advances through all jobs, and every later worker receives the global maximum profit.

- **One job:** Every capable worker earns its profit; every incapable worker earns zero.

- **Worker input mutation:** `worker.sort()` changes the ability array's order. This is intentional and does not affect the requested total.

- **Difficulty and profit preserved together:** `zip` pairs them before sorting, preventing profits from becoming detached from their jobs.
