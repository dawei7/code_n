## General

Process transactions from left to right and tentatively keep every amount. Track the sum of the kept subsequence as `balance`, and store its amounts in a min-heap.

If adding the current amount leaves `balance` non-negative, keeping it increases the selected count by one and is always preferable. If the balance becomes negative, at least one selected transaction must be discarded. Remove the smallest amount in the heap—the most negative and therefore most harmful choice. This maximizes the balance retained with one fewer transaction. The removed value is no greater than the just-added amount, so the repaired balance is at least the previously feasible balance and is non-negative.

After each processed prefix, the heap has the maximum feasible cardinality. Among subsequences of that cardinality, its sum is as large as possible: whenever one removal is forced, discarding the minimum maximizes the remaining sum. That larger balance can only make future transactions easier to accept, so the exchange never reduces the best final count. The heap size after the final prefix is therefore the maximum number of transactions that can be performed.

## Complexity detail

Let $n=\lvert\texttt{transactions}\rvert$. Each amount is pushed once and removed at most once; each heap operation costs $O(\log n)$. Total time is $O(n\log n)$, and the heap uses $O(n)$ space in the worst case.

## Alternatives and edge cases

- **Keep every currently affordable transaction:** Permanently skipping the current negative amount can be suboptimal; replacing an earlier, more negative selected amount may preserve more future balance with the same count.
- **Linear search for the worst selected amount:** The same greedy exchange is correct, but finding and removing the minimum from an unsorted list can make the total time $O(n^2)$.
- **Subset dynamic programming:** Tracking attainable balances or counts is infeasible for up to $10^5$ amounts with magnitudes up to $10^9$.
- **All negative amounts:** Each tentative choice is removed immediately, leaving an answer of `0`.
- **Zero amount:** It neither raises nor lowers the balance and can always be included.
- **Early deficit:** A receipt later in the array cannot justify an earlier negative prefix; processing in order enforces this rule.
- **Large cumulative balance:** Sums can exceed 32-bit range, so fixed-width implementations should use a wide integer for `balance`.
