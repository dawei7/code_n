## General
**Only useful change denominations need counters**

A `$5` payment requires no change and increases the number of `$5` bills. A `$10` payment requires exactly one earlier `$5`; consume it and retain the new `$10`. A `$20` payment requires `$15`, which can be made either as one `$10` plus one `$5`, or as three `$5` bills. Received `$20` bills can never help make `$5` or `$15` change later, so they do not need to be counted.

**Preserve the more flexible `$5` bills**

For a `$20` payment, use one `$10` and one `$5` whenever possible. The alternative consumes three `$5` bills. Replacing `$10 + $5` with three `$5` bills saves a `$10` but spends two additional `$5` bills. A future `$10` customer can only be served by a `$5`, and every way to change `$20` also needs at least one `$5`; the saved `$10` cannot replace either missing `$5`. Therefore the preferred choice can never reduce the set of future queues that remain serviceable.

Process customers in order with counters for `$5` and `$10`. Before accepting each larger bill, verify that the preferred change combination exists, falling back to three `$5` bills for a `$20` only when no `$10` is available. If neither combination exists, no rearrangement of earlier transactions can help, so return `false`. If the scan finishes, every transaction has been completed and the answer is `true`.

## Complexity detail
Each of the $n$ bills causes a constant number of counter checks and updates, giving $O(n)$ time. The algorithm stores only two integer counters, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Store every bill in a wallet list:** Searching for and removing change is correct with the same greedy policy, but repeated linear scans can make the total cost $O(n^2)$.
- **Backtracking over change choices:** It explores unnecessary branches; spending `$10 + $5` first is always at least as safe for future customers.
- **Spend three `$5` bills first:** This can reject a later `$10` customer even when the greedy preference would serve the entire queue.
- **First bill is `$10` or `$20`:** No change is available, so the result is immediately `false`.
- **Only `$5` bills:** Every customer pays exactly the price and the answer is `true`.
- **Queue order:** Later cash cannot be borrowed to repair an earlier failed transaction.
- **`$20` bills in the register:** They are retained but never contribute to a required `$5` or `$15` change amount.
