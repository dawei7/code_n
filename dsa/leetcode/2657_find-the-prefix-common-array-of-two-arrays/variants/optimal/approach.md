## General

Because `A` and `B` are permutations, a value can appear at most once in each array. Maintain a frequency for every value from $1$ through $n$. At index `i`, increment the frequencies of `A[i]` and `B[i]`. A frequency reaching two means that this value has now appeared once in each prefix, so increase the running common count.

Processing both values in sequence also handles `A[i] == B[i]`: the first occurrence raises the frequency to one and the second raises it to two, adding exactly one common value. A frequency can never exceed two under the permutation guarantee, so every value contributes to the count exactly once, at the first index where both prefixes contain it.

After processing index `i`, the frequency of a value equals the number of the two current prefixes containing it. Therefore the running count is precisely the number of frequencies equal to two, which is the definition of `C[i]`. Append that count at every index.

## Complexity detail

Let $n$ be the common array length. Each position performs two frequency updates and constant additional work, so the running time is $O(n)$. The frequency table and required result each use $O(n)$ space.

The benchmark uses reversed permutations and scales `size` as $n$. A correct alternative that rebuilds both prefix sets and intersects them independently at every index completes all legal tiers but takes $O(n^2)$ total time.

## Alternatives and edge cases

- **Recompute prefix intersections:** Build `set(A[:i + 1])` and `set(B[:i + 1])` for every index. This directly follows the definition but repeats $O(i)$ work per prefix and totals $O(n^2)$.
- **Two bit masks:** Since $n \le 50$, each prefix can be represented by a bit mask and intersected with bit operations; this is also linear but less portable as a general explanation.
- When the permutations are identical, `C[i] = i + 1` at every index.
- The final value is always $n$ because both full arrays contain every number from $1$ through $n$.
- The running count may increase by two at one index when `A[i]` completes one value and `B[i]` completes another.
- For $n=1$, the sole value is common immediately and the result is `[1]`.
