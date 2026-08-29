## General

**Recognize complete subtrees from the bottom up.**

A non-null binary-tree node in preorder is serialized as three consecutive logical parts:

1. the node's value;
2. a complete serialization of its left subtree;
3. a complete serialization of its right subtree.

A null subtree is represented by the single token `#`. If both child subtrees of a node have already been recognized and summarized as `#`, the top of the working sequence has the form

`value, #, #`.

That triple is itself one complete subtree. From its parent's perspective, the internal details no longer matter: the entire subtree fills one child position. The exact source therefore replaces the three tokens with one `#` marker. Repeating this reduction recognizes progressively larger subtrees until, for a valid serialization, the entire input becomes a single marker.

The marker `#` has two related meanings while processing: it can be an original null pointer, or it can summarize a complete non-null subtree that has just been reduced. Both meanings are interchangeable for the reduction rule because either represents exactly one complete child subtree.

**Process tokens with a reduction stack.**

The source first calls `preorder.split(',')`, producing the tokens in their original preorder sequence. For each token `c`, it appends `c` to `stk`.

After every append, it checks whether the last three stack entries satisfy all of these conditions:

- at least three entries exist;
- the last entry is `#`;
- the second-last entry is `#`;
- the third-last entry is not `#`.

The third-last token is therefore a non-null node value, and the last two entries represent its completed left and right subtrees. The source removes that triple with `stk = stk[:-3]` and appends one `#` in its place.

The check is inside a `while`, not an `if`. Completing one subtree may immediately complete its parent. For example, a parent might already have its value and completed left subtree on the stack; reducing the right subtree creates the parent's `value, #, #` pattern. Cascading reductions must continue until the top no longer represents a complete non-null subtree.

**A small reduction example.**

Consider the serialization `2,1,#,#,3,#,#`.

- Read `2`, then `1`, then the first two `#` tokens. The top is `1,#,#`, so reduce it. The stack becomes `[2,#]`; the marker now summarizes the complete subtree rooted at `1`.
- Read `3,#,#`. Reduce `3,#,#` to one marker. The stack becomes `[2,#,#]`.
- The `while` condition is still true, so reduce `2,#,#` to a single `#`.

The final stack is `['#']`, so the serialization is valid.

For a larger tree, the same mechanism waits until each pair of child subtrees is complete. Preorder puts the parent value before both children, so once both child summaries reach the top, their parent is located immediately before them.

**Why `#,#,#` must not collapse.**

The condition `stk[-3] != '#'` matters. A null marker cannot be the root of a non-null node with two children. Three completed-subtree markers in a row do not automatically form one subtree; the first could already have filled an earlier slot, and there is no node value introducing the other two as its children.

Only a genuine integer token can serve as the root in the `value,#,#` grammar rule. The input guarantee says every non-`#` token is an integer, so the source does not need to parse or validate the numeric text.

**Why one final marker is the exact acceptance condition.**

After all tokens have been processed, the source returns true only when the stack length is one and its sole entry is `#`.

If multiple entries remain, the input contains incomplete or extra material. For `1,#`, the stack is `[1,#]`: the root has only one serialized child. For `9,#,#,1`, the first three tokens reduce to `#`, but the extra `1` remains, producing `['#','1']`. This represents one complete tree followed by an unrelated token and is correctly rejected.

The single token `#` is accepted. It is the serialization of an empty tree, a complete tree consisting of a null root. Any non-null one-token input such as `1` remains a value rather than a completion marker and is rejected because both child serializations are missing.

**Why every reduction preserves validity information.**

Suppose the source replaces `value,#,#` by `#`. Each of the last two markers represents one complete child serialization, so the triple represents one complete non-null binary tree rooted at `value`. Replacing it by a marker records exactly the fact its parent needs: one child subtree has been completely supplied. Thus a reduction never turns an incomplete structure into a complete one.

This establishes soundness. If the entire token sequence reduces to one marker, reverse the reductions: each collapsed marker can be expanded into its stored conceptual non-null root with two complete children. These expansions reconstruct the grammatical structure of one binary tree, even though the algorithm is forbidden and does not need to allocate actual tree nodes.

For completeness, take any valid preorder serialization. Every finite non-null tree has a leaf, whose serialization is `value,#,#`; that leaf can be reduced. After all leaves are reduced, their parents eventually acquire two adjacent child markers and can be reduced as well. Repeating upward reaches the root and leaves one marker. The stack's eager reductions perform this same bottom-up process as soon as each subtree becomes available.

Therefore the final single-marker test accepts every valid serialization and rejects every invalid one.

**No tree is reconstructed.**

The stack contains only original string tokens and generic completion markers. It never creates `TreeNode` objects, stores child pointers, or reproduces node values in a tree structure. It recognizes the serialization's grammar, which satisfies the prohibition on reconstruction.

## Complexity detail

Let $L$ be the number of characters in `preorder`, and let $T$ be the number of comma-separated tokens. Splitting and appending tokens are linear in $L$, and there are only $O(T)$ successful reductions because each reduction decreases stack length by two.

However, the exact Python source performs each reduction with `stk = stk[:-3]`. List slicing copies every retained stack entry. On a deep skewed serialization, many cascading reductions can copy stack prefixes of decreasing lengths, producing $O(T^2)$ total copying in the worst case. Since $T=O(L)$, the exact implementation's worst-case time complexity is $O(L^2)$, even though the underlying stack-reduction idea can be implemented in $O(L)$ time.

The split token list and reduction stack each require $O(L)$ space in the worst case. A slice also temporarily allocates a replacement list, but peak live storage remains $O(L)$.

The variant manifest describes an in-place token-boundary slot scan with $O(L)$ time and $O(1)$ space. That is not the checked-in optimal source, which calls `split`, stores a stack, and copies slices. Its actual worst-case bounds are $O(L^2)$ time and $O(L)$ auxiliary space.

## Alternatives and edge cases

- **Slot counting over split tokens:** Start with one available root slot. Every token consumes one slot; a non-null token creates two child slots. Reject if slots are unavailable before a token, and accept only if zero slots remain at the end. This is $O(L)$ time and $O(L)$ split storage and is simpler than reduction.

- **Character-level slot counting:** Scan comma boundaries directly without creating a token array. It can achieve the manifest's $O(L)$ time and $O(1)$ auxiliary space while using the same child-slot invariant.

- **Mutate the stack in place:** Replacing the slice with three `pop` operations followed by one append makes each reduction constant time. The stack grammar would then run in $O(L)$ time, though `split` and the stack would still use $O(L)$ space.

- **Missing child:** Inputs such as `1,#` cannot form a reducible root triple and finish with multiple stack entries, so they are rejected.

- **Extra tokens after a complete tree:** Once a prefix reduces to `#`, later tokens remain beside that marker; there is no non-null root before them that can absorb the completed tree, so final length exceeds one.

- **Null root:** The single token `#` is already exactly one complete subtree marker and is accepted.

- **Negative or multi-digit integers:** Token text length and sign are irrelevant. Every token other than `#` is treated as one non-null node, which is safe because token formatting and integer validity are guaranteed.

- **Do not collapse three markers:** The explicit non-`#` root check prevents invalid `#,#,#` sequences from being mistaken for a node with two children.
