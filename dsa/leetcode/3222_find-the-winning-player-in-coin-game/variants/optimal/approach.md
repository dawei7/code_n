## General

**Determine the only legal move.** Suppose a turn removes $a$ coins worth `75` and $b$ coins worth `10`. Dividing the required-value equation by $5$ gives

$$
15a+2b=23.
$$

The parity of this equation forces $a$ to be odd. The choice $a=1$ gives $b=4$, while every odd $a\geq3$ already makes $15a>23$. Thus every successful turn consumes exactly one `75` coin and four `10` coins; players have no strategic choice among different moves.

The total number of possible turns is therefore

$$
t=\min\left(x,\left\lfloor\frac{y}{4}\right\rfloor\right).
$$

Alice takes turns $1,3,5,\ldots$, so she wins exactly when $t$ is odd. If $t$ is even, including zero, Bob is the player who cannot be answered after his last move or who wins immediately when Alice cannot start.

## Complexity detail

The formula uses a fixed number of integer arithmetic operations, taking $O(1)$ time and $O(1)$ auxiliary space. Since $x,y\leq100$, the complete legal domain contains only $10{,}000$ ordered pairs and a simulation performs at most $25$ turns. Runtime scaling cannot honestly distinguish the formula on this domain, so the package uses a bounded-domain certificate with exhaustive oracle comparison.

## Alternatives and edge cases

- **Simulate turns:** Repeatedly subtract one from `x` and four from `y`; this is correct but performs up to $25$ iterations instead of evaluating the count directly.
- **Search all coin combinations:** The value equation proves that only `(1, 4)` is possible, so branching is unnecessary.
- If `y < 4`, Alice cannot make even the first move and Bob wins.
- An abundance of one denomination cannot compensate for a shortage of the other.
- When exactly one turn is possible, Alice wins; when exactly two are possible, Bob wins.
- At `x = y = 100`, the `10`-value coins limit the game to $25$ turns, so Alice wins.
