## General

**Separate odd and even row costs**

Fix one color as the top-row color. It supplies rows $1,3,5,\ldots$, while the other color supplies rows $2,4,6,\ldots$. Filling the first $k$ odd-numbered rows costs

$$
1+3+\cdots+(2k-1)=k^2
$$

balls of the starting color. Filling the first $k$ even-numbered rows costs

$$
2+4+\cdots+2k=k(k+1)
$$

balls of the other color.

**Invert the two sums exactly**

If `first` is the starting-color supply, it can fund

$$
o=\left\lfloor\sqrt{\texttt{first}}\right\rfloor
$$

odd rows. If `second` is the other supply, the largest affordable even-row count is

$$
e=\left\lfloor\frac{\sqrt{1+4\texttt{second}}-1}{2}\right\rfloor.
$$

Integer square root evaluates both bounds without floating-point rounding.

An alternating triangle beginning with `first` can contain at most the same number of odd and even rows, or one additional odd row. Its height is therefore

$$
\min(2o,\,2e+1).
$$

The first term limits how many paired rows the starting color can support; the second limits the paired rows plus a possible final odd row. Every height up to their minimum is constructible because the closed-form sums are monotone and within both supplies. Evaluate this expression once with red first and once with blue first, then take the larger result. These are the only two possible color sequences, so the maximum is optimal.

## Complexity detail

The algorithm performs four bounded integer-square-root evaluations and a fixed number of arithmetic operations, giving $O(1)$ time and $O(1)$ auxiliary space over the legal input domain.

Because each color count is capped at $100$, the complete source domain has only $10{,}000$ ordered input pairs. Runtime scaling cannot honestly distinguish this formula from the short row-by-row simulation, so the package uses a verified bounded-domain certificate and an exhaustive oracle regression instead of benchmark tiers.

## Alternatives and edge cases

- **Simulate both starting colors:** Subtract each successive row size until a color cannot fill its row. This is correct and simple, but takes $O(\sqrt{\texttt{red}+\texttt{blue}})$ iterations instead of using the row-sum inverses directly.
- **Binary search the height:** The feasibility inequalities are monotone, so binary search works, but closed-form inversion removes the search.
- **Check only one starting color:** This can miss the optimum because the larger pile may need either the odd or even row sizes depending on the counts.
- **Unused balls:** A valid maximum need not consume either pile completely.
- **Equal supplies:** Both starting choices have the same attainable height by symmetry.
- **One scarce color:** A large surplus cannot bypass alternation; the scarce color still limits every other row.
- **Odd final row:** The starting color may supply one more row than the other color, which is why the bound is $2e+1$ rather than $2e$.
- **Exact square boundaries:** Integer square root handles supplies such as $9$ or $16$ without floating-point error.
