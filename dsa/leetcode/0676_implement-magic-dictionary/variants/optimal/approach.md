## General
**Represent all dictionary prefixes in a trie**

Insert every dictionary word character by character and mark its terminal node. Shared prefixes reuse nodes, so the trie occupies space proportional to `S`, the total number of stored characters.

**Search with whether the one change has been spent**

A search state consists of a trie node, the current query index, and a boolean indicating whether a differing character has already been chosen. Following the edge equal to the query character preserves that boolean. While no difference has been used, the search may also follow any other character edge and mark the change as used. After that choice, every remaining edge must match exactly.

**Accept only a terminal path with exactly one difference**

At the end of the query, accept only when the trie node is terminal and the changed flag is true. Requiring a terminal node enforces equal word length, while requiring the flag rejects an unchanged dictionary word unless a different stored word lies exactly one substitution away. Every accepted path spells a stored word differing at one position, and every such word supplies the corresponding trie path, so the search condition is exact.

## Complexity detail
Let `S` be the total dictionary characters, `Q` the number of searches, and `L` the maximum query length. Building the trie takes $O(S)$ time. Before the change, each query position can try at most the fixed 26-letter alphabet, and after a change only exact edges continue, so each search takes $O(26L) = O(L)$ time. The full operation sequence takes $O(S + QL)$ time, and trie storage is $O(S)$; recursion uses at most $O(L)$ additional call depth.

## Alternatives and edge cases
- **Wildcard-pattern index:** map every one-position-masked pattern to the original letters seen there; searches are simple, but constructing sliced pattern strings can cost $O(L^2)$ per word without rolling hashes.
- **Compare against every stored word:** count positional differences for equal-length candidates; it is direct but costs $O(DL)$ per search for `D` dictionary words.
- **Generate all substitutions:** try 25 replacements at each position and use a hash set, giving $O(26L^2)$ time with ordinary immutable-string construction.
- A query identical to the only matching dictionary word is false because zero changes were made.
- A query of a different length cannot match by substitution alone.
- If another stored word differs from an exact dictionary word at one position, searching that exact word is true.
