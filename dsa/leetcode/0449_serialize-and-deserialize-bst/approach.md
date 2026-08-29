## General

A general binary tree normally needs explicit markers for missing children. Without them, a traversal such as `2 1 3` would not reveal which values belong on which side. A binary search tree supplies additional structure: every value in a left subtree is smaller than its root, and every value in a right subtree is larger. The exact solution exploits that ordering rule so the serialized text needs only node values, not `None` markers.

It uses preorder traversal for serialization: visit the root, then the entire left subtree, then the entire right subtree. Deserialization reads that preorder sequence once while carrying the legal value interval for the subtree currently being reconstructed.

**Serialization records roots before descendants**

The nested `dfs` returns immediately for `None`. For a real node it appends `root.val` to `nums`, recursively visits `root.left`, and then visits `root.right`. Joining the resulting integer list with spaces produces a compact textual preorder sequence.

For the BST

```text
    8
   / \
  3  10
   \
    6
```

preorder is `8 3 6 10`. There are no null-child tokens. The spaces merely separate decimal values so values with multiple digits can be parsed unambiguously.

For an empty tree, `dfs` appends nothing and joining the empty list returns the empty string. Thus empty input has a natural compact representation rather than a special word such as `null`.

**The deserializer's state**

`data.split()` separates the string on whitespace, and `map(int, ...)` converts each token back to an integer. For the empty string, `split()` returns an empty list, so this step also needs no special case.

The index `i` identifies the next preorder value not yet assigned to a node. It is declared `nonlocal` inside the recursive `dfs(mi, mx)` so every recursive call advances the same cursor. The parameters `mi` and `mx` describe the allowed value interval for the subtree being built.

Each call first checks two reasons why the current subtree must be empty:

- `i == len(nums)` means no serialized values remain.
- `nums[i]` outside `[mi, mx]` means the next preorder value belongs to some later subtree or an ancestor's continuation, not to this subtree.

Crucially, the second case returns `None` without incrementing `i`. The value is not discarded; the caller will reconsider it under the next appropriate interval.

If the next value is legal, it must be the root of this subtree because preorder always lists a subtree root before its descendants. The method creates that node, advances `i`, reconstructs the left child within `[mi, x]`, and then reconstructs the right child within `[x, mx]`.

**Why bounds recover the missing structure**

Begin with unbounded limits `(-inf, inf)`, so the first value becomes the whole-tree root. Suppose it is `8`. Every value belonging to its left subtree must be below `8`, so the left recursive call is restricted to `(-inf, 8)`. Preorder places all left-subtree values contiguously immediately after `8`; the call consumes exactly those values that fit its recursively refined bounds.

When the next value is `10`, it does not fit the left-side upper bound. The left call returns without consuming it. Control returns to the root, whose right call uses `(8, inf)`, and `10` is now accepted as the right-subtree root. Bounds therefore detect where one subtree ends and the next begins without explicit separators.

Within a left subtree, the same reasoning repeats. If `3` is accepted below `8`, its left call permits only values below `3`, while its right call permits values between `3` and `8`. Every recursive level contributes one more BST restriction, so a value is accepted only at the unique position consistent with all of its ancestors.

The code writes inclusive comparisons and intervals. Under the conventional strict BST contract, node values do not duplicate, so whether the numerical endpoints are written inclusively or exclusively does not affect valid inputs. If a separate problem allowed duplicates, it would need to specify consistently whether equal values go left or right; preorder values alone cannot reproduce arbitrary duplicate placement without such a rule.

**Why the reconstructed tree matches the original**

Serialization emits the root value first. Deserialization accepts that first value under the whole-tree interval and recreates the same root. All values serialized next from the original left subtree satisfy the root's left bound and appear before any right-subtree value. Recursive bound checks divide and reconstruct that segment according to the same property. The first value not belonging to the left subtree remains unconsumed and becomes available to the right call, which reconstructs the original right subtree in the same way.

Applying this argument recursively to each subtree shows that every node receives the same ancestor relationships as before. No value is duplicated or skipped: `i` advances exactly once when a node is created and never advances on a rejected boundary check. Once the top-level call finishes, all values from a valid serialized BST have been consumed.

**Why no shape markers are necessary**

The compression depends on both pieces of information: preorder says which value is the next subtree root, and BST ordering says which subtree can legally contain each following value. A general binary tree lacks the second fact, which is why this encoding must not be reused for arbitrary trees.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height.

Serialization visits every node once and does constant work per node before joining the tokens, so it takes $O(n)$ time. The `nums` traversal list and encoded output contain $n$ values, requiring $O(n)$ space. Recursive calls use $O(h)$ stack frames, which is $O(\log n)$ for a balanced tree and $O(n)$ for a completely skewed tree.

Deserialization parses $n$ integer tokens in $O(n)$ time. Each token is consumed once to create one node. Boundary checks that return without consuming correspond to completed child positions and remain linear in total across the reconstruction. Thus tree construction also takes $O(n)$ time.

The parsed integer list uses $O(n)$ auxiliary space, and recursive reconstruction uses $O(h)$ stack space. The newly created tree is the required output and itself contains $O(n)$ nodes. Overall space is $O(n)$, matching the manifest.

The text's character count also depends on the number of digits and signs in the values, not merely on the node count. Under the bounded-value contract, each token has bounded length, so it is conventional to describe serialization size as $O(n)$.

## Alternatives and edge cases

- **Postorder plus bounds:** Store left subtree, right subtree, then root; deserialize from the end and build the right child before the left. It has the same asymptotic costs and also avoids null markers.
- **General-tree serialization with null markers:** Preorder plus explicit missing-child tokens works for every binary tree, but it stores structural markers that the BST ordering makes unnecessary here.
- **Level-order serialization:** Breadth-first output is easy to visualize but generally needs placeholders for missing children and a queue, producing a less compact representation.
- **Fixed-width binary encoding:** Packing each value into a fixed number of bytes eliminates variable-length decimal text and delimiters, but it is less readable and requires careful byte handling.
- **Empty tree:** Serialization returns `""`; splitting it yields no values, and the first deserialization call returns `None`.
- **Single node:** One token is accepted as the root; both child calls see the exhausted cursor and return `None`.
- **Skewed tree:** Time remains $O(n)$, but recursion depth becomes $O(n)$. With up to `10^4` nodes, a runtime using Python's default recursion limit may require an iterative implementation or a raised limit.
- **Negative values outside this source's constraints:** Space-separated parsing and infinite bounds would still handle signs, though the stated node values are nonnegative.
- **Duplicate values:** The method assumes the standard strict BST meaning. A duplicate-allowing contract must define one side for equality and use matching bounds; otherwise the original duplicate shape is not uniquely encoded.
- **Malformed serialized data:** The method is designed to decode strings produced by its own serializer. It does not validate that every token was consumed or report malformed external input, which the contract does not require.
