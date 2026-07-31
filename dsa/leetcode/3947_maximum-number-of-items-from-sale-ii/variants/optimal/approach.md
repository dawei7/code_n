## General

**Count the useful copies of every source type.** Let `factor_frequencies[f]` be the number of indexed types whose factor is $f$. For each possible $f$, summing those frequencies at $f,2f,3f,\ldots$ counts all indexed targets whose factors are divisible by $f$. The count includes the source index itself, which cannot be a target, so a type with factor $f$ has

$$
g_i=\sum_{k:\,f\mid k}\texttt{factor_frequencies}[k]-1
$$

eligible ordered pairs. Its first $g_i$ purchased copies can each be matched to a different target and therefore contribute two copies: the purchase and one reward. Every later copy contributes only itself. This turns type $i$ into a batch of $g_i$ marginal purchases of value two, followed by unlimited marginal purchases of value one, all at `price_i`.

**Use the globally cheapest type for ordinary copies.** Let $p_{\min}$ be the smallest price in the catalog. Whenever a purchase has value one, buying it from a type priced at $p_{\min}$ is optimal. A boosted copy priced above $2p_{\min}$ is also unnecessary: two ordinary copies have the same value and cost less. At price exactly $2p_{\min}$ the choices tie, so retaining the boosted copy is safe.

**Buy equal-value boosted units in increasing price order.** Every useful boosted marginal copy has value two. Sorting the types by price therefore orders batches of interchangeable value-two units by cost. For each batch with price at most $2p_{\min}$, buy as many of its $g_i$ units as the remaining budget allows. If the next unit is unaffordable, every later boosted unit is at least as expensive, so no later batch can be used. Spend the final budget on ordinary copies at $p_{\min}$.

For any chosen number of boosted copies, this prefix rule gives the minimum possible boosted cost because it takes the cheapest units. Including another affordable unit priced at most $2p_{\min}$ cannot reduce the result compared with replacing its cost by ordinary copies. After the greedy prefix ends, all remaining useful decisions are ordinary cheapest-price copies. The constructed total is therefore optimal.

## Complexity detail

Let $n=\lvert\texttt{items}\rvert$. Because every factor is at most $n$, the multiples sieve performs

$$
\sum_{f=1}^{n}\left\lfloor\frac{n}{f}\right\rfloor=O(n\log n)
$$

frequency visits. Sorting the $n$ batches also takes $O(n\log n)$ time, and the greedy scan is linear. The total running time is $O(n\log n)$.

The factor-frequency and divisible-count arrays, plus the sorted batch list, use $O(n)$ auxiliary space.

The benchmark tiers contain $32$, $128$, and $512$ equal-factor types. Their recorded size is $n$. The accepted method performs its sieve, sort, and batch scan in the required near-linear class. A correct alternative that compares every ordered pair to count eligible targets takes $O(n^2)$ time and should fail only the scaling verdict.

## Alternatives and edge cases

- **Expand every boosted copy:** Materializing all $\sum_i g_i$ value-two units before sorting can require $O(n^2)$ memory because every ordered pair may be eligible; sorting one batch per type avoids the expansion.
- **Pairwise divisibility counting:** Comparing every source against every target computes the same gains but costs $O(n^2)$ time instead of using the bounded factor domain.
- **Choose boosts by reward ratio:** Every boost has the same value two, so sorting by price is the exact ordering; floating-point ratios add no information.
- **Duplicate factors:** Equal-factor entries are distinct indexed types and divide one another. Each type excludes only its own index, not every entry with the same factor.
- **Repeated target:** Different source types may award the same indexed target, so gains are summed independently and target copies are not globally deduplicated.
- **No eligible target:** A batch with $g_i=0$ contributes no boosted units; copies of that type are useful only if it has the minimum ordinary price.
- **Partially affordable batch:** Buying a prefix of one batch is valid because its eligible targets are interchangeable for the objective; once the next unit is unaffordable, no later batch can be bought.
- **Expensive boosted copy:** A price above $2p_{\min}$ cannot improve the count because two cheapest ordinary copies provide equal value for less money.
- **Unused remainder:** The budget need not be spent completely; a remainder smaller than $p_{\min}$ buys no additional copy.
