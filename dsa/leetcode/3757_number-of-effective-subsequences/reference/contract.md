## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers whose index subsequences may be removed.

Let $n = \lvert\texttt{nums}\rvert$, and let $b$ be the number of set-bit positions in the bitwise OR of the full array. Removing a subsequence leaves the complementary indices in their original relative order. Duplicate values at distinct indices are counted as distinct subsequence choices.

**Return value**

Return the number of nonempty subsequences whose removal strictly lowers the bitwise OR of the remaining elements, reduced modulo $10^9+7$.
