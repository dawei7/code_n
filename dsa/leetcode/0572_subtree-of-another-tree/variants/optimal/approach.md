## General
**Serialize both values and missing children**

Produce preorder tokens for every node and an explicit null token for every absent child. Value tokens are tagged separately from nulls. The null markers distinguish shapes that have the same preorder values but attach children on different sides.

**Reduce subtree identity to token matching**

A complete subtree serialization appears contiguously inside the main tree's preorder serialization, beginning at the token for its root. Conversely, a matching token segment includes all descendant and null markers, so it cannot stop early or ignore extra structure.

**Build the pattern failure table**

For the `subRoot` token list, compute the KMP prefix table. It records the longest proper pattern prefix that is also a suffix after each position.

**Scan the main serialization without restarting**

Advance the pattern index on matching tokens. On a mismatch, follow failure links until the token can extend a shorter valid prefix or the index reaches zero. Reaching the pattern length proves a subtree match.

**Why token containment is equivalent to subtree containment**

Preorder with explicit null markers is a unique encoding of a binary tree: the first token identifies the root and the recursive token boundaries identify both children. Therefore identical subtree structures and values yield identical token sequences. Any occurrence of the candidate sequence in the main serialization must begin at a value token and decode to the complete subtree rooted at that main-tree node.

## Complexity detail
Serializing trees with `n` and `m` nodes produces $O(n)$ and $O(m)$ tokens. Building the failure table and scanning are linear, so total time is $O(n + m)$. The token lists and failure table use $O(n + m)$ space.

## Alternatives and edge cases
- **Compare trees at every equal-valued node:** is straightforward but can take $O(nm)$ time when many values repeat.
- **Merkle-style subtree hashing:** can run in expected linear time, but collision safety requires either structural verification or collision-resistant representations.
- **Recursive serialization and substring search:** can be linear with a safe encoding and matcher, but careless delimiters cause value-boundary collisions.
- **Identical trees:** the main serialization matches from its first token.
- **Leaf candidate:** matches any leaf with the same value, but not an internal node of that value.
- **Extra descendant:** prevents a match because a value token appears where the candidate has a null marker.
- **Left versus right child:** null markers preserve orientation.
- **Duplicate values:** do not affect structural correctness of token matching.
