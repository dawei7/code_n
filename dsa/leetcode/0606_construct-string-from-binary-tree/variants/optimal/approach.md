## General

The output follows preorder: write the current node, then the left subtree in parentheses, then the right subtree in parentheses. The subtle part is deciding when an empty child needs visible `()`. Most empty pairs can be omitted, but a missing left child must be shown when a right child exists; otherwise, the first parenthesized subtree would be ambiguous and could be mistaken for the left child.

The recursive helper returns the complete representation of one subtree. Its branches correspond to the possible child configurations.

**Null subtree**

`dfs(None)` returns the empty string. This is useful when a node has a right child but no left child: embedding the empty result inside parentheses produces the required `()` placeholder.

The public constraints give a nonempty root, but the base case also makes the helper complete for null child references.

**Leaf**

If both children are absent, the representation is only the node value:

```python
return str(root.val)
```

Appending `()()` would add redundant information. A parser already knows no children follow when the subtree representation ends.

Negative values work naturally because `str` includes the minus sign, and parentheses remain structural delimiters.

**A left child but no right child**

The leaf case has already handled “no children.” Therefore, when `root.right is None` in the next branch, a left child exists. The source returns:

```python
f'{root.val}({dfs(root.left)})'
```

The left representation needs parentheses to show that it belongs beneath the current node. No empty right parentheses are necessary. Preorder always assigns the first child group to the left; once a real left group is present and nothing follows, the right side is unambiguously absent.

**A right child exists**

When the right child is present, the source always emits two child groups:

```python
f'{root.val}({dfs(root.left)})({dfs(root.right)})'
```

If the left child also exists, both groups contain subtree strings. If it is absent, `dfs(root.left)` is empty and the first group becomes `()`. That placeholder preserves the one-to-one mapping. For example, node 2 with only right child 4 must become `2()(4)`; `2(4)` would normally mean that 4 is the left child.

This branch ordering is compact:

1. leaf avoids all child parentheses;
2. no right child means only a real left group is needed;
3. right child means the left position must be emitted whether occupied or empty, followed by the right group.

**Tracing the examples**

In the first tree, node 4 is a leaf and returns `"4"`. Node 2 has only a left child, so it returns `"2(4)"`. Node 3 is a leaf. Root 1 has both children and combines them as `"1(2(4))(3)"`.

In the second tree, node 2 has no left child and right child 4. The right-child branch calls `dfs(None)` for the left, producing `"2()(4)"`. Root combines that with node 3 to produce `"1(2()(4))(3)"`.

**Why the representation is correct**

Use structural induction. A null subtree contributes no content, and a leaf contributes exactly its value, both matching the rules.

Assume recursive calls correctly encode existing child subtrees. A node with only a left child emits its value and the correct left encoding in the first group; omitting the absent trailing right group is unambiguous. A node with a right child emits the left position first—empty if necessary—and the correct right encoding second. These are exactly the required preorder order and omission rules.

Therefore, every subtree is encoded correctly. The explicit left placeholder in the only ambiguous case makes the mapping recoverable: after a node value, the first group always means left and the second means right.

Each node receives one recursive call. The algorithm does not add placeholders for null children except the structurally necessary missing-left case.

## Complexity detail

Let $n$ be the number of nodes, $h$ the height, and $L$ the final output length. With bounded-size node values, $L=O(n)$.

The traversal itself visits each node once. However, Python strings are immutable. Each f-string creates a new parent string and copies its child subtree strings. On a skewed tree, a length-1 subtree string is copied into length 2, then length 3, and so on, for cumulative $O(n^2)$ character-copying time. A balanced tree has less repeated copying, but the exact source does not guarantee the manifest’s $O(n)$ time.

Using a shared list/StringBuilder and joining once would achieve $O(L)=O(n)$ time. The exact implementation’s recursion stack uses $O(h)$ frames, and live/final strings require $O(L)$ space; worst-case live auxiliary space is $O(n)$, consistent with the manifest’s broad space bound. Cumulative allocation over time is not the same as peak space.

At $n=10^4$, a skewed Python tree may also exceed the default recursion limit before complexity becomes the only concern.

## Alternatives and edge cases

- **Shared fragment list:** Append values and parentheses during DFS, then `''.join(parts)` once. This realizes linear output-construction time.
- **Iterative stack with enter/exit markers:** Avoids recursion depth and emits opening/closing parentheses at explicit events.
- **Always emit both child groups:** Correct structurally but violates the requirement to omit unnecessary empty pairs.
- **Omit every empty group:** Incorrect for a node with only a right child because left/right identity becomes ambiguous.
- **Leaf:** Return only its value.
- **Only left child:** Emit one nonempty group and omit trailing right `()`.
- **Only right child:** Emit `()` before the right subtree.
- **Both children:** Emit left group followed by right group.
- **Negative values:** Minus sign is ordinary value text and does not conflict with parentheses.
- **Skewed tree:** Recursion depth may fail in Python, and immutable string assembly can be quadratic.
- **Empty root:** Outside the stated node-count constraint, but helper would return an empty string.
- **Complexity fidelity:** One node visit does not automatically mean linear time when each return copies a growing immutable string.
