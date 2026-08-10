## General

**Search assignments because the job count is tiny**

Each job must go to exactly one of $k$ workers. For $n$ jobs there are up to $k^n$ labeled assignments, too many for large $n$ but feasible with strong pruning when `n <= 12`.

`cnt[j]` stores the current total time assigned to worker `j`. The recursive state `dfs(i)` means jobs at indices below `i` have been assigned and job `i` is the next decision.

**Place large jobs first**

`jobs.sort(reverse=True)` mutates the input into descending duration order. Assignment order does not change the set of possible final partitions, so correctness is unaffected.

Large-first order improves pruning. A poor distribution of the most expensive jobs raises worker loads early, allowing the current best answer to reject branches before many small jobs are placed. If small jobs came first, most partial loads would remain deceptively low until deep in the tree.

**Maintain the best complete makespan**

`ans` begins at infinity. When `i == len(jobs)`, every job has been assigned. The makespan of that assignment is `max(cnt)`, the busiest worker's total.

`ans = min(ans, max(cnt))` keeps the smallest complete makespan seen. The nonlocal declaration lets the nested DFS replace the outer variable.

The first complete branch establishes a finite upper bound; subsequent branches can then be cut off when their partial loads cannot improve it.

**Try the current job on every meaningfully different worker**

For job `jobs[i]`, the loop considers worker indices zero through `k-1`. It tentatively adds the job, recurses, and then subtracts it to restore the exact prior state:

`cnt[j] += jobs[i]`,

`dfs(i + 1)`,

`cnt[j] -= jobs[i]`.

This undo step is essential. Sibling branches must begin with the same assignments for earlier jobs.

**Prune a worker that already reaches the best answer**

Before modifying a load, the source checks

`if cnt[j] + jobs[i] >= ans: continue`.

Loads never decrease as later positive-duration jobs are assigned. If this worker would already reach or exceed `ans`, every completion of the branch has makespan at least `ans`.

The goal is only to find a smaller minimum, not count equally good assignments, so equality can also be pruned safely.

**Break symmetry among empty workers**

After undoing a trial, the source tests `if cnt[j] == 0: break`. At that moment, zero means worker `j` was empty before the current job was tentatively assigned.

All empty workers are interchangeable: placing the current job on empty worker three instead of empty worker four changes only worker labels, not the multiset of loads or any possible future makespan. The explored branch for the first empty worker already represents every such choice.

Breaking avoids factorial duplication caused by permuting identical worker roles. The check must occur after undoing so it accurately identifies the worker's original load.

**Why the search remains exhaustive enough**

Without pruning, the loop tries every worker for every job, representing every labeled assignment. The load-bound prune removes only branches that cannot beat a known feasible answer.

The empty-worker break removes assignments that are identical after renaming workers. Since the objective depends only on the maximum load and not worker identities, each removed branch has an equivalent explored branch with the same outcome.

Therefore at least one representative of every distinct load partition capable of improving `ans` remains. Evaluating all completed representatives makes the final `ans` the global minimum.

**Trace the symmetry idea**

At the root all $k$ worker loads are zero. Trying the largest job on worker zero is sufficient; placing it on any other worker merely renames that worker to zero. After the branch returns, `cnt[0]` becomes zero again and the loop breaks.

Later, if worker loads are `[8,3,0,0]`, the current job must still be tried on load-eight, load-three, and one zero worker. The two zero choices are symmetric, but nonzero workers are not necessarily equivalent and are both explored.

**Lower bounds explain the goal, even though source does not compute them**

Any answer must be at least the largest job and at least the ceiling of total work divided by $k$. The exact source does not initialize `ans` from a greedy schedule or use these lower bounds. It begins with infinity and relies on its first complete assignment for an upper bound, which is an important implementation detail when reasoning about early pruning strength.

## Complexity detail

The conventional worst-case search-tree bound is $O(k^n)$ assignment states, matching the manifest. Sorting adds $O(n\log n)$ time and is dominated by the exponential search. Descending order, load pruning, and empty-worker symmetry greatly reduce practical exploration but do not create a polynomial worst-case guarantee.

The exact leaf operation computes `max(cnt)` in $O(k)$. If that factor is retained strictly for every possible leaf, a coarse operation bound is $O(k\cdot k^n)=O(k^{n+1})$; the manifest uses the standard $O(k^n)$ backtracking-state characterization and suppresses this per-leaf polynomial factor.

The load array uses $O(k)$ space and recursion depth is $O(n)$. Python's in-place sort may use $O(n)$ temporary storage. Total auxiliary space is $O(k+n)$, matching the manifest.

## Alternatives and edge cases

- **Binary search the answer:** Test whether jobs fit under a candidate makespan with backtracking. It can add logarithmic outer iterations but sometimes prunes feasibility searches strongly.
- **Subset dynamic programming:** Precompute subset sums and assign subsets to workers, yielding alternatives based on $2^n$ states that suit the small job count.
- **Greedy list scheduling only:** Assign each job to the currently lightest worker. It gives a useful upper bound but is not always optimal.
- **No descending sort:** Correctness remains, but useful overloads are discovered later and pruning weakens.
- **`k = 1`:** Every job goes to the only worker, so the answer is their sum.
- **`k = n`:** Each positive job can occupy its own worker, making the largest job optimal.
- **Equal job durations:** Worker and job symmetries create repeated states; the source removes only empty-worker symmetry, not every duplicate-load state.
- **Equality with ans:** The branch cannot improve the stored minimum and is safely skipped.
- **Positive durations:** Partial worker loads never decrease, which makes the bound prune valid.
- **Input mutation:** Sorting permanently reorders `jobs`.
- **Backtracking restoration:** Every tentative addition is subtracted before another worker is tried.
- **Infinity initialization:** No branch is load-pruned until a first complete assignment establishes a finite answer.
