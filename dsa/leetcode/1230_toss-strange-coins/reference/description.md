## Description

You have some coins.  The `i`-th coin has a probability $\text{prob}[i]$ of facing heads when tossed.

Return the probability that the number of coins facing heads equals `target` if you toss every coin exactly once.
### Function Contract

**Inputs**

- `prob`: The head probability for each coin.
- `target`: The exact number of heads requested.

Let $n = \lvert\texttt{prob}\rvert$ and $t = \texttt{target}$. Every coin is tossed exactly once, and each toss follows the probability assigned to that coin. Values of `0` and `1` represent deterministic tails and heads respectively.

**Return value**

Return the probability that exactly $t$ of the $n$ coins land heads. Floating-point answers within `10^-5` of the correct probability are accepted.

### Examples
#### Example 1

- **Input:** $prob = [0.4], target = 1$
- **Output:** `0.40000`
#### Example 2

- **Input:** $prob = [0.5,0.5,0.5,0.5,0.5], target = 0$
- **Output:** `0.03125`
### Constraints

- $1 \le \text{prob.length} \le 1000$

- $0 \le \text{prob}[i] \le 1$

- $0 \le target$<= prob.length`

- Answers will be accepted as correct if they are within $10^{-5}$ of the correct answer.