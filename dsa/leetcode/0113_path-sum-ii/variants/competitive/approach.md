## General

The competitive solution performs left-to-right depth-first search while carrying:

- `sum`, the value still required from the current node down to a leaf;
- `cur`, one mutable list of values above the current node; and
- `result`, the shared list of completed output paths.

The algorithm uses remaining-sum arithmetic and backtracking. It copies a path only when it finds a successful leaf, so failed prefixes do not create permanent path lists.

**The helper's entry invariant**

At entry to `pathSumRecu(result, cur, root, sum)`, `cur` contains the values from the original root through `root`'s parent. The parameter `sum` is the original target minus the total of those same values.

If `root is None`, no path can continue, so the helper returns the existing `result` unchanged.

For a non-leaf node, the method appends `root.val` to `cur` and passes `sum - root.val` to both children. The list and numeric state then remain synchronized: both describe a prefix that now includes the current node.

**The successful-leaf special case**

Before appending the leaf to the shared working list, the source checks whether:

- both children are absent; and
- `root.val == sum`.

The equality means the final leaf supplies exactly the amount still needed after all ancestors. If it succeeds, `cur + [root.val]` creates a new list containing the complete path and appends that new list to `result`.

The helper returns immediately in this case. That early return is safe because it never appended the leaf to `cur`; there is nothing to pop. The parent's working prefix remains unchanged.

This ordering is an important source-specific detail. If the leaf were appended to `cur` first, an early return without a matching `pop` would corrupt the shared path for later branches.

**What happens at a mismatching leaf**

A leaf whose value does not equal the remaining amount falls through to the ordinary backtracking logic. Its value is appended to `cur`, and both recursive calls receive `None` children and return without change.

The following `cur.pop()` removes the leaf, restoring the parent's prefix. This performs two extra constant-time null calls compared with an explicit mismatching-leaf return, but it remains correct.

**Why copied output paths stay stable**

`cur + [root.val]` constructs a new list. The saved output does not alias the mutable `cur` list, so later appends and pops cannot alter it.

Because path entries are integers, a shallow list creation contains all the independence needed. The algorithm does not need to clone tree nodes or perform a recursive deep copy.

Each successful leaf creates exactly one output list. Structurally distinct leaves are visited separately, even if their value sequences happen to be identical.

**Backtracking across siblings**

For an ordinary current node, `cur.append(root.val)` extends the path. The left recursive call explores every leaf below the left child and returns with its own appended values removed. The right call then sees the same prefix through the current node.

After both children finish, `cur.pop()` removes the current value. Thus the helper restores `cur` to exactly its entry state before returning. This invariant ensures values from the left subtree never leak into a path through the right subtree.

The source threads `result` through return values, but recursive callers do not need to replace their reference with the returned object. Every helper mutates the same list in place. Returning it is convenient for the outermost call and harmless elsewhere.

**Why remaining subtraction is exact**

Let the target be $T$, and suppose values already stored in `cur` sum to $P$. By the entry invariant, `sum` equals $T-P$.

At a leaf with value $v$, the condition $v=\texttt{sum}$ is equivalent to

$$
P+v=T.
$$

At an internal node, subtracting its value produces the exact amount required from either child path. Every complete path is explored because the method recurses left and right, and only leaves satisfying the equation are copied.

This establishes that every returned list is valid and every valid root-to-leaf path is eventually returned.

**Tracing the Reference example**

On the left successful route, ancestors place `[5, 4, 11]` in `cur` while the remaining amount becomes two. Leaf two matches, so `cur + [2]` saves `[5, 4, 11, 2]` without changing `cur`.

After backtracking to the root, the search enters the right subtree. It eventually carries `[5, 8, 4]` and needs five. Leaf five matches, producing the second independent list `[5, 8, 4, 5]`.

The method never stops after the first match because the contract asks for all paths.

**No monotonic pruning**

Values may be negative. A remaining amount can change sign repeatedly, so the algorithm cannot safely stop because it becomes negative, exceeds a node value, or reaches zero before a leaf. Structural leaf status and exact final equality are the only acceptance test.

The parameter name `sum` shadows Python's built-in function inside these methods, but the built-in is unused. The source defines its own compatible `TreeNode` and does not mutate the input tree.

## Complexity detail

Let $n$ be the node count, $h$ the maximum root-to-leaf path length, and $L$ the total number of integer values in all returned paths.

Every real node is visited once. Ordinary appends, pops, subtractions, and checks are constant time, giving $O(n)$ traversal work. Each successful expression `cur + [root.val]` copies one complete output path. Across all successes, copying costs $O(L)$. Total time is $O(n+L)$.

The recursive stack and `cur` each hold at most one active root-to-node path, so auxiliary space excluding results is $O(h)$. `result` and its independent path lists require $O(L)$ output space. Including output, total space is $O(h+L)$.

The source header's plain $O(n)$ time omits the cost of materializing returned lists. The manifest's $O(n+L)$ is the more exact output-sensitive bound. In extreme tree shapes with many long successful paths, $L$ can be quadratic in $n$.

## Alternatives and edge cases

- **Accumulated-sum path state:** Add values while descending and compare with the original target at leaves. It has the same correctness and complexity.
- **Append every node before leaf testing:** This can simplify a uniform trace, but every return path—including the successful early case—must execute a matching `pop`.
- **Pass `cur + [value]` to every child:** Removes mutation and restoration hazards but copies prefixes at every node rather than only for successful outputs.
- **Iterative stack with path snapshots:** Avoids recursion limits but may hold many copied path prefixes at once.
- **Breadth-first path states:** Correct, yet expensive when a wide level requires a separate path list for every queued node.
- **Return after the first match:** Incorrect because the output must include all matching paths.
- **Append `cur` itself to `result`:** Incorrect; subsequent backtracking would mutate saved paths.
- **Empty root:** The first helper call returns the initially empty `result`.
- **Successful leaf:** It is copied with `cur + [root.val]` and does not modify `cur`.
- **Mismatching leaf:** It temporarily appends, explores two null children, and then pops; an explicit fast failure would be equivalent.
- **Internal equality:** Does not qualify because the path must reach a leaf.
- **Negative and zero values:** Do not change the structural logic and prohibit monotonic pruning.
- **Duplicate value sequences:** Separate leaf routes can legitimately contribute equal lists.
- **Mutable result ownership:** All calls share one `result`; replacing it inside a helper would require consistent propagation, but this source mutates it in place.
- **Deep chain:** Auxiliary state becomes $O(n)$ and may exceed Python's default recursion limit before reaching the 5,000-node constraint.
- **Output lower bound:** Producing all returned values inherently costs at least $\Omega(L)$ time and space.
- **Built-in shadowing:** Renaming `sum` to `remaining` would improve readability without changing the algorithm.
