## General
**Values alone do not identify the shape**

A traversal containing only node values is ambiguous. For example, preorder values `1,2` could describe a root with a left child or a root with a right child. The encoding must preserve missing-child positions as well as values.

Use preorder order and emit a null marker such as `#` whenever a child is absent. A node is encoded as its value followed by the complete encoding of its left subtree and then its right subtree. Commas delimit tokens, so negative and multi-digit integers remain unambiguous.

For the tree `[1,2,3,null,null,4,5]`, the token stream is:

`1,2,#,#,3,4,#,#,5,#,#`

Each real node contributes one value token, and each missing child contributes one marker.

**Serialize iteratively**

Start a stack with the root. Pop one entry at a time:

- for `None`, append `#`;
- for a real node, append its value, then push its right child followed by its left child.

The reversed push order makes the stack produce preorder. Handling `None` entries explicitly is what records structure. Building a token list and joining once avoids quadratic string concatenation on a skewed tree.

**Reconstruct parent slots from the token stream**

The first token creates the root unless it is `#`. Each real node has exactly two child slots to fill. Keep a stack of `(node, next_slot)` frames, where `next_slot` says whether the next token belongs to the left or right child of that node.

For each remaining token:

1. create either a child node or `None`;
2. assign it to the top frame's next slot;
3. advance or remove the parent frame after its right slot;
4. when the child is real, push a fresh frame for its two slots.

Preorder guarantees that a real child's entire subtree is consumed before the parser returns to the parent's next pending slot. The explicit stack implements that nesting without relying on recursion depth.

**Why the encoding is reversible**

At every real-node token, the next two complete encodings are uniquely its left and right subtrees; null markers are complete encodings of empty subtrees. This recursive grammar has only one parse. The deserializer fills child slots in exactly that grammar order, so it reconstructs the same values and the same missing-child structure. Serializing the result therefore yields the identical token sequence.

## Complexity detail
A binary tree with `n` nodes has $n + 1$ null child pointers. Serialization and deserialization each process $2n + 1$ tokens once, giving $O(n)$ time. Tokens, output text, and explicit stacks require $O(n)$ space; stack depth alone is $O(h)$.

## Alternatives and edge cases
- **Breadth-first encoding:** is equally valid when null placeholders are retained consistently; it may keep up to a full tree level in memory.
- **Traversal values without null markers:** cannot distinguish different shapes.
- **Recursive concatenation and front-removal from token arrays:** can degrade to $O(n^2)$ on skewed trees.
- The empty tree is encoded as a single null marker. Delimiters make negative and multi-digit values safe.
