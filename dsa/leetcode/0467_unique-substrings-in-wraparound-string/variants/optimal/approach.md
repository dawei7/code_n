## General
**Track the current cyclic run**

Scan `p` from left to right. If the current letter follows the previous one modulo 26, extend the valid run; otherwise reset its length to one. The modulo test treats `z -> a` as consecutive alongside ordinary alphabet neighbors.

**Summarize substrings by their ending letter**

For each of the 26 letters, store the longest valid run seen that ends with that letter. A run of length `L` ending in letter `c` contributes exactly one valid substring of each length `1` through `L` ending in `c`.

**Why only the maximum is needed**

In the infinite wraparound sequence, an ending letter and a length uniquely determine the substring: preceding characters are forced by cyclic order. Therefore a shorter run ending at the same letter contributes only strings already included by a longer run. Taking the maximum avoids duplicates, and summing the 26 maxima counts every distinct valid substring exactly once by its final letter.

## Complexity detail
The scan performs constant work for each of `n` characters, giving $O(n)$ time. The table has exactly 26 entries, so auxiliary space is $O(1)$ relative to input length.

## Alternatives and edge cases
- **Enumerate valid substrings in a set:** is direct but creates quadratically many substring occurrences and stores many strings.
- **Dictionary by ending character:** expresses the same dynamic program with $O(26)$ keys instead of an array.
- **Suffix trie:** deduplicates substrings but is far larger than needed because cyclic order makes characters deterministic.
- **Empty string:** contains no nonempty substring and returns zero.
- **Repeated occurrence:** only a longer run for the same ending letter can add new strings.
- **`z` followed by `a`:** must extend the run through modular adjacency.
- **Broken adjacency:** reset to length one because the current character itself remains a valid substring.
