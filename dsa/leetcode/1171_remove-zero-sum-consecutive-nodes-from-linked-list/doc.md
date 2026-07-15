# Remove Zero Sum Consecutive Nodes from Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1171 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) |

## Problem Description

### Goal

You are given the `head` of a singly linked list whose nodes contain integers. Repeatedly choose a consecutive sequence of nodes whose values sum to zero and remove that entire sequence from the list. A removal may join nodes that were previously separated, so it can expose another zero-sum consecutive sequence that must also be eligible for removal.

Continue until the list contains no consecutive sequence with sum zero, then return its head. If more than one sequence can be removed at some stage, any final list obtainable by valid repeated removals is accepted.

### Function Contract

**Inputs**

- `head`: The first node of a singly linked list containing between $1$ and $1000$ nodes.
- Every node value is between $-1000$ and $1000$, inclusive.
- Let $n$ be the number of nodes in the input list.

**Return value**

- The head node of the resulting linked list after repeated zero-sum removals. Return `None` if all nodes are removed.

### Examples

**Example 1**

- Input: `head = [1,2,-3,3,1]`
- Output: `[3,1]`

Removing `[1,2,-3]` leaves `[3,1]`. The list `[1,2,1]` is another accepted result because removing `[-3,3]` is also valid.

**Example 2**

- Input: `head = [1,2,3,-3,4]`
- Output: `[1,2,4]`

**Example 3**

- Input: `head = [1,2,3,-3,-2]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Translate zero-sum ranges into repeated prefix sums.** Place a dummy node of value zero before `head`. Let the prefix sum at a node include all values from the dummy through that node. If two nodes have the same prefix sum, every node strictly between them has total zero and may be bypassed.

**Remember the last node for every prefix sum.** Traverse from the dummy to the tail while mapping each prefix sum to its latest occurrence. Choosing the last occurrence is important: when a prefix sum repeats several times, jumping after its final occurrence removes the longest intervening zero-sum region. That single jump also accounts for removals that would otherwise expose further removable regions.

**Rebuild the surviving links.** Start a second traversal from the dummy and recompute the same prefix sums. At each current node, set `current.next` to `last[prefix].next`. The mapped node has the same prefix sum as `current`, so every skipped value sums to zero. If it is the current node itself, the link remains unchanged. Advance along the updated link and repeat. Every retained adjacent pair has no later equal-prefix occurrence between it, so no zero-sum consecutive sequence remains.

#### Complexity detail

Each of the two traversals visits at most $n+1$ nodes, giving $O(n)$ time. The map stores at most one node per distinct prefix sum, so it uses $O(n)$ auxiliary space. Link updates reuse the original list nodes.

#### Alternatives and edge cases

- **Repeatedly scan for one zero-sum sequence:** Removing the first range found and restarting is valid, but repeated full scans can take $O(n^2)$ time.
- **Check every start and end pair:** Prefix sums can identify a removable range for each pair, but enumerating all pairs is also $O(n^2)$.
- **Entire list sums to zero:** The dummy and tail share a prefix sum, so the dummy link jumps to `None`.
- **Zero-valued nodes:** A zero repeats the preceding prefix sum and is removed like any longer zero-sum sequence.
- **Overlapping choices:** Different valid deletion orders can produce different accepted lists; using the last prefix occurrence deterministically removes the longest available region.
- **No removable sequence:** Every stored prefix occurrence used by the second pass is the current node, so all original links are preserved.

</details>
