## General

**Normalize the only values that can participate**

Every element of a subsequence whose GCD is `p` must be divisible by `p`. Replace each divisible value $x$ by $x/p$, and represent every non-divisible value by zero. The original array has a good subsequence exactly when some non-empty proper selection of the positive normalized values has GCD $1$.

Maintain the GCD of the complete normalized array in a segment tree, using $gcd(0,x)=x$. A point update changes one leaf and $O(\log N)$ ancestors. If the root GCD is not $1$, no subset can have GCD $1$: the GCD of a subset can only be a multiple of the GCD of a superset.

When the root is $1$ and at least one normalized entry is zero, all positive entries already form a proper subsequence. This immediately proves that the current query is successful.

**Characterize the all-divisible boundary case**

Suppose every normalized entry is positive. The whole array is forbidden because a good subsequence must be shorter than $N$. It is nevertheless enough to inspect selections of length $N-1$: any smaller selection with GCD $1$ can be extended to $N-1$ positions, and adding values keeps its GCD equal to $1$.

Removing index $i$ leaves a GCD greater than $1$ precisely when some prime divides all other $N-1$ normalized values. Because the segment-tree root is already $1$, that prime cannot also divide the value at $i$. Call $i$ critical for such a prime. A valid removal exists exactly when at least one array index is not critical for any prime.

For each prime, store how many normalized values contain it and the XOR of their indices. If its count is $N-1$, its unique missing index is

$$
i_{\mathrm{missing}}=(0\mathbin{\mathtt{xor}}1\mathbin{\mathtt{xor}}\cdots\mathbin{\mathtt{xor}}(N-1))\mathbin{\mathtt{xor}}X_p,
$$

where $X_p$ is the XOR of the indices whose values contain prime $p$. A multiplicity map records how many such primes mark each missing index. Therefore, in the all-divisible case with root GCD $1$, the answer is yes exactly when the number of distinct critical indices is less than $N$.

**Update only changed prime memberships**

Build a smallest-prime-factor table through the largest normalized initial or queried value. Cache each value's distinct prime factors. During an update, only primes in the symmetric difference between the old and new factor sets change their count or index XOR. Before changing one such prime, remove its old critical contribution; afterward, add its new contribution. Update the positive-entry count and the segment-tree leaf, then apply the two proven success tests.

The maintained prime counts and XORs exactly describe current memberships, and the critical-index map exactly aggregates primes occurring in $N-1$ positions. Together with the segment-tree GCD, the tests cover both possible ways a proper GCD-$1$ selection can exist, so every counted query and only such a query is counted.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$, $Q=\lvert\texttt{queries}\rvert$, and let $M$ be the largest normalized value that is divisible by `p` among the initial values and all update values, taking $M=1$ if none is divisible.

The smallest-prime-factor sieve takes $O(M\log\log M)$ time. Factoring all initial values and the distinct values encountered by updates costs $O((N+Q)\log M)$ in the stated bound, while segment-tree construction and updates cost $O(N+Q\log N)$. The combined time is $O(M\log\log M+(N+Q)(\log N+\log M))$.

The segment tree, normalized array, critical-index map, factor counts, index XORs, sieve, and factor cache use $O(N+M)$ auxiliary space.

## Alternatives and edge cases

- **Recompute after every query:** Rebuilding the array GCD and all leave-one-out GCDs is conceptually direct but takes $O(NQ)$ time with prefix and suffix GCDs, which is too slow when both dimensions reach $5\cdot10^4$.
- **Track every possible subsequence GCD:** Point updates invalidate contributions from exponentially many subsequences, so explicit subset state cannot meet the constraints.
- **Check only the complete normalized GCD:** This is sufficient when at least one value is not divisible by `p`, but it falsely accepts arrays such as normalized `[2, 3]`; the whole pair has GCD $1$, while each permitted singleton has GCD greater than $1$.
- **Ignore values not divisible by `p`:** Such values can never be selected, but their presence is still important because it makes the selection of all eligible values a proper subsequence.
- **Normalized value one:** Its distinct-prime set is empty, and any proper subsequence containing it already has normalized GCD $1$.
- **Repeated prime powers:** Only distinct prime membership matters. For example, $2$, $4$, and $8$ each contribute once to the count for prime $2$.
- **Several primes missing at one index:** The critical map stores multiplicities so removing one prime's contribution does not accidentally clear another prime that marks the same index.
- **Assignments that preserve prime membership:** Even when the old and new normalized values have identical distinct factors, the segment-tree leaf must still change because their numeric GCD contribution can differ.
