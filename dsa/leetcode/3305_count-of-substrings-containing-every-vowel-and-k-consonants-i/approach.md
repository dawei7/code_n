## General

**Count “exactly” by subtracting two monotone conditions.** A sliding window works naturally with a condition such as “at least $k$ consonants,” because adding characters cannot destroy it. Exact equality is not monotone: adding one consonant can move a substring from too few, to exact, to too many. The source uses the identity

$$
\#(\text{exactly }k)
=
\#(\text{at least }k)
-
\#(\text{at least }k+1),
$$

while requiring all five vowels in every counted group. Helper `f(k)` computes the first at-least count, so the return value `f(k) - f(k + 1)` isolates exactly $k$ consonants.

**State maintained by `f(k)`.** Counter `cnt` holds vowel frequencies in the current window. The window contains every vowel exactly when `len(cnt) == 5`, because zero-count vowels are removed. Scalar `x` is the number of consonants in the window, `l` is its left boundary, and the loop variable's current character is the right boundary.

When a new character arrives, membership in `"aeiou"` determines its type. A vowel increments its counter entry; any other lowercase letter increments `x`.

**Shrink while the current window satisfies both at-least conditions.** When `x >= k` and all five vowel keys exist, the window is valid for `f(k)`. The source removes `word[l]` and advances `l` repeatedly until one requirement fails. Removing a vowel decrements its count and deletes its key at zero, so `len(cnt)` continues to represent distinct vowels actually present. Removing a consonant decrements `x`.

After this loop, the window beginning at the new `l` is invalid, while every start before `l` is valid for this fixed right endpoint. Why? The last removed prefix boundary was valid. Moving the start earlier only adds characters, which cannot remove a vowel or reduce the consonant count. Conversely, starts at or after `l` are contained in the now-invalid window and cannot repair its missing monotone requirement by removing more characters.

Therefore exactly `l` substrings ending at the current right boundary satisfy “all vowels and at least $k$ consonants.” The source adds them in one step with `ans += l`.

**A useful $k=0$ trace.** For `word = "aeiou"`, `f(0)` becomes valid when `u` arrives. The shrink loop removes the leading `a`, causing one vowel to disappear and setting `l=1`. Thus one ending-at-`u` substring is counted. `f(1)` counts none because the word has no consonants. Their difference is one.

**Why subtraction leaves exactly the desired set.** Every substring counted by `f(k+1)` is also counted by `f(k)` because at least $k+1$ implies at least $k$. Removing that subset from `f(k)` leaves substrings with at least $k$ but not at least $k+1$ consonants. Since counts are integers, that means exactly $k$. Both helper calls enforce all vowels independently, so subtraction does not introduce substrings missing a vowel.

**Why this is linear despite the nested loop.** In one helper call, the right boundary advances through each character once. The left boundary starts at zero and never moves backward; every inner-loop iteration increments it. It can therefore move at most $n$ times in the entire call. Calling the helper twice changes only a constant factor.

**The exact source is faster than its manifest description.** The manifest says this version enumerates every start and runs in $O(n^2)$. The protected source does not do that. It is the same at-least subtraction sliding window used for the larger version II and runs in linear time. This matters even though the smaller constraint of 250 would permit a quadratic solution.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. Each `f` call advances its right pointer $n$ times and its left pointer at most $n$ times, for $O(n)$ expected time with counter operations. Two calls remain $O(n)$ total time, not $O(n^2)$.

The counter contains only vowels and has at most five entries. All other state is scalar, so auxiliary space is $O(1)$. Python dictionary operations are expected constant-time; with this fixed tiny alphabet, an array implementation could make the bound deterministic.

## Alternatives and edge cases

- **Quadratic start/end enumeration:** For each start, extend the end while maintaining counts. This matches the manifest summary and is viable for $n\le250$, but it is unnecessary because the exact source is linear.
- **Count at most $k$ instead:** Exactly-$k$ window problems often use `atMost(k) - atMost(k - 1)`. Here “contains all vowels” interacts more naturally with shrinking a valid at-least window, so the source uses the dual identity.
- **Direct exact-$k$ window with next-consonant positions:** It can count multiple vowel-only right extensions, but requires more bookkeeping than subtracting at-least counts.
- **`k = 0`:** `f(0)` treats consonant count zero as sufficient and shrinks whenever all vowels exist. Subtracting `f(1)` removes every substring containing a consonant.
- **Missing one vowel globally:** Neither helper ever sees five vowel keys, so both return zero and the difference is zero.
- **Repeated vowels:** Counts above one allow extra copies to be removed before a vowel key disappears; validity depends on presence, not exact vowel frequency.
- **Consonants before the minimal valid window:** Shrinking can discard them while the consonant threshold remains satisfied, increasing `l` and counting additional starts.
- **Exactly $k+1$ consonants:** Such a substring appears in both helper totals and cancels, as required.
- **Every character is a vowel:** Only the $k=0$ result can be nonzero.
- **Answer type:** The number of substrings can be quadratic in $n$. Python integers are safe; larger-language variants should use a sufficiently wide integer.
- **Vowel test:** Inputs are lowercase, so membership in the literal `"aeiou"` is exact and case normalization is unnecessary.
- **Manifest discrepancy:** The protected implementation is $O(n)$ time and $O(1)$ auxiliary space; the listed quadratic approach does not describe it.
