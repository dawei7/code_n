## General
**Why only suffixes can share a delimiter**

A word is recovered by starting somewhere inside `s` and reading until the next `#`. If two words use the same delimited segment, the later starting position reads a suffix of the word that begins earlier. Conversely, every suffix of an explicitly stored word can use the appropriate later index in that same segment. Therefore, the shortest encoding needs one `word#` segment exactly for each distinct word that is not a suffix of another distinct word.

**Make suffix relationships into trie prefixes**

Insert every distinct word into a trie from its final character toward its first. Reversal turns a suffix comparison into an ordinary shared-prefix path: for example, reversed `"me"` is the prefix `"em"` of reversed `"time"`, which continues as `"emit"`.

Keep the terminal trie node and length for each distinct word. After all insertions, a terminal node with children belongs to a word whose reversed form continues into a longer reversed word, so the original word is a suffix and requires no separate segment. A terminal node with no children represents a word that is not covered by any longer word and contributes `len(word) + 1`, including its delimiter.

**Why summing trie leaves is minimal**

Every leaf word must be written explicitly: if it were recovered from some other segment, it would be a suffix of that segment's word and its reversed terminal would have a continuation. Writing all leaf words followed by `#` is also sufficient, because every non-leaf terminal lies on a path to at least one leaf and is therefore a suffix of that leaf word. The leaf contributions consequently form both a lower bound and a valid encoding length.

## Complexity detail
Hashing the words and inserting the distinct reversed words visit $O(S)$ characters. Inspecting one terminal per distinct word is also bounded by $O(S)$, so total time is $O(S)$. The distinct-word set, trie nodes, and terminal references use $O(S)$ space.

## Alternatives and edge cases
- **Suffix-set elimination:** Put distinct words in a set and remove every proper suffix of every word. This is concise, but constructing and hashing all suffix slices can require $O(SL)$ work for maximum word length $L$.
- **Sort reversed words:** Sorting reversed strings makes suffix-related words adjacent and can identify explicit segments, but comparison sorting costs $O(S \log U)$ in the usual bound for $U$ distinct words.
- **Pairwise suffix tests:** Comparing every word with every other word is correct, but takes $O(U^2L)$ time and scales poorly as the number of distinct words grows.
- **Duplicate words:** Deduplicate first; repeated occurrences can use the same reference index and must not add another segment.
- **A complete suffix chain:** Only the longest word contributes because every shorter word terminates at an internal trie node.
- **Several words sharing a suffix:** The shared suffix is covered, but each longer word on a different leaf branch still contributes its own length and delimiter.
- **One-character input:** Its reversed terminal is a leaf and contributes `2`, one character plus `#`.
