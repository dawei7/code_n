## General

**Drink the initial bottles immediately.** The source initializes `ans = numBottles`. This counts every initially full bottle as drunk. Delaying a drink cannot create any advantage: drinking changes a full bottle into an empty one, and empty bottles are the only resource required for exchanges. Making those empties available as early as possible can only help.

After this initialization, the variable still named `numBottles` should be interpreted as the current number of empty bottles. The code reuses the parameter rather than introducing an `empty` variable. This change of meaning is important when reading the loop.

**One loop iteration is one exchange-and-drink cycle.** An exchange is possible exactly when:

`numBottles >= numExchange`.

The source then performs four state changes in order:

1. `numBottles -= numExchange` spends the required empties;
2. `numExchange += 1` raises the price for the next exchange;
3. `ans += 1` counts the new full bottle as drunk;
4. `numBottles += 1` adds the empty bottle produced by that drink.

If the old exchange price was $e$, the net change in empty bottles is $-e+1=-(e-1)$. The price then becomes $e+1$. The separate subtraction and addition mirror the physical actions, while the net view helps with the complexity analysis.

**Why one exchange at a time matches the rule.** The task explicitly forbids exchanging several batches at the same price. After every single exchange, `numExchange` must increase. The loop performs exactly one exchange before incrementing the price, so it cannot accidentally buy multiple bottles using an outdated rate.

**Why the greedy simulation is optimal.** Whenever enough empties exist, making the exchange increases the answer by one. It does not remove any alternative that could yield more bottles later, because every future exchange must eventually pay the current price before the price can advance. There is no way to spend empties on anything else, lower the price, or obtain new empties without drinking an exchanged bottle.

Suppose the algorithm stops because current empties are less than the current price. No full bottle remains: every initial or exchanged bottle has already been counted as drunk. Without another full bottle, no new empty can appear. Without enough empties, no exchange can occur. The state is terminal, so no omitted strategy can drink another bottle.

These two observations prove optimality: taking an affordable exchange is always productive and safe, and failing the affordability test makes all further progress impossible.

**A trace for 10 bottles and exchange price 3.** The method first drinks all 10, so `ans=10` and there are 10 empties.

- Spend 3, drink the new bottle, and receive its empty: empties become 8, price becomes 4, answer becomes 11.
- Spend 4 and receive one back: empties become 5, price becomes 5, answer becomes 12.
- Spend 5 and receive one back: empties become 1, price becomes 6, answer becomes 13.

One empty is less than the next price six, so the result is 13.

**The price-one case is still finite.** If the initial price is one, the first exchange spends one empty and drinking the result returns one empty, so the empty count does not decrease. However, the price rises to two. Later exchanges have positive net empty cost, and the process terminates. The mandatory price increase prevents an infinite free cycle.

**Why drinking “any number” at once causes no extra choices.** The operation wording permits drinking any number of full bottles, not necessarily all. Yet all full bottles are interchangeable and each produces exactly one empty. Drinking fewer only postpones access to a resource and never improves an exchange price. Thus the source can treat every acquired bottle as drunk immediately.

**State meaning after each iteration.** At the loop condition:

- `ans` is the total number of bottles already drunk;
- `numBottles` is the number of empties currently available;
- `numExchange` is the exact price of the next single exchange.

The body preserves this invariant. The condition is therefore both necessary and sufficient for another legal cycle.

## Complexity detail

Let $B$ be the initial number of bottles and $E$ the initial exchange price. If the loop performs $t$ exchanges, the net empty reductions are:

$$
(E-1), E, (E+1), \ldots, (E+t-2).
$$

Their sum is:

$$
t(E-1)+\frac{t(t-1)}2.
$$

This sum cannot exceed the finite supply created from the initial bottles. The quadratic term implies $t=O(\sqrt B)$ in the worst case. Each iteration does constant work, so the source's time complexity is $O(\sqrt B)$.

Only the answer, current empty count, and current price are stored. Auxiliary space is $O(1)$. The simulation does not allocate an array of bottles.

With the stated limit `numBottles <= 100`, even the direct loop is tiny. The asymptotic derivation explains why it scales well beyond that bound.

## Alternatives and edge cases

- **Quadratic formula:** Solve for the maximum exchange count $t$ from the arithmetic-series inequality and return `B + t`. It can be $O(1)$ but requires careful integer rounding.
- **Batch exchange at one price:** It violates the rule because the price must rise after each individual exchange.
- **Track full and empty separately:** This mirrors the story more literally but adds state without changing the greedy logic.
- **Initial price exceeds bottle count:** No exchange is affordable, so the answer is exactly the initial number of bottles.
- **Initial price equals bottle count:** Exactly one exchange is affordable; after drinking it, only one empty remains.
- **Initial price one:** The first exchange has zero net empty cost, but the price increase makes later progress finite.
- **Drink all immediately:** This is safe because empties are useful and full bottles have no other function.
- **Returned bottle's empty:** The final `numBottles += 1` is essential; omitting it undercounts future exchange resources.
- **Price timing:** The new bottle was bought at the old price, and only the next exchange uses the incremented price.
- **Loop termination:** Once empties are below the next price and no full bottle remains, the state can never change.
- **Maximum, not minimum:** Every affordable exchange adds one drink, so stopping early cannot be optimal.
- **Variable reuse:** Inside the loop, `numBottles` represents empties rather than full bottles despite its original name.
- **No overflow:** Python integers are unbounded; fixed-width implementations should evaluate the arithmetic-series formula carefully if used.
- **Constraint minimums:** At least one initial full bottle exists, so `ans` starts positive.
- **Source versus editorial math:** The checked-in Optimal source is the simulation approach, and its $O(\sqrt B)$ manifest bound matches the exact loop.
