## Description

Given the head of a singly linked list, rearrange its nodes by their one-based positions. Nodes originally at odd indices must appear first, followed by those originally at even indices.

The head occupies index `1`, so it belongs to the odd-index group; the next node is at even index `2`, and the position parity continues to alternate. This classification depends on position, not on a node's stored value.

Within each group, retain the nodes' original relative order. Return the head of the reordered list, using $O(1)$ extra space and $O(n)$ time for a list of $n$ nodes.
