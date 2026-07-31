## General

Reverse the order of counting. Fix an unordered pair of distinct grid cells. Every arrangement containing both cells is completed by choosing the other $k-2$ occupied cells from the remaining $N-2$ cells, so this pair contributes its distance exactly

$$
\binom{N-2}{k-2}
$$

times. This multiplier is identical for every cell pair. It remains to find the sum of Manhattan distances over all unordered pairs of cells.

Manhattan distance separates into independent row and column differences. For a row gap $d$, there are $m-d$ unordered row pairs with that gap and $n^2$ choices of columns for their cells. Thus the total row contribution is

$$
n^2\sum_{d=1}^{m-1} d(m-d)
=n^2\frac{m(m^2-1)}{6}.
$$

By symmetry, the column contribution is

$$
m^2\frac{n(n^2-1)}{6}.
$$

Add these two quantities, then multiply by the common binomial coefficient modulo $10^9+7$. Compute the binomial coefficient using the shorter of $r=k-2$ and $N-2-r$, accumulating one numerator product and one factorial denominator. Fermat's little theorem supplies the denominator's modular inverse.

## Complexity detail

Let $N=mn$ and $r=\min(k-2,N-k)$. The closed-form distance calculation is constant time. The binomial product takes $O(r)$ time, which is $O(N)$ in the worst case, plus $O(\log M)$ time for modular exponentiation with the fixed modulus $M=10^9+7$. Only a constant number of integers are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every cell pair:** This applies the same combinatorial multiplier correctly but costs $O(N^2)$ time and is too slow for $N=10^5$.
- **Enumerate arrangements:** There may be $\binom{N}{k}$ arrangements, making direct generation infeasible even on much smaller grids.
- **Factorial table:** Precomputing factorials and inverse factorials also evaluates the binomial coefficient in $O(N)$ time but consumes $O(N)$ space.
- **Exactly two pieces:** The multiplier is $\binom{N-2}{0}=1$, so the answer is simply the sum over all cell pairs.
- **Every cell occupied:** The multiplier is again $1$ because each cell pair belongs to the sole full-grid arrangement.
- **One-dimensional grids:** One of the two closed-form contributions becomes zero without requiring a special case.
- **Modular division:** The division by `6` is performed on the exact integer formulas before reduction; the binomial denominator uses a modular inverse.
