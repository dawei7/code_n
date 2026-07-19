## General
**Record both each value and its child count**

Write nodes in preorder. For every node, emit two tokens: its value and the number of direct children. The child count is structural information that distinguishes, for example, one node with two children from a chain of three nodes. Use a dedicated empty marker for a missing root.

**Decode with one shared token cursor**

Read a value and child count to create the current node, then recursively decode exactly that many children. Each recursive call advances the same token iterator, so after the requested children return, the cursor is already positioned at the next sibling or ancestor continuation.

**Why the token stream has one interpretation**

Preorder fixes which node appears next, and every child count fixes the exact size in nodes—not bytes—of the following child sequence through recursive parsing. The decoder therefore consumes precisely the tokens emitted for each subtree. Induction on subtree size shows that values, child order, and branching are all restored exactly.

**Keep calls independent**

The serializer builds a fresh token list and the deserializer creates a fresh iterator on every call. No cursor or output buffer survives between invocations, so the same codec instance can process multiple trees safely.

## Complexity detail
Serialization and deserialization each visit `n` nodes once and process a constant number of structural tokens per node, giving $O(n)$ time. The token sequence, reconstructed output, and worst-case recursion depth require $O(n)$ space.

## Alternatives and edge cases
- **Breadth-first child counts:** level-order values paired with child counts also form an unambiguous linear codec.
- **Sentinel after every child list:** preorder with end markers is valid but emits an extra structural token per node.
- **Repeated immutable-string concatenation:** preserves correctness but can copy an ever-growing prefix and take $O(n^2)$ time.
- **Restart token scanning for every cursor access:** reconstructs the same tree but turns direct indexing into $O(n^2)$ parsing.
- **Empty tree:** encode and decode a dedicated marker rather than a numeric node.
- **Leaf node:** its zero child count makes parsing stop without a sentinel.
- **Child order:** N-ary children are ordered and must be reconstructed in the same sequence.
