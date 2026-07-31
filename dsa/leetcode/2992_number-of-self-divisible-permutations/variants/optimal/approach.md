## General

**Represent used values as a subset.** Number values `1` through `n` by bits.
A mask identifies exactly which values have already been placed. All partial
permutations represented by the same mask have the same next position,
`mask.bit_count() + 1`, and the same future choices, so their counts can be
merged.

**Extend only coprime assignments.** Initialize the empty mask with one way.
For every mask, try each unused value. When its greatest common divisor with
the next position is one, add the mask's count to the state with that value's
bit set. No invalid placement is introduced. Conversely, removing the final
value from any valid partial permutation reaches exactly one predecessor state,
so every valid permutation is counted once. The full mask therefore stores
the requested answer.

## Complexity detail

There are $2^N$ masks and at most $N$ candidate values per mask, giving
$O(N2^N)$ time. The count table contains $2^N$ entries, so auxiliary space is
$O(2^N)$.

## Alternatives and edge cases

- **Enumerate all permutations:** Direct checking takes $O(N!\,N)$ time and quickly becomes impractical.
- **Memoized backtracking:** Caching by the remaining-value mask is equivalent to the iterative subset DP.
- **Recompute mask size manually:** This preserves correctness but adds an unnecessary factor of $N$ across transitions.
- **Position one:** Every value is coprime with `1`, so all values are initially eligible.
- **Value one:** The value `1` is eligible at every position.
- **No legal extension:** Such a mask contributes nothing and naturally dies out.
