## General

**Fix the final selected value.** A candidate $x$ may be any original array value, because it can remain unchanged even when it exceeds `maxVal`. It may also be any value from $1$ through `maxVal`, created by changing the selected element.

Let $B(x)$ be the number of original elements whose greatest common divisor with $x$ exceeds $1$. Every non-selected element counted by $B(x)$ must change; setting it to $1$ always resolves its conflict.

- If $x$ already occurs and $x>1$, choose one occurrence as the selected index. That occurrence is included in $B(x)$ but does not change, so the minimum cost is $B(x)-1$.
- If an existing $x$ equals $1$, it is co-prime with everything and the minimum cost is zero.
- If $x$ is absent but can be created, and $B(x)>0$, change one conflicting element into the selected $x$. That modification is already one of the $B(x)$ necessary changes, so the total cost remains $B(x)$.
- If $x$ is absent and $B(x)=0$, every original element is already co-prime with it, but one element must still change to create $x$. The cost is one.

These cases determine the best score for every candidate once $B(x)$ is known.

**Count shared factors without scanning the array per candidate.** Build `frequency[v]`, then for every divisor $d$ compute

$$
D(d)=\sum_{d\mid v}\operatorname{frequency}(v),
$$

the number of array values divisible by $d$. The harmonic multiples loop computes all $D(d)$ values.

Factor $x$ into its distinct primes $p_1,\ldots,p_k$. An element belongs to $B(x)$ exactly when it is divisible by at least one of those primes. Inclusion-exclusion therefore gives

$$
B(x)=
\sum_{\emptyset\ne S\subseteq\{1,\ldots,k\}}
(-1)^{\lvert S\rvert+1}
D\!\left(\prod_{i\in S}p_i\right).
$$

A smallest-prime-factor sieve supplies the distinct factors, and signed subset products evaluate this expression. Checking every creatable value and every distinct original value covers all possible optima, so the largest computed score is the answer.

## Complexity detail

Let $U=\max(\texttt{maxVal},\max(\texttt{nums}))$. Building frequencies costs $O(n)$. The divisor-multiples sums cost

$$
O\!\left(U\sum_{d=1}^{U}\frac1d\right)=O(U\log U).
$$

The smallest-prime-factor sieve costs $O(U\log\log U)$. A number at most $10^5$ has at most six distinct prime factors, so its inclusion-exclusion enumeration has at most $2^6-1$ terms; across all candidates this is $O(U)$ under the fixed source bound. Total time is $O(n+U\log U)$ and the frequency, divisor-count, and factor arrays use $O(U)$ auxiliary space.

The benchmark grows both $n$ and $U$ through arrays containing every value from $1$ to $U$. It separates the divisor sieve from a correct implementation that scans the whole array and computes a GCD for every candidate.

## Alternatives and edge cases

- **Candidate-by-candidate GCD scan:** Directly compute $B(x)$ by testing every array value for every candidate. It is easy to verify but takes $O(nU\log U)$ time in the worst case.
- **Möbius inversion:** Precomputing the Möbius function gives an equivalent divisor-sum formula for co-prime counts. Prime-subset inclusion-exclusion is more local and needs only the distinct factors of each candidate.
- **Existing value above `maxVal`:** Such a value cannot be created elsewhere, but an original occurrence may remain unchanged and be selected.
- **Selected value one:** Since $\gcd(1,y)=1$ for every positive $y$, an existing one needs no supporting modifications.
- **Absent conflict-free candidate:** Even when all originals are co-prime with $x$, creating the selected $x$ still costs one modification.
- **Duplicate selected values:** For $x>1$, all non-selected duplicates conflict with the chosen occurrence and must change.
- **Single-element array:** Co-primality with every other element is vacuous; the original value may remain, or the element may change once to a more profitable bounded value.
