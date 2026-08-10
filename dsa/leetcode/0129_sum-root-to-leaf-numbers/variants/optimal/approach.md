## General

Each root-to-leaf path spells a decimal number. When a path prefix already represents value `s`, appending one digit `d` produces:

`s * 10 + d`.

The selected depth-first search carries that prefix value down the tree. A leaf returns its completed number; an internal node returns the sum of completed numbers from both child subtrees.

**The recursive parameter invariant**

At entry to `dfs(root, s)`, `s` is the decimal number formed by the real nodes from the original root through the parent of `root`.

The public call uses zero because no digit precedes the original root. At a real node, `s = s * 10 + root.val` extends the number by exactly one decimal digit.

Python integers are immutable, so each call receives its own numeric prefix. Passing the updated `s` into the left subtree cannot be changed by work in the right subtree, and no backtracking subtraction is needed.

**Why multiplication by ten appends a digit**

If the current prefix has decimal digits $d_1d_2\ldots d_k$, its value is:

$$
\sum_{i=1}^{k}d_i10^{k-i}.
$$

Multiplying by ten shifts every digit one place left. Adding the new value `root.val`, which lies from zero through nine, places it in the units position. The result represents $d_1d_2\ldots d_k\texttt{root.val}$.

This works for leading zeros too. A path `0 -> 1 -> 2` has numeric value twelve, and repeated arithmetic produces zero, then one, then twelve.

**Why only leaves return completed numbers**

A valid number uses a complete root-to-leaf path. An internal node cannot contribute its current prefix directly, even if it has only one child.

The source checks that both `left` and `right` are absent before returning `s`. That is the exact leaf definition.

If `root` is null, the call returns zero. This means a missing child contributes no completed path, not a shorter number ending at the parent.

**How child results combine**

For an internal node, every leaf below it lies in either the left subtree or the right subtree. The sets are disjoint.

`dfs(root.left, s) + dfs(root.right, s)` sums the completed numbers from both groups. A missing side contributes zero through the base case, while the real side contributes all of its paths.

Because the contract asks for the total of all paths rather than a maximum or minimum, both recursive branches must be evaluated and added.

**Why every path is counted exactly once**

Each leaf has one unique route from the root in a tree. DFS follows that route once, carrying the exact decimal prefix at every step.

When the leaf is reached, its full number is returned once. Internal additions combine disjoint leaf sets, so no leaf number is duplicated. Null calls add nothing, so no nonexistent route is counted.

Inductively, every `dfs` call returns the sum of all root-prefix-extended numbers ending at leaves in its subtree. The initial prefix is empty, so the root call returns exactly the required total.

**Tracing `[1,2,3]`**

At root one, the prefix changes from zero to one. The left call appends digit two and reaches a leaf, returning twelve.

The right call independently appends digit three to the same parent prefix one and returns thirteen. Root addition produces twenty-five.

The integer prefix avoids storing character strings or explicit node paths.

**Tracing `[4,9,0,5,1]`**

The route through four and nine carries prefix forty-nine. Leaves five and one turn it into 495 and 491.

The right child zero of the root carries prefix forty. Because that node is a leaf, it returns forty. Adding all three leaf results gives 1,026.

The zero digit is preserved by positional multiplication even though ordinary integer formatting does not display a leading or trailing marker.

**Source dependencies**

The selected file annotates `Optional[TreeNode]`, but `Optional` and `TreeNode` are not actively imported or defined. The surrounding harness must supply them; a standalone module needs the typing import and node class.

The source only reads node fields and does not mutate the tree.

## Complexity detail

Let $n$ be the number of nodes and $h$ the maximum root-to-leaf node count. Each real node is visited once and does constant arithmetic, so time is $O(n)$.

The recursive stack follows one path at a time and uses $O(h)$ auxiliary space. The contract bounds depth by ten, so actual stack depth is very small, but $O(h)$ is the structural complexity.

Only one integer prefix exists per active frame. No path list or string is constructed. The returned integer uses constant output space.

Python integer arithmetic is effectively constant for the bounded path values here. The problem also guarantees the final sum fits a signed 32-bit integer.

## Alternatives and edge cases

- **Iterative preorder stack:** Store `(node, prefix)` pairs and add prefixes at leaves. It avoids recursion and uses $O(h)$ to $O(n)$ explicit stack entries depending on shape.
- **Morris preorder traversal:** Temporarily threads the tree to achieve $O(1)$ extra space, but prefix rollback and leaf detection are substantially more delicate.
- **Build digit strings:** Join path digits and convert at leaves. It works but allocates more data and requires explicit path backtracking.
- **Empty tree outside the contract:** The helper returns zero.
- **Single node:** Its digit is the only path number.
- **Digit zero:** Appending it multiplies the prefix by ten, as decimal notation requires.
- **Leading zero root:** Numeric value naturally ignores leading zeros without changing the sum.
- **One-child node:** It is not a leaf; the missing side returns zero and the real side continues.
- **Both children:** Their disjoint leaf totals are added.
- **No negative digits:** The decimal append formula relies on values from zero through nine.
- **Depth bound:** Keeps represented numbers and recursion shallow.
- **Input preservation:** No node link or value is changed.
- **Missing names:** `Optional` and `TreeNode` must be available.
- **All paths, not best path:** Child totals use addition rather than `min` or `max`.
