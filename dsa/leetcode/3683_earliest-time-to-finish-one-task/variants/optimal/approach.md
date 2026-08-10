## General

Each task is described by two numbers:

- `s`, the time when the task starts; and
- `t`, the amount of time the task takes after it starts.

Therefore, that task's finishing time is

$$
s+t.
$$

The requested result is the earliest time at which **at least one** task is finished. The tasks do not depend on one another, they do not share a worker or machine in the statement, and completing one does not delay another. There is consequently no scheduling simulation to perform. Compute every independent finishing time and choose the smallest one.

The exact Optimal source expresses the whole scan as:

`return min(s + t for s, t in tasks)`

Although this is one line, it performs three meaningful operations that are worth separating.

**Unpacking each task**

The expression `for s, t in tasks` visits the task rows one at a time. Since every row has the required form `[s_i, t_i]`, Python unpacking assigns its first entry to `s` and its second entry to `t`.

This avoids index-heavy expressions such as `task[0] + task[1]`, but the meaning is identical. The variable `t` is a duration, not an absolute finish timestamp. That distinction is why the two entries must be added.

For example, a task `[2, 3]` starts at time $2$ and then runs for $3$ units. Its finish time is $2+3=5$. Returning just the duration $3$, or taking the larger of the two fields, would misinterpret the contract.

**Producing completion times lazily**

For every row, the generator expression yields `s + t`. It does not construct a separate list containing all completion times. Instead, `min` requests one generated value at a time and keeps only the smallest value seen so far.

Conceptually, the running state is:

- after the first task, the best finishing time is that task's `s + t`;
- for each later task, compare its `s + t` with the current best; and
- retain the smaller of the two.

The generator syntax merely packages this ordinary one-pass minimum scan compactly.

For `tasks = [[1, 6], [2, 3]]`, the generated finishing times are $7$ and $5$. The minimum is $5$, so the second task is the first one that can be completed.

For `tasks = [[100, 100], [100, 100], [100, 100]]`, every generated value is $200$. The minimum is still $200$; ties do not require identifying which task finishes first because the function returns only the time.

**Why taking the minimum answers “at least one”**

Let the finishing times be

$$
f_i=s_i+t_i.
$$

Before time $\min_i f_i$, every task has a finishing time later than the current time, so zero tasks have completed. At time $\min_i f_i$, the task attaining that minimum has completed, so at least one task is finished. This is exactly the first moment at which the requested condition becomes true.

Any value larger than the minimum would not be the earliest such time. Any value smaller than the minimum would occur before every task's completion. Thus the minimum is both attainable and minimal.

The algorithm does not need to compare start times separately. A task that starts earlier may take much longer, while a later-starting task may finish first. Only the sum captures both effects. In the first example, the first task starts at $1$ but finishes at $7$, whereas the task starting at $2$ finishes at $5$.

**Why no special initialization is needed**

An explicit loop often initializes an answer to infinity. Here, `min` initializes itself from the first generated finishing time. The constraints guarantee at least one task, so the generator is never empty and `min` cannot raise the empty-sequence error.

All start times and durations are positive, which means every finish time is also positive. The implementation does not rely on a made-up sentinel such as zero that could accidentally be smaller than every genuine completion time.

## Complexity detail

Let $n$ be `len(tasks)`.

The generator visits every one of the $n$ tasks exactly once. For each task it performs one unpacking operation, one addition, and one comparison inside `min`. Each of these is constant work for the bounded integers in the problem. The total running time is therefore $O(n)$.

This linear scan is asymptotically necessary in the general case. If an algorithm ignored some task, that unseen task could have the uniquely smallest finishing time. Reading all task rows is required to guarantee the minimum.

The generator does not allocate an $n$-element completion-time list. At any moment, it holds the current `s`, `t`, their sum, and the running minimum maintained by `min`. The auxiliary space usage is therefore $O(1)$.

The input array itself is not modified, and no output collection is built because the returned result is one integer.

## Alternatives and edge cases

- **Sort all finishing times:** Sorting would place the earliest completion first, but it costs $O(n \log n)$ time and may require $O(n)$ additional storage. A single minimum scan is sufficient.
- **Build a list and call `min`:** `min([s + t for s, t in tasks])` produces the same value but materializes $n$ sums. The generator used by the source preserves $O(1)$ auxiliary space.
- **Choose the earliest start time:** The earliest-starting task is not necessarily the earliest-finishing task because durations differ. The relevant quantity is always `s + t`.
- **Choose the shortest duration:** A short task may begin much later than a longer one. Duration alone also cannot determine the earliest absolute finish time.
- **One task:** Its completion time is automatically both the minimum and the answer. The nonempty guarantee lets `min` handle this without a branch.
- **Several tasks tie:** If multiple tasks share the earliest finish time, `min` returns that time once. The problem does not ask for a task index or tie-breaking rule.
- **Identical tasks:** Repeated rows generate repeated completion values, which do not change the minimum and require no deduplication.
- **Largest permitted values:** With `s = 100` and `t = 100`, the sum is $200$. Python integers handle this directly, and the constraints make overflow irrelevant in any standard integer type.
- **No task interaction:** The statement does not say tasks run sequentially or compete for a resource. Introducing such a restriction would solve a different scheduling problem.
