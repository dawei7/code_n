## General

**Search a monotone answer**

If every index can be marked within the first $t$ seconds, the same schedule remains valid for every longer prefix: the added seconds may simply do nothing. Feasibility is therefore monotone, so binary search can find the smallest feasible prefix length.

**Reserve the last marking opportunity**

To test a prefix of length $t$, record the last occurrence of every index in `changeIndices[0:t]`. If an index is absent, the prefix is immediately impossible because that index can never be marked.

Suppose an index is marked at an occurrence earlier than its last one. Moving that mark to its last occurrence cannot hurt: the former marking second becomes available for a decrement, and no deadline moves earlier. Consequently, there is always a feasible schedule that marks every index at its last occurrence in the tested prefix.

**Maintain the decrement budget**

Scan the prefix chronologically. Every second that is not the reserved last occurrence of its named index can be used for one arbitrary decrement, so it increases `available_decrements` by one. At a reserved occurrence for index `i`, that second must perform the mark. Before it arrives, at least `nums[i]` earlier free seconds must have been available to reduce this index to zero. If the current budget is smaller, the prefix is infeasible; otherwise consume `nums[i]` units from the budget.

The budget represents interchangeable decrement seconds because a decrement may target any index. Processing reserved deadlines in chronological order ensures that every value charged to the budget can actually be decremented before its mark. If the scan reaches the end, all indices had an eligible last occurrence and enough prior work, so the prefix is feasible. Binary search over this exact predicate returns the earliest feasible second, or `-1` when even the full sequence fails.

## Complexity detail

For one prefix, constructing the last-occurrence array takes $O(n+t)$ time and the chronological scan takes $O(t)$ time. Across $O(\log m)$ binary-search probes, the total time complexity is $O((n+m)\log m)$. The last-occurrence array uses $O(n)$ auxiliary space.

The values in `nums` may be as large as $10^9$, but the algorithm never performs decrements individually; it subtracts each required count from an accumulated budget.

## Alternatives and edge cases

- **Linear prefix search:** Testing seconds `1, 2, \ldots, m` with the same feasibility predicate is correct but can require $O(m(n+m))$ time instead of exploiting monotonicity.
- **Dynamic programming over marked subsets:** A state for every subset is exponential in $n$ and cannot support $n=2000$.
- **Earliest-occurrence marking:** Reserving an index's first occurrence can waste later flexibility and incorrectly reject schedules that need additional time for decrements.
- An index missing from the tested prefix makes that prefix impossible even when its initial value is zero, because a separate marking second is still required.
- A zero value requires no decrement budget, but its reserved occurrence must still be spent on marking.
- Multiple values compete for the same pool of free seconds; checking only each value against its own deadline independently would double-count those seconds.
- Decrementing a value and marking it cannot happen in the same second because only one operation is allowed.
- The answer may occur before the end of `changeIndices`; unused suffix seconds do not affect the earliest result.
- Very large values are handled without simulation. If their total required work cannot fit before the reserved deadlines, the budget check rejects the prefix directly.
