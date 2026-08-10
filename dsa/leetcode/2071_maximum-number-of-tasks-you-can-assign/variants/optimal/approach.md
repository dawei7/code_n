## General

**Binary-search how many tasks can be completed**

If `x` tasks can be assigned, then any smaller number can be assigned by discarding some task-worker pairs. Feasibility is monotone.

The source sorts tasks and workers, then binary-searches `x` from zero through `min(n,m)`. A successful midpoint moves the lower bound upward; a failure moves the upper bound downward.

The upper-middle expression prevents an infinite loop when two candidates remain.

**Choose the easiest tasks and strongest workers**

To test `x`, it is sufficient and optimal to use `tasks[0:x]`, the `x` easiest requirements. Replacing any selected task with a harder unselected task cannot improve feasibility.

Similarly, use `workers[m-x:m]`, the `x` strongest workers. Replacing one with a weaker excluded worker cannot help.

The check must decide whether these two selected groups can be paired using at most the available pills.

**Process selected workers from weakest to strongest**

The loop begins at worker index `m-x` and moves upward. At each worker, pointer `i` adds every still-unadded selected task satisfying

`tasks[i] <= workers[j] + strength`.

These are exactly the remaining tasks this worker could perform if given a pill. Because tasks are sorted, they enter deque `q` from easiest to hardest.

Tasks too hard even with a pill stay outside until a stronger worker is processed.

**Why an empty deque proves failure**

Exactly `x` selected workers must complete `x` selected tasks. If the current weakest remaining worker cannot perform any unassigned selected task even with a pill, skipping that worker would leave fewer than `x` workers.

Every excluded worker is weaker, so changing the selected worker set cannot rescue the assignment. The check correctly returns false.

**Prefer no pill when possible**

If `q[0] <= workers[j]`, the current worker can complete the easiest available task without a pill. The source removes that task from the left.

Using a pill would waste a limited resource. Assigning a harder task instead is also unnecessary: later workers are at least as strong, while preserving easy tasks offers no advantage over preserving harder ones for them.

The easiest-task choice leaves the remaining assignment no more difficult.

**When a pill is mandatory, use it on the hardest eligible task**

If the easiest queued task exceeds current worker strength, every queued task requires a pill for this worker.

With a pill, the worker can complete all tasks currently in `q` by the enqueue condition. The source removes `q.pop()`, the hardest one, and decrements pill count.

This spends the boost where it has greatest value. Easier tasks remain for stronger future workers, who may complete them without pills. Giving the pill to an easier task would leave a harder obligation and cannot improve feasibility.

**Why deque endpoints are enough**

Tasks enter in ascending order. The left endpoint is the easiest pill-reachable task and the right endpoint is the hardest.

The greedy rules need only these two choices, so both removal operations are constant time. No balanced tree is required.

**Trace a successful check**

For tasks one, two, three and selected workers zero, three, three with one strength-one pill, the weakest worker zero can enqueue task one and must use the pill on it.

The later workers perform tasks two and three without pills. All three workers receive one task, so feasibility is true.

**Why the check is correct**

At each weakest-worker step, every task it might possibly handle with a pill is in `q`. If it can work unboosted, pairing it with the easiest available task is an exchange-safe choice. If not, every assignment must spend a pill on this worker, and choosing the hardest eligible task preserves the easiest remainder.

Inductively, the greedy choice never turns a feasible suffix into an infeasible one. Failure conditions mean no legal assignment exists for the selected groups. The check is therefore necessary and sufficient.

**Why binary search returns the maximum**

Feasible counts form a prefix beginning at zero. The loop preserves a feasible-or-unknown lower boundary and eliminates impossible larger values.

When bounds meet, `left` is the greatest feasible task count and is returned.

**Input mutation**

Both `tasks.sort()` and `workers.sort()` reorder caller-provided lists in place. Repeated feasibility checks then read these stable sorted arrays without further mutation.

## Complexity detail

Let $N$, $M$, and $R=\min(N,M)$ be task, worker, and maximum assignment counts. Sorting costs $O(N\log N+M\log M)$.

One feasibility check performs $O(x)$ worker iterations and enqueues each of the first `x` tasks at most once, so it is $O(x)\subseteq O(R)$. Binary search performs $O(\log R)$ checks, giving $O(R\log R)$ additional time.

Total time is $O(N\log N+M\log M+R\log R)$. The deque uses $O(R)$ space. Python sorting may use additional linear temporary storage, while the explicit algorithmic helper space is $O(R)$.

## Alternatives and edge cases

- **Sorted multiset check:** Process hardest tasks and remove chosen workers in $O(\log R)$ each, yielding an extra logarithmic factor.
- **Try every task count linearly:** Repeats feasibility work and loses monotonic binary search.
- **Zero pills:** Every assigned worker must meet its task directly.
- **Zero strength:** Pills provide no benefit, though the check can still spend them harmlessly only when equality permits.
- **More pills than tasks:** At most one is used per selected worker.
- **Worker handles task exactly:** No pill is needed because comparison is inclusive.
- **Task too hard even with pill:** It is not enqueued for that worker.
- **Empty deque:** Proves the current selected worker cannot be assigned.
- **Duplicate requirements or strengths:** Sorted ordering and deque multiplicity preserve separate tasks and workers.
- **Zero tasks feasible:** Provides the binary-search base.
- **Strongest workers:** Testing any weaker group cannot improve feasibility.
- **Input mutation:** Both arrays are sorted in place.
