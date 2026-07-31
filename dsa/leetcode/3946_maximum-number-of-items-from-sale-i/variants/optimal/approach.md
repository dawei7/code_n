## General

**Turn divisibility rewards into one value per type.** Build `frequencies[f]`, the number of indexed types whose factor is $f$. For every possible factor $f$, sum the frequencies at $f,2f,3f,\ldots$ to obtain `divisible_counts[f]`: the number of indexed targets with factors divisible by $f$.

For a particular type $i$, this count includes type $i$ itself. Activating $i$ does not award a free self-copy, so its free bonus is `divisible_counts[factor_i] - 1`. The first purchased copy contributes one purchased item as well, making the complete first-copy value exactly `divisible_counts[factor_i]`. Every later copy of the same type has value one.

**Combine activation and repetition in one capacity DP.** Let `dp[c]` be the greatest number of copies obtainable with capacity at most $c$ after the processed types. Before processing one type, save `previous = dp[:]`. Scan capacities upward from its price $p$ and consider three possibilities:

- leave the type unused, retaining the current value;
- buy its first copy, using `previous[c - p] + first_value`;
- buy one additional copy, using `dp[c - p] + 1`.

The first-copy transition reads from the snapshot, so it activates the type at most once. The additional-copy transition reads the current row in ascending capacity order, so it may repeat the type any number of times. If that transition happens to extend a state that has not activated the current type, the first-copy transition from the same prior state is at least as valuable and dominates it. Thus no invalid purchase can determine the maximum.

After a type is processed, every legal quantity of that type has been combined with every optimum over earlier types. Induction over the catalog therefore establishes that `dp[budget]` is the maximum attainable purchased-plus-free total. Because each activation bonus already counts every eligible indexed target, duplicate factors and repeatedly awarded targets require no special handling in the DP.

## Complexity detail

Let $n=\lvert\texttt{items}\rvert$, $B=\texttt{budget}$, and $F=\max_i\texttt{factor_i}$. The multiples sieve performs

$$
\sum_{f=1}^{F}\left\lfloor\frac{F}{f}\right\rfloor=O(F\log F)
$$

frequency visits. Processing each of the $n$ types scans at most $B$ capacities, giving $O(nB)$ DP work. The total running time is $O(F\log F+nB)$.

The factor-frequency arrays use $O(F)$ space. The current DP row and its snapshot use $O(B)$ space, for $O(F+B)$ auxiliary space overall.

The benchmark tiers set $n=B$ to $16$, $24$, and $48$, while all types have factor and price one. The recorded size is the governing product $nB$: $256$, $576$, and $2304$. The accepted-class transition stays linear in that authored workload. A correct alternative that enumerates every possible quantity for every type and capacity takes $O(nB^2)$ time and therefore exhibits an additional square-root growth factor when $n$ and $B$ scale together.

## Alternatives and edge cases

- **Explicit quantity enumeration:** Trying every affordable copy count from the previous DP row is correct, but costs $O(nB^2)$ when prices are small.
- **Separate activated-state table:** Tracking inactive and active states for the current type makes the first-versus-later distinction explicit, but the snapshot and ascending transitions encode the same states with less storage.
- **Quadratic reward counting:** Comparing every ordered pair of types computes all bonuses in $O(n^2)$ time; the bounded factor domain supports the faster multiples sieve.
- **Duplicate factors:** Equal-factor types are distinct indices. Activating one awards a free copy of every other equal-factor type, because equal positive factors divide one another.
- **Repeated free target:** A target may be counted once for each different activated source type; rewards are not deduplicated by target.
- **Unaffordable type:** When its price exceeds the budget, it has no transition and remains skipped.
- **Additional copies:** Only the first purchased copy receives the activation value; every later copy adds exactly one purchased item.
- **Unused budget:** The DP represents cost at most each capacity, so spending the full budget is never required.
