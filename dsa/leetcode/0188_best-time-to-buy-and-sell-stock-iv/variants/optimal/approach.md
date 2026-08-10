## General

**Model decisions by the resources that still matter**

On each day, a strategy may do nothing, buy if it holds no stock, or sell if it
currently holds one stock. The future value of earlier history depends only on
three facts: the current day, how many transaction opportunities remain, and
whether a stock is currently held. Exact earlier buy and sell dates no longer
matter once their profit effect has been accumulated.

The memoized function `dfs(i, j, k)` represents the greatest additional profit
available from day `i` onward. Here `j` is the number of buys still available,
and the inner parameter named `k` is actually a holding flag: zero means no
stock is held and one means a stock is held. This inner name shadows the outer
method parameter `k`, which is legal Python but unnecessarily confusing. A name
such as `holding` would express the state more clearly.

The initial call `dfs(0, k, 0)` starts before day zero with all transaction
opportunities available and no stock in hand.

**Why counting at the buy is valid**

The code decrements `j` when buying rather than when selling. Every completed
transaction has exactly one buy followed by one sell, and the state forbids a
second buy while already holding. Reserving a transaction at its buy therefore
limits the strategy to at most the original `k` buys and hence at most `k`
completed transactions.

It is possible for a branch to buy and reach the end without selling. Because
all prices are nonnegative, that branch has paid a nonnegative amount and gains
nothing at the base case, so it cannot improve over skipping that buy. Thus the
final maximum still corresponds to completed profitable transactions even
though the recursion does not explicitly mark an unfinished holding state as
impossible.

**Always include the choice to wait**

The first candidate is `dfs(i + 1, j, k)`: take no action on day `i` and carry
the same resources into the next day. This choice is essential. A local price
may be unattractive, and “at most” `k` transactions means the algorithm must be
free to use fewer than `k`, including none.

Waiting also handles equal prices and declining markets naturally. The search
is never forced into a zero-profit or losing trade merely to consume the
transaction limit.

**Sell only when holding**

If the holding flag is one, the method may sell on day `i`. Selling receives
`prices[i]`, changes the holding flag to zero, and leaves `j` unchanged because
the transaction slot was already consumed at the corresponding buy. The
candidate is:

`prices[i] + dfs(i + 1, j, 0)`

The method takes the maximum between this action and waiting. It cannot buy in
the same state, so two stocks can never be held simultaneously.

**Buy only when empty and a slot remains**

If the holding flag is zero and `j` is positive, the method may buy. Buying pays
the current price, represented by the negative contribution `-prices[i]`,
decrements the remaining buy count, and sets the holding flag to one:

`-prices[i] + dfs(i + 1, j - 1, 1)`

The next recursive call begins on day `i + 1`, so the same day cannot contain a
sell followed by another buy. This respects the rule that a position must be
closed before another transaction begins.

When `j` is zero and no stock is held, buying is unavailable; waiting is the
only meaningful action. When `j` is zero but a stock is held, selling remains
available because its buy already used a slot.

**Terminate after the final day**

When `i >= len(prices)`, no market action remains and the function returns zero
additional profit. This value is exact for an empty position. For a held
position it means the earlier purchase cost remains in the accumulated path,
so, with nonnegative prices, abandoning the stock is never better than the
alternative that skipped its purchase.

The recursion also handles a one-day array: it may skip, or buy and finish with
a nonpositive result. The maximum is zero because no later selling day exists.

**Trace the second example**

For prices `[3,2,6,5,0,3]` with two slots, the search can wait past 3, buy at 2,
sell at 6, wait past 5, buy at 0, and sell at 3. The signed contributions are
`-2 + 6 - 0 + 3 = 7`.

Branches such as buying at 3 or selling at 5 are also explored, but memoization
and maximization discard them when they reach a state with a smaller achievable
balance. The result does not depend on greedily identifying these days in
advance.

**Why the recurrence covers every legal strategy**

Consider any state `(i, j, holding)`. Every legal strategy makes exactly one of
the actions represented by the recurrence on day `i`: wait; sell if holding;
or buy if empty with a remaining slot. There is no fourth legal action because
multiple simultaneous holdings and same-day action chains are excluded.

After the chosen action, the recursive state records precisely the resources
available for later days. Assuming recursive results are optimal for later
states, adding today's cash change gives the best strategy beginning with that
action. Taking the maximum over all legal first actions therefore gives the
best strategy for the current state. The base case is correct after the last
day, so this reasoning applies backward to the initial state.

**Memoize overlapping states**

Many different action histories reach the same `(i, j, holding)` state. Once
there, they have identical future choices. `@cache` stores the computed result
so each state is solved once instead of expanding an exponential decision tree.

There are at most $n(k+1)2$ such states. This is the central dynamic-programming
idea: retain the best future value for each resource configuration and discard
the irrelevant path details.

**Exact source and runtime caveats**

The file uses `List` and `cache` without importing them. A standalone Python
module needs `from typing import List` and `from functools import cache` unless
the harness supplies those names.

The recursion can also reach depth $n$. With the allowed length near 1000,
Python's default recursion limit may be reached depending on the harness and
call-stack overhead. An iterative DP avoids that execution risk.

## Complexity detail

There are $O(nk)$ combinations of day and remaining-transaction count and two
holding states. Each cached state performs constant work besides its cached
calls, so time is $O(nk)$.

The cache stores $O(nk)$ results, and recursion uses up to $O(n)$ stack frames.
Therefore the exact source uses $O(nk)$ auxiliary space, not the manifest's
$O(k)$ space. The $O(k)$ bound belongs to an iterative state-compressed DP that
keeps only transaction states for the current day; this memoized implementation
does not perform that compression.

## Alternatives and edge cases

- **Compressed iterative DP:** Maintain best holding and not-holding balances for each transaction count, achieving $O(nk)$ time and $O(k)$ space without recursion.
- **Unlimited-transactions shortcut:** When $k \ge \lfloor n/2 \rfloor$, sum every positive adjacent rise because the transaction limit cannot bind.
- **Full three-dimensional DP:** Store every day explicitly; easier to tabulate but uses $O(nk)$ space like the cache.
- **Greedy valley/peak decomposition:** The competitive primary method builds marginal profits and selects the largest ones; faster on average but much harder to derive and verify.
- **No profitable increase:** Waiting throughout returns zero.
- **One day:** Buying cannot be followed by a sale, so profit is zero.
- **Zero prices:** Buying at zero is allowed and the signed transition remains valid.
- **Very large `k`:** The memoized state space can be much larger than needed unless the unlimited shortcut is added.
- **Unfinished final holding:** Nonnegative prices ensure it cannot improve the answer, but an explicit negative-infinity base would make the state contract stricter.
- **Missing imports and recursion depth:** Both must be addressed in a standalone Python 3 runtime.
