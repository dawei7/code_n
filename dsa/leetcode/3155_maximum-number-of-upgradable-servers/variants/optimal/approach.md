## General

Consider one data center with $c$ servers, upgrade cost $u$, sale income $s$, and initial money $m$. Suppose exactly $x$ servers will be upgraded. The other $c-x$ servers may all be sold; there is no reason to leave one unsold when maximizing a fixed $x$, because every sale only increases the available money.

After those sales, the center has $m+(c-x)s$ money and needs $xu$ for the upgrades. Thus $x$ is feasible exactly when

$$
xu \le m+(c-x)s.
$$

Move the term involving $x$ to the left:

$$
x(u+s) \le m+cs.
$$

Because $u+s$ is positive, the largest integer satisfying the budget inequality is

$$
\left\lfloor\frac{m+cs}{u+s}\right\rfloor.
$$

At most $c$ servers exist, so the answer for this center is that quotient capped at $c$. Apply the same calculation to every index. The derivation is exact in both directions: any feasible plan must obey the inequality, and whenever the inequality holds, selling the $c-x$ non-upgraded servers supplies enough money to realize that value of $x$. Since money cannot cross centers, choosing each center's maximum independently produces the complete answer.

## Complexity detail

Let $n$ be the common length of the four input arrays. One constant-time arithmetic calculation is performed per data center, so the running time is $O(n)$.

Apart from the returned array, the algorithm retains only the current four values and arithmetic intermediates, giving $O(1)$ auxiliary space. The product $cs$ can reach $10^{10}$, so fixed-width implementations must use 64-bit arithmetic.

## Alternatives and edge cases

- **Binary search per center:** Feasibility is monotone in the number upgraded, so binary search is correct in $O(n\log C)$ time, where $C=\max_i\texttt{count[i]}$, but the rearranged inequality gives the boundary directly.
- **Descending exhaustive search:** Trying $c,c-1,\ldots,0$ upgrades until one is affordable is correct, but its total work can be quadratic when every center contains $\Theta(n)$ servers.
- **Simulate sales one at a time:** Selling servers and repeatedly checking affordability also finds an optimum, but performs unnecessary work proportional to the server counts.
- If the initial money already pays for every upgrade, the cap at $c$ prevents the algebraic quotient from exceeding the number of servers.
- Selling the only server may raise enough cash in isolation, but leaves no server to upgrade; the $c-x$ term captures this automatically.
- Exact divisibility is feasible, while any remainder is discarded by integer floor division.
- Use 64-bit intermediates outside Python because both $m+cs$ and the denominator sum can exceed 32-bit arithmetic.

