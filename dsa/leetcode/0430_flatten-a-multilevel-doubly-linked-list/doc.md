# Flatten a Multilevel Doubly Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 430 |
| Difficulty | Medium |
| Topics | Linked List, Depth-First Search, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) |

## Problem Description
### Goal
Given a multilevel doubly linked list, each node may have `next`, `prev`, and `child` pointers, and a child pointer heads another doubly linked level. Flatten the complete structure in depth-first order, visiting a node's child list before continuing with that node's original next sibling.

Return the original top-level head after rewiring all existing nodes into one doubly linked list. Clear every `child` pointer, make all adjacent `next` and `prev` links reciprocal, preserve each level's order, and reconnect the tail of a flattened child section to the saved next node. Empty input returns `null`.

### Function Contract
**Inputs**

- `nodes`: the app representation of one level as `[value, child_nodes]` entries, recursively, with an empty child list when absent

**Return value**

- Return the first flattened node. Every `child` link must be cleared, `next` and `prev` must be reciprocal, and examples show the complete forward value order.

### Examples
**Example 1**

- Input: `nodes = [[1, []], [2, []], [3, [[7, []], [8, [[11, []], [12, []]]], [9, []], [10, []]]], [4, []], [5, []], [6, []]]`
- Output: `[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]`

**Example 2**

- Input: `nodes = [[1, [[3, []]]], [2, []]]`
- Output: `[1, 3, 2]`

**Example 3**

- Input: `nodes = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Model the required order as iterative depth-first traversal**

The flattened order visits a node, then its entire child sequence, then its original next node. Use a stack of pending nodes. After popping the current node, push its original `next` first and its `child` second, so last-in-first-out order processes the child before returning to the sibling.

**Link each visited node to the previous output node**

Keep `previous`, the tail of the flattened prefix. Connect `previous.next` to the popped node and set the node's `prev` back to `previous`. Clear the node's `child` after saving it on the stack. The original head remains the first node and must keep `prev = None`.

**Why each pointer is rewritten exactly as required**

The stack order is precisely preorder over the multilevel structure. Every original node is pushed once from either a `next` or `child` link and popped once. Linking consecutive pops creates the exact flattened adjacency in both directions, while clearing every popped node's child removes all remaining levels. The final node has no pending successor, so the chain terminates normally.

#### Complexity detail

Each of the `n` nodes is pushed, popped, and linked once, giving $O(n)$ time. In the worst case the stack holds $O(n)$ pending siblings; the transformation itself reuses all original nodes.

#### Alternatives and edge cases

- **Recursive splice returning the tail:** flatten a child and return its tail to reconnect the saved sibling; this takes $O(n)$ time and $O(d)$ call-stack space.
- **Walk from every child head to rediscover its tail:** produces the same order but can revisit long flattened children and take $O(n^2)$ time.
- **Empty input:** return `None`.
- **No child links:** preserve the existing order while ensuring reciprocal pointers remain valid.
- **Nested children:** a descendant is completed before any saved sibling resumes.
- **Head predecessor:** the returned head's `prev` must remain `None`.

</details>
