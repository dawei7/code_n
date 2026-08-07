## Function Contract

**Inputs**

- `words`: Dictionary words claimed to be in alien lexicographic order.

Let $c$ be the total number of characters across all words, $a$ the number of distinct letters, and $e$ the number of
distinct precedence edges inferred from adjacent words.

**Return value**

Return any valid order of all distinct letters found in `words`, or `""` if the supplied word order is impossible.
