## General

The competitive source expresses the path-sum search as a “remaining amount” recursion. At each node, it asks: after accounting for this node, can either child complete the amount still required?

This is algebraically equivalent to carrying an accumulated sum, but the leaf test becomes especially direct. If the current node is a leaf and `root.val == sum`, then the value still needed on entry is supplied exactly by that last node.

**The recursive parameter's exact meaning**

`hasPathSum(root, sum)` means: does this subtree contain a path that starts at `root`, ends at a leaf, and whose node values total `sum`?

For the initial public call, `sum` is the original target. When descending from a non-leaf node to either child, the source passes `sum - root.val`. It has consumed the current value, so the child path must provide precisely the difference.

Although the parameter name `sum` shadows Python's built-in `sum` function inside the method, the algorithm never needs that built-in. The shadowing is stylistically inconvenient but does not change behavior.

**Why an empty subtree returns false**

When `root is None`, there is no starting node and no leaf, so no valid path can be formed. Returning `False` also handles missing children during recursion.

In particular, an empty input with target zero is false. It would be incorrect to interpret “zero values add to zero” as a path because the contract requires a root-to-leaf sequence of real nodes.

**Why equality is checked at a leaf**

The condition requires all of the following:

- the left child is absent;
- the right child is absent; and
- the leaf's value equals the entire amount still needed.

Only then does the method return true immediately. If an internal node's value equals the remaining amount, its descendants still have to be included before a leaf is reached, so the internal equality is not sufficient.

At a leaf whose value does not match, the final recursive expression invokes the method on two null children with `sum - root.val`; both return false. That is correct, although an explicit `return False` for a mismatching leaf could avoid those two constant-time calls.

**How subtracting preserves the target equation**

Suppose the original target is $T$ and the values already passed above the current node total $P$. The call's `sum` equals $T-P$.

If the current node has value $v$, each child receives

$$
T-P-v.
$$

Thus the invariant remains true: the child is asked to supply exactly what is still missing after all nodes above it, including the current node. At a leaf, `root.val == sum` is equivalent to $P+\texttt{root.val}=T$, the required complete-path equation.

No value is added twice. A node's value is subtracted only when recursion moves to its child; at the leaf it is compared with the remaining amount instead of being subtracted and then compared with zero.

**Why searching both child directions is complete**

Every root-to-leaf path from an internal node begins through either its left child or its right child. The recursive `or` represents exactly those two possibilities.

Python evaluates the left call first. If it returns true, `or` short-circuits and the right subtree is not visited. If it returns false, the right call receives the same remaining amount because integers are immutable and neither call mutates `sum`.

Therefore the method returns true if at least one qualifying path exists and false only after all relevant candidate paths have failed.

**Tracing the successful example**

Starting with target twenty-two at root five, both child calls are asked for seventeen. Along the left route, node four leaves thirteen, and node eleven leaves two for its children.

Leaf seven does not equal two and fails. Leaf two equals the remaining amount two, so it succeeds. The resulting true value propagates through each pending `or` and reaches the original call.

The actual path equation is $5+4+11+2=22$. The sequence of remaining amounts—twenty-two, seventeen, thirteen, two—encodes the same arithmetic from the opposite direction.

**Why there is no safe greater-than pruning**

Node values may be negative. A remaining amount can move upward or downward when the next value is subtracted. For example, needing five at a node valued ten leaves `-5` for the child, and a child path totaling `-5` can still complete the target.

Accordingly, the source explores based on tree structure and leaf equality rather than assuming all path sums grow monotonically.

**Source and object behavior**

The source defines a module-level `TreeNode` with the expected fields. It reads the tree but never changes child pointers or values. Its recursive calls are instance-method calls, but the object stores no mutable search state, so sequential or nested invocations do not share a cursor or cache.

## Complexity detail

Let $n$ be the number of nodes. If no valid path exists, or if the successful path is encountered after all earlier branches, each real node is processed once. Local work is constant, so worst-case time is $O(n)$.

The `or` short circuit may avoid visiting the right subtree after a left-side success. This improves best-case and typical work in some shapes but does not lower the worst-case asymptotic bound.

Let $h$ be the tree height in nodes. Recursive stack depth is at most $h$, giving $O(h)$ auxiliary space. This is logarithmic for a balanced tree and linear for a skewed chain.

The method retains only a node reference and one integer amount per active frame. It does not store complete paths or a visited set. Its Boolean output uses constant space.

## Alternatives and edge cases

- **Accumulated-sum recursion:** Begin at zero, add each node value, and compare the total with the target at leaves. It maintains the same invariant in forward rather than remaining form.
- **Iterative stack of remaining amounts:** Push `(child, remaining - current_value)` states. This avoids Python recursion depth limits while preserving depth-first short-circuit behavior.
- **Breadth-first states:** Queue `(node, remaining)` pairs. It may discover a shallow successful leaf early but uses frontier-width space.
- **Return false immediately at a mismatching leaf:** Avoids two null recursive calls while leaving complexity and meaning unchanged.
- **Compare at any node:** Incorrect because root-to-internal-node paths do not satisfy the leaf requirement.
- **Treat null as a zero-sum path:** Incorrect for an empty input and for missing children of internal nodes.
- **Prune by sign or magnitude:** Unsafe because both node values and the target may be negative.
- **Empty tree:** Always false, including when the target is zero.
- **One node:** True exactly when its value equals the requested sum.
- **Only one child:** The null side fails immediately, and the real side continues with the reduced amount.
- **Zero-valued nodes:** They simply leave the remaining amount unchanged; leaf status still controls acceptance.
- **Repeated and negative values:** The equation depends on the ordered path total, not uniqueness or monotonicity.
- **Multiple solutions:** Any one successful leaf is enough, so short-circuiting is desirable.
- **Right-only successful path:** It is examined after the entire relevant left search returns false.
- **Recursion limit:** A legal 5,000-node chain can exceed default Python stack depth. An explicit DFS stack is the robust alternative.
- **Built-in name shadowing:** Renaming `sum` to `remaining` would improve clarity and restore access to Python's `sum` function, but it is not a correctness issue here.
- **Fixed-width languages:** Choose a numeric type able to hold a full root-to-leaf sum; Python automatically expands integers.
