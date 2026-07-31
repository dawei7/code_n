## General

**Turn nearest-ten rounding into integer arithmetic**

For a nonnegative integer, adding $5$ moves every upward-rounding remainder into the next block of ten. Integer division by $10$ then selects the rounded block:

$$
q = \left\lfloor \frac{\texttt{purchaseAmount}+5}{10} \right\rfloor.
$$

Multiplying $q$ by $10$ restores the rounded dollar amount. Remainders from $0$ through $4$ stay in their original block, while remainders from $5$ through $9$ move into the next one. In particular, the added $5$ makes every exact half-way value round upward as required.

Subtract the rounded purchase from the initial $100$ dollars. The constraints guarantee the result is between $0$ and $100$, inclusive. This direct formula covers zero, exact multiples of ten, and the upper boundary without special cases.

## Complexity detail

The method executes a fixed number of integer operations regardless of `purchaseAmount`, so its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.

The legal domain contains only the $101$ integers from $0$ through $100$, which cannot support honest asymptotic runtime scaling. A bounded-domain certificate instead verifies the constant operation count and compares every legal input with an independent rounding oracle.

## Alternatives and edge cases

- **Inspect the last digit:** Compare `purchaseAmount % 10` with `5`, then add or subtract the appropriate remainder. This is correct but needs a branch and more bookkeeping.
- **Search nearby multiples of ten:** Testing candidate multiples works within the small domain but obscures the simple arithmetic rule.
- Zero is already a valid multiple of ten, so a zero-dollar purchase leaves the full balance.
- Remainders below $5$ round down; a remainder of exactly $5$ rounds upward rather than toward an even multiple.
- An amount already divisible by $10$ remains unchanged.
- Prices from $95$ through $100$ round to $100$, leaving a zero balance.
