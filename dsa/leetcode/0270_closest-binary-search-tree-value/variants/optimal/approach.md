## General

**Use the BST ordering to avoid visiting the whole tree**

A general binary tree offers no information about where values lie, so finding the closest value could require inspecting every node. A binary search tree is different. At a node with value `x`, every value in the left subtree is smaller than `x`, and every value in the right subtree is larger than `x`. That ordering lets the solution prove that one entire subtree cannot beat a value it has already considered.

The exact solution follows one root-to-leaf search path. Along that path, it keeps the best candidate seen so far in `ans` and that candidate's absolute distance from `target` in `diff`.

**Define exactly what “better” means**

For a node value $x$, its distance from the target is

$$
d(x)=\lvert \texttt{target}-x\rvert.
$$

A smaller distance is always better. If two values have the same distance, the contract requires the smaller value. The source implements this lexicographic preference explicitly. For the current node it computes `nxt = abs(target - node.val)` and replaces the stored answer when either:

- `nxt < diff`, meaning the current value is strictly closer; or
- `nxt == diff and node.val < ans`, meaning the distance ties but the current value is smaller.

This is equivalent to comparing candidate keys `(distance, value)` and keeping the minimum key. Stating both parts is important: an implementation that updates only for a smaller distance can return the wrong member of an exact tie, depending on traversal order.

The initial distance is positive infinity. Therefore, the first real node always becomes the current answer. Although `ans` begins as zero, that placeholder cannot leak into the result because the contract guarantees a nonempty tree and every finite node distance is less than infinity.

**Why only one child can still improve the answer**

After evaluating the current value `x`, compare `target` with `x`.

If `target < x`, every value $y$ in the right subtree satisfies $y>x>\texttt{target}$. Therefore,

$$
\lvert y-\texttt{target}\rvert
>
\lvert x-\texttt{target}\rvert.
$$

The current node is closer than every value in the right subtree. Since the current node has just been considered, no right-subtree value can improve the saved answer. Only the left subtree might contain values closer to the smaller target, so the source recurses left.

If `target >= x`, every value $y$ in the left subtree satisfies $y<x\le\texttt{target}$. Hence

$$
\lvert \texttt{target}-y\rvert
>
\lvert \texttt{target}-x\rvert
$$

for distinct BST values. The checked current node dominates the whole left subtree, and only the right subtree can contain an improvement. The source consequently recurses right in the `else` case.

This pruning is safe even relative to the best candidate from an earlier ancestor. The discarded subtree cannot beat the current node, and the saved answer is no worse than the current node after the update step. A value that cannot beat the current node therefore cannot beat the saved answer either.

If `target == x`, the current distance is zero, the smallest possible distance. The answer can no longer improve. The exact source still follows the right branch because equality enters its `else` case, but this extra traversal cannot change the zero-distance answer. An early return would be a valid optimization, not a correctness requirement.

**Recursive state and termination**

The helper `dfs(node)` returns immediately for `None`. For a real node, it updates the shared `ans` and `diff`, selects exactly one child, and calls itself on that child. The `nonlocal` declaration allows every recursive frame to update the two variables created by the enclosing method rather than creating unrelated local copies.

Each call moves down one tree edge. A finite tree eventually reaches a missing child, so recursion terminates. Because there is no branching, the visited nodes form the same search path that ordinary BST lookup would follow for `target`.

The maintained fact after each visited node is simple: `ans` is the best value, using `(distance, value)` ordering, among all visited nodes. The update preserves this fact directly. The BST pruning proof shows that every skipped subtree is dominated by a visited boundary node and cannot contain a better answer. When the path ends, all unvisited regions have been safely excluded, so the best visited value is also the best value in the entire tree.

**Trace the first example**

For the BST represented by `[4,2,5,1,3]` and `target = 3.714286`:

| Visited value | Distance | Best after visit | Direction and reason |
|---:|---:|---:|---|
| 4 | 0.285714 | 4 | Target is smaller, so go left |
| 2 | 1.714286 | 4 | Target is larger, so go right |
| 3 | 0.714286 | 4 | Target is larger, so go right |

The right child of `3` is absent, so the search stops and returns `4`. The right subtree of `4` was safely skipped because all of its values are greater than `4`, already farther from a target below `4`. The left subtree of `2` was safely skipped because all of its values are smaller than `2`, already farther from a target above `2`.

For the single-node tree `[1]` with `target = 4.428571`, the first visit changes `ans` from its placeholder to `1`. The search goes right, reaches `None`, and returns `1`.

For a tie illustration, suppose the tree contains `2` and `4` and the target is `3`. Both distances equal one. If `4` is seen first, it becomes the initial answer; when `2` is later seen, the equal-distance and smaller-value condition replaces `4` with `2`. If `2` is seen first, `4` cannot replace it. The result is therefore independent of which tied candidate happens to be encountered first.

## Complexity detail

Let $h$ be the height of the tree and $n$ its number of nodes. The helper visits at most one node at each depth, so it performs $O(h)$ time. In a balanced BST, $h=O(\log n)$; in a completely skewed BST, $h=O(n)$. The worst-case time is therefore $O(n)$, while the height-sensitive bound is $O(h)$.

The manifest records $O(1)$ auxiliary space, which is the bound for the iterative version of this one-branch search. The exact protected source is recursive. Its calls do not branch, but each active call remains on Python's call stack until the deeper call returns. The maximum number of simultaneous frames is $h$, so the exact implementation uses $O(h)$ auxiliary stack space.

Apart from recursion, `ans`, `diff`, `nxt`, and the current node reference occupy $O(1)$ state. Rewriting the helper as a `while node is not None` loop would preserve the same decisions and $O(h)$ time while achieving the manifest's $O(1)$ auxiliary-space target.

The tree itself is input storage and is not counted as auxiliary space. The method returns one integer, so output storage is $O(1)$.

## Alternatives and edge cases

- **Iterative BST descent:** Maintain the same best candidate in a loop and move to one child each iteration. It has identical $O(h)$ time, avoids recursion limits, and uses $O(1)$ auxiliary space, exactly matching the manifest bound.
- **Full inorder traversal:** Inorder produces all BST values in sorted order and can then find the closest one. It is correct but costs $O(n)$ time and up to $O(n)$ storage if the values are materialized, discarding the opportunity to prune.
- **Iterative inorder with early stopping:** Stop once traversal crosses the target and compare its predecessor and successor. This can be useful, but it needs an explicit stack of up to $O(h)$ and may visit many values before reaching the crossing point.
- **Ordinary full-tree DFS:** Comparing every node requires $O(n)$ time and recursion or stack space. It works even without the BST property, but it is not optimal for an ordered tree.
- **Exact target match:** Distance zero is globally optimal. The source remains correct if it continues down the right branch, though an immediate return could avoid unnecessary calls.
- **Equal-distance values:** The smaller value must win. The second half of the update condition is essential and should not be replaced by traversal-order assumptions.
- **Target below every node:** The path repeatedly moves left, and the minimum tree value is ultimately closest. Every skipped right subtree lies even farther above the target.
- **Target above every node:** The path repeatedly moves right, and the maximum tree value is closest. Every skipped left subtree lies even farther below the target.
- **Single-node tree:** Infinity guarantees that the root replaces the placeholder answer, after which the missing selected child ends the search.
- **Zero-valued node:** The initial `ans = 0` does not give zero special status. Candidate validity is controlled by `diff`, which starts at infinity; a zero is returned only if an actual tree node makes it optimal.
- **Highly skewed tree:** The runtime becomes $O(n)$ and the exact recursive source also uses $O(n)$ call-stack space. With as many as $10^4$ nodes, a sufficiently deep Python tree can exceed the interpreter's recursion limit; the iterative form avoids that implementation hazard.
- **Floating-point target:** Distances are computed with ordinary floating-point arithmetic. The explicit equality test correctly handles exactly represented ties such as an integer midpoint ending in `.5`; as usual with binary floating point, values produced by prior approximate computation may not represent an intended mathematical tie exactly.
- **Empty root outside the contract:** The reference guarantees a nonempty tree. If `None` were passed, DFS would never replace the placeholder and the source would return `0`, which is not a meaningful result for an empty tree; callers must respect the stated precondition.
