## General
**Track exact members but cap profit at the threshold**

Let `dp[used][earned]` count subsets of the crimes processed so far that use exactly `used` members. The profit coordinate records the exact total only below $P$; index $P$ represents every total of at least $P$. Initialize `dp[0][0] = 1` for the empty subset.

For a crime requiring `members` and producing `gain`, extend each state that still fits within `n`. Its destination is `used + members` and `min(P, earned + gain)`. Iterate `used` downward so a state created by the current crime cannot select that same crime again. Iterating the profit coordinate downward gives the same one-use protection within each member row and keeps the update conventional.

**Each subset follows one unique transition path**

For every processed crime, a subset either omits it and stays in its existing state or includes it and moves through exactly one update from the corresponding smaller subset. Thus no subset is lost or counted twice. Capping profit is safe because once a subset reaches $P$, only its member usage matters for all future feasibility. After all crimes, summing `dp[used][P]` over every allowed `used` counts precisely the profitable schemes.

## Complexity detail
For each of the $m$ crimes, the algorithm scans at most $n+1$ member counts and $P+1$ capped profit states. Total time is $O(mn(P+1))$. The table contains $(n+1)(P+1)$ counters, so auxiliary space is $O(n(P+1))$.

## Alternatives and edge cases
- **Enumerate all crime subsets:** Direct inclusion/exclusion is correct but takes $O(2^m)$ time.
- **Three-dimensional dynamic programming:** Adding a crime-index dimension makes the recurrence explicit but increases space to $O(mn(P+1))$.
- **Track uncapped total profit:** This preserves correctness but wastes states above the only threshold that affects the answer.
- **Zero minimum profit:** The empty subset is a valid scheme, as are any other subsets that satisfy the member limit.
- **Crime too large for the group:** It cannot be selected, but all states that omit it remain unchanged.
- **Zero-profit crime:** It can still double some scheme counts when enough members are available because selecting it creates a distinct subset.
- **Identical crime data:** Crimes remain distinct by index, so subsets choosing different equal-looking crimes are counted separately.
- **Modulo updates:** Apply the modulus while accumulating counts so fixed-width implementations do not overflow.
