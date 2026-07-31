## General

Build the undirected adjacency list and traverse the tree from root `1`, carrying each node's parent and depth. The largest observed depth $d$ is the number of edges on every root-to-deepest-node path. Parent tracking is sufficient because the input is a tree: the only already visited neighbor of a node is its parent.

On a path of $d$ edges, each edge independently receives `1` or `2`, so there are $2^d$ assignments. Weight `2` contributes even parity, while weight `1` flips parity. Toggling the first edge between `1` and `2` pairs every even-cost assignment with exactly one odd-cost assignment. Consequently exactly half of all assignments have odd total cost, giving $2^{d-1}$.

Compute that power with modular exponentiation. Since the tree has at least two nodes, every maximum-depth path contains at least one edge and the exponent is nonnegative.

## Complexity detail

Let $n$ be the number of tree nodes. Building the adjacency list processes $n-1$ edges, and the traversal visits every node and edge once. The total time is $O(n)$. The adjacency list and traversal stack use $O(n)$ space. Modular exponentiation uses $O(\log n)$ time, which is contained in the traversal bound, and $O(1)$ additional space.

## Alternatives and edge cases

- **Depth-first search from every node:** Recomputing each node's root distance is correct but can take $O(n^2)$ time on a path.
- **Enumerate weight assignments:** Trying all $2^d$ assignments is unnecessary because toggling one fixed edge proves an exact even/odd split.
- **Recursive DFS:** It has the same asymptotic cost, but a path with $10^5$ nodes can exceed the language's recursion limit; an explicit stack is safer.
- **Several deepest nodes:** Only their shared depth matters, so do not multiply the answer by the number of deepest nodes.
- **Edges outside the path:** They receive no assignment for this count and contribute no factor.
- **Single path edge:** Of the assignments `1` and `2`, exactly one has odd cost, so the answer is one.
- **Modulo:** Apply modular exponentiation directly rather than constructing the potentially enormous integer $2^{d-1}$ first.
