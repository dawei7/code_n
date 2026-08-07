## Function Contract

**Inputs**

- `prices`: a nonempty array of decimal strings, each containing exactly three fractional digits.
- `target`: the required integer sum of all rounded prices.

Every price must be rounded independently to either its floor or its ceiling. Let $N=\lvert\texttt{prices}\rvert$, and let $K=1000$ be the number of thousandths in one unit.

**Return value**

- The minimum total absolute rounding error, formatted as a string with exactly three decimal places, or `"-1"` when no permitted choices sum to `target`.
