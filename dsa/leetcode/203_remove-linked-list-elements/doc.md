# Remove Linked List Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 203 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-linked-list-elements/) |

## Problem Description
### Goal
Given the head of a singly linked list and an integer `val`, remove every node whose stored value equals `val`. Matching nodes may occur at the beginning, middle, or end of the chain, and several matching occurrences may be consecutive.

Return the head of the filtered list after reconnecting the retained nodes in their original relative order. Reuse the existing nonmatching nodes rather than returning only their values, and ensure the final retained node points to `null`. If the original head is removed, the head must advance appropriately; if every node matches or the input is empty, return `null`.

### Function Contract
**Inputs**

- `head`: the first node of a singly linked list
- `val`: the value to remove

**Return value**

The head of the filtered linked list, preserving the relative order of retained nodes.

### Examples
**Example 1**

- Input: `head = [1,2,6,3,4,5,6], val = 6`
- Output: `[1,2,3,4,5]`

**Example 2**

- Input: `head = [], val = 1`
- Output: `[]`

**Example 3**

- Input: `head = [7,7,7], val = 7`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Deleting the head is awkward because there is no predecessor whose `next` pointer can be changed. Add a dummy node before the original head so every real node, including the first, has a predecessor.

Keep `current` at the final node of the already-filtered prefix and inspect `current.next`:

- If `current.next.val == val`, bypass that node by assigning `current.next = current.next.next`. Do **not** advance `current`; the replacement next node may also need deletion.
- Otherwise advance `current` to that retained node.

For `[1,2,6,6,3]` with `val = 6`, the pointer advances through `1` and `2`. It bypasses the first `6`, remains at `2`, then bypasses the second `6` as well. Advancing after a deletion would skip inspection of consecutive matches.

At every iteration, the chain from the dummy through `current` contains only retained nodes in their original order, and `current.next` begins the unprocessed suffix. Rewiring one pointer preserves all later nodes while removing exactly the matching node from reachability.

If the inspected node matches, bypassing it removes exactly that node and keeps the processed prefix unchanged. If it does not match, advancing incorporates it into the valid prefix. In both cases the prefix property is preserved and the unprocessed suffix shrinks by one node. When the suffix is empty, every original node has been inspected: all matching nodes are unreachable and every nonmatching node remains in original order. Returning `dummy.next` supplies the correct possibly changed head.

#### Complexity detail

Every real node is inspected once, so time is $O(n)$. The dummy node and a constant number of pointers use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- Recursively filtering `head.next` and then deciding whether to keep `head` is concise but uses $O(n)$ call-stack space.
- Repeatedly special-casing matching head nodes works but complicates control flow and proof.
- Copying retained values into new nodes needlessly allocates another list and changes node identity.
- Empty lists, all-matching lists, and matching runs at either end are handled uniformly by the dummy predecessor.

</details>
