## General

Root the tree at node `1`. For every node, record its parent and its initial distance from the root. Updating an edge between a parent and child by a delta does not require finding new paths—the unique tree paths stay the same. It adds that delta to the distance of the child and every descendant of that child, while all other nodes are unaffected.

An iterative depth-first traversal assigns each node an entry time. Record the timer again when leaving the node. DFS visits an entire subtree before returning, so the descendants of `node` occupy exactly the half-open interval from `entry[node]` through `exit_time[node] - 1`. The traversal also avoids recursion-depth failure on a path of $10^5$ nodes.

Maintain accumulated distance changes as a difference array over this Euler order. To add `delta` to a subtree interval `[left, right)`, add `delta` at `left` and `-delta` at `right`. A prefix sum at one entry time then gives the total of every active edge delta whose descendant interval contains that node. A Fenwick tree supports both difference-array point additions and prefix sums in logarithmic time.

For an update, use the rooted `parent` relation to identify which endpoint is the child. Compute `delta = new_weight - current_weight`, save the replacement weight, and range-add the delta across that child's Euler interval. Saving the current weight is essential because later updates replace the latest value rather than accumulating from the original edge weight.

For a request at node `x`, add the Fenwick prefix sum at `entry[x]` to its initial root distance. Every updated edge on the root-to-`x` path has a subtree containing `x`, and no other updated edge does. The point value therefore contains exactly the changes to that path, proving the returned distance is current and complete.

## Complexity detail

Let $n$ be the number of nodes and $q=\lvert\texttt{queries}\rvert$. Constructing adjacency lists and performing the Euler traversal take $O(n)$ time. Each update performs at most two Fenwick additions, and each distance request performs one Fenwick prefix sum, all in $O(\log n)$ time. Total time is $O(n+q\log n)$, which is within the manifest's equivalent upper bound $O((n+q)\log n)$.

Adjacency lists, tree metadata, the edge-weight map, traversal stack, and Fenwick tree each use $O(n)$ space. The returned list uses $O(q)$ output space and is not counted as auxiliary space. The benchmark grows a path and an equal number of alternating root-edge updates and deepest-node requests, contrasting logarithmic operations with a correct implementation that walks the entire root path for every request.

## Alternatives and edge cases

- **Recompute all distances after every update:** A traversal per update is correct but costs $O(nq)$ in the worst case.
- **Walk parents for every request:** Keeping current edge weights and summing the requested root path uses only simple state, but a path-shaped tree makes each request linear.
- **Lowest common ancestor:** Static LCA answers arbitrary pair distances, but these requests always start at the root and edge weights change, so LCA does not handle the required updates.
- **Segment tree:** Lazy range addition plus point query is equally valid, but a Fenwick difference tree is smaller and sufficient for this exact operation pair.
- **Reversed update endpoints:** The query may name an edge in either orientation; the stored parent relation, not argument order, identifies the descendant subtree.
- **Repeated edge updates:** Each delta is measured from the most recently stored weight, including the zero delta from replacing a weight with itself.
- **Root request:** Node `1` belongs to no child-edge subtree, so its distance remains zero after every update.
- **Branch isolation:** Updating one child edge shifts only that child's descendants; sibling branches lie outside its Euler interval.
- **Large distances:** A root path may contain nearly $10^5$ weights of up to $10^4$, so implementations need integers capable of representing totals near $10^9$.
- **Singleton tree:** With no edges, the Euler interval and Fenwick query still return distance zero for the root.
