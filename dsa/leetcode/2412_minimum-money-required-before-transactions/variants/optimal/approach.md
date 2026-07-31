## General

**Separate permanent losses from temporary affordability.** A transaction with `cost > cashback` permanently reduces the balance by `cost - cashback`; every ordering eventually incurs that loss. Define

$$
L = \sum_i \max(0, \texttt{cost}_i-\texttt{cashback}_i).
$$

After reserving $L$, one extra amount must make whichever transaction becomes the final bottleneck affordable. For a losing transaction, its own loss is still inside the unspent part of $L$ before it runs, so the extra amount needed is its cashback. For a non-losing transaction, no future loss reserve helps meet its cost, so the extra amount is its cost. Both cases equal $\min(\texttt{cost},\texttt{cashback})$.

**One maximum covers every order.** Let $B$ be the maximum of those per-transaction bottlenecks and start with $L+B$. Before any losing transaction, the reserve for all unperformed losses includes its own `cost - cashback`, while $B$ covers at least its cashback; together they cover its cost. Before any non-losing transaction, prior losses can consume at most $L$, leaving at least $B$, which covers its cost.

This amount is also necessary. An adversarial order can perform all other losing transactions before a chosen transaction. If the chosen transaction loses money, affordability then requires $L+\texttt{cashback}$ initially; if it does not lose money, it requires $L+\texttt{cost}$. Choosing the transaction with bottleneck $B$ proves the lower bound $L+B$.

## Complexity detail

Two linear reductions compute $L$ and $B$, taking $O(n)$ time. Only scalar accumulators are retained, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort and simulate candidate orders:** Sorting can construct demanding orders, but the aggregate loss-and-bottleneck formula makes ordering unnecessary.
- **Recompute total loss per candidate:** Testing every possible final bottleneck while rescanning all transactions is correct but costs $O(n^2)$ time.
- **All non-losing transactions:** Then $L=0$, and the answer is simply the largest cost.
- **All losing transactions:** Their losses accumulate, while the largest cashback supplies the final bottleneck.
- **Zero-cost transaction:** It never creates an affordability requirement.
- **Large total:** The answer can exceed 32-bit range even though each individual value does not.
