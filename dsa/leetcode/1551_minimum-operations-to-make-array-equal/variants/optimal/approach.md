## General
**Identify the only possible final value**

The sum of the first $n$ positive odd numbers is $n^2$, so their average is $n$. Because every operation transfers one unit without changing the sum, all elements must finish at value $n$.

**Count the unavoidable deficit below the average**

Each operation can supply one missing unit to a value below $n$, and the same operation removes one surplus unit from a value above $n$. The total deficit therefore is both a lower bound on the operation count and achievable by pairing deficits with surpluses.

If $n=2k$, the deficits form the odd sequence $2k-1, 2k-3, \ldots, 1$, whose sum is $k^2$. If $n=2k+1$, the middle element already equals $n$, and the deficits are $2k, 2k-2, \ldots, 2$, summing to $k(k+1)$. Both cases equal

$$
\left\lfloor \frac{n^2}{4} \right\rfloor.
$$

Integer division computes this expression directly as `n * n // 4`.

## Complexity detail
The algorithm performs a fixed number of integer arithmetic operations independent of $n$, so it takes $O(1)$ time and $O(1)$ auxiliary space. It never constructs the implicit array.

## Alternatives and edge cases
- **Sum every lower-half deficit:** this directly follows the transfer interpretation but takes $O(n)$ time.
- **Simulate unit transfers:** moving one unit per iteration takes time proportional to the answer, which can be $O(n^2)$.
- For $n=1$, the formula returns zero.
- Even and odd lengths have different deficit sequences but the same floor formula.
- The final common value is forced to be $n$ by sum preservation.
- Every operation fixes at most one unit of total deficit, establishing minimality.
- Multiplication should occur in a sufficiently wide integer type in languages with fixed-width arithmetic.
