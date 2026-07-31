## General

Let $M=N^2$, let $a$ be the repeated value, and let $b$ be the missing value.
Compared with the complete sequence from $1$ through $M$, the grid's ordinary
sum differs by

$$
\Delta=a-b.
$$

The sum of squares differs by

$$
\Delta_2=a^2-b^2=(a-b)(a+b)=\Delta(a+b).
$$

Scan the grid once to obtain both observed sums, and compute their expected
counterparts from the closed-form formulas. The contract guarantees
$a\ne b$, so $\Delta$ is nonzero and $a+b=\Delta_2/\Delta$. Solving the two
linear equations gives

$$
a=\frac{\Delta+(a+b)}{2},\qquad b=(a+b)-a.
$$

These equations uniquely recover the repeated and missing values, which are
returned in the required order.

## Complexity detail

Let $N$ be the grid dimension. Visiting all $N^2$ cells takes $O(N^2)$ time.
Only a fixed collection of integer totals is stored, so auxiliary space is
$O(1)$.

## Alternatives and edge cases

- **Frequency array:** Counting every value directly is straightforward and takes $O(N^2)$ time but also $O(N^2)$ space.
- **Search the grid for every candidate:** Counting each integer from $1$ through $N^2$ with a fresh full scan is correct but takes $O(N^4)$ time.
- **XOR partitioning:** XOR can separate the two exceptional values in constant space, but an additional membership check is needed to label repeated versus missing.
- **Smallest or largest exception:** The equations do not depend on either value being internal to the range.
- **Arbitrary cell order:** Only aggregate sums matter, so shuffling grid positions does not change the result.
- **Integer arithmetic:** Under the guaranteed structure, both divisions are exact; no floating-point computation is needed.
