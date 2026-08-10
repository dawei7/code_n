## General

**Break the target order into three familiar operations**

The requested order alternates from the front and back:

`L0, Ln, L1, Ln-1, ...`

A singly linked list cannot move backward from the tail. The solution makes backward-order access possible by:

1. finding the end of the first half;
2. cutting and reversing the second half;
3. weaving one node from each half.

Only `next` pointers change. Node values remain untouched, as required.

**Choose the first half’s final node**

`fast` and `slow` begin at `head`. The loop continues while both `fast.next` and `fast.next.next` exist. Each iteration moves `slow` one step and `fast` two.

When the loop stops, `slow` is the last node of the first half:

- for four nodes, `slow` is `L1`, giving halves `[L0, L1]` and `[L2, L3]`;
- for five nodes, `slow` is `L2`, giving `[L0, L1, L2]` and `[L3, L4]`.

The first half therefore has the same number of nodes as the second half or one more.

`cur = slow.next` remembers the second-half head, and `slow.next = None` cuts the list. Cutting first is important: it gives the first half a proper tail and prevents old links from creating a cycle during the later merge.

The contract guarantees at least one node, so reading `fast.next` is safe. This exact source does not handle `head is None`.

**Reverse the second half**

The variables `pre` and `cur` hold the already reversed prefix and the next unreversed node.

For each node:

1. save its old successor in `t`;
2. point `cur.next` backward to `pre`;
3. advance `pre` to the node just reversed;
4. advance `cur` to the saved successor.

When the loop ends, `pre` is the old tail `Ln`, followed by `Ln-1`, and so on down to the first node of the original second half.

The reversal is safe because `t` saves the only forward path before `cur.next` is overwritten.

**Weave the halves without losing successors**

`cur` is reset to the original head, while `pre` begins the reversed second half. Each merge iteration inserts the current `pre` node immediately after `cur`.

The code first saves `pre.next` in `t`. Then:

- `pre.next = cur.next` points the back-half node to the next front-half node;
- `cur.next = pre` inserts that back-half node after the current front node;
- `cur = pre.next` advances to the saved next front node;
- `pre = t` advances to the next reversed back node.

For `[1,2,3,4]`, the split is `1->2` and `3->4`. Reversal produces `4->3`. The first insertion gives `1->4->2`; the second gives `1->4->2->3`.

For `[1,2,3,4,5]`, the split is `1->2->3` and `4->5`. Reversal produces `5->4`. Weaving gives `1->5->2->4->3`. The middle node `3` remains the final unpaired node of the longer first half.

**Why the final topology is exact**

The split partitions every original node into two disjoint chains. Reversal changes only the order of the second chain. The merge consumes one reversed node per iteration and never creates or discards a node.

At iteration `k`, the prefix already has:

`L0, Ln, L1, Ln-1, ...`

through the first `k` pairs. The saved pointers identify the next unused front node and next unused back node. Inserting the latter after the former extends that pattern by one pair.

When `pre` becomes null, every second-half node has been consumed. The first half has at most one node left, already connected as the tail. Therefore the whole list has the required order and ends at `None`.

The function returns nothing explicitly; its result is the in-place mutation reachable from the original `head`.

## Complexity detail

Let $n$ be the number of nodes.

Middle finding visits at most half the nodes with `slow`, reversal processes at most half, and merging processes at most half. The combined work is $O(n)$.

The algorithm stores a fixed number of node references: `fast`, `slow`, `cur`, `pre`, and `t`. It allocates no list, array, stack, or replacement nodes, so auxiliary space is $O(1)$.

The existing nodes constitute the output and are merely relinked. These bounds match the manifest.

## Alternatives and edge cases

- **Array of node references:** Store all nodes, then connect indices from the two ends inward. It is simple but uses $O(n)$ extra space.
- **Recursive outside-in reorder:** Recursion can pair front and back during unwinding, but locating or carrying the back side is delicate and the call stack costs $O(n)$.
- **Repeatedly find the tail:** Move the last remaining node after the next front node on each round. It uses constant space but takes $O(n^2)$ time.
- **One node:** The split leaves an empty second half, so reversal and merge skip and the node remains unchanged.
- **Two nodes:** The first half ends at the head, the second contains the tail, and one insertion recreates the same order.
- **Odd length:** The first half owns the center node, which naturally remains last.
- **Even length:** Both halves have equal size and every node participates in a pair.
- **Cut-before-reverse requirement:** Omitting `slow.next = None` can retain links between halves and form cycles while weaving.
- **Nonempty contract:** Passing `None` would raise on `fast.next`; the stated input has at least one node.
- **Runtime dependency:** The selected annotations use `Optional` without importing it. The platform supplies `ListNode`; standalone Python needs both the type definition and `from typing import Optional`.
