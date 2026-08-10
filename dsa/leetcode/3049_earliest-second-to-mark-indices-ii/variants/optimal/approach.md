## General

**Start with the cost when no fast reset is used.** Index $i$ with value `nums[i]` can always be prepared by that many decrement operations and then marked in one operation. Across all indices, the baseline number of operations is

$$
B=\sum_i\texttt{nums}[i]+N.
$$

The special operation at a scheduled occurrence may set its indicated index directly to zero. Using one reset replaces `nums[i]` individual decrements with one reset second, saving

$$
\texttt{nums}[i]-1
$$

operations. Values zero or one provide no positive saving, so the exact source never selects their resets.

**Binary-search the earliest feasible prefix.** Feasibility is monotone: a schedule that finishes in $t$ seconds also finishes by any later prefix. The outer loop performs ordinary binary search and calls `can_finish(middle)`.

**Choose the earliest reset opportunity per index.** For a tested prefix, the first reversed loop fills `first_occurrence`. Although it scans from right to left, it assigns on every encounter; the last assignment made is the smallest second, so each entry becomes the earliest occurrence in the prefix.

An earliest reset leaves the most later time for marking and other work. A later reset of the same index never gives more saving and has a tighter scheduling deadline, so only the earliest occurrence is a useful candidate.

**Scan backward to enforce a later mark slot.** A reset makes an index zero, but marking it requires a separate second after the reset. Scanning from the deadline backward makes this precedence easy to enforce.

`free_seconds` counts later seconds not committed as resets and therefore available to serve as marks or ordinary work. Every noncandidate second—duplicate occurrence, or an occurrence for value at most one—adds one free second.

At an eligible earliest occurrence with value $v>1$, the algorithm tentatively selects its reset:

- push $v$ into a min-heap;
- add $v-1$ to `saved_operations`;
- if a later free second exists, consume one to pair with this reset's eventual mark.

**Repair over-selection with a min-heap.** If no later free second exists, all tentatively selected resets cannot be scheduled: there are more resets than available later mark slots. The algorithm removes one selected reset with the smallest value. Since its benefit is $v-1$, smallest $v$ means smallest lost saving.

Removing that reset turns its occurrence second back into a free ordinary-operation slot, so `free_seconds` increases by one. The heap maintains the maximum total savings among reset selections compatible with the backward scheduling constraint.

**Why local removal of the smallest saving is optimal.** At any backward prefix, selected resets all consume the same kind of resource: one reset second and one later mark slot. When capacity is exceeded, retaining the candidates with largest savings maximizes the reduction from baseline. A min-heap removes exactly the least valuable candidate, the standard greedy rule for equal-weight choices under a capacity constraint.

**Final feasibility equation.** After scanning, `saved_operations` is the maximum schedulable reduction from baseline within this deadline. The remaining number of operations required is

`baseline_operations - saved_operations`.

If it is at most `seconds`, the prefix has enough time. The selected resets already satisfy reset-before-mark precedence by the backward invariant; the remaining free slots can host baseline decrements and marks.

**Why ordinary marks need no specific `changeIndices` occurrence.** Version II permits marking any index whose value is zero at any second. Only the reset operation is tied to `changeIndices[s]`. This is why free seconds after a selected reset can serve its mark regardless of which index appears in the schedule then.

**A conceptual example.** Suppose two reset candidates save 9 and 2 operations, but only one later marking slot is available. Keeping the saving-9 reset and returning the other occurrence to ordinary work gives a better schedule. The min-heap makes exactly that choice.

**What the heap values mean.** The heap stores original values rather than savings, but ordering is identical because $v-1$ increases with $v$. When a value is removed, the source subtracts `removed - 1` from total savings.

## Complexity detail

Let $N$ be the number of indices and $M$ schedule length. For a deadline $t$, initializing `first_occurrence` costs $O(N)$, finding earliest occurrences costs $O(t)$, and the backward scan costs $O(t\log N)$ in the worst case because at most one reset per index is in the heap. Thus a check costs $O(N+t\log N)$.

Binary search performs $O(\log M)$ checks, giving

$$
O((N+M\log N)\log M)
$$

time. `first_occurrence` and the heap each use $O(N)$ space, so auxiliary space is $O(N)$. Inputs are not modified.

## Alternatives and edge cases

- **Use only baseline decrements:** It is always a valid fallback when enough seconds exist but may miss major savings from resetting large values.
- **Select every positive reset:** Each reset needs a later mark second; selecting too many can make the schedule impossible.
- **Choose latest occurrences:** Earlier resets dominate because they leave at least as much time afterward for marking.
- **Sort all savings globally:** Timing constraints vary by occurrence; the backward heap enforces capacity at every suffix, not merely in total.
- **Value zero:** Resetting saves $-1$ relative to no decrements and is never useful; it still needs a mark.
- **Value one:** A reset replaces one decrement with one reset, saving zero, so ignoring it is safe.
- **No occurrence for an index:** Version II can still decrement and mark that index because only resets depend on `changeIndices`.
- **No later free second:** One tentative reset must be discarded; removing the smallest saving is optimal.
- **More deadline time:** Feasibility cannot become false, justifying binary search.
- **Impossible by $M$:** The outer search leaves `answer=-1`.
- **Heap size:** At most one earliest reset candidate per index is considered, keeping space linear in $N$.
