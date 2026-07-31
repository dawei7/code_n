## General

Only the relative placement of `x` and `y` is constrained. Separate the input characters into three groups: count the occurrences of `y`, retain every character that is neither `x` nor `y`, and count the occurrences of `x`. Then concatenate all copies of `y`, the retained neutral characters, and all copies of `x`.

This construction preserves the input multiset. Every input character enters exactly one of the three groups, the two counted groups reproduce their original multiplicities, and the neutral list reproduces every other character once. In the concatenation, every `y` belongs to the first group and every `x` belongs to the last group, so no `x` can precede a `y`. The result is therefore a valid permutation with the required ordering.

Retaining neutral characters in their original order is not required for correctness, but it makes the construction deterministic without doing additional work.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The algorithm scans the input once and assembles an output of length $n$, taking $O(n)$ time. The neutral-character list and the returned string require $O(n)$ space in the worst case.

## Alternatives and edge cases

- **Directional sorting:** Sort descending when `x < y` and ascending otherwise. This also places `y` before `x`, but costs $O(n\log n)$ time instead of a linear partition.
- **Two filtering passes:** Collect all non-`x` characters after first extracting `y`, then append `x`. This is still linear but scans the input more than once and must avoid duplicating `y`.
- **One distinguished letter absent:** The ordering condition is automatic; the partition still returns a valid permutation.
- **Neither distinguished letter present:** Every character is retained in the middle group, so the result equals `s`.
- **All characters equal `x` or all equal `y`:** The other outer group and the middle group are empty, and multiplicity is preserved.
- **Distinct-letter guarantee:** Because `x != y`, each input character belongs to exactly one partition group.
