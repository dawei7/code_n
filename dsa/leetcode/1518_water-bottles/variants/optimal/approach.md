## General
**Measure the net empty-bottle cost**

The initial bottles contribute `numBottles` drinks immediately. Consider each additional bottle obtained through an exchange. Paying `numExchange` empties and then drinking the received bottle gives one empty back, so the lasting decrease in the empty-bottle supply is only `numExchange - 1`.

One empty bottle must remain unavailable for spending after the final drink: if every empty could be consumed in net-cost groups, there would be no bottle representing that last drink. Therefore at most `numBottles - 1` initial empties can fund these net decreases. The number of extra drinks is

$$
\left\lfloor\frac{\texttt{numBottles}-1}{\texttt{numExchange}-1}\right\rfloor.
$$

Adding the initial drinks gives the returned closed form.

**Why the bound is attainable**

Every time at least `numExchange` empties exist, exchanging them cannot reduce the eventual total: it creates one drink and returns an empty afterward. Repeating this action spends exactly `numExchange - 1` net empties per added drink until fewer than `numExchange` remain.

The floor expression counts precisely how many such net reductions fit while preserving the final empty bottle. Thus it is both an upper bound and the total achieved by greedy exchange, proving the formula maximal.

## Complexity detail
The implementation performs a fixed number of subtractions, one integer division, and one addition, so its running time and auxiliary space are both $O(1)$.

The complete legal input space contains only $100 \cdot 99 = 9900$ pairs. Because those source bounds provide no honest asymptotic scaling dimension, a strict `bounded_domain` certificate replaces runtime tiers and exhaustively compares the formula with direct simulation.

## Alternatives and edge cases
- **Round-by-round simulation:** repeatedly use `divmod` on the empty count. It is straightforward and correct but performs multiple iterations instead of using the invariant directly.
- **Exchange one bottle at a time:** subtracting `numExchange`, adding one empty after drinking, and repeating is also correct but does avoidable work.
- **Exchange rate two:** each extra drink loses only one net empty, producing `2 * numBottles - 1` total drinks.
- **Threshold above the initial count:** no exchange is possible, and the formula's quotient is zero.
- **Exact threshold:** when the initial count equals `numExchange`, exactly one additional bottle can be consumed.
- **Leftover empties:** any remainder below the threshold is unusable and must not be rounded up.
