## General
**Word extraction performs spacing normalization before reversal**

Extract nonempty words by splitting on whitespace without a literal single-space separator. This discards leading/trailing whitespace and collapses internal runs conceptually into one boundary. Using `split(" ")` would instead produce empty fields between repeated spaces.

**Reverse whole-word positions, not characters**

Traverse or reverse the extracted word list. Each word remains an unchanged substring; only its position among words changes. Character-level reversal would produce different words and requires a second repair step.

**One join establishes all output-space guarantees**

Join the reversed sequence with exactly one ordinary space. Join inserts separators only between elements, so it creates neither leading nor trailing whitespace.

**Extracted and emitted word sequences preserve content exactly**

After appending `k` output words, they are exactly the final `k` input words in reverse order, with one separator between adjacent words and no extra separators.

**Trace a run of several spaces**

For `"a good   example"`, extraction yields `['a','good','example']` with no empty words. Reversing gives `['example','good','a']`, and joining yields `"example good a"`.

**Normalized tokens determine the unique output**

Word extraction yields every maximal non-space token exactly once, in its original order, while discarding only separator whitespace. Reversing that list changes no word content and places the words in precisely the required order. Joining with one literal space then creates the unique normalized result: no leading or trailing space and exactly one space between adjacent words.

## Complexity detail
Splitting, reversing, and joining inspect or copy a total linear number of characters. The word list and returned string require $O(n)$ space because Python strings are immutable.

## Alternatives and edge cases
- **Manual two-pointer scan:** offers precise control and is useful in mutable-buffer languages, but Python's word extraction already expresses the invariant safely.
- **Reverse all characters twice:** can be in-place with mutable storage, but Python must allocate a new string anyway.
- **Literal `split(" ")`:** incorrectly retains empty fields for repeated spaces.
- A one-word string returns that word without surrounding spaces. Arbitrarily long space runs collapse to one separator.
- The LeetCode contract guarantees at least one word; a broader all-whitespace input would naturally produce an empty output under this extraction method.
