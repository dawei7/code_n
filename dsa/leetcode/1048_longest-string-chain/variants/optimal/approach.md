## General
**Process possible predecessors first:** Sort the words by length. Any predecessor is exactly one character shorter, so its best chain length is already known before the current word is processed.

**Generate every immediate predecessor:** For each index in a word, form the string obtained by deleting that one character. These are precisely all strings that could become the word by one insertion while preserving the other characters' order. Look up each candidate in a map from processed words to their longest ending-chain lengths.

**Extend the best available chain:** Initialize the current word's chain length to one. For every generated predecessor present in the map, consider its stored length plus one. Store the maximum under the current word and update the global answer.

Every transition used by the algorithm is valid because inserting the deleted character reconstructs the current word without reordering the predecessor. Conversely, the previous word in any valid chain must be obtainable by deleting the one inserted character, so it appears among the generated candidates. Induction over increasing word length therefore proves that each stored value is the longest chain ending at that word and that the global maximum is optimal.

## Complexity detail
Sorting $W$ words costs $O(W log W)$ comparisons. For a word of length at most $L$, there are $L$ deletion positions and constructing each candidate string costs $O(L)$, for $O(WL^2)$ additional time. The map stores up to $W$ strings and chain lengths, using $O(WL)$ space.

## Alternatives and edge cases
- **Pairwise predecessor testing:** Compare every word with every one-character-longer word using two pointers. Each comparison costs $O(L)$ and the total can reach $O(W^2L)$.
- **Top-down memoization:** Build successor relationships or test candidates recursively and cache each word, but efficient successor discovery still needs careful indexing.
- **Length buckets:** Group words by length before deletion lookup. This can replace the full sort because lengths are bounded, while preserving the same dynamic program.
- **Single word:** It forms a valid chain of length one.
- **Same-length words:** Neither can be a predecessor of the other because exactly one insertion must increase length.
- **Character order:** Inserting a letter may occur anywhere, but all existing characters must retain their relative order.
- **Branching chains:** Several predecessors may reach one word; only the greatest stored chain should be extended.
- **Missing intermediate word:** A longer word cannot skip a length, because every adjacent chain step inserts exactly one letter.
