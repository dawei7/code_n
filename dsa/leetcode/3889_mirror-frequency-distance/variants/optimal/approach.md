## General

**Encode the two character sets without mixing them**

Use a fixed array of 36 counters. Indices $0$ through $9$ represent the digits, and indices $10$ through $35$ represent the lowercase letters. One pass over `s` increments the appropriate counter for every occurrence.

Within the digit segment, index $i$ mirrors index $9-i$. Within the letter segment, letter offset $i$ mirrors offset $25-i$, so their full-array indices are $10+i$ and $35-i$.

**Visit each unordered mirror pair once**

The five digit pairs are obtained with offsets $0$ through $4$, and the thirteen letter pairs with offsets $0$ through $12$. For each pair, add the absolute difference of its two counters. Restricting the loops to the first half of each character set prevents the reversed pair from being counted again.

This also handles an absent mirror naturally: its counter remains zero. Pairs whose two characters are both absent contribute zero, so iterating all 18 possible pairs gives the same total as considering only pairs represented in the string.

Every occurrence contributes to exactly one correct character counter. The fixed pair loops then compare precisely the two counters prescribed by the reversed ordering and include every unordered pair once. Therefore their accumulated sum is exactly the required mirror frequency distance.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting the string takes $O(n)$ time, and the 18 pair comparisons take constant time, so the total is $O(n)$. The 36 counters occupy $O(1)$ auxiliary space because the character domain is fixed.

The benchmark defines size as the string length and repeats one character at every position. The optimal method remains linear. A correct implementation that recomputes both relevant frequencies by scanning the entire string separately for every input position performs $\Theta(n^2)$ work on these tiers.

## Alternatives and edge cases

- **Hash map or `Counter`:** A keyed frequency map produces the same $O(n)$ time and $O(1)$ bounded-domain space, though the fixed array makes the two character ranges and their mirror indices explicit.
- **Recount for every position:** Repeated full-string scans can still produce the right pair values, but doing so for all $n$ positions wastes $\Theta(n^2)$ time.
- **Missing mirror:** A character may occur while its mirror does not; the pair contributes the occurring character's full frequency.
- **Balanced pair:** Equal nonzero frequencies contribute zero, but the pair is still represented and must not affect the sum.
- **Pair orientation:** Encountering the mirror first does not create a different pair; both directions must share one contribution.
- **Letters and digits:** Mirroring never crosses between the two character sets, so `a` cannot pair with a digit and `0` cannot pair with a letter.
- **Maximum length:** The answer is at most $n$, so the stated maximum fits comfortably in a standard integer.
