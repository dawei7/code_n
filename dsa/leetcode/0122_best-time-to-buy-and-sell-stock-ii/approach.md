## General

Unlike the one-transaction version, this problem allows any number of transactions while holding at most one share. That freedom means every upward movement in price can contribute to profit.

The selected solution sums each positive difference between consecutive days. `pairwise(prices)` yields adjacent prices `(a, b)`, and `max(0, b - a)` keeps the rise while discarding a flat or falling step.

**Why a long profitable transaction decomposes**

Suppose one transaction buys on day $i$ and sells on later day $j$. Its profit is

$$
\texttt{prices}[j]-\texttt{prices}[i].
$$

Insert and cancel every intermediate price:

$$
\texttt{prices}[j]-\texttt{prices}[i]
=
\sum_{k=i}^{j-1}
\bigl(\texttt{prices}[k+1]-\texttt{prices}[k]\bigr).
$$

This telescoping identity says holding across several days earns exactly the sum of the daily changes along that interval.

If every change in an interval is positive, collecting each rise separately gives the same profit as one buy at the beginning and one sale at the end. For prices `[1, 2, 3, 4, 5]`, four adjacent profits of one sum to four, identical to `5 - 1`.

**Why negative daily changes should be excluded**

If a held interval includes a negative daily difference, selling before that fall and buying again afterward avoids the loss. Transactions are unlimited, and the contract permits selling and buying on the same day, so splitting positions around turns is valid while never holding more than one share.

Flat differences add nothing and can be included or omitted without affecting profit.

Therefore an optimal strategy never needs to absorb a negative daily change. It can collect every positive one and skip every nonpositive one.

**An upper bound for every possible strategy**

Any valid strategy consists of disjoint chronological holding intervals. Each interval's profit decomposes into its adjacent daily differences.

The strategy can include only some daily differences, and including a negative one reduces its total. Even if it includes every positive difference, it cannot exceed:

$$
\sum_{k=0}^{n-2}
\max\bigl(0,\texttt{prices}[k+1]-\texttt{prices}[k]\bigr).
$$

So the selected sum is an upper bound on every valid strategy.

**Why the upper bound is achievable**

For each positive adjacent difference, buy on its first day and sell on its second day. If another positive difference begins immediately, the contract permits selling and buying on their shared day.

Alternatively, merge consecutive positive steps into one transaction from the beginning of an increasing run to its end. Telescoping shows the merged profit is the same.

Thus a legal strategy realizes every term in the sum. Because the sum is both an upper bound and achievable, it is the maximum profit.

**Tracing the first example**

For `[7, 1, 5, 3, 6, 4]`, adjacent differences are `-6`, `4`, `-2`, `3`, and `-2`.

The source contributes zero, four, zero, three, and zero. Their total is seven. This corresponds to buying at one and selling at five, then buying at three and selling at six.

The falling days separate the profitable holding intervals. Carrying stock through either fall would reduce the result.

**Why no explicit holding state is necessary**

The transaction rules contain no fee, cooldown, transaction limit, or other coupling between profitable rises. Therefore accepting one rise cannot make another rise unavailable, except for sharing a day—which the contract explicitly allows.

If any such restriction were introduced, positive-difference summation could fail and a state-machine dynamic program would be needed. Under this exact contract, the local contributions are independent.

**Generator behavior and dependencies**

The expression inside `sum` is a generator, so it does not allocate a list of all adjacent differences. It produces one contribution at a time.

The source uses `List[int]` and `pairwise` without importing them. A standalone file needs `from typing import List` and `from itertools import pairwise`. `pairwise` is available in Python 3.10 and newer.

For one price, `pairwise` yields nothing and `sum` returns zero, which is correct.

## Complexity detail

Let $n$ be the number of prices. `pairwise` yields $n-1$ adjacent pairs, and each generator step performs constant work. Time is $O(n)$.

The generator, `pairwise` iterator, and running sum retain only constant state, so auxiliary space is $O(1)$. No array of differences is materialized.

The returned integer uses constant output space, and the input is never modified.

Every price except possibly one endpoint participates in adjacent comparisons. In the worst case, the final difference affects the answer, so a linear inspection is necessary.

## Alternatives and edge cases

- **Explicit index loop:** Add `max(0, prices[i + 1] - prices[i])` for every adjacent pair. It avoids `pairwise` and has identical bounds.
- **Peak-and-valley transactions:** Find each local valley, then sell at the following local peak. It produces the same profit but requires more control flow.
- **Two-state dynamic programming:** Track best cash while holding or not holding a share. It generalizes to fees and cooldowns but is unnecessary here.
- **One-transaction minimum-price scan:** Incorrect for this problem because it discards profit from later independent rises.
- **One price:** No transaction is possible, and the empty sum is zero.
- **Strict decrease:** Every contribution is zero, so no stock is bought.
- **Strict increase:** All daily gains telescope to last price minus first price.
- **Flat days:** Difference zero neither helps nor hurts.
- **Alternating rises and falls:** Each rise is captured and every fall is skipped.
- **Same-day handoff:** Selling one transaction and buying the next on a shared day preserves the at-most-one-share condition.
- **Price zero:** A following rise is collected normally.
- **Unlimited transactions:** Essential to the greedy independence argument.
- **No fees or cooldown:** Either restriction would invalidate simple summation.
- **Missing imports:** `List` and `pairwise` must be supplied.
- **Python version:** Use `zip(prices, prices[1:])` or an index loop when `itertools.pairwise` is unavailable.
