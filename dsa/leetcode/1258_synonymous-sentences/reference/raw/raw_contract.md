## Function Contract

### Inputs

- `synonyms`: A list of unique two-string pairs `[s_i, t_i]`, each declaring its distinct strings equivalent.
- `text`: A sentence containing at most ten words, separated by single spaces.

For the complexity discussion, let $P$ be the number of synonym pairs, $V$ the number of distinct strings appearing in those pairs, $W$ the number of words in `text`, and $K$ the number of returned sentences.

### Return value

Return every possible synonymous sentence in lexicographically ascending order. Each output preserves the number and order of word positions from `text`.
