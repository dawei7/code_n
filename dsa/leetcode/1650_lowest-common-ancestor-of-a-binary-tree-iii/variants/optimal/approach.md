## General

**Parent pointers turn the problem into intersecting ancestor chains**

Starting at any node and repeatedly following `parent` produces a unique chain ending at the root. The common ancestors of `p` and `q` are exactly the node objects that occur in both chains. The lowest common ancestor is the first shared node encountered while walking upward from either target.

The source first records the complete ancestor chain of `p` in a set `vis`. It includes `p` itself before moving to `p.parent`, which respects the rule that a node may be its own descendant.

When the first loop ends, `vis` contains `p`, its parent, its grandparent, and so on through the root.

**Walk upward from q until entering p's chain**

The second loop starts `node = q` and tests `node not in vis`. While the node is not an ancestor of `p`, it moves to `node.parent`.

The first node that is in `vis` is returned. It is an ancestor of `q` because it lies on the path just traversed, and it is an ancestor of `p` because it belongs to the recorded set.

The contract guarantees both nodes belong to the same tree, so their chains share at least the root. The loop therefore finds a member before walking beyond the root. No explicit null failure case is necessary under that guarantee.

**Why the first intersection is the lowest**

The walk from `q` visits ancestors in increasing distance from `q`: `q` first, then its parent, then higher nodes. Any common ancestor skipped before the returned node would have been in `vis` and would have stopped the loop.

Thus there is no lower common ancestor on `q`'s path. In a tree, every common ancestor lies on that one path, so the first intersection is exactly the lowest common ancestor.

**Ancestor case**

If `p` is an ancestor of `q`, `p` is stored in `vis`. Walking from `q` eventually reaches `p` before any ancestor above it, so `p` is returned.

If `q` is an ancestor of `p`, then `q` itself is already in `vis`. The second loop executes zero iterations and immediately returns `q`.

These cases show why both starting nodes, rather than only their parents, must participate.

**Identity rather than value**

The set stores Node objects, and membership compares node identity under the platform's ordinary Node behavior. This directly answers whether two paths reach the same tree node.

Although values are unique, the algorithm does not need them. Parent structure alone determines ancestry, which makes the method robust to any actual numeric values.

**A path example**

Suppose `p` is node 5 and its ancestor chain is `5 -> 3 -> root-null`. The set contains nodes 5 and 3. If `q` is node 4 with chain `4 -> 2 -> 5 -> 3`, the second walk rejects 4 and 2, then stops at 5. Node 5 is the lowest common ancestor because it is the first point where the chains merge.


After the first loop, a node belongs to `vis` if and only if it is an ancestor of `p`. During the second loop, every node passed over is an ancestor of `q` but not of `p`. When the loop stops, the current node is an ancestor of both.

Since all lower ancestors of `q` were tested and rejected, no common ancestor lies below the returned node. Therefore the result satisfies both commonality and lowestness.

## Complexity detail

Let $h_p$ and $h_q$ be the numbers of nodes on the two parent chains through the root. The first loop takes $O(h_p)$ time and the second at most $O(h_q)$ expected time with hash-set membership. Total time is $O(h_p+h_q)$, commonly written $O(h)$ where $h$ bounds the tree height.

The set stores every ancestor of `p` and therefore uses $O(h_p)=O(h)$ auxiliary space. This differs from the manifest's `O(1)` space claim. A two-pointer chain-switching method can achieve constant space, but the exact checked-in source explicitly allocates `vis`.

There is no recursion, so even a tree of height $10^5$ does not risk call-stack overflow.

## Alternatives and edge cases

- **Two-pointer chain switching:** Move one pointer up from `p` and one from `q`; when a pointer reaches null, redirect it to the other start. They align path lengths and meet at the LCA in $O(h)$ time and $O(1)$ space, matching the manifest.
- **Compute depths first:** Raise the deeper node until depths match, then move both upward together. This also uses constant auxiliary space but requires separate depth walks.
- **Store both chains as lists:** Compare from the root end until they diverge. It is correct but stores $O(h_p+h_q)$ references instead of one set.
- **One node is the other's ancestor:** Starting nodes are included, so the ancestor itself is returned.
- **LCA is the root:** Both chains eventually reach it and the second loop stops there.
- **Nodes are siblings:** Their parent is the first shared node.
- **Different depths:** Set membership needs no explicit depth alignment.
- **Same tree guarantee:** Without it, `node` could become null and remain absent from `vis`; a defensive implementation would handle that case.
- **Distinct nodes:** The contract says `p != q`, though the method would also return `p` immediately if they were identical.
- **Manifest space mismatch:** The exact source is not constant-space because `vis` grows with the ancestor chain.
