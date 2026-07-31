## General

**Separate the independent exact-skill markets.** A regular worker with skill `s` can affect only tasks whose requirement is exactly `s`. Count workers by skill and group task profits by required skill. Within one group, if there are $c$ matching workers, assigning anything other than the $c$ largest available profits can be improved by swapping a lower-profit chosen task with a higher-profit unchosen task.

Store each profit group as a max-heap, represented in Python by negating profits in a min-heap. Building all heaps is linear in the number of tasks. For each distinct worker skill, pop up to its worker count from the matching heap and add those profits. These pops select precisely the best regular assignments in every group, without mixing incompatible skill levels.

**Delay the flexible choice.** Once every regular skill group has taken its best possible tasks, every heap contains exactly the tasks not assigned to regular workers. The extra worker ignores requirements, so its optimal choice is simply the largest remaining heap root across all groups. This ordering is safe: for any one skill, the regular workers plus a possible extra assignment should receive that group's largest profits; taking the regular prefix first leaves its next-largest profit as the correct candidate for the flexible worker. Choosing the greatest such candidate globally therefore maximizes the complete assignment.

If no task remains, the extra worker stays unused. All profits are positive, so every eligible regular assignment and any available extra assignment can only increase the total.

## Complexity detail

Let $w$ be the number of regular workers, $t$ the number of tasks, and $a$ the number of tasks assigned to regular workers. Counting workers, grouping tasks, heapifying every group, and inspecting the remaining heap roots cost $O(w+t)$. The $a$ heap removals cost at most $O(a\log t)$ in total. Thus the time bound is $O(w+t+a\log t)$, where $a\le\min(w,t)$; this is $O((w+t)\log t)$ in the worst case.

The worker counter and grouped task heaps store $O(w+t)$ values. The algorithm does not create assignment combinations or a worker-by-task matrix.

## Alternatives and edge cases

- **Sort each profit group:** Descending lists make the same greedy choice straightforward, with $O(t\log t+w)$ worst-case time; heaps avoid sorting beyond the assignments actually removed.
- **Sort all tasks globally:** Processing profits from largest to smallest while preserving the extra worker for tasks without an available exact-skill worker is also correct, but sorting every task costs $O(t\log t)$.
- **Scan tasks once per worker:** Repeatedly searching for the best exact match is correct but can take $O(wt)$ time.
- **Use the extra worker first:** Committing the flexible worker before regular assignments can hide which task is truly left over; compute all exact-skill prefixes first.
- **Duplicate worker skills:** Counts, not distinct skill presence, determine how many tasks may be removed from one heap.
- **More workers than matching tasks:** Only the available matching tasks are assigned; unused regular workers contribute nothing.
- **No regular match:** The best unmatched task remains eligible for the extra worker, even when none of its required skill appears in `workers`.
- **All tasks assigned regularly:** No heap remains nonempty, so the extra contribution is zero rather than reusing a task.
- **Several equal profits:** Any tied tasks may be selected; only the maximum total matters.
- **Large values:** The total can exceed 32-bit range, so implementations in fixed-width languages need a 64-bit accumulator.
