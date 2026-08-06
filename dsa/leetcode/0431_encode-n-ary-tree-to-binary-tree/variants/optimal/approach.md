## General
**Store the first child on the binary left link**

For each N-ary node, create a binary node with the same value. An explicit continuation frame tracks the next child index and the previously encoded child. Attach the first encoded child through `left`; this link means “first child,” not an ordered binary-search relation.

**Chain later children through right links**

Keep the previously encoded child in the parent's continuation frame and attach each next sibling through `previous.right`. Push that continuation below a frame for the child, so the traversal finishes the child's subtree before resuming the next sibling. The binary `right` chain therefore records the complete ordered sibling list without rescanning links.

**Decode the two link meanings symmetrically**

Create an N-ary node from the binary value. A decoding frame pairs an N-ary parent with its next binary child. Append that child, save a continuation for its `right` sibling, then descend through the child's `left` link. These explicit frames apply the inverse rule at every depth without interpreter recursion.

**Why the mapping is reversible**

Encoding maps exactly one N-ary node to one binary node. Its ordered child list becomes exactly one left edge followed by a right-sibling chain. Decoding interprets those same links with the inverse meanings, so induction over each subtree restores its value and ordered children. No structural choice is ambiguous.

## Complexity detail
Encoding and decoding each visit all `n` nodes once, giving $O(n)$ time. At most a constant number of continuation frames are retained per structural level; excluding the required encoded and decoded objects, auxiliary space is $O(h)$ without depending on Python's recursion limit.

## Alternatives and edge cases
- **Child-count serialization inside binary nodes:** could store explicit metadata but violates the intended use of the existing binary-node fields.
- **Search from the first child for every appended sibling:** remains correct but can take $O(n^2)$ time for one wide child list.
- **Recursive first-child/next-sibling conversion:** mirrors the definition, but a legal height-1000 chain exceeds Python's default recursion limit in this adapter.
- **Empty structure:** both directions return `None`.
- **Leaf node:** its binary `left` link is `None` and decoding yields an empty child list.
- **Sibling order:** the right chain must follow the original child order exactly.
- **Repeated calls:** the codec must not retain a tail pointer or node mapping between invocations.
- **Maximum-height chain:** continuation frames preserve the required $O(h)$ bound while remaining safe at height 1000.
