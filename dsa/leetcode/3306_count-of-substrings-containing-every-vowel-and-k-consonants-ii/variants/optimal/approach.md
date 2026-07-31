## General

Counting ranges with exactly `k` consonants directly is awkward because moving a boundary may create several valid starts at once. Instead, define $F(t)$ as the number of substrings that contain all five vowels and at least $t$ consonants. Every qualifying range with $c$ consonants contributes to $F(t)$ precisely when $c\geq t$, so the ranges with exactly `k` consonants are counted by $F(k)-F(k+1)$.

Compute one $F(t)$ with a sliding window. As the right endpoint advances, maintain the consonant count and frequencies for the five vowel types in the current range beginning at `left`. While the range already has every vowel and at least $t$ consonants, remove its leftmost character and advance `left`. When that loop stops, every start before `left` forms a valid range ending at the current right endpoint: those starts were removed only while the range remained valid, and extending farther left cannot lose a vowel or consonant. Conversely, the range beginning at `left` is invalid, so no later start can qualify. Adding `left` therefore counts exactly all valid starts for this endpoint.

Both pointers move only forward. Running this window for thresholds `k` and `k + 1`, then subtracting, preserves precisely the substrings whose consonant count equals `k`.

## Complexity detail

Let $n=\lvert word\rvert$. Each of the two window passes advances its right endpoint $n$ times and its left endpoint at most $n$ times, so the total time is $O(n)$. The vowel set and frequency map contain at most five keys, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Track last vowel positions with a consonant window:** The earliest last occurrence of the five vowels can count valid starts, but isolating exactly `k` consonants requires more boundary bookkeeping than the two-threshold formulation.
- **Enumerate every start:** Extending each range until it has too many consonants is correct for the small companion problem, but costs $O(n^2)$ and is infeasible when $n$ reaches $2\cdot10^5$.
- **Zero consonants:** The threshold $F(0)$ is valid; its window shrinks whenever all five vowels are present, while subtracting $F(1)$ removes ranges containing any consonant.
- **Repeated vowels:** Frequency counts ensure a vowel remains represented until its final copy leaves the window.
- **Missing vowel:** The shrink loop never runs, so the contribution is zero at every endpoint.
- **Large answer:** Many overlapping ranges may qualify, so the count must not be restricted to 32-bit arithmetic.
