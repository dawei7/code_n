## General

**Use the left-child/right-sibling representation**

An N-ary node may have many children, while a binary node has only `left` and `right`. The chosen reversible representation assigns those two pointers different meanings:

- `left` points to the encoded first child; and
- `right` points to the encoded next sibling.

The first child is enough to connect a parent to its child group, and the right-sibling chain preserves every remaining child in order. Every original N-ary node corresponds to exactly one newly created binary node with the same value.

This convention must be used consistently by both `encode` and `decode`. A binary `right` pointer is not interpreted as an ordinary right child here; it is a same-parent sibling link.

**Encode one N-ary node**

If `root is None`, encoding returns `None`. Otherwise it creates `node = TreeNode(root.val)`.

If `root.children` is empty or false, there is no child group to attach, so this binary leaf is complete and returned.

For a node with children, the first child is recursively encoded and assigned to `node.left`. The local variable `left` points to that encoded child's root. For each remaining child in original order, the code recursively encodes it, assigns the result to `left.right`, and advances `left` to this new sibling.

The resulting shape is:

`parent.left -> child0`, then `child0.right -> child1`, `child1.right -> child2`, and so on.

Each encoded child can still use its own `left` pointer for its first child. Attaching its sibling through `right` does not interfere with its descendants because the two pointer roles are separate.

**Decode one binary representation node**

If `data is None`, decoding returns `None`. Otherwise it creates `Node(data.val, [])`; initializing an actual empty list is important because children will be appended.

If `data.left is None`, the encoded node had no children, and the new N-ary leaf is returned.

Otherwise `left = data.left` points to the first encoded child. The `while left` loop recursively decodes that binary node, appends the resulting N-ary child, and follows `left.right` to the next sibling. This recreates the complete ordered child list.

Notice that a recursive `decode(left)` processes `left.left` as that child's own descendants but does not consume `left.right` as one of its children. The caller's sibling loop owns the right chain. That division of responsibility exactly mirrors encoding.

**A concrete example**

Suppose N-ary root `1` has children `3`, `2`, and `4`, and node `3` has children `5` and `6`.

The binary root `1` points left to `3`. Binary `3.right` points to `2`, and `2.right` points to `4`, preserving root's child order. Separately, `3.left` points to `5`, whose `right` points to `6`.

During decoding, the root follows its left-then-right chain to recover `[3,2,4]`. Recursive decoding of `3` follows its own left-then-right chain to recover `[5,6]`. The original hierarchy is restored without storing child counts.

**Why encoding is one-to-one and reversible**

For every N-ary node, encoding preserves its value, recursively preserves each child subtree, and records the ordered child sequence as one left edge followed by right sibling edges. No child is omitted or reordered.

Decoding reads exactly that convention: value from the current node, first child from `left`, and later children from successive `right` pointers. By induction on subtree height, decoding each encoded child restores the original child subtree. Therefore `decode(encode(root))` reconstructs a tree equivalent to `root`.

Empty trees and empty child lists have distinct, consistent representations: `None` represents no root, while a real binary node with `left = None` represents an N-ary leaf.

**Statelessness**

Both methods use only parameters and local variables. They do not store mappings or traversal state on the `Codec` instance, so repeated calls are independent and satisfy the statelessness requirement.

## Complexity detail

Let $n$ be the number of N-ary nodes and $h$ its height. Every node is encoded once and decoded once; iterating all child lists touches exactly $n-1$ parent-child relationships. Each direction therefore takes $O(n)$ time. The newly allocated binary or N-ary nodes are required output.

Ignoring language-level temporary containers, recursive call depth follows parent-child depth and uses $O(h)$ stack space.

However, the exact Python encoder iterates `root.children[1:]`, which creates a copied slice of all remaining child references at each active node. A root with $n-1$ children creates an $O(n)$ temporary list. Therefore the exact implementation's worst-case auxiliary space is $O(n)$, not only $O(h)$. Replacing the slice with index-based iteration or `itertools.islice` would recover the manifest's $O(h)$ auxiliary bound. Decoding itself uses $O(h)$ recursion beyond its required output lists.

## Alternatives and edge cases

- **Breadth-first paired traversal:** Maintain queues of corresponding N-ary and binary nodes while building sibling chains. It is also $O(n)$ time but uses width-dependent queue space.
- **Serialize to text first:** A value/count codec can bridge representations, but creates an intermediate string and performs more conversion than direct structural encoding.
- **Place first child on `right` and siblings on `left`:** This is equally valid if decoding uses the same convention. Mixing conventions is not reversible.
- **Store every child as an ordinary binary descendant:** Without a fixed sibling convention or counts, arbitrary arity and order cannot be recovered unambiguously.
- **Empty tree:** Both methods map `None` to `None`.
- **N-ary leaf:** It becomes a binary node with no left child and decodes to a node with an empty child list.
- **One child:** The parent points left to it; no right sibling link is needed.
- **Many children:** Their binary roots form one rightward chain in exactly the original order.
- **Deep tree:** Recursion stack reaches $O(h)$ and may approach the stated height limit.
- **Duplicate values:** Structure comes from pointers, not value identity, so duplicates would remain unambiguous even though values need not serve as keys.
- **Temporary slicing:** It preserves correctness but is the reason exact worst-case auxiliary memory can reach $O(n)$.
