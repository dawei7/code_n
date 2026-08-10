## General

An in-order traversal of a binary search tree visits node values in nondecreasing order: left subtree, node, right subtree. The requested output is exactly those same nodes relinked into a chain where every left pointer is null and each right pointer leads to the next in-order node.

The solution performs an in-order traversal while maintaining `prev`, the last node already placed in the new chain. When the current node is visited:

```text
prev.right = root
root.left = None
prev = root
```

The first assignment appends the current node after its in-order predecessor. Clearing `root.left` enforces the output requirement. Updating `prev` makes the current node the predecessor for the next visited node.

**Why a dummy node is useful.** Before visiting the smallest node, there is no real predecessor. The code creates `dummy` and initializes `prev` to it. The first visited node is linked through `dummy.right`. After traversal, `dummy.right` is the new root, and the artificial node itself is discarded.

The constructor initially gives the dummy a right link to the old root, but that link is overwritten when the leftmost node is visited. Its initial value is not needed for correctness; the dummy simply needs to exist as a stable predecessor placeholder.

**Traversal order and mutation interact safely.** At a node `root`, recursion first processes `root.left`. Once that finishes, all smaller nodes have been chained and `prev` is the largest node from that left subtree. Linking `prev.right = root` correctly appends the current node.

Then `root.left = None` removes the old backward branch. The current node's original right pointer has not yet been replaced, so `dfs(root.right)` still reaches the original right subtree. During that recursive traversal, the first node in the right subtree is linked after `root`, overwriting `root.right` with the correct successor when necessary.

For a node with no right subtree, a later ancestor or successor visit overwrites its right pointer when it becomes `prev`. The maximum node has no successor and originally has no right child in a BST, so the final chain ends with null.

**Why the chain is sorted and complete.** In-order traversal visits every node exactly once and, by the BST property, in ascending value order. Each visit appends that node after the previously visited node. Therefore the chain contains all original nodes exactly once in sorted order.

Every visited node has its left pointer cleared. Every right pointer used in the final structure connects consecutive in-order nodes. The dummy is not one of the original nodes and is excluded by returning `dummy.right`.
Immediately before processing a current node after its left recursion:

- the dummy's right chain contains exactly all nodes visited earlier in in-order;
- they appear in required order;
- every node in that partial chain has a null left child;
- `prev` is the chain's last node.

The three relinking assignments extend this invariant by the current node. Right recursion repeats it for all larger nodes. When the top call finishes, the partial chain is the complete requested tree.

The algorithm reuses node objects instead of allocating a second collection of values or new tree nodes. As a result, references to original nodes observe the rearranged structure after the method returns.

## Complexity detail

Let $n$ be the number of nodes and $h$ the original tree height. Each node is visited and relinked once.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(h)$ for the recursion stack.

The dummy node and `prev` reference use constant additional space. The output reuses existing nodes, so no $O(n)$ node array or replacement tree is allocated.

## Alternatives and edge cases

- **Collect nodes in a list first:** In-order traversal into an array followed by relinking is straightforward but uses $O(n)$ extra storage.
- **Create new nodes:** Building a fresh chain preserves the original tree but requires $O(n)$ output allocations beyond reused structure.
- **Iterative in-order traversal:** An explicit stack achieves the same $O(n)$ time and $O(h)$ space without recursion.
- **Morris traversal:** Temporary threaded links can achieve $O(1)$ auxiliary space, but pointer management is considerably more delicate while also producing the chain.
- **Single node:** It becomes `dummy.right`, its left is cleared, and its right remains null.
- **Already increasing right chain:** In-order order matches the existing chain; assignments preserve its logical structure.
- **Only left children:** Traversal visits from bottom upward and reverses those relationships into right links.
- **Balanced tree:** Recursion uses $O(\log n)$ stack height.
- **Skewed tree:** Stack depth can reach $O(n)$.
- **Duplicate values:** The standard BST contract determines their traversal order; the algorithm preserves exact in-order node order even when values tie.
- **Input mutation:** The original tree is rearranged in place. Callers needing the old structure must copy it beforehand.
- **Dummy exclusion:** Return `dummy.right`, not `dummy`, because the artificial node is not part of the requested result.
- **Clear every left link:** The assignment occurs for every visited real node, including the new root.
