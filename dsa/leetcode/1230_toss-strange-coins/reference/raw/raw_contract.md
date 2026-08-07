## Function Contract

**Inputs**

- `prob`: The head probability for each coin.
- `target`: The exact number of heads requested.

Let $n = \lvert\texttt{prob}\rvert$ and $t = \texttt{target}$. Every coin is tossed exactly once, and each toss follows the probability assigned to that coin. Values of `0` and `1` represent deterministic tails and heads respectively.

**Return value**

Return the probability that exactly $t$ of the $n$ coins land heads. Floating-point answers within `10^-5` of the correct probability are accepted.
