## General

**A cousin sum is a level sum minus one sibling family**

For a node $x$ at depth $d$, its cousins are all nodes at depth $d$ except:

- $x$ itself;
- any sibling sharing $x$'s parent.

If $L_d$ is the sum of original values at depth $d$, and $F_x$ is the sum of the original values of all children of $x$'s parent, then:

$$
\text{newValue}(x)=L_d-F_x.
$$

This formula includes both one-child and two-child families. It is also valid when no cousins exist: the level total equals the family's total, producing zero.

The exact solution uses two depth-first passes. The first records every $L_d$ before any values change. The second applies the subtraction family by family.

**First DFS: collect original level sums**

List `s` stores the sum for each depth. `dfs1(root, depth)` performs:

1. return immediately for a null child;
2. append a zero when this depth is reached for the first time;
3. add `root.val` to `s[depth]`;
4. recurse into left and right children at `depth + 1`.

Although traversal is depth-first, all nodes with the same depth write to the same list entry. After the pass:

$$
\texttt{s[d]}
=
\sum_{\text{node }v\text{ at depth }d}\text{originalValue}(v).
$$

No node has been mutated yet, so these totals contain exactly the source values needed by every later calculation.

**Handle the root separately**

The root has no parent and therefore no cousins. Its replacement must be zero.

After the first pass, the code assigns:

`root.val = 0`.

The node-count constraint guarantees a nonempty tree, so dereferencing root is safe.

The second DFS computes values only for children of its current node. Starting it at the root naturally handles depth one and below, while the root's special value is already settled.

**Second DFS: process one sibling family together**

At current parent `root`, the code calculates:

`sub = leftChildOriginalValue + rightChildOriginalValue`,

using zero for a missing child.

This `sub` is the original-value total of exactly one sibling family.

The code increments `depth` so it now denotes the children's depth. For each existing child, it assigns:

`s[depth] - sub`.

Both children receive the same cousin sum because they have the same depth and same parent. This is exactly what the definition implies.

**Why in-place mutation does not corrupt later families**

The order deserves careful attention. A parent computes `sub` from both of its children before changing either one.

After assigning a child's new value, the code recursively processes that child's children. Those grandchildren have not yet been modified, so their parent can still read their original values to form its own `sub`.

The algorithm never again needs the old value of the current child:

- all depth totals were saved in `s` during the first pass;
- its parent's sibling sum was computed before mutation;
- its own children's family sum uses the children's values, not its old value.

Therefore, top-down in-place updates preserve every source value until its final necessary use.

**Trace the example tree**

For tree values `[5,4,9,1,10,null,7]`, original level sums are:

- depth zero: five;
- depth one: $4+9=13$;
- depth two: $1+10+7=18$.

The root becomes zero.

At the root, its child-family sum is $4+9=13$. Both depth-one children receive $13-13=0$.

At former node four, child-family sum is $1+10=11$. Its two children receive $18-11=7$, representing cousin value seven.

At former node nine, its only child family has sum seven. That child receives $18-7=11$, representing cousins one and ten.

The final values are `[0,0,0,7,7,null,11]`.

**Why the first pass must precede mutation**

If the algorithm tried to compute a later level sum after some nodes on that level had already been replaced, original and new values would be mixed.

For example, after changing the first sibling family, a running total built from the tree could no longer recover their original contributions.

Saving all level totals first separates data collection from mutation and makes every second-pass formula stable.


After `dfs1`, `s[d]` equals the original total at every depth by direct accumulation over all nodes.

Consider a call of `dfs2` on parent $p$. Its children are still original-valued when `sub` is computed, so `sub` equals the total of all nodes at the children's depth having parent $p$.

For each child $x$, nodes at that depth partition into:

- $x$'s sibling family, totaling `sub`;
- nodes with different parents, exactly the cousins of $x$.

Subtracting `sub` from `s[depth]` therefore leaves precisely the cousin sum. Recursion applies this argument to every parent, while the root is correctly set to zero separately.

**DFS versus the manifest wording**

The manifest describes level-by-level processing, but the stored implementation uses two recursive DFS traversals. Its mathematical idea still relies on level totals and sibling-family subtraction. This explanation follows the exact code's data flow.

## Complexity detail

Let $n$ be the number of tree nodes. `dfs1` visits every node once, and `dfs2` visits every node or parent relationship once. Total time is $O(n)$.

List `s` has one entry per tree depth, at most $O(n)$. Recursive call stacks can reach tree height $h$, also at most $O(n)$ for a skewed tree. Total auxiliary space is $O(n)$ in the worst case.

The tree is modified in place; no replacement tree is allocated.

## Alternatives and edge cases

- **Two-pass BFS:** Compute level sums with a queue, then update children level by level; same $O(n)$ bounds without recursion depth risk.
- **Single BFS with next-level totals:** Possible by temporarily carrying sibling sums, but update timing becomes more subtle.
- **Compute totals while mutating:** Incorrect because later calculations would mix original and replaced values.
- **Single-node tree:** The root becomes zero and there are no child calls.
- **Only children of root:** Their family equals the entire depth, so both become zero.
- **One-child family:** Subtract that child's original value; all other nodes at the level are cousins.
- **Missing child:** It contributes zero to `sub`.
- **Skewed tree:** Every level has one node and every replacement is zero.
- **In-place safety:** A parent's children are read before either is overwritten.
- **Recursion depth:** A highly skewed $10^5$-node tree may require an iterative traversal in runtimes with limited Python recursion.
