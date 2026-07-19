## General
**Represent kept positions as a bit mask**

A one bit means the target letter at that position remains literal; consecutive zero bits become one numeric token. Only dictionary words with target length `m` can match an abbreviation of the target, so ignore all other lengths.

**Turn uniqueness into a hitting-set condition**

For each relevant dictionary word, build a difference mask whose one bits are positions where it differs from `target`. A kept-letter mask distinguishes that word exactly when their bitwise intersection is nonzero. Therefore a unique abbreviation is a mask that hits every difference mask.

**Branch only on an uncovered word's differences**

During backtracking, choose an unhit difference mask—preferably one with few bits. At least one of those positions must be kept in every completion, so branch by adding each possible bit. Memoize visited kept masks and prune once their abbreviation token length cannot improve the best known result.

**Measure abbreviation tokens, not decimal characters**

Scan a candidate mask from left to right. A kept letter contributes one token, and each maximal run of abbreviated positions also contributes one token regardless of whether its printed count has one or two digits. Convert the best mask afterward by flushing each zero run as its decimal count.

**Why the search returns a minimum unique result**

Every branch adds a bit required to hit the selected uncovered word, so no valid completion is excluded. A leaf hits all difference masks and is therefore unique. The search compares every non-pruned feasible token length, while pruning uses the fact that adding kept positions cannot reduce token count, so the retained leaf is globally minimum.

## Complexity detail
Let `d` be the number of same-length dictionary words, `m` the target length, and `p` the number of positions that differ in at least one such word. At most $2^{p}$ relevant masks are visited; checking differences and measuring a mask costs $O(d + m)$, for $O((d + m)2^p)$ worst-case time. Difference masks and visited states use $O(d + 2^p)$ space.

## Alternatives and edge cases
- **Enumerate all target masks:** checks $2^{m}$ candidates even when only a few positions can distinguish dictionary words.
- **Generate abbreviation strings directly:** duplicates structural work that masks encode compactly.
- **Greedily keep the most common differing position:** can miss the minimum hitting set because local coverage does not determine abbreviation token length.
- Dictionary words of another length can never match and are irrelevant.
- An empty relevant dictionary makes the fully numeric abbreviation optimal.
- Several different masks may produce equally short valid answers.
- Adjacent abbreviated positions must form one numeric run.
