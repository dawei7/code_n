## General
**Precompute every palindromic boundary in linear time**

A valid pair can have words of different lengths. After the shorter word mirrors an equal-length portion of the longer word, the unmatched prefix or suffix of the longer word must be a palindrome. The candidate therefore needs to recognize every palindromic prefix and suffix without rescanning each split.

For each word, insert delimiters between characters and run one Manacher scan: character centers represent odd-length palindromes and delimiter centers represent even-length palindromes. Whenever a maximal palindrome reaches the word's left boundary, mark its ending length as a palindromic prefix; whenever it reaches the right boundary, mark its starting position as a palindromic suffix. Empty prefixes and suffixes are marked explicitly. Each center reuses the rightmost known palindrome, so all boundary flags for a word take linear time.

**Store reversed words and their palindromic remainders**

Insert every word into a trie from right to left. Before inserting character `word[j]`, append the word's index to the current node when `word[:j + 1]` is a palindrome. The node then records that the trie path has already matched a suffix of this word and that its unmatched prefix can safely sit at the far end of a concatenated palindrome. At the terminal node, record both the exact word index and its empty remainder.

To query a word from left to right, follow the trie characters. If the current trie node terminates another word and the query suffix beginning at `j` is palindromic, the query word followed by that shorter partner is valid. If the entire query is consumed, every distinct index recorded in the final node's palindrome-remainder list is a valid longer partner. The empty string follows the same rules: it terminates the root and pairs in both directions exactly with palindromic words.

For `"lls"`, the query consumes the reversed prefix of `"sssll"`; the longer word's stored remainder is palindromic, so `[2,4]` is emitted. The word `"s"` consumes the first trie edge of reversed `"lls"`, whose remaining `"ll"` is recorded as palindromic, so `[3,2]` is emitted.

**Trie matches are necessary and sufficient**

Every emitted terminal match mirrors all characters supplied by the shorter side, and its boundary flag proves that the unmatched characters are palindromic. The concatenation is therefore a palindrome. Conversely, in any valid pair, matching mirrored characters from the concatenation's ends consumes one entire word first; the other word's unmatched portion must be a palindromic boundary. Insertion records exactly that boundary at exactly the trie node reached by the shorter word, so the query emits every valid ordered pair. Rejecting the same index enforces the distinct-entry requirement.

## Complexity detail
Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

and let `P` be the number of returned pairs. Manacher preprocessing, reverse-trie insertion, and trie queries each process $O(S)$ characters. Emitting results costs $O(P)$, so total time is $O(S + P)$. Boundary flags and trie nodes use $O(S)$ storage, while the returned pairs use $O(P)$, for $O(S + P)$ total space.

## Alternatives and edge cases
- **Test every ordered word pair:** is simple but costs $O(n^2 k)$ time for `n` words of maximum length `k`.
- **Hash-map every split:** is concise, but repeated slicing, reversal, and palindrome checks cost $O(nk^2 + P)$ time.
- **Use rolling hashes for boundary tests:** can approach the same asymptotic bound but introduces collision risk unless equality is verified.
- The empty string pairs only with palindromic words. Pair direction matters, duplicate output pairs must not be emitted, and the outer result order does not matter.
