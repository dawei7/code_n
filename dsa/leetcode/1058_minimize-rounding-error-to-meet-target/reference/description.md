## Description

Given an array of `prices` `[p_1,p_2...,p_n]` and a `target`, round each price $p_{i}$ to $\text{Round}_{i}(p_{i})$ so that the rounded array `[Round_1(p_1),Round_2(p_2)...,Round_n(p_n)]` sums to the given `target`. Each operation $\text{Round}_{i}(p_{i})$ could be either $Floor(p_{i})$ or $Ceil(p_{i})$.

Return the string `"-1"` if the rounded array is impossible to sum to `target`. Otherwise, return the smallest rounding error, which is defined as $Σ |\text{Round}_{i}(p_{i}) - (p_{i})|$ for <italic>`i`</italic> from `1` to <italic>`n`</italic>, as a string with three places after the decimal.
### Function Contract

**Inputs**

- `prices`: a nonempty array of decimal strings, each containing exactly three fractional digits.
- `target`: the required integer sum of all rounded prices.

Every price must be rounded independently to either its floor or its ceiling. Let $N=\lvert\texttt{prices}\rvert$, and let $K=1000$ be the number of thousandths in one unit.

**Return value**

- The minimum total absolute rounding error, formatted as a string with exactly three decimal places, or `"-1"` when no permitted choices sum to `target`.

### Examples
#### Example 1

- **Input:** $prices = ["0.700","2.800","4.900"], target = 8$
- **Output:** `"1.000"`
- **Explanation:**
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .
#### Example 2

- **Input:** $prices = ["1.500","2.500","3.500"], target = 10$
- **Output:** `"-1"`
- **Explanation:** It is impossible to meet the target.
#### Example 3

- **Input:** $prices = ["1.500","2.500","3.500"], target = 9$
- **Output:** `"1.500"`
### Constraints

- $1 \le \text{prices.length} \le 500$

- Each string $\text{prices}[i]$ represents a real number in the range `[0.0, 1000.0]` and has exactly 3 decimal places.

- $0 \le target \le 10^{6}$