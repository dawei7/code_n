## General

**Store enough information to recover both values and structure**

An N-ary tree cannot be reconstructed from node values alone. Values may repeat, and a flat preorder sequence does not reveal where one node's children end. The exact codec resolves this by writing two tokens for every node in preorder:

1. the node's value; and
2. the number of children it has.

Once the decoder knows that count, it knows exactly how many complete child subtrees must follow. Each child subtree uses the same format recursively, so no closing delimiter or unique node identifier is necessary.

Tokens are converted to decimal strings and separated by single spaces. Unlike a character-only encoding, this safely supports multi-digit values and child counts without ambiguity.

**Serialize in preorder**

For a nonempty root, `serialize` creates a local `tokens` list and invokes `encode(root)`. At each node, `encode` appends `str(node.val)` and `str(len(node.children))`, then recursively encodes children in their existing list order.

This is preorder because the node's own metadata appears before every child subtree. Preserving iteration order is required: an N-ary node's children are ordered, so swapping two serialized subtrees would reconstruct a different tree even if it contained the same values.

After traversal, `" ".join(tokens)` creates one string. Building pieces in a list and joining once avoids repeated copying of a growing immutable string.

For a leaf with value `7`, the encoding contains `"7 0"`. The zero child count completely describes that no recursive records follow for this node.

**Use a distinct empty-tree marker**

If `root is None`, serialization returns `"#"`. A nonempty encoding begins with a decimal integer token, so `#` cannot be confused with a node record under the stated nonnegative value constraints.

Deserialization tests for this marker before splitting or reading tokens and returns `None`. This gives empty trees a complete round trip without inventing a dummy node.

**Deserialize with one shared token iterator**

For nonempty data, `data.split()` recovers the tokens, and `iter(...)` creates a single iterator shared by all recursive calls.

`decode()` consumes the next token as `value` and the following token as `child_count`. It then evaluates

`[decode() for _ in range(child_count)]`.

Each recursive call consumes exactly the complete token segment for one child subtree. When it returns, the iterator is positioned at the next sibling's value. After exactly `child_count` calls, the list contains this node's children in original order, and `Node(value, children)` reconstructs the node.

There is no explicit index or global state. The iterator itself holds the current position, and it is local to one `deserialize` invocation. This satisfies the statelessness requirement: separate calls do not share or retain decoding state.

**Why no subtree delimiter is needed**

Consider a node declaring three children. The decoder calls `decode` three times. The first call may recursively consume many descendants, but its own child counts determine exactly where it finishes. The second call begins at the next unread token, and likewise for the third.

This is analogous to a length-prefixed message format. Child counts provide structural boundaries, while preorder establishes which node each count belongs to. Duplicate values cause no ambiguity because structure is derived from counts, not from value identity.

**A small round trip**

Suppose root `1` has children `2` and `3`, and node `2` has one child `4`. Preorder metadata is:

`1 2 2 1 4 0 3 0`.

The decoder reads root value `1` and count `2`. Its first child reads `2 1`, then recursively consumes leaf `4 0`. The root's second child then reads leaf `3 0`. The reconstructed child order and nesting exactly match the source.


For a leaf, serialization writes its value and zero; deserialization reads those tokens, performs zero child calls, and constructs an equal leaf.

Assume every child subtree round-trips correctly. Serialization of a parent writes its value, exact child count, and each serialized child in order. Deserialization reads the same value/count, invokes one decode per child, and by the inductive assumption reconstructs each child in that order. It therefore reconstructs the complete parent subtree. Structural induction proves `deserialize(serialize(root))` is equivalent to `root` for every finite N-ary tree.

The codec need not reproduce the same Python object identities. It creates a structurally and valuably equivalent new tree, which is the required meaning of deserialization.

## Complexity detail

Let $n$ be the number of nodes, $h$ the tree height, and $M$ the number of characters in the serialized representation. Serialization visits every node once and emits two tokens, taking $O(n)$ structural operations and $O(M)$ character-writing time. Under the bounded numeric constraints, this is conventionally reported as $O(n)$.

Deserialization splits the $M$-character string, consumes each of the $2n$ tokens once, and constructs each node once, taking $O(M)$ time, conventionally $O(n)$ here.

Serialization stores $O(n)$ token strings plus an $O(h)$ recursion stack and produces an $O(M)$ output string. Deserialization's split token list and iterator use $O(n)$ auxiliary space, while recursion uses $O(h)$. The reconstructed nodes are required output. Overall working/output-associated space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Preorder with an end-of-children sentinel:** Emit a marker after every node's child list. It is also unambiguous but uses a structural token per node instead of a numeric child count.
- **Level-order encoding with separators:** Breadth-first serialization can group children by parent, but needs careful sentinels or counts to preserve parent boundaries and child order.
- **Values alone in preorder:** This is insufficient because different N-ary shapes can have the same preorder values.
- **Store unique node and parent IDs:** It reconstructs relationships but adds identifiers and usually a map, unnecessary when recursive counts already define structure.
- **Empty tree:** `"#"` round-trips directly to `None`.
- **Leaf node:** Its zero child count prevents any recursive child reads.
- **Node with many children:** The count drives exactly that many sequential decodes, preserving their order.
- **Duplicate values:** They remain safe because records are positioned structurally and are not used as identities.
- **Multi-digit values/counts:** Space-separated tokens prevent boundaries such as `1` followed by `23` from being confused with `12` followed by `3`.
- **Very deep tree:** Time remains linear, but recursive stack depth is $O(h)$ and may approach the stated height limit.
- **Repeated codec calls:** All mutable state is local to each method call, so earlier calls cannot affect later ones.
- **Malformed data:** Exhausted or invalid tokens would raise conversion/iteration errors. The contract only requires decoding strings produced by the matching serializer.
