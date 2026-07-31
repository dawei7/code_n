## General

**Translate the definition into one direct test**

A word qualifies precisely when `s.startswith(word)` is true. This test
simultaneously enforces all required boundaries: comparison begins at index
zero, every character of the word must match, a word equal to `s` succeeds,
and a longer word fails.

Apply that predicate independently to each array entry and add its Boolean
result to the count. Independent processing is necessary because array
positions, rather than distinct string values, are counted. Thus two equal
prefixes contribute two, and no set or deduplication step is appropriate.

For each word the predicate is true exactly under the problem's prefix
definition. Summing one for every true predicate therefore counts every
qualifying occurrence once and counts no non-prefix.

## Complexity detail

Let $S$ be the total number of characters across `words`, as defined in the
function contract. Prefix comparisons inspect at most each word's length, so
the total time is $O(S)$. The running count and iterator state use $O(1)$
auxiliary space.

## Alternatives and edge cases

- **Slice then compare:** Testing `s[:len(word)] == word` is correct, but it creates a temporary substring for every word.
- **Build a trie:** A trie can answer many different target queries, but for one `s` it adds storage and construction without improving the linear bound.
- **Deduplicate words:** A set loses multiplicity and produces the wrong answer when a prefix is repeated.
- **Whole-string equality:** A word exactly equal to `s` is a valid prefix.
- **Longer word:** A word longer than `s` cannot be its prefix.
- **Later substring:** A match beginning after index zero does not count.
- **First-character mismatch:** The comparison can stop immediately for that word.
- **Repeated prefixes:** Every array occurrence contributes independently.
