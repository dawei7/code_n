## General

**The first value must remain the root**

BST insertion starts with an empty tree, so the first array value becomes the root. Any reorder that produces the identical tree must therefore place the same root first.

Every remaining value smaller than the root belongs to the left subtree. Every larger value belongs to the right subtree because all values are distinct.

The source forms `left` and `right` by filtering the current sequence while preserving relative order within each subsequence.

That relative order is exactly the insertion order seen by each subtree after values for the other subtree are ignored.

**Count valid orders recursively inside each subtree**

`dfs(nums)` returns the number of reorderings of this sequence that construct the same subtree, including the sequence's current order.

If fewer than two values exist, only one ordering is possible, so it returns one.

For a larger sequence, it recursively computes:

- `a = dfs(left)`, valid internal insertion orders for the left subtree.
- `b = dfs(right)`, valid internal insertion orders for the right subtree.

Those choices are independent because a left-subtree insertion never changes the structure of the right subtree and vice versa.

**Interleave left and right orders**

After fixing one valid left order and one valid right order, their elements may be interleaved behind the root.

The internal relative order of the chosen left sequence must stay intact, and the internal relative order of the right sequence must stay intact. Only their cross-subtree positions are free.

If there are `m` left elements and `n` right elements, choose which `m` of the `m+n` post-root positions hold left elements. The count is:

$$
\binom{m+n}{m}.
$$

The remaining positions automatically hold right elements in their chosen relative order.

Thus the recurrence is:

`C[m+n][m] * dfs(left) * dfs(right)`,

with every multiplication reduced modulo $10^9+7$.

**Why interleaving does not change either subtree**

During BST insertion, every value smaller than the root moves left immediately, while every value larger moves right.

Inserting a right value between two left values delays the second left insertion globally but does not insert anything into the left subtree during that delay. The left subtree sees its values in the same relative order.

The same argument holds symmetrically for the right. Therefore every order-preserving interleaving produces the same two subtrees and root.

Conversely, any reorder producing the same BST must induce a valid order within each subtree and some order-preserving interleaving of those induced sequences. The recurrence counts all and only valid reorders.

**Build binomial coefficients with Pascal's triangle**

The source allocates an `n`-by-`n` table `c`.

`c[i][j]` represents $\binom{i}{j}$ modulo `mod`. The first entry and first column are one. Every later entry uses Pascal's identity:

`c[i][j] = c[i - 1][j] + c[i - 1][j - 1]`.

Values are reduced modulo the required constant as the table is built.

The recurrence needs at most $\binom{N-1}{m}$ because one value is the subtree root, so rows zero through `N-1` are sufficient.

**Tracing the three-value example**

For `[2,1,3]`, root is two. Left contains one and right contains three.

Each one-element subtree has one valid ordering. There are $\binom{2}{1}=2$ ways to interleave the two values after root: one then three, or three then one.

`dfs` returns two, including the original `[2,1,3]`. The final subtraction removes that original and returns one alternative.

**Why the original ordering is subtracted**

The recursive count includes every sequence producing the same tree, and the supplied `nums` itself is always one of them.

The problem asks for different reorderings, so the source returns `dfs(nums) - 1`.

Adding `mod` before the final remainder prevents a negative intermediate when the count is one, as for an already forced sorted chain. The result becomes zero.


Induct on subtree size. Empty and one-node subtrees have one ordering.

For a larger subtree, every valid order has the fixed root first, a valid recursively counted order for each child subtree, and one of the binomial order-preserving interleavings. These choices uniquely describe the complete sequence.

Multiplying their counts therefore gives the exact number including the original. Final subtraction yields precisely the requested number of alternative reorderings.

**Degenerate trees**

For a strictly increasing sequence, every node has only a right child. Each recursion has one empty side, and every binomial coefficient is one.

The total count is one, so after removing the original ordering the answer is zero.

The recursion depth in that case is $N$, which is close to Python's default recursion limit at the maximum input size of 1000.

## Complexity detail

The exact source builds an $N$-by-$N$ Pascal table, taking $O(N^2)$ time and $O(N^2)$ space.

Recursive filtering scans the current list in each state. Across a balanced tree this is $O(N\log N)$ total filtering, while a degenerate tree scans lengths $N,N-1,\ldots$, costing $O(N^2)$. The table already makes overall worst-case time $O(N^2)$.

This contradicts the manifest's $O(N)$ time and space. Those bounds do not describe this exact Pascal-table and list-filtering implementation.

Transient left and right lists plus recursion can use $O(N^2)$ cumulative live storage in the worst-shaped recursion, though the Pascal table already dominates the space order.

## Alternatives and edge cases

- **Factorials and modular inverses:** Precompute combinations in $O(N)$ space and roughly $O(N)$ setup, reducing the quadratic Pascal-table storage.
- **Build the BST explicitly:** Subtree sizes and combinatorial products can be computed on nodes, but degenerate insertion may itself be quadratic.
- **Memoize list states:** Inputs partition uniquely down one recursion tree, so repeated identical subproblems are not the main issue.
- **One value:** Only the original order exists, so the returned alternative count is zero.
- **Two values:** Root and child order are forced, also producing zero alternatives.
- **Empty child subtree:** Its recursive count is one and the binomial coefficient handles zero chosen positions.
- **Balanced root split:** Many left-right interleavings can preserve the tree.
- **Strictly sorted input:** The BST is a chain and every coefficient is one.
- **Distinct values:** They make left-versus-right partition unambiguous.
- **Modulo multiplication:** Reduction after each factor keeps values bounded.
- **Original sequence:** It is included recursively and removed exactly once at the end.
- **Recursion depth:** A chain-shaped BST can approach the Python recursion limit.
- **Manifest mismatch:** The exact source is quadratic in both time and table space.
