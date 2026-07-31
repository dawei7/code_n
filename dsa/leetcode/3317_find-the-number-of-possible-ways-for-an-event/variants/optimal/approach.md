## General

Fix the number $k$ of nonempty stages. First partition the $n$ distinct performers into $k$ nonempty, unlabeled bands. The number of such partitions is the Stirling number of the second kind $S(n,k)$. Then assign those bands injectively to $k$ of the $x$ labeled stages in

$$
(x)_k=x(x-1)\cdots(x-k+1)
$$

ways. Finally, each nonempty band independently receives one of $y$ scores, contributing $y^k$. Empty stages receive no score. The contribution for a fixed $k$ is therefore $S(n,k)(x)_k y^k$, and valid $k$ range from 1 through $\min(n,x)$.

Compute the final row of Stirling numbers using

$$
S(i,k)=S(i-1,k-1)+kS(i-1,k).
$$

The first term puts performer $i$ into a new singleton band; the second inserts that performer into one of the existing $k$ bands. Updating band counts from high to low lets one array represent consecutive rows without overwriting a state that is still needed.

After the Stirling row is complete, accumulate the falling factorial and score power incrementally while summing all $k$ contributions. Reducing every multiplication and addition modulo $10^9+7$ keeps values bounded and preserves the requested result.

## Complexity detail

Let $L=\min(n,x)$. The Stirling recurrence evaluates at most $L$ states for each of $n$ performers, taking $O(nL)$ time. The final sum takes $O(L)$ additional time. The rolling Stirling row has $L+1$ entries, so auxiliary space is $O(L)$.

## Alternatives and edge cases

- **Inclusion-exclusion for each stage count:** Surjections can be counted as $\sum_j(-1)^j\binom{k}{j}(k-j)^n$, but repeating this for every $k$ adds another factor and repeated modular exponentiation.
- **Two-dimensional Stirling table:** Keeping every row uses $O(nL)$ memory even though only the previous row is required.
- **All stages may be empty except used ones:** The sum includes every feasible nonempty-stage count rather than forcing all $x$ stages to be occupied.
- **More stages than performers:** Terms above $n$ are impossible and are excluded by $L=\min(n,x)$.
- **One score:** When $y=1$, score assignments add no multiplicity and the formula reduces to ordinary performer-to-stage assignments.
- **Modulo arithmetic:** Falling factorials, powers, Stirling values, and the accumulated answer must all be reduced to avoid large intermediates in fixed-width languages.
