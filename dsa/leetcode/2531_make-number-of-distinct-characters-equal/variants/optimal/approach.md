## General

Only the values of the two selected characters matter, not which occurrence of each value is chosen. Count both strings and record their current numbers of distinct characters. Then enumerate every character present in the first string as its outgoing value and every character present in the second as the other outgoing value.

When the values differ, removing a character decreases its string's distinct count exactly when its frequency was one. Adding the incoming character increases the count exactly when that character was previously absent. Applying those two Boolean deltas to each string gives both post-swap distinct counts without modifying either frequency map.

Equal selected characters require separate treatment: exchanging the same character value leaves both strings unchanged, even if one selected occurrence was its string's only copy. Such a move succeeds precisely when the original distinct counts already match. Because every legal index pair corresponds to one enumerated present-character pair, accepting any equal post-swap counts is both necessary and sufficient.

## Complexity detail

Let $n = \lvert\texttt{word1}\rvert + \lvert\texttt{word2}\rvert$ and let $A=26$ be the fixed lowercase alphabet size. Building the frequency maps costs $O(n)$ time; examining at most $A^2$ character pairs costs $O(1)$ under the fixed alphabet. The total is therefore $O(n)$ time. Both maps contain at most 26 entries, giving $O(1)$ space.

## Alternatives and edge cases

- **Enumerate index pairs:** Trying every position pair repeats identical character-value swaps and can require $O(\lvert word1\rvert\lvert word2\rvert)$ checks before accounting for copied state.
- **Mutate and restore counters:** Temporarily applying each character-pair swap is correct, but direct count deltas are simpler and avoid restoration mistakes.
- **Same outgoing character:** Swapping equal values changes nothing and must not be processed with ordinary removal/addition deltas.
- **Frequency one:** Removing the only occurrence deletes a distinct character; larger frequencies preserve it.
- **Previously absent incoming value:** Only a genuinely new value increases the distinct count.
- **Exactly one move:** Already equal distinct counts are sufficient only when some legal swap preserves equality; choosing equal characters in both strings is one such route when they share a character.
