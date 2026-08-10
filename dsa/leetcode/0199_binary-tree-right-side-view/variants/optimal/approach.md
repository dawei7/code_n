## General

**Interpret visibility one depth at a time**

From the tree's right side, exactly one node can be visible at each occupied
depth: the geometrically rightmost existing node on that level. Breadth-first
search is a natural fit because its queue can hold one complete level at a
time, allowing the algorithm to identify that level's rightmost member before
moving deeper.

The exact source uses a right-to-left queue order. This differs from the
manifest summary, which mentions taking the final node from a left-to-right
group. Both conventions work, but the code actually records the first node of
a right-to-left group.

**Handle the empty tree immediately**

The answer list starts empty. If `root is None`, there are no occupied levels,
so returning that empty list exactly matches the contract. This guard also
prevents constructing a queue containing a null value and then accessing its
`.val` field.

**Establish the queue's ordering invariant**

The queue begins with only the root, which is trivially the rightmost node of
level zero. At the beginning of every outer `while` iteration, the queue
contains exactly all nodes of one depth, ordered from rightmost to leftmost.

Because of this invariant, `q[0].val` is the value visible from the right side
at that depth. The solution appends it before removing any level nodes.

`deque` supports indexing at zero, but `q[0]` is only safe because the loop
condition has already established that the queue is nonempty.

**Freeze the current level size**

The loop `for _ in range(len(q))` must process only nodes already in the queue
at the start of the level. In Python, the argument to `range` is evaluated once
before iteration begins. Children appended during the loop do not increase the
number of current loop iterations.

After exactly that many `popleft()` operations, every old level node has been
removed, and the queue contains only the next level. Without a frozen count,
the algorithm could mix depths and append too many visible values.

**Append children in right-before-left order**

For each current node, the algorithm appends its right child first and then its
left child, skipping missing children. Current parents themselves are processed
from right to left. Therefore children of a more-right parent enter before
children of a more-left parent, and within one parent the right child enters
before the left.

This preserves global right-to-left order for the next depth. The induction is
still valid when some children are missing: nonexistent positions add nothing,
and the earliest existing child remains the geometrically rightmost one.

**Trace the first example**

The first queue is `[1]`, so value 1 is recorded. Processing root 1 appends
right child 3 and then left child 2, producing next queue `[3,2]`.

Value 3 is recorded for the second level. Processing 3 appends its right child
4; processing 2 appends its right child 5. The next queue is `[4,5]`, so value
4 is recorded for the third level. The answer is `[1,3,4]`.

Node 5 exists at the same depth as 4 but is geometrically left of it, so it is
hidden in the right-side view even though it is a right child of node 2.

**Why one recorded value per iteration is exact**

Assume the queue invariant at the start of a level. The first queued node is
the rightmost existing node at that depth, so appending it is sound. Processing
all current nodes right-to-left and appending each right child before its left
child constructs the next occupied level in the same order.

The root establishes the invariant, and the child construction preserves it.
The outer loop runs once for every nonempty level and stops when no next-level
nodes exist. Therefore the result contains exactly one correct visible value
per occupied level, ordered top to bottom.

**Tree shape does not require special cases**

In a completely right-skewed tree, each queue contains the sole right child. In
a completely left-skewed tree, each queue contains the sole left child, which is
still visible because it is the only node at that depth. In a sparse tree, the
right-first ordering identifies the first existing node rather than assuming a
right-child chain always exists.

Negative and duplicate node values do not affect traversal because visibility
depends on structure and position, not value comparison.

**Exact source integration requirements**

The file comments out the platform-provided `TreeNode` definition and annotates
with `Optional[TreeNode]` and `List[int]`; it also uses `deque`. A LeetCode-style
harness commonly provides the node type and typing/import context. Standalone
execution needs the appropriate `TreeNode`, `Optional`, `List`, and
`collections.deque` definitions or imports.

## Complexity detail

Let $n$ be the number of nodes. Every node enters and leaves the deque exactly
once, and each child pointer is checked once, so time is $O(n)$.

The queue holds at most the maximum tree width $w$, and the answer holds one
value per height level $h$. Auxiliary storage is $O(w+h)$ including output, or
$O(w)$ excluding the returned list. Both are bounded by $O(n)$, matching the
manifest's worst-case space bound.

## Alternatives and edge cases

- **Left-to-right BFS:** Enqueue left before right and record the final node of each frozen level; this matches the manifest wording.
- **Right-first DFS:** Visit right before left and record the first node reached at each depth, as the competitive variant does.
- **Sentinel BFS:** Insert a level marker and retain the last node before each marker; works but adds sentinel bookkeeping.
- **Empty tree:** Return an empty list before queue access.
- **Single node:** Record the root once.
- **Left-only chain:** Every node is visible because each level has one node.
- **Missing right child:** A left descendant can still become the rightmost existing node at its depth.
- **Duplicate values:** Return values per level even if equal; do not deduplicate.
- **Frozen queue length:** Required so appended children are not processed in the current level.
- **Missing imports:** Supply deque and typing names in a standalone runtime.
