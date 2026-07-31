## General

**Canonicalize factor order.** Reordering factors changes neither their product nor their maximum-minus-minimum difference. Therefore every solution can be represented uniquely as a non-decreasing sequence

$$
a_1\le a_2\le\cdots\le a_k,
\qquad
\prod_{i=1}^{k}a_i=n.
$$

Backtrack while storing the chosen prefix. A state contains the remaining product, the number of factor slots left, and the minimum value allowed for the next factor.

**Bound the next factor.** Suppose `slots` factors remain and the next candidate is $f$. All later factors must be at least $f$. Their combined product with $f$ is therefore at least $f^{\texttt{slots}}$. If that power exceeds the remaining product, neither $f$ nor any larger value can begin a valid completion.

Loop from the current minimum while $f^{\texttt{slots}}$ does not exceed the remaining product. Recurse only when $f$ divides that product exactly, replacing the remaining product by its quotient and keeping $f$ as the next minimum.

When one slot remains, the remaining product is forced. Accept it only when it is at least the previous factor. The resulting sequence is non-decreasing, and its spread is simply its last value minus its first.

Every accepted leaf multiplies to $n$ and contains exactly $k$ factors. Conversely, take any valid decomposition and sort it. At each level its next factor divides the remaining product, respects the previous minimum, and satisfies the power bound because all remaining factors are no smaller. The search follows that branch and reaches the decomposition. Thus every canonical factorization is examined once, and selecting the smallest leaf spread is globally optimal.

## Complexity detail

Let $F$ be the total number of integer factor candidates tested across all recursive states, including nondivisors rejected by a modulo check. The search takes $O(F)$ time. This input-sensitive quantity depends on the divisor structure of $n$ and the remaining slot counts; the power bound keeps every loop within the largest possible next factor.

The recursion depth and chosen factor list contain at most $k\le5$ entries, so auxiliary space is $O(k)$ apart from the returned list.

The benchmark defines its size as $n$ and uses perfect fourth powers with `k = 4`. The accepted root-bounded search examines only small candidate ranges. A calibrated correct alternative scans every integer through $n$ to build the complete divisor list and then tests all non-decreasing four-divisor combinations, preserving optimality but growing substantially faster.

## Alternatives and edge cases

- **Enumerate all k-tuples:** Trying unrestricted factors through $n$ costs an enormous $O(n^k)$ search and repeats permutations.
- **Generate all divisors first:** Combining divisor tuples is correct, but scanning every integer to find divisors adds avoidable linear work in $n$.
- **Prime factor balancing greedily:** Assigning prime factors to the currently smallest bucket is intuitive but does not guarantee the minimum final spread.
- **Factor one:** Ones are valid and are necessary when no more balanced nontrivial split exists.
- **Perfect k-th power:** Equal factors produce the optimal spread zero.
- **Repeated factors:** Non-decreasing enumeration permits equality and avoids duplicate permutations.
- **Final factor:** Reject it when it is smaller than the preceding factor, because that ordering was already considered elsewhere.
- **Output order:** Any permutation of an optimal factor multiset is valid; the reference returns non-decreasing order.
