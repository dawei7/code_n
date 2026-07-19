## General
**Return two directional arms from every subtree**

For each node, compute an increasing arm that starts at the node and descends through values one larger at each step, and a decreasing arm that descends through values one smaller. Both lengths begin at one for the node itself.

**Use child states only when the edge continues the sequence**

After a child has returned its two lengths, a child value of `node.val + 1` can extend the node's increasing arm with the child's increasing arm. A child value of `node.val - 1` similarly extends the decreasing arm. Any other difference cannot contribute across that edge.

**Join opposite arms at their highest node**

A complete path may approach the current node along a decreasing downward arm read in reverse and leave along an increasing downward arm. Its length is `decreasing + increasing - 1`, subtracting the shared current node. Taking this candidate at every node covers paths contained in either one subtree and paths that cross between children.

**Evaluate children before their parent**

An explicit postorder stack stores traversal phase plus the returned pair from each child. This supplies both arms before the parent is finalized while avoiding recursion-depth failure on a long chain.

**Why every valid path is measured**

Every valid path has a unique highest node in the rooted tree. From that node, each used side must move consistently by `+1` or `-1`; if two sides are used, they are opposite directional arms of one globally consecutive sequence. The postorder state records the longest possible arm of each type, so their combination at that highest node is at least as long as the path. Every combined pair also describes an actual simple consecutive path, making the maximum exact.

## Complexity detail
Every node is pushed, finalized, and combined with at most two child results once, giving $O(n)$ time. The explicit stack contains one frame per level and therefore uses $O(h)$ auxiliary space.

## Alternatives and edge cases
- **Recursive postorder:** uses the same two-arm recurrence in $O(n)$ time and $O(h)$ call-stack space, but a skewed tree can exceed recursion limits.
- **Recompute both arms from every node:** is correct but revisits descendants and takes $O(n^2)$ time on a consecutive chain.
- **Parent-to-child-only tracking:** misses paths that turn at a parent and continue into the other subtree.
- **Single node:** forms a consecutive path of length one.
- **Equal adjacent values:** do not extend either arm because the difference must be exactly one.
- **One-sided chain:** one arm may contain the whole answer while the other remains length one.
- **Turn at a node:** the two arms can come from different children, but two increasing or two decreasing arms cannot be joined into one monotone sequence.
