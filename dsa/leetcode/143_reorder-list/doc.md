# Reorder List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reorder-list/) |

## Problem Description
### Goal
Given a singly linked list ordered as $L_{0} \to L_{1} \to \ldots \to L_n$, rearrange its nodes into $L_{0} \to L_n \to L_{1} \to L_n - 1 \to L_{2} \to L_n - 2 \to \ldots$. The sequence alternates between the next unused node from the front and the next unused node from the back until every node appears once.

Perform the reordering in place by changing links between the existing nodes. Do not create a replacement list or satisfy the order by copying values into different nodes. The head remains the original first node, the new final node must point to `null`, and lists with zero, one, or two nodes require no substantive rearrangement.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of values in app cases

**Return value**

`None`; mutate the linked list in place. The app displays the reordered list.

### Examples
**Example 1**

- Input: `head = [1,2,3,4]`
- Output: `[1,4,2,3]`

**Example 2**

- Input: `head = [1,2,3,4,5]`
- Output: `[1,5,2,4,3]`

**Example 3**

- Input: `head = [1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Choose a split that leaves the first half at least as long**

Move slow one edge and fast two under a loop condition chosen so slow stops at the final node of the first half. For odd length, the first half contains the middle node; for even length, both halves have equal size. Save `second = slow.next` and set `slow.next = None` before reversal.

Detaching is essential: otherwise the original first-to-second link can survive the later weave and create a cycle.

**Reversal turns back-to-front order into a forward chain**

Reverse the detached second half with standard saved-next pointer updates. Its head becomes the original tail, followed by the original second-last node, exactly the order that must be inserted between successive first-half nodes.

**Save both suffix pointers before each pair of rewires**

While the reversed second half remains, save `first_next` and `second_next`. Link `first.next = second`, then `second.next = first_next`, and advance to the saved nodes. The first half's extra middle node, when present, is already null-terminated and remains last.

**The completed prefix alternates original low and high indices**

Before every weave step, the completed prefix has the required front/back order, `first` begins the unused front segment, and `second` begins the unused reversed-back segment. Appending one of each preserves the invariant.

**Trace even and odd endpoints**

For `[1,2,3,4]`, split into `1,2` and `3,4`, reverse the latter to `4,3`, and weave `1,4,2,3`. For `[1,2,3,4,5]`, split after `3`; weaving `5,4` into `1,2,3` leaves middle node `3` at the end.

**Reversing the back half exposes the required tail order**

The midpoint split divides the list into the original front sequence and the back sequence. Reversing the latter changes it into `last, second-last, ...`, exactly the order in which tail nodes must be inserted.

Alternating one node from each sequence produces `first, last, second, second-last, ...`. Detaching before reversal and terminating the weave prevents stale links and cycles. Both halves are disjoint and exhausted once, so every original node appears exactly once without changing values.

#### Complexity detail

Midpoint search, reversal, and weaving each process at most $O(n)$ nodes, so total time is $O(n)$. A fixed number of pointers gives $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Array of node references:** makes indexing easy but requires $O(n)$ extra space.
- **Repeated tail search:** uses constant space but takes $O(n^2)$ time.
- **Copy values into a new list:** violates both node identity and the in-place contract.
- Empty, one-node, and two-node lists need no meaningful rearrangement beyond preserving their links.
- Node values are never exchanged; the required order is achieved entirely through link changes.

</details>
