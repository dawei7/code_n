# Intersection of Two Linked Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 160 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/) |

## Problem Description
### Goal
Given the heads of two singly linked lists that contain no cycles, determine whether their pointer chains merge at a shared node. Intersection is based on object identity: equal values stored in separate nodes do not count. Once the two lists share one node, all following nodes form the same common tail.

Return the first shared node object, or `null` when the lists remain separate. Do not change either list's structure while searching. The two prefixes may have different lengths, either head may itself be the intersection, and the lists may be empty. App cases construct one shared tail and display the returned node through its suffix values, preserving the same identity-based contract.

### Function Contract
**Inputs**

- `head_a`: first `ListNode` head, encoded as `{"prefix": [...], "shared": [...]}` in app cases
- `head_b`: second `ListNode` head with its own prefix and the same shared-tail values; the runner constructs one shared tail object for both heads

**Return value**

The shared `ListNode`, displayed by the app as its suffix values, or a null result displayed as `[]` when the lists do not intersect.

### Examples
**Example 1**

- Input: prefixes `[4,1]` and `[5,6,1]`, shared tail `[8,4,5]`
- Output: `[8,4,5]`

**Example 2**

- Input: prefixes `[1,9,1]` and `[3]`, shared tail `[2,4]`
- Output: `[2,4]`

**Example 3**

- Input: prefixes `[2,6,4]` and `[1,5]`, shared tail `[]`
- Output: `[]`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Each pointer walks both list lengths in opposite order**

Start `pointer_a` at `head_a` and `pointer_b` at `head_b`. On every iteration, advance each one node; when a pointer is null, redirect it to the other list's head. Stop when the two references are identical, including the shared null result for disjoint lists.

**Switching cancels unequal private-prefix lengths automatically**

If the private prefixes have lengths $a$ and $b$ and the shared suffix has length $c$, the two routes have lengths $a+c+b+c$ and $b+c+a+c$ conceptually until meeting. Before the shared section of their second route, each pointer has traversed the same combined private distance $a+b$. The longer initial prefix is therefore exactly offset by switching to the shorter list.

Equivalently, each pointer follows list A then B or B then A, giving equal total route length when no intersection exists.

**Equal step counts align pointers relative to the shared suffix**

After the same number of steps, both pointers have traversed equal total distances across their concatenated routes. Once each has absorbed the other list's prefix-length difference, they are aligned relative to any shared tail.

**Trace different prefix lengths**

If A has private prefix `[4,1]` and B has `[5,6,1]` before shared node `8`, B begins one node farther from the intersection. After each pointer switches heads, A's pointer spends that extra node in B's prefix; both then arrive at node `8` together.

**Switching heads cancels the unequal private prefixes**

Let the lists have private-prefix lengths `a` and `b` and a shared suffix of length `c`. One pointer follows $a + c + b$ nodes and the other follows $b + c + a$; after switching heads, both have traversed equally long routes when they reach the first shared node. Their unequal private prefixes have therefore been canceled without explicitly measuring them.

If no shared suffix exists, both routes contain $m + n$ nodes and terminate at `None` together. Comparing node identity—not stored value—ensures that equal-valued but separate nodes can never produce a false intersection.

#### Complexity detail

Each pointer traverses at most both lists once, giving $O(m + n)$ time. Only two node references are stored.

#### Alternatives and edge cases

- **Hash nodes from one list:** is linear time but uses $O(m)$ extra space.
- **Compute lengths then advance the longer prefix:** also achieves the target bounds but requires separate length passes.
- **Compare node values or suffix values:** is invalid because distinct nodes may carry identical data.
- Either head may be empty, both heads may already be the same node, or the lists may have equal-valued but disjoint suffixes.
- Intersection is defined by object identity. Once singly linked lists share one node, they necessarily share the entire suffix after it.

</details>
