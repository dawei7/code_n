## General
**Carry one root prefix down the DFS**

Append each visited value to the current textual prefix. At a leaf, store that complete path; otherwise recurse into every existing child.

On entry to a node, the prefix lists exactly the values from the root through that node in order. Each recursive call extends it with precisely one child.

**Leaves are the only complete paths**

DFS reaches each tree node once and hence reaches every leaf once. At a leaf, the carried prefix contains exactly its unique root-to-leaf chain, so emitting there produces a required path. Internal nodes do not emit, and every emitted endpoint is a leaf; the result therefore contains all and only the requested paths.

## Complexity detail
Traversal visits `n` nodes and constructing returned strings costs their output length. Recursion stores one path of height `h`, excluding returned strings.

## Alternatives and edge cases
- **Search from the root separately for every leaf:** repeats traversal and can take $O(n^2)$.
- An empty tree returns no paths; negative and multi-digit values use their normal decimal form.
