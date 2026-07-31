## General

For a node to exceed at least $k$ subtree values, only the $k$ smallest values among its proper descendants matter. If those $k$ values exist and even their largest value is strictly below the node's value, then all $k$ are smaller. Any additional, larger descendant value cannot change that decision.

Process the tree in postorder so both child summaries are ready before their parent. Each summary is a sorted list containing at most the $k$ smallest values from that child's entire subtree. Merge the two sorted child lists with two pointers, stopping after $k$ values. This produces the $k$ smallest proper-descendant values for the current node.

**Why discarded values never become relevant**

A child summary omits only values that are no smaller than the values it retained. Such an omitted value cannot enter the first $k$ positions after combining the two child subtrees: the retained values that precede it are still available to the parent. Truncating every summary is therefore safe at every level.

If the merged descendant list has length $k$ and its last value is less than the current node's value, count the node. Then insert the current value into that sorted list and remove its largest entry if the list exceeds length $k$. The resulting list is exactly the $k$ smallest values in the current node's full subtree and is the only information its parent needs.

Use an explicit expanded/unexpanded stack for postorder traversal. This avoids recursion failure on a tree whose height approaches $10^4$.

## Complexity detail

Let $n$ be the number of nodes. Merging two summaries and inserting the current value each take $O(k)$ time because every list has length at most $k$. The total running time is $O(nk)$. The postorder stack and stored summaries use at most $O(nk)$ space in the conservative worst case; $k \le 10$ by contract.

## Alternatives and edge cases

- **Collect every subtree value:** Return complete sorted lists from children. It is correct, but a chain can require $O(n^2)$ total copying or sorting work.
- **Rescan each subtree:** For every node, traverse all descendants and count smaller values. This also becomes $O(n^2)$ on a skewed tree.
- **Size-$k$ max-heaps:** Merge bounded heaps instead of sorted lists. They retain the same information but add heap overhead for a very small fixed $k$.
- **Single node:** Its subtree contains no strictly smaller node value, so it cannot be great enough for any legal `k`.
- **Equal values:** The comparison is strict; a descendant equal to the current node never contributes.
- **Exactly $k$ descendants:** The node qualifies only when all $k$ retained descendant values are strictly smaller.
- **Large `k` relative to a subtree:** If fewer than $k$ proper descendants exist, the node cannot qualify regardless of its value.
- **Deep tree:** Iterative postorder prevents call-stack overflow on a long one-sided chain.
