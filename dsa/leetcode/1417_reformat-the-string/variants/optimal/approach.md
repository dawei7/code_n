## General
**Separate the two character types.** Collect the letters in one list and the digits in another. An alternating sequence can use at most one more character of one type than of the other. Therefore, if their counts differ by more than one, no valid answer exists.

**Start with the larger group.** When the counts are equal, either type may come first. When one group has one extra character, that group must occupy both the first and last positions. Select the larger group as the first sequence and append one character from each group in turn, adding its final unmatched character when necessary.

The construction preserves every occurrence because each collected character is consumed exactly once. Consecutive output positions come from different groups by construction. The count condition is also sufficient: equal groups pair completely, while a one-character surplus fits at one end. Thus returning empty precisely when the difference exceeds one is correct.

## Complexity detail
Classifying and interleaving the $n$ characters each take $O(n)$ time. The two groups and the output together use $O(n)$ space.

## Alternatives and edge cases
- **Repeated search and removal:** Find the next required type in a mutable character list. It is correct but repeated scans and shifts can take $O(n^2)$ time.
- **In-place swapping:** Place one type at even indices and the other at odd indices. This can reduce temporary grouping but is easier to implement incorrectly when counts differ.
- **Equal counts:** Either a letter or a digit may occupy the first position.
- **One-character input:** A single letter or digit already satisfies the adjacency rule.
- **Duplicate characters:** Preserve multiplicity; character uniqueness is not required.
- **Impossible imbalance:** Two or more extra characters of either type force two same-type neighbors.
- **Semantic output:** Any valid alternating permutation is acceptable, not only the example ordering.
