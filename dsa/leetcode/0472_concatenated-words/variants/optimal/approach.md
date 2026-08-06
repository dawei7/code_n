## General

**Build a prefix-search structure in length order**

Sort the distinct words by length. A trie initially contains no words; after a word is checked, insert its characters
and mark its terminal node. Thus the trie used for a candidate contains every shorter input word. A previously
inserted word of the same length cannot match the whole candidate because the input strings are unique, and it
cannot be one piece of a longer concatenation because every piece is nonempty.

Each trie node stores its outgoing characters in `children` and records a complete dictionary word with `is_word`.
Following trie edges from a position tests all dictionary prefixes beginning there without constructing and hashing
every possible substring.

**Combine trie walks with word-break reachability**

For a word of length `length`, let `reachable[end]` mean that `word[:end]` can be assembled from words already in the
trie. Set `reachable[0]` to true. For every reachable `start`, begin at the trie root and follow `word[end]` from
`start` toward the end of the word. Stop that walk as soon as the required edge is absent. Whenever a visited node
has `is_word` set, mark `reachable[end + 1]`.

Stop the outer scan once `reachable[-1]` becomes true: another segmentation cannot change the classification. If the
full position is never reached, the word is not concatenated. Insert the checked word afterward regardless of that
result, because a concatenated word may itself be a component of a later, longer word.

**Why the reachability result is exact**

Every transition begins at an already reachable prefix and ends at a terminal trie node, so it appends exactly one
nonempty word from the input dictionary. Chaining those transitions therefore constructs the candidate without gaps
or leftover characters. Because the candidate itself was absent during its check, a successful chain cannot consist
of the candidate as one piece; it necessarily contains at least two shorter words.

Conversely, consider any valid concatenation. All of its components are shorter than the complete word and are
already in the trie. Starting from `reachable[0]`, the trie walk recognizes the first component and marks its ending
position. Repeating the same argument for each component eventually marks the full length, so no valid concatenated
word is omitted.

## Complexity detail

Let $L_w = \lvert w \rvert$ for each word $w$, and let

$$
S = \sum_{w \in \texttt{words}} L_w.
$$

For one word, at most $L_w$ reachable starts each advance through at most $L_w$ trie edges. Trie insertion takes
$O(L_w)$ additional time. Across the input, the word checks and insertions therefore take
$O(\sum_w L_w^2)$ time. Sorting the distinct lowercase words by their integer lengths does not exceed that bound on
the source domain.

The trie contains at most $S$ character nodes. The sorted list and result contain references to at most all input
words, and the largest reachability array has one entry per character of its word. Total auxiliary space is $O(S)$.

## Alternatives and edge cases

- **Hash-set substring DP:** the protected and immutable Accepted implementations use the same length ordering and
  reachability recurrence, but Python must allocate and hash each `word[start:end]`. Those linear substring costs can
  raise actual worst-case time to $O(\sum_w L_w^3)$ despite the two explicit boundary loops.
- **Memoized DFS with a trie:** explores the same reachable suffix positions recursively with comparable polynomial
  work, but the iterative array makes progress and stack usage explicit.
- **Unmemoized decomposition search:** recomputes the same suffix after many overlapping prefixes and can take
  exponential time.
- **Build the trie from every word first:** arbitrary processing order is possible, but the check must then count
  pieces or explicitly reject the one-piece match of the word with itself.
- **Repeated components:** a trie terminal may be used from multiple reachable starts, so a valid source word can be
  reused as many times as necessary.
- **Multiple valid segmentations:** reachability records only whether an ending position is possible; the output still
  contains the candidate once.
- **Output order:** length-ordered processing may return the valid set in a different order from the input, which the
  contract permits.
