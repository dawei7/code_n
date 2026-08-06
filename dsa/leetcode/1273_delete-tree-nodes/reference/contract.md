## Function Contract

**Inputs**

- `nodes`: the number $n$ of nodes in the tree.
- `parent`: a length-$n$ array in which `parent[i]` gives node `i`'s parent and `parent[0] = -1` marks node `0` as the root.
- `value`: a length-$n$ array in which `value[i]` is node `i`'s integer value.

The three inputs are guaranteed to describe a valid tree rooted at node `0`. The contract does not require a parent to have a smaller index than its child.

**Return value**

- Return the number of nodes remaining after every subtree whose node-value sum is zero has been removed.
