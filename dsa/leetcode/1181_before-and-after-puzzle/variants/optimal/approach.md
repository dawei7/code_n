## General
**Extract only the boundary words once.** Split every phrase to obtain its first and last word. Also retain the suffix that begins immediately after the first word; this suffix includes its leading space when the phrase has more words and is empty for a one-word phrase.

**Index possible after phrases.** Build a hash map from each first word to the indices of phrases beginning with it. For phrase `i` as the before part, only indices stored under its last word can match. Skip `j == i`, because a phrase cannot be paired with itself. For every other candidate, form `phrases[i] + suffix[j]`, which keeps the shared word from the before phrase and omits its duplicate at the start of the after phrase.

**Deduplicate before sorting.** Insert each merged candidate into a set, so different ordered pairs producing identical text contribute only once. Sorting that set at the end establishes the required lexicographic order. Duplicate input text at different indices remains usable because the map stores indices rather than unique phrase strings.

## Complexity detail
Parsing and indexing examine $S$ characters. Hash lookup avoids testing incompatible pairs; constructing all compatible candidates processes $G$ characters. Sorting the $R$ distinct results costs $O(R\log R)$ comparisons under the usual string-key abstraction, giving $O(S+G+R\log R)$ time. Parsed phrases, the boundary index, and generated strings use $O(S+G)$ space.

## Alternatives and edge cases
- **Test every ordered pair:** This is straightforward and correct but performs $O(n^2)$ boundary comparisons even when no phrases can match.
- **Deduplicate input phrases first:** This is incorrect because equal text at different indices may pair with one another while a lone phrase may not pair with itself.
- **One-word phrase:** Its first and last word are the same, and its after suffix is empty.
- **Pair direction:** `(i, j)` and `(j, i)` are separate possibilities and may yield different puzzles.
- **Duplicate merged results:** Multiple pairs may create the same text; only one copy belongs in the result.
- **No compatible boundary:** The correct result is an empty list.
- **Shared word placement:** The matching word appears once, with the remaining words of the after phrase appended in order.
