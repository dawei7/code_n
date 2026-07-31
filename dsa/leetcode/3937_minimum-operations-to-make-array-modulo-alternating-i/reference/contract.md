## Function Contract

**Inputs**

- `nums`: A nonempty integer array whose elements may be increased or decreased by unit operations.
- `k`: The modulus that defines the allowed target residues.

Let $N=\lvert\texttt{nums}\rvert$ and $K=k$. A feasible result chooses residues $x,y\in\{0,\ldots,K-1\}$ with $x\ne y$. Every even-indexed element must become congruent to $x$ modulo $K$, and every odd-indexed element must become congruent to $y$ modulo $K$.

**Return value**

Return the minimum number of single-element increments and decrements required over all feasible distinct residue pairs.
