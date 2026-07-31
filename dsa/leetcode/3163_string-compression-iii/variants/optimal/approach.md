## General

Scan `word` from left to right. At the start of each output chunk, advance an `end` pointer while the character still matches the chunk's first character and the chunk length remains below nine. Append that length and character, then begin the next chunk at `end`.

The inner scan stops for exactly one of three reasons: the input ends, the next character differs, or the current chunk already contains nine copies. In every case, the consumed substring is the longest legal prefix of the remaining input. The next iteration starts immediately after it, so the chunks are disjoint, preserve order, cover all characters, and reproduce the specified compression.

## Complexity detail

Let $n = \lvert\texttt{word}\rvert$. Each input character advances the scan exactly once, so the time complexity is $O(n)$. The returned string can contain two characters for each input character, and the implementation accumulates its pieces before joining them, requiring $O(n)$ space including output construction.

## Alternatives and edge cases

- **Run-length grouping first:** Find an entire equal-character run and then split its length into chunks of at most nine. This is also linear but requires a second loop for each run's chunk emission.
- **Repeated prefix slicing:** Remove `word[:count]` after each chunk. It is correct, but repeatedly copying the unconsumed suffix can take $O(n^2)$ time.
- **Exactly nine copies:** Emit one `9c` chunk; do not create an empty or zero-length follow-up chunk.
- **Runs longer than nine:** Continue with the same character in the next chunk, for example ten `a` characters become `9a1a`.
- **Character changes:** A new character always begins a new chunk even when the preceding chunk contains fewer than nine copies.
- **No compression-size guarantee:** Alternating characters legitimately produce an output twice as long as the input.
