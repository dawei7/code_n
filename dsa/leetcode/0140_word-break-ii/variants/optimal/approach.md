## General
**Memoize the complete sentence set for each suffix boundary**

Let `sentences(start)` return an immutable tuple containing every valid sentence whose words concatenate to `s[start:]`. Different prefix choices can reach the same suffix, so caching this function reuses its already-constructed continuations. At `start == len(s)`, return `("",)` as the single empty continuation; returning no continuation would prevent a word ending at the final character from completing a sentence.

**Only source-length candidates can be the next word**

Store the dictionary in a hash set and record its maximum word length. From `start`, try ending boundaries only through `start + max_word_length`. For each matching word, combine it with every cached sentence from the remaining suffix. Emit the word alone for the empty continuation and otherwise insert exactly one space before the suffix.

Every constructed result consists solely of a dictionary prefix followed by a complete dictionary segmentation of the remaining suffix, so it is valid. Conversely, every valid sentence has a unique first-word boundary; the bounded loop reaches that boundary, and the cached recursive state contains the remainder by induction. Therefore the root state returns every valid sentence exactly once per distinct cut sequence.

## Complexity detail
Let $n = \lvert\texttt{s}\rvert$, let $D$ be the number of dictionary words, let $S$ be their total character count, and let $R$ be the total number of characters stored across all memoized suffix sentences, including the returned sentences. With maximum word length $L$, set construction costs $O(S)$ and the suffix states spend $O(nL^2)$ time on Python slicing and hashing before sentence construction. Creating the cached strings costs $O(R)$, for $O(S + nL^2 + R)$ time and $O(D + n + R)$ space. The verified bound $L \le 10$ yields the manifest's legal-domain time bound $O(S + n + R)$.

## Alternatives and edge cases
- **Unmemoized backtracking:** reconstructs the same suffix sentence sets repeatedly.
- **Scan every remaining ending boundary:** creates and hashes substrings longer than any legal dictionary word; the candidate's maximum-length bound avoids that work.
- **Boolean word-break DP alone:** decides existence but discards the required sentences.
- **Greedily select one prefix:** misses alternative valid cut sequences.
- Caching an empty tuple for an impossible suffix is important because later callers can then reject it immediately.
- The empty continuation is an internal identity only; it prevents trailing spaces and is never returned for the nonempty source input.
