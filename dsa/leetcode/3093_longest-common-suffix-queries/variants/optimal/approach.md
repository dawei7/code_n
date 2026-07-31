## General

**Reverse suffix matching into prefix traversal.** Reading every word from right to left makes a common suffix become a common path from the root of a trie. Insert each container word in reverse order. The root represents the empty suffix, and every deeper node represents one additional matching character.

**Store the tie-break winner at every node.** Every container word passing through a node shares that node's suffix. Record the best such index according to the pair `(word length, index)`. Update the root as well, because it must hold the globally shortest, earliest word for queries with no nonempty match.

For a query, follow its characters from right to left until the next trie edge is absent. The deepest reached node represents its longest suffix present among the container words. Returning that node's stored index applies both required tie breaks without searching any candidates at query time.

Every traversed trie edge certifies one equal suffix character. Traversal stops exactly when no container word can extend the current common suffix, so the reached depth is maximal. All and only container words sharing that suffix passed through the reached node during construction, and its stored pair is their shortest-word then earliest-index minimum. Thus each returned index satisfies the complete selection order.

## Complexity detail

Let $C$ and $Q$ be the total character counts of `wordsContainer` and `wordsQuery`. Building the trie visits every container character once, and answering all queries visits at most every query character once, for $O(C+Q)$ time. The trie has at most $C+1$ nodes and stores constant metadata per node, so it uses $O(C)$ space.

## Alternatives and edge cases

- **Compare every query with every container word:** Direct suffix scanning is simple but can multiply the two array sizes and repeat the same suffix work.
- **Sort reversed strings:** Neighbor searches can identify prefix ranges, but applying the shortest-length and earliest-index tie breaks over every possible prefix requires additional range structures.
- **Store a winner only at terminal nodes:** Queries often stop at an internal suffix node, so they need the best word passing through that node, not merely a word ending there.
- **Prefer the shortest word before suffix length:** Tie breaks apply only after maximizing the suffix; a longer word with a longer match must win.
- A query with no matching final character uses the root's globally shortest and earliest word.
- Duplicate container words choose their earliest index.
- A query may be shorter than its best container word and can still match in full.
- A container word that ends at an internal node remains a candidate for every prefix of its reversed path.
