## General
**Store the first child on the binary left link**

For each N-ary node, create a binary node with the same value. Recursively encode its children in their existing order. Attach the first encoded child through `left`; this link means “first child,” not an ordered binary-search relation.

**Chain later children through right links**

Keep the previously encoded child and attach each next sibling through `previous.right`. The binary `right` chain therefore records the complete ordered sibling list. Advancing a tail pointer avoids rescanning siblings already linked.

**Decode the two link meanings symmetrically**

Create an N-ary node from the binary value. Start at its `left` child, recursively decode each binary node encountered, append it to the child list, and follow `right` to the next sibling. Apply the same rule recursively within every child.

**Why the mapping is reversible**

Encoding maps exactly one N-ary node to one binary node. Its ordered child list becomes exactly one left edge followed by a right-sibling chain. Decoding interprets those same links with the inverse meanings, so induction over each subtree restores its value and ordered children. No structural choice is ambiguous.

## Complexity detail
Encoding and decoding each visit all `n` nodes once, giving $O(n)$ time. Recursive calls follow the structural height; excluding the required encoded and decoded objects, auxiliary space is $O(h)$.

## Alternatives and edge cases
- **Child-count serialization inside binary nodes:** could store explicit metadata but violates the intended use of the existing binary-node fields.
- **Search from the first child for every appended sibling:** remains correct but can take $O(n^2)$ time for one wide child list.
- **Empty structure:** both directions return `None`.
- **Leaf node:** its binary `left` link is `None` and decoding yields an empty child list.
- **Sibling order:** the right chain must follow the original child order exactly.
- **Repeated calls:** the codec must not retain a tail pointer or node mapping between invocations.
