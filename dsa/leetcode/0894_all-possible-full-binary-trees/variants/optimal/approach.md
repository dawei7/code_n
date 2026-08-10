## General

In a full binary tree, every node has either zero children or exactly two. If the root is not a leaf, it consumes one node and the remaining $n-1$ nodes must be split between a left full tree and a right full tree.

The memoized helper `dfs(n)` returns a list of roots representing every full binary tree with exactly `n` nodes.

**Base tree.** With one node, there is exactly one possibility: a leaf whose value is zero. The helper returns a one-element list containing a new `TreeNode()`.

**Compose larger trees.** For every `i` from zero through `n - 2`, the code sets

$$
j=n-1-i.
$$

It obtains every left tree with `i` nodes and every right tree with `j` nodes. The Cartesian product of those two lists gives every ordered pair of child shapes for that split. For each pair, it creates a new zero-valued root and attaches the selected left and right roots.

Left and right order matters. A shape with a three-node subtree on the left and a five-node subtree on the right is generally different from the mirror arrangement, so both node-count splits are considered.

**Why even counts naturally yield no trees.** Every full binary tree has an odd number of nodes. A leaf has one. Adding a root to two odd-sized full subtrees gives $1+\text{odd}+\text{odd}=\text{odd}$. No even total can occur.

The exact loop includes zero and even split sizes, but `dfs(0)` and every positive even `dfs` return an empty list because they have no base construction and every attempted composition contains an empty child list. Consequently, only odd positive `i` and `j` actually create roots. An explicit parity check could skip wasted calls, but memoization makes each impossible size resolve once.

**Why every constructed tree is valid.** The one-node base is full. In a recursive construction, both selected children came from lists of full trees, and the new root receives exactly two children. All existing nodes remain full, and the new root satisfies the definition. Its node count is $1+i+j=n$. Every node constructor uses value zero.

**Why every valid full tree is generated.** Take any full tree with $n>1$ nodes. Its root has exactly two children. Let its left subtree contain $i$ nodes; then its right subtree contains $j=n-1-i$. Both subtrees are themselves full. By induction, `dfs(i)` contains the left shape and `dfs(j)` contains the right shape. When the loop reaches that split, their pair appears in the Cartesian product and the algorithm constructs the original overall shape.

This proves completeness. The split sizes and ordered child shapes also identify a rooted ordered tree uniquely, so the construction does not create duplicate structural results.

**Memoization shares computed lists.** Many larger sizes request the same subtree size. `@cache` computes `dfs(size)` once and returns the stored root list afterward. This saves enormous recomputation.

It also means returned trees may share subtree node objects. For example, the same cached one-node leaf object can be attached in multiple output trees. The problem only asks for tree roots and does not mutate them, so structural sharing represents all required shapes correctly. A caller intending to mutate returned trees independently would need deep copies.

For `n=3`, only split $1+1$ produces children. The result is one root with two leaves. For `n=7`, splits $1+5$, $3+3$, and $5+1$ combine all smaller shapes to produce the five valid ordered full-tree shapes.

## Complexity detail

Let $F(n)$ be the number of full binary trees with $n$ nodes, with $F(n)=0$ for even $n$. The output itself contains $F(n)$ roots and represents structures totaling $O(nF(n))$ node occurrences if each result is viewed independently.

- **Time complexity:** $O(nF(n))$ in output-sensitive accounting.
- **Space complexity:** $O(nF(n))$ for returned structures and memoized lists in the manifest's accounting, plus $O(n)$ recursion depth.

Because memoization permits physical subtree sharing, the number of allocated node objects can be smaller than fully independent copies, but the logical output size remains proportional to all represented tree nodes.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Build lists for increasing odd node counts. It uses the same composition recurrence and similar output-sensitive complexity without recursion.
- **Generate arbitrary binary trees then filter:** This constructs many invalid shapes and is far less efficient than enforcing two children during generation.
- **Skip parity explicitly:** Return an empty list immediately for even `n` and iterate only odd child sizes. This removes wasted states but does not change output complexity.
- **Deep-copy every chosen subtree:** It makes output trees physically independent but increases allocation toward the full $O(nF(n))$ logical size.
- **`n = 1`:** The only result is a single zero-valued leaf.
- **Even `n`:** No full binary tree exists, and the recursive Cartesian products produce an empty result.
- **Root of a larger tree:** It must have two children; a one-child construction is never created.
- **Left-right mirrors:** They are distinct ordered binary trees and are both generated by opposite splits or child choices.
- **All values zero:** Every new root and base leaf uses the default or explicit zero value.
- **Any answer order:** Nested-loop order determines one valid ordering, but the contract accepts all orderings.
- **Shared nodes:** Safe for read-only judge serialization; clone if independent mutation is required.
- **Constraint up to 20:** Only odd values can yield results, so input 20 correctly produces an empty list.
