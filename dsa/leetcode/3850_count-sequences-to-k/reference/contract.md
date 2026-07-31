## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, processed once in its given left-to-right order.
- `k`: The positive integer that the final exact rational value must equal.

Every index contributes one of three distinct choices: multiplication, division, or no change. Two sequences are distinct when they choose different actions at any index, even if those actions happen to produce the same value, as multiplication and division by `1` do.

Let $N=\lvert\texttt{nums}\rvert$. Represent a reachable rational value by its signed exponents of the only possible prime factors $2$, $3$, and $5$. Let $S$ be the maximum number of distinct exponent triples reachable after any processed prefix.

**Return value**

Return the number of distinct length-$N$ action sequences whose final rational value is exactly `k`.
