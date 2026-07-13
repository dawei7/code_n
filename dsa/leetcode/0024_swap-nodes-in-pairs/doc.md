# Swap Nodes in Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 24 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/) |

## Problem Description
### Goal
Given the head of a singly linked list, divide its nodes from the front into consecutive pairs. Reverse the order inside every complete pair: the first node should follow the second, the third should follow the fourth, and so on.

Return the head after all pair swaps. The links between actual nodes must change; exchanging only their stored values is not allowed. If the list length is odd, the final node has no partner and remains after all swapped pairs. Empty and one-node lists are unchanged.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases

**Return value**

The swapped linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4]`
- Output: `[2, 1, 4, 3]`

**Example 2**

- Input: `head = []`
- Output: `[]`

**Example 3**

- Input: `head = [1, 2, 3]`
- Output: `[2, 1, 3]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Name all three links before rewiring a pair**

If fewer than two nodes exist, return the original head. Otherwise the second node becomes the new head. For each pair, name its nodes `first` and `second` and save `following = second.next` before modifying anything. Then point `second.next` to `first` and `first.next` to `following`. Saving the suffix first prevents the rest of the list from becoming unreachable.

Keep `previous`, the tail of the already swapped prefix. When it exists, connect `previous.next` to `second`, which is the new head of the current pair. Advance `previous` to `first` and continue at the saved suffix.

**Reconnect both sides of the swapped pair**

Before each iteration, every node before `current` has been swapped in pairs and forms a valid chain ending at `previous`; `current` begins the untouched suffix. The current pair reversal reconnects its new head to `previous` and its new tail to `following`. The list therefore remains one chain, and advancing `previous` to `first` and `current` to `following` moves the invariant forward by exactly two nodes.

**Trace a representative input**

For `[1, 2, 3, 4]`, reverse links within `1, 2` to obtain prefix `2, 1`, then connect node 1 to the swapped pair `4, 3`. The new head is node 2 and the final chain is `[2, 1, 4, 3]`.

**Three links preserve both boundaries of a pair**

Before a swap, the saved predecessor reaches the first node, the first reaches the second, and the second reaches the untouched suffix. Repointing the predecessor to the second, the second to the first, and the first to the saved suffix reverses exactly that pair without losing either surrounding boundary.

The first node then becomes the completed prefix's tail and predecessor for the next pair. Repeating swaps every complete pair once. If one node remains, no second node exists to trigger another iteration, and the existing boundary link leaves that final node unchanged as required.

#### Complexity detail

Every complete pair is processed once, with a constant number of pointer reads and writes. Time is $O(n)$, and the iterative algorithm stores only a fixed set of node pointers, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recursive pair swapping:** concise but uses $O(n)$ call-stack space.
- **Copy values into an array:** makes pair swapping easy but allocates $O(n)$ storage and does not exercise link manipulation.
- **Repeatedly search for the processed tail:** is unnecessary and can make an otherwise linear operation quadratic.
- Empty and one-node lists are returned unchanged. For an odd-length list, the saved suffix eventually contains one node and remains attached without being swapped.
- Swapping node values may produce the same visible output for simple data, but it violates the explicit requirement to change links rather than payloads.

</details>
