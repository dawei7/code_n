## General

**Represent all useful history with one match length.** The stream permits only forward reads, so an algorithm cannot restart from an earlier candidate position after discovering a mismatch. Instead, maintain `matched`: the length of the longest prefix of `pattern` that is also a suffix of every bit consumed so far. This value summarizes exactly the portion of the past that may still grow into the earliest unresolved match.

**Precompute how far a mismatch may fall back.** Build the Knuth-Morris-Pratt prefix function for `pattern`. At pattern index $i$, the table stores the length of the longest proper prefix of `pattern[0..i]` that is also its suffix. If a stream bit disagrees with the next requested bit, replace `matched` with the prefix value for the previous matched position. Repeating that step tests every viable shorter border without reading any stream bit twice.

After all necessary fallbacks, an equal bit extends the current prefix. If `matched` becomes $M$, the last $M$ consumed bits equal the full pattern. If the current stream index is $i$, their start is $i-M+1$.

**Why the returned occurrence is the first.** Stream indices are processed strictly from left to right. Before the algorithm reaches a full match, `matched` retains the longest suffix capable of representing every still-viable overlapping candidate. Therefore no earlier candidate is discarded incorrectly. The first moment `matched` reaches $M$ is exactly the end of the earliest occurrence, so returning immediately produces its first starting index.

## Complexity detail

Let $M=\lvert\texttt{pattern}\rvert$, and let $S$ be the number of bits consumed through the first match. Prefix construction costs $O(M)$. During the stream scan, every increase of `matched` can pay for at most one later fallback, so all KMP transitions across the $S$ bits cost $O(S)$. Total time is $O(S+M)$.

The prefix table uses $O(M)$ auxiliary space. The algorithm does not retain the consumed stream prefix or a length-$M$ sliding window.

## Alternatives and edge cases

- **Explicit sliding window:** Save the latest $M$ bits and compare the entire window after every read. It is easy to express but can require $O(SM)$ time on repetitive streams, which is prohibitive when $M$ reaches $10^4$.
- **Rolling hash:** A rolling binary hash can update each window in constant time, but collision-free correctness requires additional verification or multiple carefully chosen hashes; KMP is deterministic.
- **Restart on every mismatch:** Resetting `matched` directly to zero loses overlapping candidates. A long run of `1` bits while searching for a pattern such as `[1,1,0]` requires retaining a shorter suffix of ones.
- **One-bit pattern:** The prefix table contains one zero, and the scan returns the index of the first equal stream bit.
- **Match at index zero:** Matching after the first $M$ reads returns `M - M`, which is `0`.
- **Maximum pattern length:** The $10^4$-entry pattern fits in the prefix table, and the scan still stores no stream-sized buffer.
- **Deep self-overlap:** Repeated prefix links preserve the longest viable border after each mismatch, so highly periodic patterns do not cause rereads or quadratic fallback work.
