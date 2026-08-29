## General

The task no longer asks whether one qualifying path exists. It asks for every qualifying root-to-leaf path, represented by its sequence of values. The search therefore cannot stop after the first success, and it must preserve a separate snapshot for each successful path.

The selected solution uses depth-first search with two pieces of current-branch state:

- `s`, the accumulated sum from the original root through the parent of the current call; and
- `t`, one shared mutable list containing the values on the active traversal path.

`ans` collects independent copies of `t` whenever the active path reaches a leaf with the target sum.

**The state before and after entering a node**

At entry to `dfs(root, s)`, `s` and `t` describe the same prefix path: all real nodes from the original root through `root`'s parent.

If `root is None`, there is no node to add and the function returns immediately. Otherwise it performs `s += root.val` and `t.append(root.val)`. Now both state representations include the current node.

The integer update and list update behave differently. Python integers are immutable, so the updated `s` is local to this call. The list `t` is shared by all recursive calls through the closure, so it must be explicitly restored before the call returns.

**Why acceptance requires both a leaf and the target sum**

A valid path must end at a leaf, defined as a real node with neither child. The condition therefore tests both child references and `s == targetSum`.

An internal node whose accumulated sum equals the target is not enough. Its path has not ended at a leaf, and every continuation must include additional values. Conversely, a leaf with the wrong sum is a complete path but not a qualifying one.

The empty tree returns `[]`, even when the target is zero, because no real root-to-leaf path exists.

**Why `t[:]` is necessary**

When a successful leaf is reached, `t` contains exactly that path's values. The source appends `t[:]`, a shallow copy of the current integer list, to `ans`.

Appending `t` itself would store a reference to the one mutable working list. Later `t.pop()` operations would shorten every stored reference, and subsequent branch exploration would replace its contents. The final answer could become a collection of references to the same empty list.

The slice creates a distinct outer list for the output path. Its integer elements are immutable, so a shallow copy is sufficient; no nested mutable path elements need deep copying.

**How backtracking reuses one working list**

After checking the current node, the solution recursively explores the left child and then the right child. When a child call returns, that child has popped every node it appended, so `t` is again the current node's path before the sibling begins.

After both children finish, the current call executes `t.pop()`. This removes its own value and restores the exact prefix that existed at entry. That restoration invariant lets the algorithm reuse one list instead of allocating a complete path copy at every edge.

The `pop` is executed for leaves too. Even a successful leaf first saves a snapshot, then makes two harmless null calls, and finally removes itself from the working path. There is no early return that could leave stale state behind.

**Why all and only valid paths are returned**

At every real node, `t` is the exact root-to-current value sequence and `s` is its exact sum. This is true at the root after adding its value. If it is true for a parent, appending a child value and adding it to the sum preserves the statement for that child.

Every root-to-leaf path corresponds to one depth-first route. The search visits both children of every real node, so every leaf route is reached once. A snapshot is appended exactly when that route's final sum equals `targetSum`.

Thus no valid path is omitted, no invalid path is added, and no path is added twice. Backtracking changes only the working list after a saved copy has become independent.

**Tracing the two target-22 paths**

Starting at value five, the left traversal builds `t = [5, 4, 11, 7]` with sum twenty-seven at leaf seven, so it saves nothing. Backtracking removes seven, then the sibling leaf two produces `[5, 4, 11, 2]` with sum twenty-two, and a copy is saved.

The search continues rather than returning. After fully undoing the left branch, it explores the right side and eventually reaches `[5, 8, 4, 5]`, also totaling twenty-two. That list is copied separately.

The output order follows left-before-right DFS, giving the two paths in the Reference order for this tree. The contract requires all paths; unless otherwise stated, correctness should not depend on a particular order among independent qualifying paths.

**Why sums cannot safely prune the traversal**

Node values may be negative. A partial sum greater than the target can later decrease, and a partial sum smaller than the target can later increase. The source correctly explores to leaves rather than pruning on `s > targetSum` or on equality at an internal node.

The method reads the tree without mutation. Its type names `Optional`, `List`, and `TreeNode` are expected from the surrounding harness because they are not actively defined or imported in the selected file.

## Complexity detail

Let $n$ be the number of tree nodes, $h$ the maximum root-to-leaf node count, and $L$ the total number of integer entries across all paths returned in `ans`.

DFS visits every node once and performs $O(1)$ local work apart from successful-path copying, for $O(n)$ traversal time. Each `t[:]` copy costs time proportional to that path's length. Summed over all returned paths, those required copies cost $O(L)$. Exact total time is therefore $O(n+L)$.

The recursion stack and shared working list each contain at most one root-to-current path, so auxiliary space excluding output is $O(h)$. The two are both linear in height, and constant factors do not change the bound.

The returned snapshots occupy $O(L)$ output space. Including output, peak memory is $O(h+L)$. $L$ can be much larger than $n$ because many successful paths may share long prefixes yet each must be returned as its own full list.

In a comb-shaped tree, many leaves can occur at progressively large depths, making total returned path length quadratic in $n$. The output-sensitive notation $O(n+L)$ is more accurate than simply saying $O(n^2)$, because it distinguishes mandatory result construction from traversal work.

## Alternatives and edge cases

- **Remaining-sum backtracking:** Pass `remaining - root.val` instead of accumulating `s`. It is algebraically equivalent and can compare the final leaf value with the remaining amount.
- **Immutable path creation at every node:** Pass `path + [root.val]` to children. It removes explicit `pop` operations but copies prefixes at every visited node, increasing allocation and potentially time even for paths that are never returned.
- **Iterative DFS:** Store `(node, sum, path)` states on a stack. Avoiding recursion is useful for deep trees, but independently stored path lists can consume substantially more memory.
- **Breadth-first search:** Queue each frontier node with its path and sum. It is correct but may retain many full path prefixes simultaneously.
- **Store node references instead of values:** Violates the return contract, which specifically asks for lists of node values.
- **Append the shared `t` directly:** Incorrect because later backtracking mutates the saved object.
- **Stop after one success:** Incorrect because every qualifying path must be returned.
- **Empty tree:** Returns an empty list, including for target zero.
- **Single-node tree:** Returns `[[root.val]]` exactly when the value equals the target.
- **Internal sum equals target:** Do not save it unless the node is also a leaf.
- **Negative values:** Prevent greater-than, less-than, or early-equality pruning.
- **Duplicate path values:** Two structurally different root-to-leaf routes may yield identical value lists; both paths satisfy the structural query and should be represented.
- **Backtracking symmetry:** Every successful `append` to the working path must have exactly one matching `pop`, including at mismatching and successful leaves.
- **Deep tree:** A 5,000-node chain can exceed Python's recursion limit; an explicit stack is safer for the whole legal domain.
- **Output size:** No algorithm can avoid $\Omega(L)$ time and storage when it must materialize $L$ returned integers.
