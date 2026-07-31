## General

**Separate the unknown start from fixed offsets**

Temporarily set the first hidden value to zero. Applying `differences` produces
a sequence of prefix offsets beginning with zero. If the true first value is
$x$, every hidden value is $x$ plus its corresponding offset.

**Keep only the extreme offsets**

Scan the differences while maintaining the running offset and its minimum and
maximum values, $p_{\min}$ and $p_{\max}$. Every shifted value lies within the
bounds exactly when

$$
\texttt{lower} \leq x+p_{\min}
\quad\text{and}\quad
x+p_{\max} \leq \texttt{upper}.
$$

Thus valid integer starts form the inclusive interval
`[lower - p_min, upper - p_max]`. Its size is
`upper - lower - (p_max - p_min) + 1` when nonnegative, and zero otherwise.
Every start in that interval generates one unique valid sequence, while any
start outside it violates a bound at an extreme offset.

## Complexity detail

Let $n$ be the length of `differences`. One scan performs $O(n)$ time. Only the
running offset and two extremes are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Materialize every prefix offset:** Storing the full offset sequence is
  correct but uses $O(n)$ unnecessary space.
- **Recompute each prefix sum:** Summing `differences[:i]` for every endpoint
  repeats work and takes $O(n^2)$ time.
- The initial zero offset must participate in both extrema.
- Negative differences can make the minimum offset constrain the starting
  value more strongly than the maximum does.
- If the offset span exceeds `upper - lower`, no sequence is possible.
- Inclusive bounds contribute the final `+1` when counting valid starts.
