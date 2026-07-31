## General

For any collection containing at least three values, its maximum triple
product has one of only two forms: the three largest values, or the largest
value multiplied by the two smallest values. The second form captures two
negative costs whose product becomes positive. Therefore, a subtree need not
retain every cost; its two smallest and three largest values are sufficient.

**Orient the tree without recursion.** Build the undirected adjacency lists,
then traverse from root `0` to record each node's parent and a parent-before-
child order. Processing that order in reverse ensures every child's summary is
ready before its parent.

**Merge constant-size subtree summaries.** Start a node's summary with its own
cost. Feed in the at-most-five extreme values retained by each child, pruning
back to the two smallest and three largest after each insertion. Also sum the
children's subtree sizes. Every edge contributes only a constant number of
values, regardless of how large the child subtree is.

For a subtree smaller than three, assign one coin as required. Otherwise,
evaluate the two possible extreme triple products and zero, and store their
maximum. The retained extremes are sufficient for the node's own answer and
for every ancestor, so the bottom-up summaries lose no candidate that could be
optimal later.

## Complexity detail

Let $N=\lvert\texttt{cost}\rvert$. Building and traversing the tree touches
each node and edge a constant number of times. Every merge handles at most five
values per child, so the total time is $O(N)$. Adjacency lists, traversal state,
answers, sizes, and summaries use $O(N)$ space.

## Alternatives and edge cases

- **Collect every subtree's costs:** Materializing and sorting a full list for each node repeats descendant work and can require $O(N^2)$ time and space on a chain.
- **Two heaps per subtree:** Heaps can retain extremes, but fixed arrays of five values are simpler and keep each merge constant-sized.
- **Two negative costs:** The maximum product may use the two most negative values with the largest positive value.
- **All triple products negative:** Store zero rather than a negative coin count.
- **Subtree size below three:** The answer is exactly one, independent of its costs.
- **Large products:** Three absolute costs of `10000` produce values up to $10^{12}$, requiring 64-bit arithmetic in fixed-width languages.
- **Deep tree:** Iterative traversal avoids recursion-depth failure on a chain of $2\cdot10^4$ nodes.
