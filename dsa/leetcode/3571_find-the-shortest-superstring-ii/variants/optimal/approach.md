## General

There are only two possible relative orders unless one string is already contained in the other: place `s1` before `s2`, or place `s2` before `s1`. For a fixed order, the shortest merge reuses the longest suffix of the first string that equals a prefix of the second. Any shorter overlap would append more characters, and any longer reuse is invalid.

Compute containment and boundary overlap together with a KMP prefix function. For an ordered pair `(first, second)`, build `second + "#" + first`, where `#` cannot occur in either lowercase input. While constructing its prefix array, reaching a prefix length of `len(second)` inside the `first` portion proves that `second` occurs within `first`. The final prefix value is exactly the longest suffix of `first` matching a prefix of `second`.

Run that process in both directions. If either containment test succeeds, return the containing string. Otherwise create both boundary merges by appending only the non-overlapping suffix of the second string. Returning the shorter candidate is optimal because every valid superstring must realize one of the two orders, and each candidate is already the shortest merge for its order. Equal-length candidates are both permitted.

## Complexity detail

Each combined KMP string has length $m+n+1$. Prefix-function fallback never moves more often than the forward scan advances, so the two directional computations take $O(m+n)$ time. Constructing the candidates is also linear. The prefix arrays and returned string use $O(m+n)$ space.

The benchmark size is the common input length $S$. Its strings force every candidate overlap in a direct descending scan to compare almost all participating characters before failing. KMP remains $O(S)$, while that correct alternative performs $\Theta(S^2)$ character comparisons.

## Alternatives and edge cases

- **Descending overlap scan with slicing:** It is concise and correct, but comparing every possible suffix-prefix length can take $O((m+n)^2)$ time.
- **Concatenate without overlap:** This is valid only when neither direction has a non-empty boundary match; otherwise it is not shortest.
- **One string contained in the other:** Return the containing string even when the occurrence is in its middle rather than at a boundary.
- **Identical strings:** Either containment check returns that unchanged string.
- **Directional overlap:** The best reuse can differ by order, so both `s1`-then-`s2` and `s2`-then-`s1` must be evaluated.
- **Equal-length optima:** The contract allows either candidate; no lexicographic tie-break is required.
- **Single-character inputs:** They follow the same containment and overlap rules without special indexing.
