## General
**Reverse the parent relation**

The input directly maps each process to its parent, but termination must travel from a parent to its children. Scan the paired arrays once and build an adjacency map from every parent identifier to the list of its direct child identifiers.

**Traverse only the killed subtree**

Start an explicit stack with `kill`. Repeatedly remove one process, add it to the result, and push all children from the adjacency map. This depth-first traversal reaches descendants at every depth without recursion limits.

**Why the result is exact**

The killed process is inserted initially. Whenever a reached process is handled, every direct child is scheduled, so induction on tree depth shows that all descendants are eventually included. Conversely, the traversal follows only parent-to-child edges beginning at `kill`, so every added process is either `kill` itself or one of its descendants. Unique process identifiers and the process-tree structure prevent duplicate visits.

## Complexity detail
For `n` processes, building adjacency examines `n` parent-child pairs. Traversal visits at most `n` processes and edges, so total time is $O(n)$. The adjacency map, stack, and output use $O(n)$ space.

## Alternatives and edge cases
- **Breadth-first traversal:** a queue over the same adjacency map has identical asymptotic bounds and returns a different valid order.
- **Recursive depth-first search:** is concise but a deep process chain can exceed the language recursion limit.
- **Scan all parent entries for every killed process:** avoids adjacency storage but can take $O(n^2)$ time.
- **Kill a leaf:** returns only that process.
- **Kill a root:** returns the entire process tree rooted there.
- **Multiple children:** every child subtree must be traversed.
- **Deep chain:** use an explicit stack or queue rather than recursion.
- **Parent identifier zero:** marks a root and is not itself a real process.
- **Output order:** is unrestricted; correctness depends on membership, not traversal order.
