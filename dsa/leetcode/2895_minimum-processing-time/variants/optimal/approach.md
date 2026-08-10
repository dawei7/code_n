## General

**Each processor receives exactly four simultaneous tasks.** A processor has four cores, and every core is used once. If a processor becomes available at time $p$ and receives task durations $d_1,d_2,d_3,d_4$, their completion times are $p+d_1$ through $p+d_4$. Since the cores run in parallel, that processor finishes its assigned work at

$$
p+\max(d_1,d_2,d_3,d_4).
$$

The three shorter tasks in the group do not affect the global completion time once the group's longest task is known. The assignment problem can therefore be viewed as forming groups of four tasks, then pairing each group maximum with a processor availability time.

**Sort processors from early to late.** `processorTime.sort()` places the smallest availability first. An early processor has more room to absorb a long task without creating a large sum, so it should receive a group with a large maximum. A late processor should receive a smaller group maximum.

**Sort tasks and consume them from the largest end.** `tasks.sort()` orders durations ascending. Variable `i` starts at the final index, which is the largest task. For each processor time `t`, the source considers `tasks[i]` and then executes `i -= 4`.

This step implicitly assigns a block of four descending tasks to that processor:

`tasks[i], tasks[i-1], tasks[i-2], tasks[i-3]`.

Only `tasks[i]` is used in the answer because it is the largest duration in that block. After decreasing by four, the next iteration sees the maximum of the next group of four.

**Why pack large tasks together.** If the largest tasks were spread among many groups, each would become a different group maximum and would delay a different processor. Putting the four largest tasks into one four-core group makes only the single largest one matter; the other three execute in parallel underneath that same finishing time.

More formally, among the first $4r$ tasks in descending order, at most $r$ groups can contain them if each group has four slots. The greedy grouping fills those slots densely. Its $r$-th group maximum is the task at descending rank $4r-3$, the smallest possible value any arrangement can guarantee for that ordered group maximum. Grouping consecutive blocks of four therefore minimizes the sequence of maxima from largest to smallest.

**Why pair opposite orders.** Suppose two processor times satisfy $a\le b$ and two group maxima satisfy $x\ge y$. Pairing large with early produces completion candidates $a+x$ and $b+y$. Pairing large with late produces $a+y$ and $b+x$.

The second pairing's $b+x$ is at least both $a+x$ and $b+y$, because $b\ge a$ and $x\ge y$. Therefore

$$
\max(a+x,b+y)\le\max(a+y,b+x).
$$

Whenever an assignment has two pairs in the wrong relative order, swapping them cannot worsen the makespan. Repeated exchanges yield earliest processors paired with largest group maxima, exactly the source's traversal.

**Following the answer update.** For each sorted processor time `t`, `t + tasks[i]` is that processor's finishing time under its implicit four-task group. `ans = max(ans, t + tasks[i])` records the latest processor finish seen. After all processors are assigned, this maximum is the time when every task has completed.

For the first example, sorted processor times are `[8,10]` and sorted task durations are `[1,2,2,3,4,5,7,8]`. Time eight is paired with maximum eight from the four largest tasks, producing sixteen. Time ten is paired with maximum three from the remaining four, producing thirteen. The global completion time is sixteen.

**The inputs are mutated.** Both `sort()` calls operate in place. The function does not preserve original processor or task order. That is harmless to the returned minimum time, but callers that need the original lists must pass copies.

## Complexity detail

Let $p$ be the number of processors; there are exactly $4p$ tasks. Sorting processors costs $O(p\log p)$. Sorting tasks costs $O(4p\log(4p))=O(p\log p)$. The final loop visits $p$ processors, so total time is $O(p\log p)$.

Python's Timsort may use $O(p)$ auxiliary memory for processors and $O(4p)=O(p)$ for tasks in the worst case, giving $O(p)$ additional space. The lists are sorted in place at the language level, but that does not imply constant internal sorting workspace. The manifest's $O(n\log n)$ time and $O(n)$ space are accurate when `n` denotes the problem scale.

## Alternatives and edge cases

- **Heap assignment:** Repeatedly choosing processors and tasks with heaps adds complexity; one global sort exposes the optimal opposite ordering directly.
- **Arbitrary task groups:** Spreading the four largest tasks across four processors creates four large group maxima instead of one and can only hurt.
- **One processor:** All four tasks run on its cores, and the answer is its availability plus the longest duration.
- **Equal processor times:** Their relative ordering is irrelevant.
- **Equal task durations:** Any grouping among tied values has the same maxima.
- **Only group maxima matter:** The other three tasks still occupy cores but finish no later than the maximum-duration task.
- **Large values:** Availability plus duration can reach $2\times10^9$, which fits signed 32-bit only narrowly; wider arithmetic is safer in general.
- **Input mutation:** Both arrays finish sorted, so copy them first when original ordering must be retained.
