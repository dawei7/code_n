## General
**Scan one prefix position at a time**

Any common prefix must be a prefix of the first string. Visit its characters from left to right. At position `i`, compare the character `c` with `strs[j][i]` in every other string.

The prefix ends immediately if another string has no position `i` or stores a different character there. In either case, `first[:i]` is the answer. If every position of the first string matches, the entire first string is common to the array.

**Why the first failure determines the answer**

Before position `i` is checked, every string matches `first[:i]`. A string that ends at `i` cannot share a longer prefix. Likewise, a mismatch at `i` makes any longer common prefix impossible. Returning `first[:i]` therefore gives a shared prefix that cannot be extended.

If all comparisons succeed, no input string limits the first string, so the first string itself is the longest common prefix.

**Trace the vertical scan**

For `flower`, `flow`, and `flight`, every string contains `f` at position 0 and `l` at position 1. At position 2, the first two strings contain `o`, while `flight` contains `i`. The scan returns `first[:2]`, which is `fl`.

## Complexity detail
Let $S$ be the total number of characters across all input strings. Each string is examined only along the portion that can belong to the common prefix, so the total work is $O(S)$. Apart from the returned slice, the scan stores only `first`, `i`, `j`, and `c`, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Repeated `startswith` while trimming:** compact, but adversarial long near-matches can rescan the same prefix characters and become quadratic.
- **Shrink a retained prefix length after each string:** also runs in $O(S)$ time, but carries mutable boundary state that the vertical scan does not need.
- **Sort the strings:** only the lexicographic minimum and maximum then need comparison, but sorting costs $O(k \log k)$ string comparisons and may mutate input.
- **Trie:** useful when many prefix queries reuse the same corpus, but allocates storage proportional to all characters for a single query.
- **Single or identical strings:** every examined position succeeds, so the first string is returned unchanged.
- **An empty or shorter string:** the length check stops before any out-of-range access and returns the prefix established so far.
