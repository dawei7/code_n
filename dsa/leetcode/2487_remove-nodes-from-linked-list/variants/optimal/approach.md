## General

**The decision depends on a suffix maximum.** A node must be removed exactly when the maximum value among the nodes to its right is greater than its own value. Traversing from the tail toward the head would therefore make each decision immediate: keep a running maximum, retain the current node when its value is at least that maximum, and otherwise discard it.

**Reverse to expose the list from right to left.** A singly linked list cannot be scanned backward, but its links can be reversed in place. After reversal, the original tail is visited first. Maintain `maximum`, initially below every legal node value, and a `kept_head` for the result being rebuilt. Save the current node's next pointer before changing any link.

If the current value is smaller than `maximum`, a greater node originally lay to its right, so leaving the node out is required. Otherwise update `maximum`, point the current node at `kept_head`, and make it the new result head. This second link reversal simultaneously restores the retained nodes to their original order.

At every step, `maximum` is the greatest value already visited from the original suffix, and `kept_head` contains exactly the retained portion of that suffix in original order. The comparison therefore makes the contract's decision for the current node, and the invariant covers the whole list when the scan ends.

## Complexity detail

Let $n$ be the number of nodes. Each node is visited once while reversing and once at most while filtering, so the running time is $O(n)$. Only a fixed number of pointers and one maximum value are stored, giving $O(1)$ auxiliary space. The app-local adapter serializes the returned nodes as a list for the JSON judge; that unavoidable output representation contains $O(k)$ values for $k$ retained nodes and is not auxiliary algorithmic storage.

## Alternatives and edge cases

- **Monotonic stack:** Store nodes or values in decreasing order, removing smaller stack entries when a greater value arrives. This is also $O(n)$ time but requires $O(n)$ auxiliary space.
- **Recursive suffix processing:** Solve the suffix first and compare the current node with the returned suffix head. The reasoning is concise, but recursion can consume $O(n)$ call-stack space and exceed Python's recursion limit at the maximum input size.
- **Scan every suffix:** For each node, searching all later nodes directly is correct but takes $O(n^2)$ time on an increasing list.
- **Single node:** There is no node to its right, so it is retained.
- **Equal values:** Equality never satisfies the strictly greater removal condition, so repeated suffix maxima are all retained.
- **Increasing input:** Every node except the final maximum is removed.
- **Decreasing input:** No node has a greater value to its right, so the entire list remains.
