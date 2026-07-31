## General

**Turn the ordinary schedule into a baseline**

Without using the assignment operation, index `i` needs `nums[i]` decrement seconds and one additional marking second. The complete baseline therefore requires

$$
B = \sum_{i=1}^{n} \texttt{nums[i]} + n
$$

operations.

If an assignment is used for an index with value $v$, choosing zero is always optimal: no other non-negative value makes the later mark easier. The index then needs one assignment and one mark instead of $v$ decrements and one mark. Its saving is $v-1$, so values zero or one never provide a positive benefit.

**Binary-search a monotone prefix**

A schedule that finishes within $t$ seconds also finishes within every longer prefix by ignoring the added seconds. Feasibility is monotone, allowing binary search for the earliest successful prefix.

For a fixed prefix, an index that will be reset should use its first occurrence. Moving the reset earlier only creates more possible seconds for its separate later mark. Compute that first occurrence for every index in the prefix.

**Select compatible resets from right to left**

Scan the prefix backward. `free_seconds` counts later seconds not committed to a selected reset or its required mark. A non-first occurrence, or the first occurrence of a value at most one, becomes another free second.

At the first occurrence of a value $v>1$, tentatively select its reset and push $v$ into a min-priority queue. This choice saves $v-1$ operations but needs one later free second for the mark. Consume such a second when one exists.

If none exists, all tentative resets cannot coexist. Discard the smallest value in the heap because it contributes the least saving. Removing that reset also releases the scheduling capacity associated with its set-and-mark pair, leaving one free second after the remaining commitments are honored. The min-heap performs this exchange while retaining the maximum total saving among schedulable choices seen so far.

After the reverse scan, let $S$ be the sum of `value - 1` over the retained resets. Their assignments and marks, together with the ordinary work for every other index, require exactly $B-S$ operations. The prefix is feasible precisely when $B-S \le t$. This greedy predicate is exact, and binary search returns the smallest prefix satisfying it.

## Complexity detail

For a prefix, building first occurrences takes $O(n+t)$ time. The reverse scan performs at most one heap push and pop per second, for $O(t\log n)$ time. Across $O(\log m)$ binary-search probes, the total time complexity is $O((n+m\log n)\log m)$. The occurrence array and heap use $O(n)$ auxiliary space.

The baseline and savings can reach well beyond 32-bit range because each value may be $10^9$; their sums require a wide integer representation.

## Alternatives and edge cases

- **Linear prefix search:** Applying the same heap predicate to every prefix is correct but grows to $O(m(n+m\log n))$ rather than using monotonicity.
- **Always reset at the first occurrence:** Some resets have too little saving or leave no later marking slot; selecting all of them can make a feasible ordinary schedule appear impossible.
- **Choose resets by value alone:** Sorting the largest values ignores whether each assignment has a distinct later second available for its mark.
- **Dynamic programming over reset subsets:** Explicitly tracking selected indices is exponential and cannot support $n=5000$.
- An assignment may choose any non-negative value, but zero dominates every positive choice when the objective is to enable marking.
- Setting a value to zero and marking its index require two different seconds because only one operation may be performed per second.
- The marking operation is not restricted by `changeIndices[s]`; any currently zero index may be marked.
- Initially zero values still require one marking second, but they need no decrement or assignment.
- Resetting a value of one replaces one decrement with one assignment and saves nothing, so it is never necessary.
- Repeated occurrences matter as possible free work or marking seconds; only the first occurrence is useful for an optimal reset.
- If fewer than $n$ seconds are available, completion is impossible because every index needs its own mark.
