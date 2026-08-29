## General

**Exact skill equality separates ordinary workers into independent groups.** A regular worker with skill $q$ can take only a task whose requirement is exactly $q$. Therefore, tasks of one required skill never compete for workers of another skill. The source groups every task profit in dictionary `d` under its required skill.

Each dictionary value is a `SortedList`, which keeps profits in ascending order. Adding all task profits preserves duplicates, which is necessary because two distinct tasks may have the same profit. The largest remaining profit in a group is at index $-1$ and can be removed with `pop()`.

**Give each ordinary worker the most profitable remaining exact match.** The source visits every skill in `workers`. Accessing `d[skill]` yields that group's sorted list; because `d` is a `defaultdict(SortedList)`, a skill with no tasks produces an empty list. In that case the worker is left idle.

When the group is nonempty, the code removes its final and therefore largest profit and adds it to `ans`. Removing the profit ensures no later worker can reuse the same task.

This greedy choice is safe within a skill group. If $c$ workers share that skill and the group has task profits sorted from largest downward, any optimal assignment to those indistinguishable workers uses the largest $\min(c,\text{task count})$ profits. Replacing a chosen smaller profit with an unchosen larger one preserves exact skill compatibility and increases or preserves the total.

All profits are positive, so there is no reason to leave a regular worker idle when a compatible task remains. Worker iteration order within a skill group does not matter because workers of equal skill have identical eligibility.

**Let the additional worker take the best task still available anywhere.** After ordinary assignments, the extra worker ignores skill requirements. The source scans every group in `d.values()`, looks at `ls[-1]` when the group is nonempty, and records the maximum in `mx`. The largest remaining element of each sorted group is its only candidate for the global maximum; scanning smaller elements would be unnecessary.

The extra worker performs at most one task, so `ans += mx` completes the result. If all tasks were consumed, `mx` remains zero and no nonexistent task is assigned.

**Why assigning ordinary workers before choosing the extra task is still optimal.** A natural concern is that an ordinary worker might consume the globally best task, seemingly leaving less for the extra worker. Consider the skill group from which the extra worker is ultimately chosen.

If that group has enough tasks for both its regular assignments and the extra assignment, the combined contribution is the sum of the group's top $c+1$ profits, where $c$ is the number assigned to regular workers. It does not matter whether the largest goes to a regular worker and the next to the extra worker or vice versa; the same top set is used. If the extra worker is chosen from another group, assigning the largest compatible task to each regular worker is plainly best. Thus the regular-first greedy ordering cannot reduce the optimum.

For the first example, skill one contributes $100$, skill two contributes $400$, and one skill-three worker takes one of the two profits $400$ and $100$. Greedy gives that regular worker $400$, leaving $100$ as the best remaining task for the extra worker, for total $1000$. Giving the skill-three worker $100$ and the extra worker $400$ would tie, illustrating the exchange argument.

When no regular skill matches any task, every task remains in its group and `mx` becomes the largest profit overall. The additional worker alone takes it, as in the second example.

**Why the complete result is correct.** Within each exact-skill group, removing the largest profit for each available regular worker maximizes the group's regular contribution. The exchange argument shows this choice remains compatible with the one unrestricted worker. After all regular assignments, any task available to the extra worker lies in one group, and that group's largest remaining profit dominates its other tasks. Taking the maximum of those group maxima is therefore the best possible final assignment.

**The exact data structure differs from the manifest summary.** The manifest describes max-heaps. The protected source uses `SortedList` from the execution environment. Both support repeated maximum extraction, but construction and operation costs differ: tasks are inserted one at a time into maintained sorted containers rather than heapified in linear time.

## Complexity detail

Let $w$ be the number of workers, $t$ the number of tasks, $a$ the number of regular assignments actually made, and $g$ the number of dictionary skill keys.

In the conventional documented model for `SortedList`, each insertion and pop costs approximately $O(\log t)$ in the worst group-size bound. Grouping tasks therefore costs $O(t\log t)$ rather than the manifest's heap-oriented linear grouping term. Worker dictionary checks cost $O(w)$ expected time, and the $a$ successful pops cost $O(a\log t)$. Scanning group maxima costs $O(g)$. A faithful overall bound is

$$
O(t\log t+w+a\log t+g).
$$

Since $g\le t+w$—unmatched worker accesses can create empty defaultdict entries—this can be simplified to $O((t+a)\log t+w)$.

The manifest's $O(w+t+a\log t)$ time corresponds to grouping tasks into heaps with linear total heap construction; it does not precisely describe this source's repeated `SortedList.add` calls.

All task profits are stored once. The defaultdict may also hold one empty container for each distinct unmatched worker skill, so auxiliary space is $O(t+w)$, matching the manifest.

## Alternatives and edge cases

- **Sort one global task list:** Skill equality still requires finding and removing tasks within separate requirement groups, so global order alone is inconvenient.
- **Use a max-heap per skill:** This matches the manifest description and can build groups efficiently, but the protected file uses `SortedList`.
- **Choose the extra worker's task first:** It can still be made correct with careful opportunity-cost accounting, but ordinary-first greedy plus a final leftover maximum is simpler.
- **Assign a smaller task to save the largest for the extra worker:** Within the same skill group this only swaps who receives the top two tasks and does not improve their combined profit.
- **More workers than matching tasks:** Later workers see an empty group and remain idle.
- **More matching tasks than workers:** The unused group maximum remains eligible for the extra worker.
- **No matching ordinary worker:** Those task groups remain untouched and participate in the extra-worker scan.
- **Duplicate profits:** `SortedList` retains every occurrence, so separate equal-profit tasks can be assigned separately.
- **Duplicate worker skills:** Each worker independently pops at most one task from the shared group.
- **All tasks consumed:** `mx` stays zero, correctly adding no extra profit.
- **Positive profits:** Taking every available regular assignment and one leftover extra assignment cannot reduce the total.
- **Defaultdict side effect:** Looking up an unmatched worker skill creates an empty group, increasing dictionary keys but not changing the answer.
- **Input preservation:** Worker and task arrays are read only; profits are copied into grouped containers.
