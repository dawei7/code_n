# Delete the Middle Node of a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2095 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) |

## Problem Description

### Goal

You are given the head of a nonempty singly linked list containing $n$ nodes. Under zero-based indexing, its middle node is the node at index $\lfloor n/2 \rfloor$. In an even-length list this selects the second of the two central nodes.

Remove that one node by reconnecting its predecessor to its successor, and return the head of the resulting list. When the input contains only one node, removing its middle leaves an empty list.

### Function Contract

**Input**

- `head`: the first node of a singly linked list with $1$ through $10^5$ nodes.
- Every node value is between $1$ and $10^5$.

**Return value**

Return the head after deleting the node at zero-based index $\lfloor n/2 \rfloor$, or `None` when no node remains.

### Examples

**Example 1**

- Input: `head = [1, 3, 4, 7, 1, 2, 6]`
- Output: `[1, 3, 4, 1, 2, 6]`
- Explanation: With $n=7$, index $\lfloor 7/2 \rfloor=3$ is deleted.

**Example 2**

- Input: `head = [1, 2, 3, 4]`
- Output: `[1, 2, 4]`
- Explanation: The selected middle index is `2`, the second central node.

**Example 3**

- Input: `head = [2, 1]`
- Output: `[2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Positioning a pointer before the node to remove**

Use a slow pointer that advances one node per iteration and a fast pointer that advances two. Start the slow pointer at the head and the fast pointer two nodes ahead. When the fast pointer reaches the end, the slow pointer is immediately before index $\lfloor n/2 \rfloor$.

The one-node list is handled separately because its middle is the head itself and no predecessor exists. For all longer lists, bypass the middle with `slow.next = slow.next.next`.

**Why the even case chooses the second center**

For length $2q$, the fast pointer can make $q-1$ two-node advances from index `2` before stopping, leaving slow at index $q-1$ and deleting index $q$. For length $2q+1$, it leaves slow at the same predecessor index and deletes index $q$. These are exactly the required floors.

**Why the remaining links are preserved**

No pointer before `slow` is changed, and the only update connects the middle's predecessor directly to its successor. Thus every other node remains in original order, while exactly the designated node becomes unreachable from the returned head.

#### Complexity detail

The fast pointer traverses at most $n$ links and the slow pointer at most half as many, so the time is $O(n)$. Only two pointers are stored and the list is modified in place, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Two linear passes:** First count the nodes, then walk to the middle predecessor; this is also $O(n)$ time and $O(1)$ space but traverses more links.
- **Store nodes in an array:** Random access makes the middle easy to locate but requires $O(n)$ auxiliary space.
- **Repeated traversal by index:** Starting from the head for every successive position eventually locates the middle but takes $O(n^2)$ time.
- A one-node list becomes empty.
- For two nodes, index `1` is deleted and the head remains.
- Node values may repeat; the node is selected only by position.

</details>
