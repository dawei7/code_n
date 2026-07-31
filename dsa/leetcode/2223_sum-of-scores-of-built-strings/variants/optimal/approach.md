## General

**Recognize the suffix scores as Z-values**

Because each prepended intermediate string is a suffix of the final string, its score is the number of characters matching between `s` and the suffix starting at some index $i$. This is exactly the Z-value $Z[i]$. The full string contributes $n$, so the answer is $n+\sum_{i=1}^{n-1}Z[i]$.

**Reuse a known matching interval**

Maintain the rightmost interval `[left, right]` already known to match a prefix of `s`. When index $i$ lies inside that interval, the earlier Z-value at `i - left` supplies a safe initial match, capped at the interval boundary. Compare characters only beyond that guaranteed portion.

If the extended match reaches farther right, make it the new rightmost interval. Every successful comparison outside an existing interval advances `right`, which can move forward at most $n$ times. Failed comparisons occur at most once per index, giving linear total work rather than restarting every suffix from zero.

The initial copied portion is valid because the active interval equals the corresponding prefix character for character. Explicit extension then finds the first mismatch or string boundary, so each computed Z-value is exact.

## Complexity detail

Let $n=\lvert s\rvert$. The Z-box boundary advances monotonically, so all comparisons total $O(n)$ time.

The Z-value array uses $O(n)$ space.

## Alternatives and edge cases

- **Compare every suffix directly:** Restarting at the first character for each suffix is simple but takes $O(n^2)$ time on repeated characters.
- **Rolling hash plus binary search:** Hash comparisons can find each score in $O(\log n)$ time, but introduce collision concerns or more complex exact hashing.
- **Suffix array or suffix automaton:** These structures can support related matching queries but are excessive for matches against one fixed prefix.
- **Single character:** Only the full string exists, so its score is one.
- **All equal characters:** Every suffix matches completely and the answer is $n(n+1)/2$.
- **No repeated first character:** Every proper suffix has score zero, leaving only $n$.
- **Overlapping matches:** The Z-box reuse remains valid even when repeated prefixes overlap themselves.
