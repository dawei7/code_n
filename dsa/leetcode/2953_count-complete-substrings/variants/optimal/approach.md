## General

**Separate the adjacency constraint first.** If two neighboring letters differ
by more than two alphabet positions, no complete substring can cross that
boundary. Split `word` into maximal segments whose consecutive differences are
all at most two. Every substring wholly inside one segment automatically
satisfies the adjacency rule, so the remaining work is purely frequency based.

**A distinct-count choice fixes the window length.** Suppose a complete
substring contains exactly $d$ distinct letters. Because every present letter
must occur exactly `k` times, its length is exactly $d\cdot\texttt{k}$. The
lowercase alphabet limits $d$ to the 26 values from 1 through 26. For each
choice, slide a fixed-size window of that length through the current segment.

**Maintain how many letters occur exactly k times.** Store the 26 letter
frequencies and a counter `exactly_k`. Before and after adding or removing a
letter, update that counter when its frequency crosses `k`. A full window of
length $d\cdot\texttt{k}$ is complete exactly when `exactly_k == d`: those $d$
letters already account for every position in the window, so no additional
letter can have a positive count. Conversely, any complete window with $d$
distinct letters meets this test in the corresponding pass. Segmenting and
fixed-length enumeration therefore count every complete substring exactly once.

## Complexity detail

Let $N=\lvert\texttt{word}\rvert$. Each position participates in at most 26
sliding-window passes, a constant determined by the alphabet, so total time is
$O(N)$. The 26-entry frequency array and scalar counters use $O(1)$ auxiliary
space.

## Alternatives and edge cases

- **Enumerate every substring:** Updating a frequency table for every left endpoint is correct but takes $O(N^2)$ time.
- **One variable-length window:** Completeness is not monotone as a window grows, so a single ordinary shrink rule cannot represent all possible distinct counts.
- **Alphabet gap greater than two:** Such a neighboring pair is a hard segment boundary; no valid substring may include both positions.
- **Alphabet gap equal to two:** The rule is inclusive, so the pair remains within one segment.
- **Frequency above k:** A letter occurring more than `k` times makes that window incomplete even if other letters occur exactly `k` times.
- **One distinct letter:** Runs of exactly `k` copies are tested by the $d=1$ pass and may overlap.
- **k larger than a segment:** No window in that segment can be complete, and the first candidate length already exceeds it.
