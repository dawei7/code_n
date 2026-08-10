## General

The competitive solution uses half-open inorder intervals and an exclusive postorder end. A dictionary maps each unique value to its inorder index, allowing constant-time splits.

`buildTreeRecu(..., post_end, in_start, in_end)` reconstructs values in inorder interval `[in_start, in_end)`. The matching postorder block ends just before index `post_end`; its start is implicit from the equal subtree size.

The `inorder` array parameter is passed recursively but never read. Bounds and `lookup` contain all information the helper uses.

**Empty interval and root**

When `in_start == in_end`, the subtree has no values and returns `None`.

Otherwise, postorder's final value is the root:

`postorder[post_end - 1]`.

Let its inorder index be $i$. The left interval is `[in_start, i)`, and the right interval is `[i + 1, in_end)`.

Their sizes are:

$$
L=i-\texttt{in\_start},
\qquad
R=\texttt{in\_end}-i-1.
$$

**The right subtree's postorder end**

The root occupies index `post_end - 1`. Immediately before it lies the complete right-subtree postorder block, so that block's exclusive end is `post_end - 1`.

Its inorder bounds are `[i + 1, in_end)`. This yields the right call in the source.

**The left subtree's postorder end**

The left block must end before the $R$ right values and before the one root value. Starting from `post_end`, subtract:

$$
1+R=1+(\texttt{in\_end}-i-1)=\texttt{in\_end}-i.
$$

Therefore its exclusive end is:

$$
\texttt{post\_end}-1-(\texttt{in\_end}-i-1),
$$

exactly the expression in the selected code. Its inorder bounds are `[in_start, i)`.

Although the code constructs `node.left` before `node.right`, explicit interval endpoints make this safe. No global postorder cursor is consumed.

**Detailed root split**

For the Reference arrays, the initial `post_end` is five and inorder interval is `[0,5)`. Root is `postorder[4] = 3`, located at inorder index one.

The right size is three, so the left postorder end is `5 - 1 - 3 = 1`. Its block is `[0,1)`, containing nine. The right postorder end is four, so its block ends at twenty and covers the three right values.

The same calculations recursively place fifteen and seven under twenty.

**Why the ranges remain consistent**

The child inorder sizes sum to the parent size minus one. The child postorder blocks also partition the parent block before its root into a left block of size $L$ followed by a right block of size $R$.

Unique values make the root lookup singular. Valid-traversal guarantees ensure the root lies inside the current inorder interval. Therefore every child call receives matching value sets.

By induction on interval length, each returned subtree has exactly the requested inorder and postorder traversals. Since root and splits are forced at every step, reconstruction is unique.

The implicit postorder start can be recovered whenever needed. The current subtree size is `in_end - in_start`, so its block starts at:

$$
\texttt{post\_end}-(\texttt{in\_end}-\texttt{in\_start}).
$$

The left block begins there and has $L$ entries. The right block follows with $R$ entries, and the root is final. Although the helper does not pass this start explicitly, the derived child ends preserve exactly that partition.

Half-open bounds also make empty sides uniform. If the root is the first inorder value, `[in_start, i)` is empty. If it is the last, `[i+1, in_end)` is empty. Both reach the same equality base case without special branches.

## Complexity detail

The lookup loop visits all $n$ inorder values. Each node is constructed once with expected constant-time lookup and fixed arithmetic, so time is $O(n)$.

The lookup map requires $O(n)$ space. The recursion stack uses $O(h)$, at most $O(n)$, and output contains $n$ new nodes. Overall auxiliary and total space are $O(n)$, matching the manifest.

For balanced trees, stack usage falls to $O(\log n)$, but the dictionary remains linear, so this implementation's total auxiliary bound stays $O(n)$.

No slice or linear root search is performed.

## Alternatives and edge cases

- **Starts-plus-size state:** Carry inorder start, postorder start, and subtree size. It makes both child sizes explicit.
- **Mutating `postorder.pop()`:** Recurse right before left while consuming roots backward. It is concise but changes the caller's list.
- **Iterative reconstruction:** A stack and reverse-postorder scan avoid deep recursion.
- **Search inorder each call:** Correct but potentially quadratic on skewed trees.
- **Single node:** Both half-open child intervals are empty.
- **Skewed input:** Linear work still produces linear recursion depth and possible `RecursionError`.
- **Unique values:** Without them, one value could have several split positions and traversals might not determine one tree.
- **Unused `inorder` parameter:** Removing it from the helper would not affect behavior.
- **Negative values:** Work normally as dictionary keys.
- **Output structure:** Child pointers are assigned after creating each root; traversals are not modified.
- **Left-first construction:** Safe only because every call has explicit boundaries; a shared backward iterator would require right-first construction.
- **Block lengths:** The postorder and inorder blocks for a state always have the same length, even though only the inorder length is written in the parameter list.
- **No slicing:** Arrays are shared read-only across all calls, preventing copying overhead.
