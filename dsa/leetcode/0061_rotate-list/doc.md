# Rotate List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 61 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-list/) |

## Problem Description
### Goal
You are given the head of a singly linked list and a nonnegative integer `k`. One right rotation removes the final node and places that same node before the former head, leaving the cyclic order of all nodes otherwise unchanged.

Apply this operation `k` times and return the resulting head. Rotation counts larger than the list length wrap around, so only `k` modulo the length affects a nonempty list. Do not reorder values independently of their nodes. Empty and one-node lists remain unchanged for every `k`.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases; it may be empty
- `k`: a nonnegative rotation count

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5], k = 2`
- Output: `[4,5,1,2,3]`

**Example 2**

- Input: `head = [0,1,2], k = 4`
- Output: `[2,0,1]`

**Example 3**

- Input: `head = [], k = 7`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the rotation before changing any link**

Empty and one-node lists are unchanged. Otherwise walk from `head` to the final node while counting length `n`. Rotating by `k` is equivalent to rotating by `rotation = k % n`, because every full cycle restores the list. If `rotation = 0`, return immediately and never create a temporary cycle.

**Turn every possible rotation into a different cut of one cycle**

Connect the old tail to the old head. The new tail is `n - rotation - 1` links after the old head, and its successor is the new head. Save that successor before setting `new_tail.next = None`; otherwise the new head would no longer be directly available after the cut.

**The cyclic order never changes**

Once the cycle is formed, following `next` visits every original node forever in its original cyclic order. Choosing the cut exactly `rotation` nodes before the old boundary makes those final nodes the new prefix without changing any internal order. Only the location of the null link changes.

**Trace a rotation larger than the list length**

For `[0,1,2]` and $k = 4$, reduce to rotation `1`. Form `2 -> 0`; the new tail is node `1`, its successor `2` becomes the new head, and cutting after `1` yields `[2,0,1]`.

**Closing the cycle turns rotation into one cut**

Reducing `k` modulo the list length removes complete rotations that return every node to its original position. Linking the old tail to the old head then makes the list circular, so choosing a new tail is sufficient to define any rotation without moving nodes individually.

After walking $n - k - 1$ links from the original head, the next node begins the original final `k`-node suffix. Cutting there places that suffix first and leaves the original first $n - k$ nodes after it, exactly the requested right rotation.

#### Complexity detail

One traversal measures the list and at most one more partial traversal locates the cut, for $O(n)$ time. Only pointers and counters are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Move the tail to the front `k` times:** can take $O(nk)$ time because each move must rediscover the predecessor.
- **Store nodes in an array:** makes the cut easy but uses $O(n)$ auxiliary space.
- **Copy values into a new list:** violates the intended pointer-rewiring behavior and also spends linear extra storage.
- $k = 0$ and any multiple of the list length return the original head without modifying links.
- Breaking the temporary cycle is mandatory; forgetting it creates a nonterminating linked structure that serializers and traversals cannot finish.

</details>
