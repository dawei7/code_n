## General

**Track suffixes by GCD rather than by start.** Fix a right endpoint. Every
subarray ending there is a suffix of the processed prefix. Extending a suffix
whose greatest common divisor is $g$ with the next value $x$ changes its GCD
to $\gcd(g,x)$. Start a new one-element suffix with GCD $x$, extend every
state from the preceding endpoint, and merge states that produce the same new
GCD.

**Only the earliest start survives a merge.** Two suffixes ending at the same
position and having the same GCD will evolve identically under every future
extension. Because all array values are positive, the earlier suffix is also
longer and has a strictly larger sum. It is therefore at least as eligible for
the minimum-length condition and gives a larger gcd-sum for the shared GCD.
Discarding the later suffix cannot remove an optimal present or future answer.

Store each surviving GCD with its earliest left endpoint and current sum.
After constructing the states for a right endpoint, evaluate
`current_gcd * total` whenever the state's length is at least `k`. Every
eligible subarray appears in a state before equal-GCD consolidation, and the
dominance argument preserves a candidate at least as good, so the largest
evaluated product is the required maximum.

**There are few distinct suffix GCDs.** Ordered by increasing suffix length,
each changed GCD is a proper divisor of the previous value. A proper positive
divisor is at most half its multiple, so the number of distinct values at one
endpoint is $O(\log V)$ rather than $O(N)$.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and
$V=\max(\texttt{nums})$. Each endpoint maintains $O(\log V)$ states.
Accounting for the $O(\log V)$ Euclidean-algorithm cost of each GCD operation,
the total time is $O(N\log^2 V)$. The current and next compressed state maps
contain $O(\log V)$ entries, so auxiliary space is $O(\log V)$.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintain a running sum and GCD for each left endpoint; this is correct but takes $O(N^2\log V)$ time when GCD cost is included.
- **Range-GCD structure plus boundary searches:** A sparse table or segment tree can group ranges with equal GCD, but needs more storage and more involved index searches.
- **Inspect only length k:** This misses longer subarrays whose added positive values preserve enough GCD to increase the product.
- **Positive values:** Positivity is what makes an earlier equal-GCD suffix dominate a later one by both length and sum.
- **k equals one:** Singletons are eligible, but longer subarrays must still be considered.
- **k equals N:** Only the entire array is eligible.
- **Large result:** Both the sum and GCD can be large, so the product requires a wide integer type.

