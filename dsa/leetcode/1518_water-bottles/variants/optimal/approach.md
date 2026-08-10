## General

**What one exchange-and-drink cycle changes**

The source begins with `ans = numBottles` because every initially full bottle can certainly be drunk. After those drinks, the same number of empty bottles exists.

Whenever at least `numExchange` bottles are available for exchange, spending that many empties obtains one full bottle. Drinking that new bottle adds one to the answer and returns one empty bottle.

The net number of available bottles therefore decreases by

$$
numExchange - 1.
$$

That is exactly why each loop executes

`numBottles -= numExchange - 1`

and `ans += 1`.

Although the variable is still named `numBottles`, after initialization it is best understood as the current number of bottles available in the exchange cycle, effectively empties after all currently counted full bottles have been drunk.

**Why the loop condition is correct**

An exchange is possible exactly when the current bottle count is at least `numExchange`. If fewer remain, no combination of waiting or rearranging can create another full bottle, because no new empty bottle appears without first obtaining and drinking a full one.

The loop stops at that point, and `ans` already includes every full bottle ever drunk.

The guarantee `numExchange >= 2` ensures each iteration reduces `numBottles` by at least one. The process must terminate. If the exchange cost were one, every empty could be exchanged for a full bottle that produces another empty, creating an infinite process.

**A trace for nine bottles and exchange cost three**

Initially, `ans = 9` and nine empty bottles remain conceptually.

- Exchange three and drink the result: the usable count drops by two to seven, and answer becomes ten.
- Repeat until the counts move from seven to five, then three, then one.
- Four extra bottles have been drunk, so the result is thirteen.

This per-bottle loop differs from batching all possible simultaneous exchanges, but both simulate the same conservation rule.

**Why greedily exchanging whenever possible is optimal**

Empty bottles have no value except as inputs to an exchange. Performing an available exchange cannot reduce future drinking opportunities: it consumes `numExchange` empties, produces one drink, and returns one empty. Delaying the exchange leaves the same resources and gains nothing.

Every extra full bottle necessarily requires one such exchange. The loop performs exchanges until none is possible, so no strategy can drink more.

**Deriving the closed form**

Each additional drink permanently consumes `numExchange - 1` bottles from the reusable pool. However, at least one bottle must remain as the final nonexchangeable remainder. Starting with $B$ bottles, the number of extra drinks is

$$
\left\lfloor\frac{B-1}{E-1}\right\rfloor,
$$

where $E$ is the exchange cost. The total is initial $B$ plus that quotient.

The stored source does not use this formula. It carries out one iteration per extra drink.

The minus one in the numerator is essential. One final empty bottle cannot be permanently consumed by an exchange chain, because each exchanged full bottle returns an empty after drinking. Treating all initial bottles as freely divisible by the net cost would overcount some boundary cases.

**Exact complexity versus the manifest**

The Optimal manifest labels the method constant time, which describes the closed-form arithmetic solution. The exact while loop has a number of iterations proportional to the extra bottles obtained and is not constant with respect to the input magnitude.

With the small bound of one hundred initial bottles, it is fast in practice, but bounded constraints should not be confused with the algorithm's general asymptotic control flow.

## Complexity detail

Let $B$ be the initial full-bottle count and $E$ the exchange requirement. Every iteration decreases the current count by $E-1$. The number of iterations is

$$
\left\lfloor\frac{B-1}{E-1}\right\rfloor.
$$

Exact time is therefore $O(B/(E-1))$, which is $O(B)$ in the worst case $E=2$. The manifest's $O(1)$ time belongs to the closed formula rather than the stored simulation.

Only `ans` and the mutated scalar parameters are stored, so auxiliary space is $O(1)$.

Integer arithmetic is exact. The source mutates only its local integer bindings, not external objects.

## Alternatives and edge cases

- **Closed-form calculation:** Return `B + (B - 1) // (E - 1)`. This achieves the manifest's true $O(1)$ time and $O(1)$ space.
- **Batch exchanges:** Compute quotient and remainder of current empties to process many exchanges at once. It takes logarithmic-like rounds and is easy to simulate explicitly.
- **Drink one full bottle at a time:** It is correct but performs more state updates than the net-change loop.
- **Fewer bottles than exchange cost:** The loop never runs, and the answer is the initial bottle count.
- **Exact exchange threshold:** One exchange produces exactly one additional drink and leaves one empty.
- **Exchange cost two:** Every extra drink reduces the pool by one, producing the most loop iterations.
- **One initial bottle:** No exchange is possible under the valid minimum cost two.
- **Exchange cost one:** It would imply infinitely many drinks, which is why the contract excludes it.
- **Unused final empties:** They cannot contribute to another exchange and correctly add no drinks.
- **At most maximum consumption:** There is no strategic reason to skip an available exchange.
