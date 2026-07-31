## General

Each index progresses through three states: it has seen no greater value, it has seen exactly one, or its answer is known. Maintain `waiting_first` for the first state and `waiting_second` for the second.

Both stacks keep candidate values in non-increasing order from bottom to top. When a new `value` arrives, first pop every smaller index from `waiting_second`; the current value is the next strictly greater value after the one that moved each index into this stack, so it is exactly that index's answer.

Next, pop smaller indices from `waiting_first`. The current value is their first greater value, so they must move to `waiting_second`. The first stack pops them in reverse order; reversing that popped batch before appending preserves the second stack's non-increasing value order. Finally, push the current index onto `waiting_first`.

An index enters `waiting_second` precisely when its first greater position is processed. It can leave only at the first later value strictly greater than its own, which is therefore its second greater position. Strict comparisons correctly ignore equal values. Indices left in either stack have seen fewer than two greater values and retain `-1`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each index is pushed onto `waiting_first`, moved at most once to `waiting_second`, and popped at most once when answered. The total number of stack operations is $O(n)$, so time is $O(n)$.

The answer and stacks contain $O(n)$ entries, giving $O(n)$ auxiliary space under the repository's reference-solution accounting.

## Alternatives and edge cases

- **Scan right from every index:** Counting later greater values directly is simple and correct but takes $O(n^2)$ time.
- **Ordered set or heap:** Values waiting for their first or second event can be managed in $O(n\log n)$ time with more complex bookkeeping.
- **Sort indices by value:** Activating positions in value order with an ordered index structure also costs $O(n\log n)$.
- **Equal values:** They never trigger either transition because the definition requires strictly greater values.
- **Decreasing array:** No index leaves the first stack, so every answer is `-1`.
- **Increasing array:** Every index except the last two receives the value two positions to its right.
- **Zeros and duplicates:** Non-negative bounds and repeated values do not alter the stack invariants.
- **Transfer order:** Appending the popped first-stack batch without reversing it breaks the monotonic order and can assign later answers incorrectly.
