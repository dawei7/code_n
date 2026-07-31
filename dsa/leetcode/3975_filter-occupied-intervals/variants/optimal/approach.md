## General

The requested output describes a set of integer points, so adjacent occupied points must share one interval in its minimum representation. After sorting by start and then end, a new interval `[start, end]` belongs to the current merged component whenever `start <= current_end + 1`. This single condition covers both ordinary overlap and the problem's discrete touching rule. If it holds, extend the current end to `max(current_end, end)`; otherwise, begin the next component.

Because the intervals are sorted, every interval already processed starts no later than the next one. The current merged interval therefore contains exactly the connected occupied component at the end of the processed prefix, and no future interval can connect to an earlier closed component without first connecting to the current one. The merge pass consequently produces the unique minimum interval representation of the entire occupied set.

Subtract `[freeStart, freeEnd]` from each merged interval `[start, end]` independently. If the two intervals are disjoint, keep the occupied interval unchanged. Otherwise, a left remainder exists exactly when `start < freeStart`, and its inclusive bounds are `[start, freeStart - 1]`. A right remainder exists exactly when `end > freeEnd`, with bounds `[freeEnd + 1, end]`. These strict tests also handle complete removal, one-sided trimming, and a split into two pieces without emitting an empty interval.

The merged components were sorted and separated by at least one unoccupied integer point. Removing points cannot join distinct components, and each retained piece is maximal within its component. Appending the left piece before the right piece therefore yields sorted, pairwise non-overlapping intervals with exactly the original occupied points outside the free interval and with no avoidable split.

## Complexity detail

Let $n = \lvert\texttt{occupiedIntervals}\rvert$. Sorting takes $O(n\log n)$ time. The merge and subtraction passes each take $O(n)$ time, so the total is $O(n\log n)$. The sorted copy, merged components, and returned intervals use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Endpoint event sweep:** Recording starts and ends as events can reconstruct the occupied union, but it still needs sorting and makes inclusive touching and removal boundaries more cumbersome than direct interval merging.
- **Repeated unsorted merging:** Scanning all existing components for every input interval can be correct, but it degrades to $O(n^2)$ time.
- **Touching versus a real gap:** `[1,1]` and `[2,2]` merge, while `[1,1]` and `[3,3]` remain separate because integer point `2` is unoccupied.
- **Complete removal:** When a merged interval lies wholly inside the free interval, neither strict remainder test succeeds, so it contributes nothing.
- **Free interval strictly inside a component:** Both remainder tests succeed and produce two intervals separated by the removed points.
- **Inclusive endpoints:** A retained side ends at `freeStart - 1` or begins at `freeEnd + 1`; retaining either free endpoint would violate the contract.
- **Duplicate and nested intervals:** Sorting and taking the maximum end absorbs them without creating duplicate output components.
- **Maximum coordinates:** The algorithm adds one only to a merged end that is below a later legal start, and constructs `freeEnd + 1` only when an occupied end is larger, so every emitted endpoint remains within the stated domain.
