# Swapping Nodes in a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1721 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) |

## Problem Description

### Goal

You are given the head of a non-empty singly linked list containing $n$ nodes and a 1-indexed position `k`. Identify the $k$th node when counting from the beginning and the $k$th node when counting backward from the end.

Swap the values stored in those two nodes and return the original list head. The links between nodes do not need to be rearranged, and `k` is guaranteed to name a valid position.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list with $1 \le n \le 10^5$ and $0 \le \texttt{Node.val} \le 100$.
- `k`: a 1-indexed position satisfying $1 \le k \le n$.

**Return value**

- Return the linked-list head after swapping the values at positions $k$ and $n-k+1$.

### Examples

**Example 1**

- Input: `head = [1,2,3,4,5], k = 2`
- Output: `[1,4,3,2,5]`
- Explanation: The second node from the start and the second node from the end contain $2$ and $4$.

**Example 2**

- Input: `head = [7,9,6,6,7,8,3,0,9,5], k = 5`
- Output: `[7,9,6,6,8,7,3,0,9,5]`
- Explanation: Positions $5$ and $6$ exchange their values.

**Example 3**

- Input: `head = [1], k = 1`
- Output: `[1]`
- Explanation: Both positions refer to the sole node, so the list is unchanged.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Locate the forward position**

Start `kth_from_start` at `head` and advance it `k - 1` links. It now points to the $k$th node from the beginning. Keep this pointer because it will also establish the exact offset needed to locate the node counted from the end.

**Preserve a gap to find the backward position**

Place a runner at `kth_from_start` and a second pointer, `kth_from_end`, at `head`. Advance both pointers together until the runner reaches the final node. The runner began with exactly $n-k$ links remaining, so the second pointer also advances $n-k$ times and finishes at position $n-k+1$, the $k$th node from the end.

**Exchange values without rewiring links**

Swap the two nodes' `val` fields and return `head`. If the two positional descriptions name the same middle node, swapping its value with itself is harmless. Because no `next` pointer changes, endpoint, adjacent-node, and same-node cases require no structural special handling.

#### Complexity detail

The initial advance and synchronized traversal together follow at most a constant number of links per node, taking $O(n)$ time. The algorithm stores only three node references and a loop counter, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Compute the length first:** One full traversal can determine $n$, followed by scans to positions $k$ and $n-k+1$; this is still $O(n)$ time and $O(1)$ space but needs an additional pass.
- **Store every node:** Collecting node references in an array makes both positions directly indexable, but it uses $O(n)$ auxiliary space.
- **Repeated suffix measurement:** Testing candidates by recounting every remaining suffix can locate the node from the end correctly but takes $O(n^2)$ time.
- **Same node:** When $2k=n+1$, both pointers meet at the middle node and the output is unchanged.
- **Endpoint swap:** For `k = 1` or `k = n`, the first and last values exchange.
- **Duplicate values:** Positions, not values, identify the nodes; equal stored values may make the output appear unchanged.

</details>
