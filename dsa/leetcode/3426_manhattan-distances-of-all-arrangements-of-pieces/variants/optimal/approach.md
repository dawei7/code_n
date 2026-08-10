## General

**Reverse the order of counting.** Directly enumerate arrangements, then every pair of pieces inside each arrangement, would be enormous. Instead, fix an unordered pair of grid cells first and ask how many arrangements contain pieces in both cells.

Let

$$
N=mn
$$

be the number of cells. Once two distinct cells are fixed as occupied, the remaining $k-2$ identical pieces may occupy any $k-2$ cells among the other $N-2$. Therefore, every cell pair appears together in exactly

$$
\binom{N-2}{k-2}
$$

arrangements.

This multiplicity is identical for every pair. The required answer is consequently

$$
\left(\sum_{\{u,v\}}\operatorname{dist}(u,v)\right)
\binom{N-2}{k-2},
$$

where the sum is over all unordered pairs of distinct grid cells.

**Separate Manhattan distance into row and column contributions.** For cells $(r_1,c_1)$ and $(r_2,c_2)$,

$$
\operatorname{dist}
=
\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert.
$$

The total over cell pairs can be calculated independently for the two coordinates.

Consider two different rows separated by distance $d$. There are $m-d$ unordered row pairs with that separation. For each row pair, the column of the first cell and the column of the second cell may be chosen independently in $n^2$ ways. Thus the total row-distance contribution is

$$
n^2\sum_{d=1}^{m-1}d(m-d).
$$

The standard sum simplifies to

$$
\sum_{d=1}^{m-1}d(m-d)
=\frac{m(m^2-1)}6.
$$

The source therefore computes

`row_distance = n * n * m * (m * m - 1) // 6`.

By symmetry, column separation contributes

$$
m^2\frac{n(n^2-1)}6,
$$

which is `column_distance`. Their sum is the total Manhattan distance over every unordered pair of cells.

For a $2\times2$ grid, the four horizontal/vertical neighbor pairs contribute $4$, and the two diagonal pairs contribute $4$, giving `pair_distance = 8`. With $k=2$, each cell pair occurs in $\binom20=1$ arrangement, so the final answer is $8$.

**Compute the arrangement multiplicity modulo a prime.** Set `available = cells - 2` and `chosen = k - 2`. The needed binomial coefficient is $\binom{\textit{available}}{\textit{chosen}}$.

The identity

$$
\binom ab=\binom a{a-b}
$$

allows the source to replace `chosen` by `min(chosen, available - chosen)`, reducing the number of loop iterations.

It builds the numerator product

$$
(a-b+1)(a-b+2)\cdots a
$$

and denominator $b!$ modulo

$$
P=10^9+7.
$$

Division modulo $P$ is multiplication by an inverse. Because $P$ is prime and `available < P` under the constraints, `denominator` is nonzero modulo $P$. Fermat's little theorem gives

$$
\textit{denominator}^{-1}
\equiv
\textit{denominator}^{P-2}\pmod P.
$$

Python's three-argument `pow` computes this inverse efficiently. Multiplying `pair_distance` by `arrangements` and reducing modulo $P$ produces the requested result.

**Why there is no overcounting.** An arrangement contains $\binom k2$ unordered piece pairs. In the reversed count, each such pair corresponds to one unique pair of occupied cells. That cell pair's distance is included once in `pair_distance` and the arrangement is one of the $\binom{N-2}{k-2}$ completions. Hence every within-arrangement piece pair contributes exactly once.

Pieces are identical, so choosing the $k$ occupied cells completely determines an arrangement. No factorial ordering factor should be added.

The formulas use exact integer division by six before the modulo. The polynomial products are always divisible by six, so no modular inverse of six is needed at that step. Python integers also prevent overflow during these intermediate calculations.

## Complexity detail

Let $b=\min(k-2,N-k)$. The two distance formulas take $O(1)$ arithmetic operations. The multiplicative binomial loop runs $b$ times, and modular inversion takes $O(\log P)$ multiplications. Exact time is $O(b+\log P)$, which is $O(N)$ because $b\le N$ and $N=mn$. This supports the manifest's broader $O(N)$ bound.

Only a fixed number of integer variables are stored regardless of grid size. The binomial coefficient is computed incrementally without factorial arrays, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate arrangements:** There are $\binom Nk$ of them, making direct generation infeasible even at the stated $N\le10^5$.
- **Enumerate all cell pairs explicitly:** This takes $O(N^2)$ time. Separating row and column distances gives closed forms.
- **Precompute factorials:** Factorial and inverse-factorial arrays answer combinations in $O(1)$ after $O(N)$ preprocessing but require $O(N)$ space. One binomial query does not need them.
- **Exactly two pieces:** `chosen = 0`, both products remain one, and the answer is simply the sum of distances over all cell pairs.
- **Every cell occupied:** The multiplicity is $\binom{N-2}{N-2}=1$; there is only one arrangement.
- **One row:** `row_distance` becomes zero and the column formula alone gives all distances.
- **One column:** The symmetric column contribution is zero and row distance remains.
- **Identical pieces:** Occupied cell subsets, not permutations of labeled pieces, are the valid arrangements.
- **Unordered pairs:** The distance formulas count each pair once. Multiplying by two would incorrectly treat the two piece orders as different.
- **Modular division:** Ordinary integer division of residues is invalid. Fermat inversion is safe because the denominator contains factors only below the prime modulus.
