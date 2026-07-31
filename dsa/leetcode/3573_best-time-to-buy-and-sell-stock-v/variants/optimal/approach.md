## General

After any processed day, the future only needs to know how many transactions have been completed and whether no transaction, a normal transaction, or a short sale is currently open. For every completed count $t$, maintain three best profits:

- `flat[t]`: no open position after exactly $t$ completed transactions;
- `long[t]`: a normal transaction is open after exactly $t$ completions, including the cost of its purchase;
- `short[t]`: a short sale is open after exactly $t$ completions, including the proceeds from its initial sale.

Initially only `flat[0] = 0` is reachable. At price `p`, a flat state may stay flat, open a long position by subtracting `p`, or open a short position by adding `p`. An open long may remain open or close by adding `p`; an open short may remain open or close by subtracting `p`. Closing advances the completed count by one.

Every day's transitions read exclusively from the previous day's arrays and write to fresh copies. This detail enforces the rule that a closing day cannot also open the next transaction: a state closed today does not become an opening source until tomorrow.

The states retain the greatest profit for every possible future-relevant situation. Each legal schedule follows one of the listed transitions day by day, while every transition constructs a legal partial schedule. Taking the largest final `flat` value therefore considers every schedule of at most `k` completed transactions and excludes unfinished positions.

## Complexity detail

Let $n$ be the number of days. Each day updates three constant-time transitions for each of the $k$ transaction counts, giving $O(nk)$ time. The current and next state arrays contain $O(k)$ entries, so auxiliary space is $O(k)$.

The benchmark sets $k=S/8$ while the price-array length is $S$. The accepted state DP therefore scales as $O(S^2)$. The calibrated alternative enumerates every possible opening day when closing each transaction, requiring $O(kS^2)=O(S^3)$ time.

## Alternatives and edge cases

- **Interval-enumerating dynamic programming:** Trying every earlier opening day for every closing day and transaction count is correct, but costs $O(kn^2)$ time.
- **Unlimited-transactions greedy reasoning:** Summing adjacent price changes is not valid under a finite `k`, and it can also accidentally reuse a closing day to open another transaction.
- **In-place state updates:** Reading a state that was written on the current day can illegally close one transaction and open the next on that same day; use previous-day snapshots.
- **Short-sale sign:** Opening a short position adds the current price, while buying back subtracts the later price.
- **Unfinished positions:** An open long or short at the end is not a completed transaction and cannot contribute to the answer.
- **At most `k`:** Return the best value over every `flat[t]`; using all available transactions is never mandatory.
- **Large prices:** Total profit can exceed a 32-bit signed integer, so fixed-width implementations need a 64-bit type.
