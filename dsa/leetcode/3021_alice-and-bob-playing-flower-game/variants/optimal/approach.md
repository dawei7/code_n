## General

**Only the total number of flowers matters.** Every legal turn removes exactly
one flower. No choice can change the number of turns, so a game with lane sizes
$x$ and $y$ always lasts exactly $x+y$ moves. Alice takes the odd-numbered
moves; therefore she removes the final flower exactly when $x+y$ is odd.

**Count opposite parities.** An odd sum requires one lane size to be odd and
the other even. Among the first $n$ positive integers there are
$\lceil n/2\rceil$ odd and $\lfloor n/2\rfloor$ even choices, with analogous
counts for $m$. Thus the answer is

$$
\left\lceil\frac n2\right\rceil\left\lfloor\frac m2\right\rfloor+
\left\lfloor\frac n2\right\rfloor\left\lceil\frac m2\right\rceil
=\left\lfloor\frac{nm}{2}\right\rfloor.
$$

The final form directly yields the result with one multiplication and integer
division.

## Complexity detail

The calculation performs a fixed number of arithmetic operations, using
$O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every pair:** Checking the parity of all $nm$ games is correct but costs $O(nm)$ time.
- **Keep the two parity products:** The unsimplified odd-even count is equally correct but requires more arithmetic.
- **Both bounds odd:** Exactly one of the $nm$ pairs is left unmatched by the parity split, so integer division rounds down.
- **A bound equals one:** Only the even choices under the other bound produce an odd total.
- **Maximum bounds:** The product can reach $10^{10}$, so fixed-width implementations need a 64-bit result type.
