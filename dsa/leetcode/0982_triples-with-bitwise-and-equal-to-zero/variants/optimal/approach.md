## General
**Aggregate the first two indices:** Count every ordered pair `(i, j)` by the mask `nums[i] & nums[j]`. This takes quadratic time but compresses all pairs with the same remaining set bits into one frequency.

**Test only masks that occur:** For a third value $x$, a pair mask $p$ completes a valid triple exactly when $p\mathbin{\&}x=0$. Iterate over the distinct pair masks and add the stored frequency of each compatible one. Cache this compatible-pair total for every distinct input value so repeated occurrences of $x$ reuse the same result.

Every ordered pair is counted once in its exact AND bucket. A bucket contributes to the cached total for $x$ exactly when its mask AND $x$ is zero. Multiplying that total by the frequency of $x$ as the third selected value counts every valid ordered triple once and no invalid triple.

## Complexity detail
Building ordered pair frequencies costs $O(N^2)$. Checking all $U$ occurring pair masks for each of the $D$ distinct values costs $O(DU)$, giving $O(N^2+DU)$ time. The pair-frequency map and cached totals use $O(U+D)=O(U)$ space because every input value also occurs as a self-AND pair mask.

## Alternatives and edge cases
- **Enumerate all triples:** Three nested index loops are direct and correct but require $O(N^3)$ time.
- **Dense subset-sum transform:** A sum-over-subsets transform gives $O(N^2+B2^B)$ time for a fixed $B$-bit universe, but eagerly visiting all $2^{16}$ masks is wasteful when few pair masks occur.
- **Zero value:** Any ordered triple containing a selected zero has combined AND zero.
- **Repeated indices:** Tuples such as `(i, i, i)` are legal and must not be filtered out.
- **Ordered counting:** Permutations of three indices are separate tuples even when they select equal values.
