## General

**Represent prefixes as integers.** Removing the last decimal digit with integer division by `10` walks from a number through all of its nonempty prefixes. For example, repeated division transforms `12345` into `1234`, `123`, `12`, and `1`. Insert every value reached from every member of `arr1` into a set.

**Find the best prefix for each value in the second array.** Starting from a value in `arr2`, repeatedly discard its last digit until the remaining integer occurs in the set or becomes `0`. Because this search examines prefixes from longest to shortest, its first set match is the longest prefix that this value shares with any member of `arr1`. Update the answer with the matched integer's digit count.

Every stored integer is a prefix of at least one first-array value. Therefore, each reported match is a valid common prefix of a cross-array pair. Conversely, suppose an optimal pair shares a prefix `p`. The construction inserts `p` while processing that pair's first-array value, and the shortening search for its second-array value reaches `p` unless it encounters an even longer stored prefix first. The algorithm therefore finds a prefix at least as long as every valid candidate, while never counting an invalid one.

## Complexity detail

Let $n=\lvert\texttt{arr1}\rvert$, $m=\lvert\texttt{arr2}\rvert$, and let $d$ be the maximum decimal digit count. Each value yields at most $d$ prefixes, so construction and lookup take $O((n+m)d)$ time. The set contains at most $nd$ distinct prefixes and therefore uses $O(nd)$ auxiliary space.

## Alternatives and edge cases

- **Digit trie:** Insert the decimal strings from one array into a trie and walk each value from the other array. This has the same asymptotic bounds but requires explicit nodes and child maps.
- **String-prefix hash set:** Building strings one character at a time also gives $O((n+m)d)$ work under the bounded digit length, but integer division avoids creating a separate string for every prefix.
- **Compare every pair:** Computing a longest common prefix for all $nm$ cross-array pairs is correct but costs $O(nmd)$ time and does not scale to the array limits.
- **No matching first digit:** No nonempty common prefix can exist, so shortening every second-array value eventually reaches `0` and the result remains `0`.
- **One value is the full prefix:** If `123` is paired with `123456`, the whole shorter number is a valid prefix of length `3`.
- **Equal values and duplicates:** Equal integers from different arrays share all of their digits; repeated occurrences do not change the maximum.
- **Same-array matches:** Prefixes are stored from one array and queried only with the other, so similarities confined to a single array cannot affect the answer.
- **Largest legal value:** `100000000` has nine digits, and the same repeated-division process handles it without a special case.
