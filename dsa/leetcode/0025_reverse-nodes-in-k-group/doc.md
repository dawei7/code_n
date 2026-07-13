# Reverse Nodes in k-Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 25 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) |

## Problem Description
### Goal
You are given a singly linked list and a positive group size `k`. Starting at the head, partition the node sequence into consecutive groups of up to `k` nodes and reverse the links inside every group that contains exactly `k` nodes.

Return the resulting head after reconnecting the reversed groups. A final group shorter than `k` must retain its original order. The operation changes node links rather than swapping stored values, uses each original node once, and preserves the group order along the list.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases
- `k`: positive `int` no larger than the list length

**Return value**

The grouped linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[2, 1, 4, 3, 5]`

**Example 2**

- Input: `head = [1, 2, 3, 4, 5], k = 3`
- Output: `[3, 2, 1, 4, 5]`

**Example 3**

- Input: `head = [1], k = 1`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Confirm a complete group before changing any link**

Use a sentinel before the head and keep `group_prev`, the node before the next candidate group. Starting from `group_prev`, walk exactly `k` links to find `kth`. If the walk reaches null first, fewer than `k` nodes remain. Nothing in that suffix has been modified, and it is already connected to the processed prefix, so the algorithm can stop safely.

This validation must happen before reversal. Reversing while counting and then discovering a short group would require undoing mutations or would incorrectly reverse the final suffix.

**Reverse the group while preserving both boundaries**

Save `group_next = kth.next` before changing links. Set `previous = group_next` and `current = group_prev.next`. Repeatedly save `current.next`, point `current.next` backward to `previous`, and advance until `current = group_next`.

Initializing `previous` to `group_next` makes the old first node point directly to the untouched suffix when it becomes the group's tail. After reversal, connect `group_prev.next` to `kth`, the group's new head. Finally move `group_prev` to the old group start, which is now the correct predecessor for the next candidate group.

**The boundary invariant across groups**

Before each group search, every node before `group_prev.next` has been reversed in complete groups and forms one valid chain connected to the untouched suffix. A successful reversal reconnects both the prefix-facing and suffix-facing boundaries, then extends the completed prefix by exactly `k` nodes. No node is lost because every forward link is saved before it is overwritten.

**Trace a complete group followed by a short one**

For `[1, 2, 3, 4, 5]` with $k = 3$, identify nodes 1 through 3 as a complete group and reverse them to `3, 2, 1`. Only nodes 4 and 5 remain, fewer than three, so they stay attached unchanged. The result is `[3, 2, 1, 4, 5]`.

**Confirm the boundary before changing any link**

Locating the kth node first proves the next group is complete. Only then does ordinary pointer reversal invert every internal edge, while the saved predecessor and successor reconnect the reversed block to the finished prefix and untouched suffix. No node can be lost because both external boundaries are known before mutation starts.

After reconnection, the old group head is the new tail and becomes the predecessor for the next search. Each successful iteration therefore reverses one disjoint complete group. If kth-node lookup fails, the remaining suffix has fewer than `k` nodes and no link in it has been changed, exactly matching the required untouched remainder.

#### Complexity detail

Every node participates in at most one group-location walk and, if its group is complete, one reversal step. The final short suffix is inspected at most once, so total time is $O(n)$, not $O(nk)$. The iterative algorithm uses a fixed number of node pointers and a sentinel, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive groups:** can be correct but uses $O(n/k)$ call-stack frames.
- **Copy values into an array:** simplifies chunk reversal but uses $O(n)$ storage and changes the intended node-link operation.
- **Recompute group positions from the head:** preserves correctness but can rescan long prefixes and become quadratic.
- $k = 1$ leaves every one-node group unchanged and still satisfies the algorithm's invariants.
- A list whose length is exactly divisible by $k$ has no short suffix; otherwise the final $1,\ldots,k-1$ nodes retain both their values and original links.
- Swapping values rather than nodes violates the contract even if the displayed sequence looks correct.

</details>
