## General

**Represent equal prefixes once.** A trie node reached after reading $k$ characters represents one distinct length-$k$ prefix. Store at that node the number of input words whose path passes through it. Inserting a word creates missing child nodes and increments the count after consuming each character.

**Read scores from the same paths.** Once all words have been inserted, traverse each word from the root again. The node after its first character stores that one-character prefix's score, the next node stores its two-character prefix's score, and so on. Summing those node counts therefore gives exactly the requested answer.

Every non-empty prefix corresponds to one visited node, and each node count includes precisely the words sharing that prefix. Duplicates follow the same path but increment every count independently, so they are handled without special cases.

## Complexity detail

Insertion reads all $S$ characters once, and scoring reads the same $S$ characters once, for $O(S)$ time. At most one trie node is created per processed character, so the trie and output occupy $O(S)$ space.

## Alternatives and edge cases

- **Rescan all words per prefix:** Directly counting matches for every prefix is straightforward but can take $O(Sn)$ time for $n$ words.
- **Sort adjacent words:** Lexicographic ordering can group shared prefixes, but accumulating every word's score requires more involved range accounting.
- **Single word:** Every prefix occurs once, so its score equals the word length.
- **Duplicate words:** Each duplicate increases every node count on the shared path.
- **Nested words:** A shorter word contributes to shared prefixes even though its path ends before longer words.
- **Disjoint first letters:** Such words share no non-empty prefix, so each prefix count comes only from its own branch.
