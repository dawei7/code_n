## General

Each query asks for the greatest root-to-node depth that lies outside one named subtree. Because queries are independent, recomputing that height after every removal repeats almost all tree work. Instead, precompute the answer associated with every node value once.

**Subtree heights.** First obtain `heights[value]`, the number of edges on the longest downward path starting at that node. An empty child has height $-1$, making a leaf's height $0$. An explicit expanded-state stack performs postorder traversal without risking Python's recursion limit on a legal 100,000-node chain.

**Heights outside each subtree.** Traverse from the root again with three values: the node, its depth, and `outside_height`, the greatest root-to-node depth reachable without entering this node's subtree. Store `outside_height` as this node's query answer.

For a left child of a parent at depth $d$, a surviving deepest path either was already outside the parent's subtree or enters the parent's right subtree. The second possibility has height `d + 1 + right_height`; it evaluates to $d$ when the sibling is absent, correctly retaining the parent itself. Take the maximum of those alternatives. The right child uses the symmetric formula.

By induction from the root, the propagated value includes every path outside the current subtree and no path inside it. It is therefore exactly the remaining tree height after that subtree is removed. Once all values are indexed, each query is a constant-time lookup.

## Complexity detail

Let $n$ be the number of nodes and $m=\lvert\texttt{queries}\rvert$. Each of the two tree traversals visits every node once, and answer construction visits every query once. Time is $O(n+m)$.

The height map, answer map, and explicit traversal stacks hold $O(n)$ entries, while the returned list has $m$ entries. Under the repository's reference-solution accounting, auxiliary space is $O(n)$ because $m\le n$.

## Alternatives and edge cases

- **Recompute after every query:** Skipping the removed value during a fresh height traversal is straightforward and correct but takes $O(nm)$ time.
- **Two recursive DFS traversals:** The same recurrence is elegant recursively, but Python recursion depth can fail on the legal 100,000-node skewed tree.
- **Two greatest subtree heights per depth:** Grouping nodes by depth and retaining the largest two downward heights also answers each query in $O(1)$ after $O(n)$ preprocessing.
- **Euler-tour prefix and suffix maxima:** A subtree occupies a contiguous Euler interval; prefix and suffix depth maxima provide another $O(n+m)$ method.
- **Independent queries:** Never mutate the shared tree or let one removal affect the next answer.
- **Height uses edges:** A tree containing only the root has height $0$, and a leaf subtree has downward height $0$.
- **Root is never queried:** The guaranteed non-root query means a remaining tree always contains the original root.
- **Missing sibling:** The parent can still be the deepest survivor, which is why an absent sibling's height is $-1$.
- **Repeated query values:** Even if a value appears again, its independent answer is unchanged and can be looked up repeatedly.
- **Unique node values:** Values safely serve as keys for heights and precomputed answers.
