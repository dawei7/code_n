## General

**Classify every book into one fee band.** Each book's fee depends only on its own number of late days, so no ordering or cross-book state is needed. Scan the array once and classify every delay into the contract's three disjoint ranges.

For a delay of exactly 1, add 1. Otherwise, a delay at most 5 lies in the inclusive range from 2 through 5, so add twice the delay. Every remaining delay is at least 6, and therefore contributes three times the delay. Because these branches cover every legal positive input exactly once, the accumulated sum contains precisely the fee of every book.

**Respect the one-day exception.** The check for the one-day case must come first: treating it with the general multiplier for the next range would incorrectly charge 2. After excluding it, `days <= 5` describes exactly the second range and the final branch describes exactly the third.

## Complexity detail

Let $n = \lvert\texttt{daysLate}\rvert$. The scan performs constant work for each of the $n$ books, giving $O(n)$ time. Apart from the running total and current value, it creates no storage that grows with the input, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Precomputed fee table:** A table for all legal delays from 1 through 100 would permit constant-time lookups, but it still requires an $O(n)$ scan and adds unnecessary fixed storage.
- **One day late:** This special case contributes exactly 1, not twice the delay.
- **Five days late:** The upper endpoint remains in the middle range and contributes 10.
- **Six days late:** This is the first value in the highest range and contributes 18.
- **Repeated delays:** Every array position represents a separate book, so equal delays must each contribute their full fee.
