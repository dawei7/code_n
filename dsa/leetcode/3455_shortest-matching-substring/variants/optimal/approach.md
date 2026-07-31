## General

Splitting `p` at its two stars produces three literal blocks: `first`, `middle`, and `last`. A matching substring must contain one occurrence of each block in that order. The blocks cannot overlap: the first occurrence must end no later than the middle occurrence starts, and the middle occurrence must end no later than the last occurrence starts. Empty blocks occur at every boundary of `s`, including the boundary after its final character.

Use the Knuth-Morris-Pratt prefix function to list every start position of each nonempty block in `s`. KMP retains the longest reusable matched prefix after a mismatch or a complete occurrence, so overlapping occurrences are found without rescanning text characters. For an empty block, directly list all $n+1$ text boundaries.

Now traverse the middle-block starts in increasing order. Advance a pointer through the first-block starts while those occurrences end no later than the current middle start; the last consumed occurrence is the latest compatible first block and therefore gives the shortest possible left end for this middle occurrence. Independently advance a pointer through last-block starts that lie before the middle block ends; the first remaining occurrence is the earliest compatible last block and gives the shortest possible right end. These choices minimize the candidate for the fixed middle occurrence, and examining every middle occurrence therefore finds the global minimum. All three pointers move only forward.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert p\rvert$. Building the three KMP prefix arrays costs $O(m)$ in total, and the three searches cost $O(n)$ because there are only three literal blocks. The linking scan traverses the occurrence lists once, also in $O(n)$ time. Total time is $O(n+m)$. Prefix arrays and occurrence lists use $O(n+m)$ space.

## Alternatives and edge cases

- **Checking every text position:** Comparing each literal block character by character at every possible start can take $O(nm)$ time on repetitive strings.
- **Trying every substring:** Enumerating substring boundaries and then wildcard-matching each candidate is far beyond the $10^5$ limits.
- **Binary search on the answer:** A fixed-length feasibility check is possible, but it adds a logarithmic factor and still needs efficient block-occurrence preprocessing.
- **Pattern `**`:** All three blocks are empty, so boundary zero supplies a valid empty match of length $0$.
- **Empty outer block:** When `first` or `last` is empty, the chosen substring may start at the middle block or end immediately after it.
- **Empty middle block:** Every text boundary is a candidate bridge between the first and last literal blocks.
- **Overlapping occurrences:** KMP reports overlaps, while the pointer inequalities still prohibit the three selected blocks themselves from overlapping.
- **Missing block:** If any required nonempty literal has no compatible occurrence, no candidate is formed and the result is `-1`.
