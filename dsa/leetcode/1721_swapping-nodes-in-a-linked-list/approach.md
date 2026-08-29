## General

**Swap values, not links**

The contract asks to swap the values stored in two nodes. Their `next` pointers and the linked-list structure should remain unchanged.

This distinction avoids the complicated pointer cases that arise when physically exchanging nodes, especially when the nodes are adjacent, at the head, or identical. Once references to both required nodes are known, one tuple assignment swaps their `val` fields.

**Locate the $k$-th node from the beginning**

The source starts `fast = slow = head`. Both references initially point to the first node.

The loop `for _ in range(k - 1): fast = fast.next` advances `fast` exactly $k-1$ links. Because list positions are one-indexed, it now points to position

$$
1+(k-1)=k.
$$

The constraint `k <= n` guarantees every advancement is valid. `p = fast` saves this node as the one whose value must be swapped.

**Create a fixed positional gap**

At this moment, `fast` is at position $k$ while `slow` remains at position one. The difference between their positions is $k-1$.

The next loop moves them together:

`fast, slow = fast.next, slow.next`.

Advancing both by one preserves their position difference. The loop continues while `fast.next` exists, so it stops with `fast` at the final node, position $n$.

Since `slow` remains $k-1$ positions behind, its final position is

$$
n-(k-1)=n-k+1.
$$

Position $n-k+1$ from the beginning is exactly the $k$-th node from the end. The source saves it as `q = slow`.

**Why checking fast.next gives the right endpoint**

If the loop instead continued while `fast` existed, the final advancement would make `fast` null and move `slow` one step too far. Testing `fast.next` stops before leaving the list, making the position equation use the actual last node.

The approach never needs to compute $n$ explicitly. Reaching the tail converts the fixed gap directly into the desired end-relative position.

**Perform the value exchange**

`p.val, q.val = q.val, p.val` uses Python tuple unpacking. Both right-hand values are evaluated before either assignment, so no temporary variable is required and neither original value is lost.

The method then returns the original `head` reference. Since no `next` field changed, the same head still begins the list and all nodes remain in their original order.

**Trace an example**

For a five-node list and `k=2`, advancing `fast` once places `p` at position two. `slow` is at position one.

Moving both until `fast` reaches position five takes three iterations. `slow` reaches position four, which is the second node from the end. Swapping positions two and four changes `[1,2,3,4,5]` to `[1,4,3,2,5]`.

**Why the two-pointer invariant proves correctness**

After the first loop, `p` is the correct beginning-relative node and the position gap between `fast` and `slow` is $k-1$.

Each simultaneous move preserves that invariant. Termination places `fast` at position $n$, forcing `slow` to position $n-k+1$, the required end-relative node. The final assignment exchanges exactly those two stored values and no others.

Therefore the returned list has precisely the requested value swap.

**It is a single traversal rather than two full passes**

`fast` travels from the head to the tail across the two loops without ever restarting. `slow` begins moving only after `fast` reaches the $k$-th node. Although the implementation contains two loop constructs, the fast pointer collectively traverses each link once, so the method is commonly described as one pass.

**Special positions work without branches**

When `k=1`, the first loop is empty. `p` is the head, and the joint traversal moves `slow` to the tail, swapping first and last values.

When `k=n`, the first loop places `fast` at the tail. The joint loop is empty, `p` is the tail, and `q=slow` is the head.

If the two requested positions coincide, `p` and `q` reference the same node. Swapping its value with itself leaves the list unchanged, which is correct.

## Complexity detail

Let $n$ be the number of list nodes. `fast` advances $k-1$ times in the first loop and $n-k$ times in the second, totaling $n-1$ link traversals. `slow` advances $n-k$ times. The overall time is $O(n)$.

Only the node references `fast`, `slow`, `p`, and `q` plus loop state are stored. Their number does not grow with the list, so auxiliary space is $O(1)$. These bounds match the manifest.

The list itself is modified in place only through two value fields. No new list nodes or arrays are allocated.

## Alternatives and edge cases

- **Compute list length first:** Traverse once for $n$, then walk to positions $k$ and $n-k+1$. It remains $O(n)$ time and $O(1)$ space but uses separate passes.
- **Store all nodes in an array:** Direct indexing makes the swap easy, but costs $O(n)$ additional space.
- **Physically swap nodes:** Rewiring links is unnecessary and introduces special cases for the head and adjacent nodes.
- **`k=1`:** Head and tail values are exchanged.
- **`k=n`:** The same two endpoint values are exchanged in reverse role.
- **Middle node:** If $k=n-k+1$, tuple assignment acts on one node and changes nothing.
- **Two-node list:** Either valid `k` swaps the two endpoint values.
- **Duplicate values:** Swapping equal values may be visually unchanged, but the requested operation is still satisfied.
- **One-indexed positions:** Advancing `k-1` links, not `k`, locates the front node.
- **Non-null guarantee:** The constraints give at least one node and valid `k`, so pointer dereferences are safe.
- **Structure preservation:** Every `next` pointer remains untouched.
- **Return identity:** The original head reference remains correct even when its stored value changes.
