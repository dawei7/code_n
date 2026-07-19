## General
**Reduce an entire path to one sufficient value**

To decide whether a node is good, the individual order of its ancestors no
longer matters once their maximum value is known. If the current node's value
is at least that path maximum, no ancestor is greater and the node is good. If
it is smaller, the ancestor that established the maximum proves that it is not
good. Thus each traversal state needs only a node and the maximum value seen
on the path reaching it.

**Carry the maximum through an iterative depth-first traversal**

Initialize a stack with `(root, root.val)`. When a state is removed, compare
`node.val` with its stored path maximum and increment the answer when
`node.val >= path_maximum`. Then compute
`next_maximum = max(path_maximum, node.val)` and attach that value to each
existing child pushed onto the stack.

Using an explicit stack avoids Python recursion-depth failure on a legal tree
that degenerates into a chain of up to $10^5$ nodes. DFS order is otherwise
unimportant because each child receives state derived only from its own
root-to-parent path.

**Why the carried state gives the exact count**

The initial state is correct for the root: its stored maximum equals the only
value on its path. Suppose a node's stored value is the maximum on its full
root-to-node path. Comparing the node against it is then exactly the definition
of goodness, with `>=` correctly admitting ties. For either child, taking the
maximum of the current state and `node.val` yields the maximum on the extended
root-to-child path, so every pushed state has the same property.

By induction, the comparison is correct for every visited node. A tree gives
each non-root node exactly one parent, so the traversal pushes and evaluates
each node exactly once. Incrementing precisely on the good-node comparison
therefore produces the required total without omissions or duplicates.

## Complexity detail
Each of the $n$ nodes is pushed, removed, compared, and expanded once, giving
$O(n)$ time. The explicit DFS stack holds at most $O(n)$ node-state pairs in
the worst case, so the general auxiliary-space bound is $O(n)$. More tightly,
its size depends on the traversal frontier and is $O(h)$ for the usual
depth-first accounting, where $h$ can equal $n$ for a skewed tree. No output
collection proportional to the node count is constructed.

## Alternatives and edge cases
- **Breadth-first traversal:** A queue carrying `(node, path_maximum)` uses the
  same $O(n)$ time and is equally correct. Its frontier can contain an entire
  wide level, whereas DFS commonly retains a depth-sized frontier.
- **Recursive depth-first search:** Passing the maximum as an argument gives a
  compact recurrence and $O(h)$ call-stack space, but Python's recursion limit
  makes it unsafe for a legal $10^5$-node chain without environment changes.
- **Rescan every root-to-node path:** Retaining each path and recomputing its
  maximum is correct, but a skewed tree has total path length
  $1+2+\cdots+n=O(n^2)$.
- **Root node:** It is always counted because its value equals the maximum of
  its one-node path.
- **Equal ancestor value:** Use `>=`, not `>`; a tie does not introduce a
  greater path value.
- **Negative values:** Initialize from `root.val` rather than zero, since zero
  would incorrectly reject good nodes in an all-negative tree.
- **Branch independence:** A large value in one subtree must not affect nodes
  in another subtree; each child state inherits only its own ancestors.
- **Skewed tree:** The iterative implementation avoids recursion overflow and
  still visits every node once.
