## General

A conventional subsequence dynamic program could record the best answer ending at every source position, but future characters do not need to know that position. They need only the final chosen letter and the length already achieved.

**Compress positions into 26 ending states.** Let `best_ending_at[x]` be the maximum length of an ideal subsequence found so far whose last letter has alphabet index `x`. When the current letter has index `c`, it may follow any state with an ending index in the closed interval from `c - k` through `c + k`, clipped to the alphabet boundaries.

Take the largest length across that interval and append the current character. This creates a candidate of length one greater. Updating only `best_ending_at[c]` preserves the source order because the scan processes characters from left to right; every state used by the transition comes from the current or an earlier source position.

**Why an in-place update is safe.** The interval can include `c` itself. Reading the old value and then writing `old + 1` correctly appends another occurrence of the same letter. No other ending state changes during this character, so the current occurrence cannot be reused through a chain of multiple transitions.

Every ideal subsequence ending at the current character has some previous final letter within the permitted interval, so the transition considers its prefix. Conversely, extending any considered state by the current character satisfies the adjacency condition. The maximum of the 26 states after the scan is therefore the longest ideal subsequence length.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each character examines at most 26 fixed alphabet states, so the time is $O(26n) = O(n)$. The state array always contains 26 integers, which is $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Position-based dynamic programming:** Comparing each character with all earlier positions directly mirrors the subsequence definition, but it requires $O(n^2)$ time and $O(n)$ space.
- **Segment tree over letters:** Range maxima and point updates could reduce each transition to $O(\log 26)$, but the fixed 26-letter domain makes that structure unnecessary.
- **Zero `k`:** Adjacent chosen letters must be identical, so the answer is the greatest frequency of one letter.
- **Maximum `k`:** With `k = 25`, every pair of lowercase letters is compatible and the whole string can be retained.
- **Noncyclic alphabet:** Range clipping is essential; compatibility does not wrap between `'a'` and `'z'`.
- **Single character:** A one-character string is itself an ideal subsequence of length one.
