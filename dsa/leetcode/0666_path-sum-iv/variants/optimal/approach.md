## General
**Decode positions into a direct lookup**

For each encoded integer, extract `(depth, position)` as its structural key and the ones digit as its value. Store these pairs in a hash map. A node at `(d, p)` has possible children $(d + 1, 2p - 1)$ and $(d + 1, 2p)$.

**Carry the path sum through existing nodes only**

Start at key `(1, 1)` with accumulated sum zero. At each node, add its value to the running path sum. If neither child key exists, the node is a leaf, so add the completed running sum to the answer. Otherwise visit each child that is present.

**Why every path contributes exactly once**

The encoding assigns every real node one unique structural key, and the child formulas reproduce the binary-tree parent relation. Traversal therefore reaches every encoded node through its unique parent. Every root-to-leaf path ends at one leaf and contributes when that leaf is visited; internal nodes never contribute prematurely. Summing those leaf contributions is exactly the requested total.

## Complexity detail
Decoding and traversal each process all `N` encoded nodes once, giving $O(N)$ expected time. The lookup map and traversal stack use $O(N)$ space.

## Alternatives and edge cases
- **Bottom-up leaf-count propagation:** count leaf descendants below each node and add `value * leaf_count`; this is also linear but less directly mirrors path sums.
- **Reconstruct every leaf path by scanning the input:** is correct but repeatedly searches for ancestors and can take $O(N^2)$ time.
- **Build explicit node objects:** works, but the positional keys already provide all required relationships without allocation overhead.
- A one-node tree has one path consisting of the root value.
- Node values may be zero and still define real nodes.
- A missing left or right child does not prevent the other child from continuing a path.
- The tens digit is a level-relative position, not a global heap-array index.
