## General

**One powered-on second can serve many tasks**

The computer has unlimited parallel capacity. If it is on at time $t$, every task whose allowed interval contains $t$ may count that second toward its duration.

The problem is therefore to choose the smallest set of integer time points such that each task interval contains at least its required number of chosen points.

Array `vis` marks chosen seconds with one. `ans` is the total number of chosen seconds, which is exactly the total powered-on time.

**Process tasks by increasing deadline**

The code sorts tasks by `end`. When handling a task, every earlier processed task has a deadline no later than the current one.

This order makes a latest-possible greedy strategy safe. If the current task still needs more active seconds, choose them from its interval starting at its end and moving left. Late seconds satisfy the current deadline while preserving earlier times for tasks with tighter future start constraints.

More importantly, future tasks have deadlines at least as late. A later chosen second is generally at least as reusable for them as an earlier replacement within the current interval.

**Reuse seconds that are already on**

For task `[start,end,duration]`, the slice sum

`sum(vis[start:end + 1])`

counts powered-on seconds already present in its inclusive interval. Those seconds may have been selected for earlier tasks, but unlimited concurrency lets the current task use them too.

The code subtracts this count from `duration`. The resulting local variable is the additional number of seconds still required. If it is zero or negative, the task is already satisfied and no new activation is needed.

**Add missing seconds from right to left**

Starting with `i = end`, the loop moves backward while the task still has a deficit. Whenever `vis[i]` is zero, it turns that second on, decreases the remaining duration, and increments `ans`.

Already-active seconds are skipped because they were included in the initial slice count. The scan continues left until enough new positions have been selected.

The problem guarantees `duration <= end - start + 1`. Even if no second in the interval had previously been selected, enough positions exist, so the loop can always satisfy the task.

**Why choosing the latest free seconds is optimal**

Assume all earlier-deadline tasks have been satisfied by the greedy set. Consider any minimum completion that extends those fixed choices and satisfies the current and future tasks.

If this completion uses an earlier unselected second $u$ for the current task while greedy chooses a later free second $v$ in the same current interval, exchange $u$ for $v$. The current task remains satisfied.

Earlier tasks do not need $u$ as an additional point: their requirements were already met by the fixed greedy choices before processing the current task. Future tasks have deadlines no earlier than the current end. If a future interval contained $u$ but not $v$, its start would have to lie at or before $u$ while its end still reaches later; moving toward $v$ within the current interval generally preserves deadline availability. The standard interval-cover exchange repeatedly moves newly needed points as far right as possible without increasing the number chosen.

This establishes an induction: after each deadline-ordered task, the greedy schedule uses the minimum number of seconds and is at least as favorable for all unprocessed tasks as any equally small schedule.

**Trace the first sample**

Sorted tasks are `[2,3,1]`, `[4,5,1]`, and `[1,5,2]`.

- The first has no active seconds, so greedy turns on latest time $3$.
- The second turns on latest time $5$.
- The final interval already contains active times $3$ and $5$, exactly its duration two, so it adds nothing.

The answer is two. The statement uses time $2$ instead of $3$ for the first task, but both schedules are optimal; choosing $3$ is the exact code's latest-time policy.

**Exact implementation versus manifest**

The manifest describes a Fenwick tree plus predecessor structure that can count selected points and jump over used positions in logarithmic time. The checked-in solution uses a fixed boolean array, scans slices to count, and walks individual times backward.

Because time coordinates are bounded by $2000$, this simpler implementation is practical, but its worst-case complexity is not $O(N\log N)$.

## Complexity detail

Let $N$ be the number of tasks and $T$ the maximum time coordinate, at most $2000$. Sorting costs $O(N\log N)$. For each task, slicing and summing may inspect $O(T)$ positions, and the backward loop may inspect another $O(T)$ positions. Total exact time is $O(N\log N+NT)$.

`vis` has fixed length 2010, conceptually $O(T)$ space. Sorting may use $O(N)$ temporary memory in Python. The task list is reordered in place.

## Alternatives and edge cases

- **Fenwick plus predecessor structure:** Count active seconds in $O(\log T)$ and jump to the latest unused predecessor efficiently, matching the manifest's stronger bound.
- **Segment tree:** It can maintain selected counts and locate free positions, also avoiding linear interval scans.
- **Turn on a whole task interval:** This satisfies the task but usually wastes seconds beyond its duration.
- **Choose earliest seconds:** It can block opportunities to reuse later points for tasks with later starts; latest choice is the safe greedy direction.
- **Already satisfied task:** A nonpositive remaining duration causes no additions.
- **Identical intervals:** Active seconds selected for one are fully reusable by all others.
- **Inclusive endpoint:** Both slice and backward scan include `end`.
- **Maximum concurrency:** A chosen second counts for every compatible task, never only one.
- **Input mutation:** Sorting changes task order.
- **Bounded coordinate domain:** The simple array is viable specifically because all times are at most 2000.
