## General
**Compare one current interval from each list:** Keep pointers `i` and `j`. The candidate overlap begins at `max(firstList[i][0], secondList[j][0])` and ends at `min(firstList[i][1], secondList[j][1])`. Append that closed interval when the beginning is at most the ending.

**Discard the interval that ends first:** If the current first-list interval has the smaller endpoint, advance `i`; it cannot intersect any later second-list interval because those intervals start beyond the current second interval's position. Otherwise advance `j`. On equal ending points, advancing either pointer is safe because neither ended interval can overlap a later interval in the opposite disjoint list.

Each iteration records the complete intersection of the current pair when one exists. The interval with the earlier end has then exhausted every possible overlap, so discarding it cannot miss a future result. At least one pointer advances on every iteration, and the scan ends only when one list has no interval left to intersect. Therefore every possible cross-list overlap is produced exactly once and in order.

## Complexity detail
Pointer `i` advances at most $M$ times and `j` at most $N$ times, so time is $O(M+N)$. The returned $K$ intervals use $O(K)$ space; the two pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Test every cross-list pair:** Direct comparison is correct but costs $O(MN)$ time and ignores sorted disjointness.
- **Event sweep line:** Sorting endpoint events can solve more general overlapping collections, but these inputs are already ordered and need no extra sort.
- **Touching endpoints:** Since intervals are closed, equal overlap boundaries produce a valid one-point interval.
- **Empty list:** If either input list is empty, there can be no intersection.
- **One interval contains another:** The overlap is exactly the contained interval, after which the shorter-ending pointer advances.
