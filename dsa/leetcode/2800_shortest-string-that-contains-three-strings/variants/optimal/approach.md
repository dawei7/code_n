## General

**Merge two strings with maximum directed overlap**

For an ordered pair `(first, second)`, first check whether `second` is already a substring of `first`; if so, adding characters would only make the result longer. Otherwise find the largest $t$ such that the suffix of `first` with length $t$ equals the prefix of `second` with length $t$. Appending only `second[t:]` gives the shortest string that starts with `first` and then incorporates `second` in that order.

**Enumerate the only six possible orders**

An optimal answer induces some left-to-right order in which the three required strings can be considered, allowing ties when one is contained in another. Enumerate all $3! = 6$ permutations. For each order, merge the first two strings and then merge the third into that result. The containment check on the second merge is essential because the third word may already appear inside the combined string.

For a fixed order, using less than the maximum available overlap cannot help: it only appends extra characters while preserving the same ordering constraint. Therefore the two greedy merges produce a shortest candidate for that order. Since every possible order is examined, at least one candidate has globally minimum length.

Compare candidates by `(length, value)`. This selects the shortest result first and, among equal lengths, the lexicographically smallest. Consequently the final candidate satisfies both parts of the required ordering rule.

## Complexity detail

Let $L = \lvert a\rvert + \lvert b\rvert + \lvert c\rvert$. There are only six permutations. With ordinary substring and sliced suffix-prefix comparisons, a merge takes $O(L^2)$ worst-case time, so the constant number of merges remains $O(L^2)$. Candidate and slice storage is $O(L)$.

Each source string has length at most $100$, hence $L \le 300$. That bounded domain is too narrow for a reliable runtime scaling verdict. The package instead uses a bounded-domain certificate backed by exhaustive tiny-alphabet comparison and maximum-length containment cases.

## Alternatives and edge cases

- **Concatenate all six orders without overlap:** This always contains the inputs but can be much longer than necessary.
- **Choose one locally best pair only:** The pair with the largest immediate overlap may force a worse merge with the third word; all six global orders must be considered.
- **Shortest-common-supersequence dynamic programming:** That problem permits interleaving non-contiguous characters, while this task requires each input to remain a substring.
- If one word contains another, the contained word adds no characters.
- Duplicate inputs must not be appended twice.
- Pairwise overlaps can form a cycle, so no single original order is universally correct.
- Equal-length candidates require lexicographic comparison rather than first-found selection.
- An overlap may use the entire second word, which is already handled by the containment check.
