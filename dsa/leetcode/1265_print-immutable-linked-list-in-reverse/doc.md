# Print Immutable Linked List in Reverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1265 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) |

## Problem Description

### Goal

You receive the head of an immutable singly linked list. Its nodes cannot be inspected or changed through ordinary fields. The provided `ImmutableListNode` interface permits exactly two operations: `getNext()` returns the following node, or `null` after the tail, and `printValue()` prints the value stored in the current node.

Print every node value in reverse list order, beginning with the tail and ending with the head. The list itself must remain unchanged, and the procedure produces its answer only through calls to `printValue()`; the serialized input exists solely to construct the hidden immutable nodes for the judge.

### Function Contract

**Inputs**

- `head`: the first `ImmutableListNode` in a nonempty immutable singly linked list containing $n$ nodes, where $1 \le n \le 1000$.

A node's value is an integer in the range $[-1000,1000]$ and is accessible only by calling that node's `printValue()` method.

**Return value**

`None`. Call `printValue()` on the nodes in tail-to-head order so that the emitted sequence is the reverse of the linked-list order.

### Examples

**Example 1**

- Input: `head = [1,2,3,4]`
- Output: `[4,3,2,1]`

**Example 2**

- Input: `head = [0,-4,-1,3,-5]`
- Output: `[-5,3,-1,-4,0]`

**Example 3**

- Input: `head = [-2,0,6,4,4,-6]`
- Output: `[-6,4,4,6,0,-2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Save interfaces rather than values**

Traverse forward from `head` by repeatedly calling `getNext()`. Append each node interface to a stack. This is permitted even though the nodes are immutable: the algorithm stores references to nodes but never reads a field or changes a link.

**Reverse the only available traversal direction**

After the forward scan reaches `null`, pop the saved interfaces. Last-in, first-out order produces the tail first and the head last. Call `printValue()` exactly once on each popped node. Thus every node is printed once, and for any two adjacent original nodes, the later node was pushed later and is consequently printed earlier. The complete emitted order is therefore the reverse of the list.

It is important not to collect or return ordinary integer values: the interface does not expose a value getter, and printing through each original node is part of the contract.

#### Complexity detail

The forward traversal visits all $n$ nodes, and the pop phase processes those same $n$ interfaces, for $O(n)$ time. The stack holds $n$ node references in the worst case, so it uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Recursion:** Recurse on `getNext()` and call `printValue()` while unwinding; it has the same asymptotic bounds, but a long list can exceed the language's call-stack limit.
- **Constant-space repeated scans:** Find the last unprinted position by walking from `head` each time; it respects immutability and uses $O(1)$ extra space, but takes $O(n^2)$ time.
- **Block checkpoints:** Saving selected node interfaces reduces storage, but reconstructing reverse order within each block requires repeated forward scans and worsens the time bound.
- **Single node:** The stack contains only `head`, whose `printValue()` is called once.
- **Duplicate or negative values:** Node identity and position determine output order; values need not be distinct or positive.
- **Immutable interface:** Accessing fields such as `val` or `next`, assigning links, or printing by another mechanism violates the source-native contract.

</details>
