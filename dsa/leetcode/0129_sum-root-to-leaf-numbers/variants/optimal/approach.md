## General
**Appending a digit is one arithmetic state transition**

When descending from prefix value `p` to node digit `d`, compute $10 \cdot p + d$. Multiplication shifts every existing decimal digit one place left, and addition fills the new units place. No path string or digit list is needed.

**Only leaves terminate numbers in the sum**

At a node with neither child, add its accumulated value to the total. A node with one child is not a leaf, and an internal prefix is not a separate number. Push each existing child with the newly computed prefix.

**Every pending value belongs to one unique root path**

Every stack pair `(node, value)` stores exactly the decimal number formed by that node's unique root-to-node digit sequence. Different branches carry independent integer values, so no mutable path restoration is required.

**Trace two numbers sharing a prefix**

Path `1 -> 2` forms `12`, and path `1 -> 3` forms `13`. Both end at leaves, so the returned sum is $12 + 13 = 25$.

**The base-ten update is the exact path prefix value**

If the parent path represents `p`, appending child digit `d` produces $10p + d$, exactly the decimal value of the extended root path. Carrying that value downward therefore keeps every prefix exact.

DFS reaches each leaf through its unique root path once. Adding only at leaves contributes each complete root-to-leaf number exactly once, so their accumulated sum matches the contract.

## Complexity detail
Each of `n` nodes is processed once, giving $O(n)$ time. Depth-first pending work is bounded by $O(h)$, where `h` is tree height.

## Alternatives and edge cases
- **Store digit paths then parse:** uses additional path memory and conversion work.
- **Breadth-first traversal:** is correct but can store $O(w)$ nodes in a wide tree.
- **Sum internal prefixes:** double-counts incomplete root-to-leaf paths.
- A root digit zero and leading zeroes on a path are handled naturally by arithmetic; they do not create a separate textual representation issue.
- Empty input conventionally contributes sum zero. A single node contributes exactly its digit.
