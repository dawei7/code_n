## General

A preorder traversal visits a node before its left subtree and then its right subtree. In a binary search tree with unique values, every left-descendant value is smaller than its ancestor and every right-descendant value is larger. The challenge is not merely comparing consecutive values; it is remembering which ancestor ranges are still available as the traversal moves down and later backtracks.

The exact solution simulates that traversal with a monotonically decreasing stack and one lower bound named `last`.

- `stk` represents the active chain of ancestors whose traversal has not been completely left behind.
- `last` is the greatest ancestor value whose right subtree the sequence has already entered. Every future value must be greater than this bound.

Initially the stack is empty and `last = -inf`, so the first value has no lower restriction.

**Descending values mean continuing left**

If a new value `x` is smaller than the stack top, it can lie in the current node's left subtree. Pushing it preserves a strictly decreasing stack. For example, the beginning `[10, 9, 8, 7]` can represent a chain of left children, and the stack becomes `[10, 9, 8, 7]`.

No lower bound changes while descending left because the traversal has not yet closed a left subtree and crossed into a right subtree of one of those ancestors.

**A larger value means backtracking**

When `x` is greater than the stack top, it cannot be inside that top node's left subtree. Preorder has finished that region and must climb toward an ancestor where `x` can belong on the right.

The loop

```text
while stk and stk[-1] < x:
    last = stk.pop()
```

pops every smaller active ancestor. After the loop, either the stack is empty or its top is greater than `x`. The last value popped is the root whose right-side region has just been entered most specifically, so it becomes the new lower bound.

Because the stack is decreasing from bottom to top, popped values increase as the loop climbs. In `[5, 2, 1]` with `x = 3`, it pops `1` and then `2`, setting `last` first to `1` and finally to `2`. It stops below `5`, placing `3` in the right subtree of `2` but still in the left subtree of `5`. Future values must remain above `2`.

**Why a value below `last` is impossible**

Once a node is popped because the traversal moved to its right, preorder can never return to that node's left subtree. All future nodes in the currently open right-side region must be greater than the popped ancestor. If a later `x` is less than `last`, it belongs on the forbidden left side of an ancestor whose left subtree has already been completed.

The solution checks `if x < last: return False` before performing new pops. This is enough under the guarantee that all input values are unique. A repeated value equal to `last` cannot occur in valid input. For a version allowing arbitrary inputs but still requiring a strict BST, the rejection would normally be `x <= last`.

**Trace of a valid sequence**

For `[5, 2, 1, 3, 6]`:

- Read `5`: it is above negative infinity; push it. Stack: `[5]`.
- Read `2`: it is below `5`, so no pop is needed. Push it. Stack: `[5, 2]`.
- Read `1`: continue left and push. Stack: `[5, 2, 1]`.
- Read `3`: it is above `1`, so pop `1`; it is also above `2`, so pop `2`. `last` becomes `2`. Since `3` remains below `5`, stop and push it. Stack: `[5, 3]`.
- Read `6`: it is above `3` and `5`, so pop both. `last` becomes `5`, and push `6`.

No value violates the latest lower bound, so the sequence can be the preorder traversal of a BST and the function returns `True`.

**Trace of an invalid sequence**

For `[5, 2, 6, 1, 3]`, reading `6` pops both `2` and `5`, setting `last = 5`. This records that traversal has entered the right subtree of `5`. The next value is `1`, which is below `5`. It would need to appear in the left subtree of `5`, but preorder already passed that entire subtree before visiting `6`. The check rejects immediately.

**Why passing the scan proves validity**

The stack simulates the path that an actual preorder construction would maintain. A smaller next value extends the current left path. A larger next value closes completed subtrees until the algorithm finds the nearest greater ancestor, after which the value fits as a descendant on the right side of the last popped node while remaining on the left side of any greater stack top.

`last` captures all lower-bound restrictions from ancestors no longer on the stack. Because each later right-subtree transition can only raise that bound, checking it prevents the traversal from reentering any completed left region. If every value fits, each step has a legal placement consistent with all ancestor bounds, yielding a BST whose preorder is the given sequence. If a value falls below the bound, no legal placement exists, so rejection is necessary.

The uniqueness guarantee also keeps the stack strictly decreasing and avoids deciding which side receives an equal key.

## Complexity detail

Let $n$ be the number of preorder values. Every value is pushed exactly once. A value can be popped at most once, because it never reenters the stack. Although the `while` loop is nested inside the `for` loop, there are at most $n$ pops across the complete execution. Total time is therefore $O(n)$.

The explicit stack can hold all $n$ values for a strictly decreasing sequence, corresponding to a completely left-skewed BST. Its worst-case auxiliary space is $O(n)$.

This differs from the manifest's $O(1)$ space description, which refers to reusing the consumed prefix of the input list as stack storage. The exact protected source creates `stk = []` and does not modify `preorder`, so its real auxiliary bound is $O(n)$. The scalar lower bound and loop variable add only constant space.

## Alternatives and edge cases

- **Reuse `preorder` as the stack:** Maintain a stack length and overwrite the already-read prefix. This preserves $O(n)$ time and reduces auxiliary space to $O(1)$, but mutates the input. It is the follow-up technique described by the manifest, not the exact source.
- **Recursive bounds parser:** Consume preorder values while they fit a `(lower, upper)` range, recursively assigning left and right subtrees. It can run in $O(n)$ time but uses $O(h)$ call-stack space and requires careful shared-index handling.
- **Build the BST explicitly:** Insert every value and compare the resulting preorder. A skewed sequence can make insertion $O(n^2)$, and allocating nodes is unnecessary for simple verification.
- **Strictly decreasing input:** No values are popped; it represents an all-left chain. The stack reaches size $n$.
- **Strictly increasing input:** Each new value pops the previous top and raises `last`; it represents an all-right chain and still runs in linear time.
- **One value:** It satisfies the unrestricted root position, is pushed, and the function returns `True`.
- **A late small value:** If traversal has already entered a right subtree, the lower-bound check detects the attempt to return to a completed left side.
- **Duplicate values:** The contract excludes them. With duplicates present, the source's strict `< last` check and pop condition would need adjustment based on a clearly defined duplicate-placement policy.
- **Negative values:** The local problem bounds values positively, but `last = -inf` means the algorithm itself also supports negative integers without a special sentinel collision.
- **Input preservation:** The explicit stack leaves `preorder` unchanged, which may be preferable even though it costs linear auxiliary memory.
- **Order of the bound check:** Testing `x < last` before popping is valid because `last` summarizes previously closed ancestors. The subsequent pops can only establish a new bound for future values after `x` is placed.
