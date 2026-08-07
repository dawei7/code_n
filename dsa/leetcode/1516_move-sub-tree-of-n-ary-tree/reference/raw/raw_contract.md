## Function Contract

**Inputs**

- `root`: The root `Node` of an N-ary tree ($2 \le n \le 1000$).
- `p`: An existing `Node` whose subtree is to be moved.
- `q`: A distinct existing `Node` that will become the new parent of `p`.

**Return value**

Return the root `Node` of the adjusted N-ary tree after detaching `p` and appending it as `q`'s last child (handling ancestor/descendant relationships and root replacement as required).
