## General
**Move repeated matching work into construction**

A word of length at most $L$ has $L+1$ prefixes and $L+1$ suffixes when the empty boundary is included. Enumerate every `(prefix, suffix)` pair for each word and store its index in a hash map. Later words overwrite earlier entries, which directly preserves the greatest matching index required by the query.

**Use the pair itself as the lookup key**

Store keys as two-string tuples so no separator character can be confused with word content. For a query `f(pref, suff)`, one expected constant-time map lookup returns the precomputed maximum index or the default `-1`.

**Why overwriting finds exactly the maximum index**

Every word contributes a key for every prefix and suffix it possesses, so a query key is present exactly when at least one word matches both conditions. Construction processes words in increasing original-index order. Consequently the final value stored for that key belongs to the last—and therefore greatest-indexed—matching word.

**Account for duplicate words and overlapping affixes**

Repeated strings generate the same keys, and overwriting correctly selects the later duplicate. Prefix and suffix characters may overlap within a short word; enumerating boundaries independently still records that valid combination without special handling.

## Complexity detail
Let `w` be the number of words, `L` their maximum length, and `q` the number of queries. Each word generates $O(L^2)$ prefix-suffix pairs, so construction takes $O(wL^2)$ work and space under bounded string-key costs. Each query is expected $O(1)$, for total $O(wL^2+q)$ time and $O(wL^2)$ space.

## Alternatives and edge cases
- **Combined suffix-prefix trie:** insert rotations such as `suffix + separator + word` while storing the latest index at every node; it uses $O(wL^2)$ construction and answers in $O(|prefix|+|suffix|)$ time with less hash-key duplication.
- **Separate prefix and suffix indexes:** intersect their candidate-index sets per query; large intersections can make queries linear in the word count.
- **Scan words backward per query:** the first match gives the maximum index, but a miss or early-index match costs $O(wL)$ per query.
- **Duplicate words:** later duplicates must win because their indices are greater.
- **No match:** return `-1` rather than an arbitrary stored index.
- **Exact word query:** a full-length prefix and suffix may both name the same word.
- **Overlapping prefix and suffix:** overlap is permitted and does not require disjoint substrings.
- **Empty affix boundary:** including empty prefix and suffix combinations makes the structure robust even when such queries are allowed.
