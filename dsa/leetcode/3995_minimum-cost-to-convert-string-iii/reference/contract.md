## Function Contract

**Inputs**

- `source`: The original lowercase English string.
- `target`: The desired lowercase English string, with the same length as `source`.
- `rules`: A nonempty array of `[pattern, replacement]` string pairs.
- `costs`: A positive base cost for each rule at the same index.

Each pattern and its replacement have equal length. A pattern contains lowercase English letters and `'*'` wildcards, including at least one letter and at most five wildcards; every replacement contains only lowercase English letters.

Let $n=\lvert\texttt{source}\rvert$, $R=\lvert\texttt{rules}\rvert$, and let $L$ be the maximum pattern length.

**Return value**

Return the minimum sum of application costs that transforms `source` into `target` using pairwise disjoint ranges. Each application's charge is its base cost plus its pattern's wildcard count. Return `-1` if the transformation is impossible.
