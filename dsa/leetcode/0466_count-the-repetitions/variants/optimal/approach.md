## General

**Match target characters across source-block boundaries**

Scan one copy of `s1` at a time while `target_index` identifies the next required character of `s2`. A match advances that position. Reaching the end of `s2` completes one target copy, increments `completed`, and resets `target_index` to zero. Keeping the position between source blocks naturally permits one target copy to begin in one copy of `s1` and finish in another.

If `s2` contains a character absent from `s1`, even infinitely many source blocks cannot complete the target, so the initial alphabet check returns zero. Conversely, when every target character occurs in `s1`, repeatedly scanning source blocks will eventually encounter the target characters in order.

**A block-boundary position determines the future**

At the end of a source block, `target_index` is the only matching state that affects later work. If the same position appears after two different block counts, the interval between those boundaries is a cycle: every traversal consumes the same number of `s1` blocks and completes the same number of `s2` copies.

The `seen` map stores the first `(blocks, completed)` pair for each boundary position, including position zero before any source block. When a position repeats, subtract the stored counters to obtain `cycle_blocks` and `cycle_completed`. Skip the largest whole number of cycles that fits in the remaining `n1` blocks, then scan the short remainder normally. Clearing `seen` after the jump prevents redundant cycle processing; the unskipped remainder is shorter than the discovered cycle.

**Convert matched copies into requested groups**

The scan counts individual copies of `s2`, while one output unit contains `n2` copies. Therefore `completed // n2` is exactly the largest complete number of target groups obtainable as a subsequence.

## Complexity detail

There are only $\lvert\texttt{s2}\rvert$ possible boundary positions before one repeats. Cycle discovery and the leftover scan together process $O(\lvert\texttt{s2}\rvert)$ source blocks, with $O(\lvert\texttt{s1}\rvert)$ work per block, for $O(\lvert\texttt{s1}\rvert \cdot \lvert\texttt{s2}\rvert)$ time independent of a potentially huge `n1`. The boundary-state map uses $O(\lvert\texttt{s2}\rvert)$ space. The alphabet sets occupy constant space because both strings use only the 26 lowercase English letters.

## Alternatives and edge cases

- **Scan all `n1` source blocks:** uses constant matching state and is correct, but costs $O(\texttt{n1} \cdot \lvert\texttt{s1}\rvert)$ time and fails the scaling benchmark.
- **Precompute every target-position transition:** builds a finite-state transition table, then still needs cycle detection or binary lifting to handle large `n1`.
- **Materialize repeated strings:** consumes memory proportional to the repetition counts and is infeasible at the limits.
- **Missing target character:** makes the answer zero regardless of either repetition count.
- **Cross-block target match:** requires preserving `target_index`; resetting it after each source copy would miss valid subsequences.
- **Incomplete target copy or group:** contributes nothing unless the whole `s2` copy and then the whole group of `n2` copies are complete.
