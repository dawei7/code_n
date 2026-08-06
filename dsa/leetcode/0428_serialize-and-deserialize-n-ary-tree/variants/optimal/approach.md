## General
**Record both each value and its child count**

Write nodes in preorder. For every node, emit two tokens: its value and the number of direct children. The child count is structural information that distinguishes, for example, one node with two children from a chain of three nodes. Use a dedicated empty marker for a missing root.

**Decode with one shared cursor and an explicit stack**

Read the root value and child count, then keep stack entries containing a node and the number of its children still to decode. Each subsequent value/count pair becomes the next child of the stack's top node. Decrement the parent's remaining count, push the new child, and pop entries as soon as their child count reaches zero. One shared token position therefore advances exactly once through the stream without interpreter recursion.

**Why the token stream has one interpretation**

Preorder fixes which node appears next, and every child count fixes the exact size in nodes—not bytes—of the following child sequence through stack-based parsing. The decoder therefore attaches precisely the requested number of children to each node. Induction on the processed token pairs shows that values, child order, and branching are all restored exactly.

**Keep calls independent**

The serializer builds a fresh token list and traversal stack, while the deserializer creates a fresh token array, position, and reconstruction stack on every call. No cursor or output buffer survives between invocations, so the same codec instance can process multiple trees safely.

## Complexity detail
Serialization and deserialization each visit `n` nodes once and process a constant number of structural tokens per node, giving $O(n)$ time. The token sequence and reconstructed output require $O(n)$ space; each explicit traversal stack uses $O(h)$ additional entries for tree height `h`, remaining safe at the legal height limit of 1000.

## Alternatives and edge cases
- **Breadth-first child counts:** level-order values paired with child counts also form an unambiguous linear codec.
- **Recursive preorder parsing:** mirrors the tree definition, but a legal height-1000 chain exceeds Python's default recursion limit in this adapter.
- **Sentinel after every child list:** preorder with end markers is valid but emits an extra structural token per node.
- **Repeated immutable-string concatenation:** preserves correctness but can copy an ever-growing prefix and take $O(n^2)$ time.
- **Restart token scanning for every cursor access:** reconstructs the same tree but turns direct indexing into $O(n^2)$ parsing.
- **Empty tree:** encode and decode a dedicated marker rather than a numeric node.
- **Leaf node:** its zero child count makes parsing stop without a sentinel.
- **Child order:** N-ary children are ordered and must be reconstructed in the same sequence.
- **Maximum-height chain:** explicit stacks preserve linear behavior without relying on interpreter recursion depth.
