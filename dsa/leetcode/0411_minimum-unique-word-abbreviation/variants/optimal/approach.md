## General
**Represent kept positions as a bit mask**

A one bit means the target letter at that position remains literal; consecutive zero bits become one numeric token.
The candidate stores the target length as `n` and builds one `difference` mask for each dictionary word of that same
length, ignoring all other words.

**Turn uniqueness into a hitting-set condition**

For each relevant dictionary word, a difference mask has one bits exactly where that word differs from `target`. A
kept-letter `mask` distinguishes the word if and only if their bitwise intersection is nonzero. Therefore, a unique
abbreviation is precisely a mask that hits every difference mask.

**Branch only on an uncovered word's differences**

During `search`, choose an unhit difference mask with the fewest set bits. At least one of those positions must be
kept in every completion, so branch by adding each possible low bit. The candidate memoizes visited kept masks in
`seen` and prunes once `abbreviation_length(mask)` cannot improve `best_length`.

**Measure abbreviation tokens, not decimal characters**

The helper scans a candidate mask from left to right with `i`. A kept letter contributes one token, and each maximal
run of abbreviated positions also contributes one token regardless of how many digits print its count. After the
search, the candidate scans `target` with `i` and flushes each accumulated abbreviated run into `parts` as its
decimal count.

**Why the search returns a minimum unique result**

Every branch adds a bit that is necessary to hit the selected uncovered word, so no valid completion is excluded. A
leaf hits every difference mask and is therefore unique. The search compares every non-pruned feasible token length,
while adding kept positions cannot reduce token count; consequently, the retained leaf is globally minimum. The
constraint that `dictionary` excludes `target` ensures every relevant difference mask has at least one branch bit.

## Complexity detail
Let `d` be the number of same-length dictionary words, `m` the target length stored as `n` by the candidate, and `p`
the number of positions that differ in at least one relevant word. At most $2^p$ kept masks are visited; finding
uncovered words and measuring a mask costs $O(d + m)$, for $O((d + m)2^p)$ worst-case time. Difference masks and
visited states use $O(d + 2^p)$ space.

## Alternatives and edge cases
- **Enumerate all target masks:** checks $2^m$ candidates even when only a few positions can distinguish dictionary
  words.
- **Generate abbreviation strings directly:** duplicates structural work that masks encode compactly.
- **Greedily keep the most common differing position:** can miss the minimum hitting set because local coverage does
  not determine abbreviation token length.
- Dictionary words of another length can never match and are irrelevant.
- An empty relevant dictionary makes the fully numeric abbreviation optimal.
- Several different masks may produce equally short valid answers.
- Adjacent abbreviated positions must form one numeric run.
