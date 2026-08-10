## General

**Use the numeric labels as the tree structure**

Node `v` has parent `floor(v/2)`. Reversing that relationship, its possible children are `2v` and `2v+1`. The tree therefore has the same label layout as a binary heap, and no adjacency list is needed.

The array `tree` stores the current bit at each label from 1 through `n`. Index zero is unused. All entries begin at zero.

**Repeated identical queries cancel in pairs**

Flipping is XOR with 1. Two flips restore the original value:

$$
b \mathbin{\mathtt{\char94}} 1
\mathbin{\mathtt{\char94}} 1
= b.
$$

Therefore only the parity of the number of times each exact subtree root appears in `queries` matters. The solution builds `cnt = Counter(queries)` and runs a subtree flip only when that count `v` is odd.

If a root appears twice, its two whole-subtree operations cancel. If it appears three times, two cancel and one remains. This preprocessing is valid independently for every query label because flips commute and associate: their order does not affect the final bits.

**Flip one subtree recursively**

The helper `dfs(i)` stops when `i > n` because such a heap label is not present in the finite tree. Otherwise it toggles `tree[i]` with `tree[i] ^= 1` and recurses into labels `i << 1` and `i << 1 | 1`.

The left expression shifts the binary label left, producing `2i`. The second produces `2i+1`. These are exactly the children. Recursively visiting both therefore reaches every descendant of `i` and no node outside its subtree.

Some nodes near the bottom have only a left child or no children. The numeric boundary check handles all missing children uniformly.

**Overlapping subtrees must still interact**

Parity reduction removes repeated queries with the same root, but odd queries rooted at an ancestor and descendant do not cancel as whole operations. Their overlapping nodes must be toggled once by each DFS.

For example, a query at node 1 flips every node, and a query at node 2 flips only node 2's subtree. Nodes inside that subtree receive two flips and return to zero; nodes elsewhere receive one and become one. Running both DFS traversals produces exactly this overlap behavior.

After every odd-root DFS, `sum(tree)` counts the entries equal to one because list values are integers zero or one.


Fix any node `u`. A query rooted at `r` flips `u` exactly when `r` is an ancestor of `u`, including `r=u`. The final value at `u` is the parity of the total number of such query occurrences.

For each root, the counter keeps one effective DFS precisely when its occurrence count is odd. That DFS reaches `u` exactly when the root is its ancestor. Thus `tree[u]` is toggled once for every ancestor root with odd query count. XORing those odd contributions produces the same parity as all original query occurrences.

This argument holds independently for every node, so the completed `tree` array matches the required final state. Summing it returns the number of ones.

**Trace the first example**

For `n=5` and `queries=[1,2,5]`, every query count is odd:

- Root 1 flips nodes 1 through 5.
- Root 2 flips nodes 2, 4, and 5, returning those three to zero.
- Root 5 flips node 5 back to one.

The final one-valued nodes are 1, 3, and 5, so the sum is 3.

For `queries=[2,3,3]`, the two root-3 queries cancel in the counter. Only the subtree of 2 is toggled, giving the expected result for the relevant `n`.

**The exact implementation differs from the summary**

The manifest describes combining query parity at each label with inherited flip parity from the parent in one $O(n+q)$ traversal. The protected code does not perform that propagation. It launches a separate DFS for every distinct query root with odd frequency, so overlapping subtrees are physically revisited.

In this heap-shaped tree, a node can be revisited once for every queried ancestor. Tree depth is $O(\log n)$, so over all possible odd roots the total visits are $O(n\log n)$. Including counter construction, the exact worst-case time is $O(q+n\log n)$, not $O(n+q)$.

## Complexity detail

Building `Counter(queries)` takes $O(q)$ expected time and stores at most $\min(q,n)$ keys. Let $Q_o$ be the set of distinct roots with odd counts. The exact traversal work is

$$
O\left(\sum_{r\in Q_o}\lvert\operatorname{subtree}(r)\rvert\right).
$$

For the heap-labeled binary tree, this sum is at most $O(n\log n)$ because each node belongs to the subtree of only its $O(\log n)$ ancestors. Total time is $O(q+n\log n)$ in the worst case.

The `tree` list uses $O(n)$ space, and the counter uses $O(\min(q,n))$, which is $O(n)$ because query labels range from 1 through `n`. Recursion depth is the tree height $O(\log n)$, not $O(n)$, because the implicit tree is balanced by its heap labeling. Overall auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Inherited parity traversal:** Store query-count parity at each label, then scan nodes from 1 through `n` and XOR each node's parity with its parent's inherited parity. This matches the manifest and achieves $O(n+q)$ time.
- **Euler tour plus range XOR:** Flatten every subtree into an interval and apply difference-array toggles. It is a general-tree technique but unnecessary when heap labels already encode ancestry.
- **Run every query occurrence:** This is correct but fails to cancel duplicates early and can do far more work than the counter-based source.
- **Even duplicate count:** The entire subtree is flipped an even number of times and needs no DFS.
- **Odd duplicate count:** It is equivalent to one subtree flip.
- **Ancestor and descendant queries:** Only their overlap receives both flips; they cannot be canceled as identical operations.
- **Leaf query:** DFS toggles the leaf and immediately stops at both child labels above `n`.
- **Root query:** It visits every node in the tree.
- **`n=1`:** Every query label is 1, so the final result is the parity of the query count.
- **Index zero:** It is not a node and remains unused in the storage array; summing it adds zero harmlessly.
- **Metadata mismatch:** Separate subtree traversals can revisit nodes and have $O(n\log n)$ aggregate work, unlike inherited one-pass propagation.
