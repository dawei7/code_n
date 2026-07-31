## General

The complete range has the arithmetic-series sum

$$
T = \frac{n(n+1)}{2}.
$$

Let $q=\lfloor n/m\rfloor$. Exactly $q$ values in the range are divisible by `m`: $m,2m,\ldots,qm$. Their sum is

$$
D = m\frac{q(q+1)}{2}.
$$

The non-divisible group therefore sums to $T-D$, while the divisible group sums to $D$. Subtracting the second group from the first gives

$$
(T-D)-D = T-2D = \frac{n(n+1)}{2}-mq(q+1).
$$

Computing this expression with integer arithmetic produces the requested signed difference directly. The partition is exhaustive and disjoint, and the formula subtracts every divisible value twice from the total: once to remove it from the positive group and once to place it in the negative group.

## Complexity detail

The method performs a fixed number of arithmetic operations regardless of `n` or `m`, so it takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Direct enumeration:** Adding or subtracting each integer according to `value % m` is straightforward and correct, but takes $O(n)$ time.
- **Separate group loops:** Building the two sums independently duplicates work and still requires linear time unless both sums are expressed algebraically.
- **Divisor above the range:** When $m>n$, $q=0$, so the divisible sum vanishes and the answer is the sum of the full range.
- **Divisor equal to one:** Every value belongs to the divisible group, making the answer the negative triangular sum.
- **Inclusive upper endpoint:** When `n` is itself divisible by `m`, floor division includes it among the $q$ multiples.
- **Exact integer arithmetic:** All divisions in the formulas are exact for integer inputs; integer floor division avoids floating-point rounding.
