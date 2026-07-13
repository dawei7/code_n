# Palindrome Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 234 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-linked-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, consider the sequence of values encountered by following its `next` pointers. Determine whether that sequence is identical when read from the first node to the last and from the last node back to the first.

Return `True` for a palindromic value sequence and `False` otherwise. Node identity does not need to mirror—only corresponding stored values must match. A one-node list is a palindrome. Meet the follow-up target of $O(n)$ time and $O(1)$ space rather than copying all node values into another data structure. The function returns only the boolean classification, not a reversed list or the matching node pairs.

### Function Contract
**Inputs**

- `head`: the head of a singly linked list

**Return value**

`True` when the sequence of node values is a palindrome; otherwise `False`.

### Examples
**Example 1**

- Input: `head = [1, 2, 2, 1]`
- Output: `True`

**Example 2**

- Input: `head = [1, 2]`
- Output: `False`

**Example 3**

- Input: `head = [7]`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Locate the unpaired middle or the second half**

Advance a slow pointer by one node and a fast pointer by two. When the fast pointer reaches the end, the slow pointer begins the second half for even length or sits on the middle node for odd length.

**Reverse only the suffix that must be compared**

Reverse links from the slow pointer onward in place. The reversed chain exposes original suffix values in back-to-front order without allocating a value array.

**Align the two ends as forward walks**

Walk one pointer from the original head and another from the reversed suffix. Every pair must match until the shorter, reversed half ends.

After `i` comparison steps, the first `i` values equal the last `i` original values in reverse order. Any mismatch proves the sequence is not a palindrome.

Midpoint discovery partitions the list into equal comparison halves, ignoring only the unpaired middle value of an odd-length list. Reversal aligns symmetric positions, so all comparisons succeed exactly when every mirrored value pair is equal.

#### Complexity detail

Midpoint discovery, reversal, and comparison are each linear, for $O(n)$ time. Only a fixed number of pointers is stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Copy values into an array:** is simpler but uses $O(n)$ space.
- **Recursive comparison:** uses $O(n)$ call-stack space.
- **Restore the second half afterward:** may be desirable when callers expect the input structure to remain unchanged; it adds another linear pass but no asymptotic cost.
- Empty and one-node lists are palindromes; both even and odd lengths require correct midpoint handling.

</details>
