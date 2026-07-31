## General

Split `p` at its unique star into a fixed `prefix` and a fixed `suffix`. A matching substring must contain the prefix first, followed by whatever the star absorbs, followed by the suffix. The wildcard may absorb nothing, so the suffix search is allowed to begin exactly where the prefix ends.

Find the earliest occurrence of `prefix` in `s`. If it does not exist, no match is possible. Otherwise, search for `suffix` starting at `prefix_start + len(prefix)`. Finding it proves that the text between the two fixed fragments can be assigned to the star.

Using the earliest prefix is sufficient. Every later occurrence ends no earlier because all prefix occurrences have the same length. Therefore, if a suffix can follow any occurrence of the prefix, that same suffix also lies at or after the end of the earliest occurrence. Conversely, two occurrences returned in this order directly define a matching substring, so the test has no false positives.

Empty fragments need no special branches. Native substring search finds an empty prefix at position zero and an empty suffix at the requested starting position. This exactly models a star at either end of the pattern.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert p\rvert$. Splitting the pattern takes $O(m)$ time and storage. The two forward substring searches inspect the text and fixed pattern fragments in $O(n+m)$ total time under the linear native string-search bound used by this branch. The stored prefix and suffix occupy $O(m)$ space.

The benchmark defines `size` as $n$ and uses legal 10-, 20-, and 40-character tiers, spanning 4x. Each pattern has a long repeated prefix and a final `"b"` that is absent from the all-`"a"` text. The accepted two-search method stays within the required bound. A correct slower method that enumerates every substring and compares its fixed fragments explicitly revisits cubic total character work on these tiers and fails only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every substring:** Testing all $O(n^2)$ substrings against both fixed fragments is correct but repeats avoidable work.
- **Regular expression:** Translating the star to a regex can work, but escaping, anchoring the candidate substring, and engine-specific backtracking make it less direct.
- **Dynamic programming wildcard matcher:** General wildcard DP handles many stars and `?` symbols, but this contract has exactly one star and needs only ordered fragment searches.
- **Empty wildcard replacement:** The suffix search begins at the prefix end, so adjacent fixed fragments are accepted.
- **Star at the beginning:** The empty prefix is found at position zero, after which only the suffix must occur.
- **Star at the end:** The empty suffix is found immediately after any prefix occurrence.
- **No overlap between fragments:** The suffix cannot consume characters already used by the fixed prefix; starting its search at the prefix end enforces this.
- **Occurrence order:** A suffix found only before the prefix cannot witness a match.
