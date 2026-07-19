## General
**Restrict the target using the first domino:** If a value can fill an entire row, it must appear on either half of every domino. In particular, it must equal `tops[0]` or `bottoms[0]`. These are therefore the only candidates that need validation, regardless of the row length.

**Count both possible destination rows:** For one candidate `target`, scan paired values `top` and `bottom`. If neither equals `target`, that candidate is impossible. Otherwise, a top-row solution must rotate exactly those dominoes whose top differs from `target`, while a bottom-row solution must rotate exactly those whose bottom differs. The smaller counter is the best result for this candidate.

**Choose the best feasible candidate:** Validate both values from the first domino and take the minimum finite count. Return `-1` only when both fail. If the first domino shows the same number on both halves, evaluating it twice is harmless and still constant extra work.

Any uniform final row must use one of the two candidates, and the scan determines the forced rotations for each destination row. Consequently, the minimum across these exhaustive possibilities cannot omit a better arrangement and never counts an unnecessary rotation.

## Complexity detail
At most two candidates are checked, and each check visits all $N$ dominoes once, giving $O(N)$ time. The candidate values and two rotation counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Validate every observed value:** Trying each of the $2N$ top and bottom entries as a candidate is correct but can repeat the same full scan and take $O(N^2)$ time.
- **Frequency tables:** Counting top, bottom, and double occurrences for the six face values also gives $O(N)$ time, but needs more bookkeeping than validating the first domino's candidates.
- **Already uniform row:** Its rotation count is zero and must win even if the other row can also be made uniform.
- **Candidate missing from one domino:** Reject it immediately because rotating that domino cannot create a value absent from both halves.
- **Equal halves:** Rotating a domino whose two halves match changes nothing and is never required.
