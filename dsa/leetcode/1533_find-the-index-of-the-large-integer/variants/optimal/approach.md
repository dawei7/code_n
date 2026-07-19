## General
**Compare equal-size candidate halves**

Maintain an inclusive interval known to contain the unique larger value. Split it into equal-length left and right blocks. If the first sum is larger, the exceptional index lies in the left block; if the second is larger, it lies in the right block. Every ordinary value has an equal counterpart, so only the unique excess changes the comparison.

For an even interval, the two blocks cover every candidate. For an odd interval, leave the final index unpaired and compare the two equal blocks before it. A nonzero result selects the heavier block. Equality proves that neither compared block contains the excess, so the unpaired endpoint is the answer immediately.

**Halve until one index remains**

Each nonterminal comparison reduces the candidate interval to at most half its prior length. When its endpoints meet, that sole index must contain the larger value. The largest legal input needs at most $\lceil\log_2(500000)\rceil=19$ comparisons, within the strict 20-call limit.

The three-way result is used only after making the compared blocks equal in length. Comparing unequal blocks would let their different counts of the common value dominate the sum and invalidate the deduction.

## Complexity detail
Every query performs $O(1)$ work and halves the candidate count, so the algorithm uses $O(\log n)$ time and at most 19 `compareSub` calls on the legal domain. It stores only interval endpoints and split indices, giving $O(1)$ auxiliary space.

The accompanying asymptotic-optimality certificate records that distinguishing one exceptional position among $n$ possibilities with a constant-outcome comparison oracle requires $\Omega(\log n)$ information, matching the upper bound.

## Alternatives and edge cases
- **Compare adjacent singletons:** eventually finds the larger value but can require $O(n)$ calls and violates the 20-query limit.
- **Unequal subarray comparison:** the ordinary values no longer cancel, so the result need not reveal which block contains the exception.
- **Materialize hidden values:** direct array access is unavailable and would violate the interactive contract.
- **Two elements:** one comparison determines the answer.
- **Odd candidate count:** equality between the paired blocks identifies the unpaired endpoint.
- **Exception at an endpoint:** the interval updates retain either boundary correctly.
- **Maximum length:** binary halving uses 19 comparisons, leaving one call of margin.
- **Value magnitude:** only relative excess matters; the actual common and exceptional values need not be known.
