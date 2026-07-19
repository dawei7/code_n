## General
**Sort starts so one adjacent conflict is enough**

Sort by start time. Any overlap must then appear between a meeting and its immediate predecessor; there is no need to compare every pair.

Before inspecting index `i`, all meetings through $i - 1$ are mutually compatible. The invariant continues exactly when `intervals[i].start >= intervals[i - 1].end`.

**A compatible prefix needs only its last meeting checked**

If the next meeting overlaps the previous sorted meeting, the schedule is immediately impossible. Otherwise, assume the earlier prefix was compatible. Its meetings finish in the same nonoverlapping sequence before the previous meeting starts, and the previous meeting finishes no later than the new start. The extended prefix is therefore also compatible. Induction makes the adjacent checks sufficient for the entire schedule.

## Complexity detail
Sorting costs $O(n \log n)$ and the scan costs $O(n)$. Creating a sorted copy uses $O(n)$ space.

## Alternatives and edge cases
- **Compare every pair:** is correct but takes $O(n^2)$ time.
- Empty and one-meeting schedules are valid; touching endpoints do not overlap.
