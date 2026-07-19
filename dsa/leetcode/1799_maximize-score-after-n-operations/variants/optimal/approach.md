## General
**Encode used positions rather than values**

A bitmask records exactly which of the $m$ indices have already been selected. This preserves the identity of duplicate values and makes the remaining choices unambiguous. Since every operation sets two new bits, a reachable mask always has an even population count.

**Derive the operation number from the state**

If `mask.bit_count()` positions are used, the next operation number is `mask.bit_count() // 2 + 1`. Therefore the mask alone determines both the available indices and the multiplier; no separate operation parameter is needed in the memoization key.

**Try every next pair once**

For each state, enumerate every pair of unused indices $i<j$. Mark both bits, add the current operation number times the precomputed $\gcd(\texttt{nums[i]},\texttt{nums[j]})$, and combine that gain with the best score from the resulting mask.

The recurrence considers every legal first choice from a state. After that choice, the memoized subproblem optimally orders all remaining pairs. Induction on the number of unused positions therefore shows that each state stores its true maximum, including the initial empty mask.

## Complexity detail
There are at most $2^m$ masks. Each state examines $O(m^2)$ index pairs, giving $O(m^2 2^m)$ time. Precomputing all pairwise GCD values costs $O(m^2)$ additional time and space. The memo table contains at most $2^m$ entries, and recursion depth is $m/2$, so total auxiliary space is $O(m^2+2^m)$.

## Alternatives and edge cases
- **Unmemoized backtracking:** It explores the same pair choices repeatedly under different histories and grows factorially.
- **Bottom-up mask DP:** It has the same asymptotic bounds and avoids recursion, but must explicitly skip masks with an odd number of set bits.
- **Recompute every GCD:** This remains correct but repeats number-theoretic work inside many transitions; precomputation makes each transition constant-time.
- **Two elements:** Only one pair exists, so the answer is their GCD.
- **Duplicate values:** Track indices with mask bits; equal numbers are not interchangeable consumable counts unless their multiplicities are preserved.
- **Operation ordering:** A pairing alone is not enough—the larger pair GCDs should generally receive later, larger multipliers.
- **Completed mask:** With no unused indices, the remaining score is zero.
