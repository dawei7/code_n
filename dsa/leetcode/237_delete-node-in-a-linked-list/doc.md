# Delete Node in a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 237 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/) |

## Problem Description
### Goal
You are given direct access to a node that must be deleted from a singly linked list, but not to the list's head or the node preceding it. Every node value is unique, and the supplied node is guaranteed not to be the tail, so it has a successor.

Modify the list in place so the original target value disappears and every other value remains in the same order. Because the incoming link cannot be changed, make the accessible node represent its successor and bypass that successor object. Return nothing, preserve the rest of the suffix, and ensure the list loses exactly one node rather than merely marking a value as deleted.

### Function Contract
**Inputs**

- `node`: the specified non-tail node in a singly linked list, represented locally by the suffix beginning at that node

**Return value**

`None`; the linked list suffix beginning at `node` is mutated so that the original node value is removed.

### Examples
**Example 1**

- Input: `node = [5,1,9]`
- Output: `[1,9]`

**Example 2**

- Input: `node = [1,9]`
- Output: `[9]`

**Example 3**

- Input: `node = [3,4,5,6]`
- Output: `[4,5,6]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace the unavailable predecessor operation**

Ordinary deletion changes the predecessor's `next`, but that predecessor is unavailable. The guaranteed successor provides an equivalent representation trick.

**Make the given object represent its successor**

Copy the successor's value into the given node, then point the given node directly to the successor's next node. The externally visible value sequence loses exactly the requested value.

Nodes before the given object remain untouched. After copying, the given object represents its former successor; bypassing that successor restores the remainder of the original suffix.

Before mutation the suffix is `[target, next, rest...]`. After copying and bypassing it is `[next, rest...]`, exactly the sequence obtained by deleting the target position. No other list position changes.

The object identity of the supplied node remains in the list, but the contract observes the list's value sequence rather than requiring that exact object to be detached. This distinction is what makes constant-time deletion possible without the predecessor.

#### Complexity detail

One value assignment and one pointer assignment take $O(1)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Shift every later value left:** is correct but takes $O(n)$ time.
- **Search from the head:** is impossible because the head is not supplied.
- The method requires a successor, which is why the target is guaranteed not to be the tail.

</details>
