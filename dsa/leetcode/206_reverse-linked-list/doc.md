# Reverse Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 206 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-linked-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, reverse the direction of the chain so that nodes are encountered in the exact opposite order. The original final node becomes the new head, and each node's `next` pointer must lead to the node that previously preceded it.

Return the new head while reusing the existing nodes rather than constructing a separate list of copied values. The original head becomes the final node and must point to `null`, with every input node appearing exactly once in the reversed chain. An empty list returns `null`, and a one-node list returns the same node unchanged.

### Function Contract
**Inputs**

- `head`: the first node of a singly linked list

**Return value**

The new linked list head whose traversal yields the original values in reverse order.

### Examples
**Example 1**

- Input: `[1,2,3,4,5]`
- Output: `[5,4,3,2,1]`

**Example 2**

- Input: `[1,2]`
- Output: `[2,1]`

**Example 3**

- Input: `[]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Reversal changes every `next` edge, so the original successor must be saved before an edge is overwritten. Keep three pointer roles:

- `previous` is the head of the already reversed prefix.
- `current` is the first node of the untouched suffix.
- `following` temporarily saves `current.next`.

For each node, save `following`, redirect `current.next` to `previous`, then advance `previous = current` and `current = following`. When `current` becomes null, every node has moved into the reversed prefix and `previous` is the new head.

For `1 -> 2 -> 3`, the states progress from `previous = null, current = 1` to reversed prefix `1 -> null`, then `2 -> 1`, then `3 -> 2 -> 1`. Saving the successor before the first redirection is essential; otherwise the pointer to nodes `2` and `3` would be lost.

The node values never move. This is structural reversal, so callers retaining references to nodes observe their links change rather than seeing values swapped among nodes.

Before each iteration, `previous` traverses exactly the processed nodes in reverse original order, while `current` heads the unchanged remaining suffix. Redirecting `current.next` attaches the next suffix node to the front of the reversed prefix, and the saved `following` preserves the rest of the suffix. The property is therefore maintained while one node moves from suffix to prefix. At termination the suffix is empty, so `previous` contains every original node in reverse order and is the correct new head.

#### Complexity detail

Every node is visited and rewired exactly once, giving $O(n)$ time. Three node references use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- Recursive reversal mirrors the suffix relationship but uses $O(n)$ call-stack space and risks stack overflow on long lists.
- Copying values into an array and rebuilding or reassigning them uses extra space and does not directly reverse node links.
- Swapping node values can violate node identity semantics expected by callers.
- Empty and one-node lists are already reversed and naturally return unchanged.

</details>
