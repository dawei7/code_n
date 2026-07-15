# Middle of the Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 876 |
| Difficulty | Easy |
| Topics | Linked List, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/) |

## Problem Description
### Goal
Given `head`, the first node of a nonempty singly linked list, return the list's middle node. The returned object is a node from the original list, so it remains connected to every node that follows it.

An odd-length list has one middle node. An even-length list has two central nodes; in that case, return the second middle. Consequently, a serialized returned node appears as the suffix beginning at that selected position.

### Function Contract
**Inputs**

- `head`: the head of a singly linked list containing $n$ nodes, where $1 \leq n \leq 100$ and every node value is between $1$ and $100$.

**Return value**

Return the linked-list node at zero-based position $\lfloor n/2\rfloor$. For even $n$, this is the second of the two middle nodes.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5]`
- Output: `[3,4,5]`

The node with value `3` is the unique middle and heads the returned suffix.

**Example 2**

- Input: `head = [1,2,3,4,5,6]`
- Output: `[4,5,6]`

The nodes with values `3` and `4` are central, so the second one is returned.

**Example 3**

- Input: `head = [7]`
- Output: `[7]`

The only node is also the middle.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Let one pointer measure twice the progress of the other**

Initialize `slow` and `fast` at `head`. While `fast` has both a current node and a following node, advance `slow` by one link and `fast` by two links. No node values or list modifications are needed.

After $t$ iterations, `slow` is $t$ links from the head and `fast` is $2t$ links from it. When the loop ends, `fast` has reached the end for an even-length list or the final node for an odd-length list. Exactly $\lfloor n/2\rfloor$ iterations have occurred, placing `slow` at the required zero-based position. For even $n$, that position is deliberately the second middle.

#### Complexity detail

The fast pointer crosses the list once and the slow pointer crosses at most half of it, so the total time is $O(n)$. Only two node references are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Count, then walk halfway:** A full length pass followed by $\lfloor n/2\rfloor$ steps is also $O(n)$ time and $O(1)$ space, but it requires two traversals.
- **Store every node in an array:** Direct indexing makes the middle easy to select but uses $O(n)$ auxiliary space.
- **Repeatedly measure prefixes and suffixes:** Testing every node by rescanning both sides is correct but takes $O(n^2)$ time.
- **Single node:** The loop never executes and `head` is returned.
- **Two nodes:** One iteration moves `slow` to the second node, enforcing the second-middle rule.
- **Repeated values:** Selection depends on node position, not value, so equal values require no special handling.

</details>
