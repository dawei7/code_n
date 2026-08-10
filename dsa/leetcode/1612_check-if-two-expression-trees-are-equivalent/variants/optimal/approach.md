## General

**Addition trees reduce to variable counts**

Every internal node is addition, so parentheses and tree shape do not affect the value. Addition is associative and commutative:

$$
a+(b+c)=(a+b)+c
$$

and

$$
a+b=b+a.
$$

After flattening an expression, its value is the sum of all variable leaves. If a variable appears multiple times, its coefficient is that occurrence count. Two trees evaluate equally for every possible variable assignment exactly when every variable has the same coefficient in both trees.

The solution records the difference between those coefficient maps in one `Counter`.

**One traversal adds, the other subtracts**

The nested helper `dfs(root, v)` receives a multiplier `v`:

- traversal of `root1` uses `v = 1`, adding each leaf occurrence;
- traversal of `root2` uses `v = -1`, subtracting each leaf occurrence.

When `root is None`, the helper returns. A valid operator node has two children and a leaf has none, so these base calls simply end branches.

If `root.val != '+'`, the node is a variable leaf and the source executes:

`cnt[root.val] += v`.

For an addition node, it does not modify the counter. In either case, it recursively calls the left and right children. Leaf child calls immediately return.

After both traversals, `cnt[c]` equals:

$$
\text{occurrences of }c\text{ in root1}
-\text{occurrences of }c\text{ in root2}.
$$

**Why tree order is irrelevant here**

A traditional expression-tree comparison might require matching corresponding nodes. That would incorrectly reject `a + (b + c)` versus `(b + c) + a` even though they are equivalent under addition.

Collecting leaves ignores grouping and order while preserving multiplicity, exactly the information addition expressions need.

A set would be insufficient. `a + a + b` and `a + b + b` contain the same distinct variables but have different coefficients and can evaluate differently. The counter distinguishes them.

**Final zero test**

The return expression is:

`all(x == 0 for x in cnt.values())`.

If every difference is zero, each variable occurs equally often in both trees. Their flattened sums have identical coefficients, so they evaluate equally for every assignment.

If some difference is nonzero, choose an assignment where that variable is one and every other variable is zero. The two expressions then evaluate to different occurrence counts. They cannot be equivalent for all assignments.

This proves both necessity and sufficiency.

Counter entries that are incremented and later decremented to zero remain stored, but `all` accepts them. Variables appearing in only one tree retain nonzero values and cause failure.

**A trace**

For `a + (b + c)`, the first traversal produces counts `a:1, b:1, c:1`. Traversing `(b + c) + a` with negative one subtracts one from each, leaving every value zero. The result is true.

If the second tree contains `d` instead of `c`, the final counter contains `c:1` and `d:-1`. The zero test fails.

For a repeated-variable case, `a + a` versus `a + b` leaves `a:1` and `b:-1`, also correctly false.

**Why the multiplier parameter is useful**

For the current addition-only problem, the multiplier remains constant throughout one traversal. Passing it through recursion still makes the two-tree comparison compact and prepares the idea used by the follow-up.

If subtraction were supported, an operator `left - right` would recurse into the left child with `v` and the right child with `-v`. Nested subtraction would automatically flip signs, producing signed coefficients. The exact checked-in source does not implement this branch because every internal node is guaranteed to be `+`.

**Why the traversal covers every coefficient**

Every expression-tree leaf is reached once by the recursive visits. Every leaf contributes exactly its traversal multiplier, while operator nodes contribute no variable. Hence the counter is exactly the coefficient difference. The algebraic argument then makes the final zero test an exact equivalence test rather than a heuristic.

## Complexity detail

Let $N_1$ and $N_2$ be the node counts of the two trees, let $H$ be the larger height, and let $U$ be the number of distinct variables encountered.

Each node is visited once, and expected `Counter` updates are constant time, so time complexity is $O(N_1+N_2)$. The final counter scan costs $O(U)$ and is dominated by the traversals.

The counter uses $O(U)$ space. Recursive call depth is $O(H)$, so auxiliary space is $O(H+U)$.

With up to 4,999 nodes, a highly skewed tree can exceed Python’s default recursion limit despite the valid asymptotic bound. An iterative stack traversal would avoid that practical issue.

## Alternatives and edge cases

- **Canonical sorted leaf list:** Collect and sort all variables from each tree, then compare. It is correct but costs $O(L\log L)$ time for $L$ leaves instead of linear counting.
- **Compare tree structures:** This rejects algebraically equivalent expressions with different association or operand order.
- **Use a set of variables:** It loses multiplicity and cannot distinguish different coefficients.
- **Build two counters separately:** This is clear and correct; the checked-in source saves one map by adding one tree and subtracting the other.
- **Single leaf in each tree:** Equal letters cancel to zero; different letters leave two nonzero entries.
- **Repeated variable:** Each leaf occurrence contributes separately, preserving coefficients.
- **Different tree shapes:** Shape is irrelevant under addition as long as leaf counts match.
- **Variables only in one tree:** Their counter difference remains nonzero.
- **Counter zero entries:** They may remain stored but pass the final all-zero test.
- **Valid full binary tree:** Operator nodes have two children and leaves have none, so the generic recursive calls are safe.
- **Subtraction follow-up:** Propagate `v` to the left child and `-v` to the right child at a minus node; ordinary addition propagates the same sign to both.
- **Deep skewed expression:** Recursive DFS may hit Python’s recursion limit; an explicit stack can preserve $O(H+U)$ storage.
- **Equal total node counts:** The contract provides it, but coefficient comparison would still work without that guarantee.
