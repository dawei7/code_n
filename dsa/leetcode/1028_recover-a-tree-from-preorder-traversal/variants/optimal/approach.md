## General
**Read one depth-value token at a time:** Starting at the current character, count consecutive dashes to obtain `depth`. Then consume consecutive digits and accumulate `value = value * 10 + digit`. Each character belongs to exactly one of these scans.

**Keep the current root-to-node path:** A stack contains the most recently created node at every active depth. Before attaching a token at depth `depth`, pop while `len(stack) > depth`. The new stack top is then the parent at depth `depth - 1`.

**Use preorder to choose the child side:** The first child encountered for a parent must be its left child. If the left slot is already occupied, the new node is its right child. Push the new node so later, deeper tokens attach beneath it.

The stack invariant places index `d` at the latest node of depth `d` on the preorder path. Popping to the token's depth therefore selects exactly its encoded parent. The left-only-child guarantee removes the only ambiguity about whether a first child belongs on the left or right, so every attachment matches the original tree.

## Complexity detail
The parser advances monotonically across all $L$ characters, and each node is pushed and popped at most once. The total time is $O(L)$. The path stack holds at most $H$ nodes, so auxiliary space is $O(H)$; the returned tree itself is output space.

## Alternatives and edge cases
- **Recursive depth-expecting parser:** Parse a node only when the next dash count matches the requested depth, then recursively request its children. This is linear with a shared index but risks recursion-depth limits on a long chain.
- **Repeated suffix slicing:** Tokenizing by replacing the unparsed string with a suffix copies characters repeatedly and can take $O(L^2)$ time.
- **Single node:** An encoding without dashes becomes the root with no children.
- **Multi-digit values:** Continue the numeric scan across every adjacent digit, including values up to `1000000000`.
- **Return to a shallower depth:** Several stack entries may need to be popped before attaching a right child.
- **One-child guarantee:** A first child is always assigned left; no marker is needed for a missing left child followed by a right child.
