# Merge Two Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 21 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) |

## Problem Description
### Goal
You are given the heads of two linked lists whose node values are sorted in ascending order. Either list may be empty, and equal values may occur within one list or across both lists.

Merge the two lists into one list sorted in ascending order and return its head. Every input node must appear exactly once in the result, with duplicate values preserved. Form the merged list by splicing together the nodes of the two input lists rather than replacing their values or allocating a new node for every element.

### Function Contract
**Inputs**

- `list1`: `ListNode` linked list head, encoded as `List[int]` in app cases
- `list2`: `ListNode` linked list head, encoded as `List[int]` in app cases

**Return value**

The merged linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `list1 = [1, 2, 4], list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

**Example 2**

- Input: `list1 = [], list2 = []`
- Output: `[]`

**Example 3**

- Input: `list1 = [], list2 = [0]`
- Output: `[0]`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Each source head is its smallest remaining value**

Handle an empty input by returning the other list. Otherwise choose the smaller first node as the merged head and advance that source list. Keep a tail pointer to the last node in the merged prefix. Choosing the first head explicitly avoids allocating a sentinel node, although a dummy-head variant is equally valid.

While both sources remain, link `tail.next` to the smaller current node, advance that source, and then advance tail. When one source ends, attach the entire remaining suffix of the other list in one operation.

**Grow a sorted prefix by relinking existing nodes**

Before each comparison, the merged chain from head through tail contains exactly the nodes already consumed from both inputs in nondecreasing order. The two current source heads are the smallest unconsumed values in their respective lists, so choosing the smaller is the globally smallest remaining value and preserves the invariant.

Relinking a selected node does not disturb the unconsumed order behind the other head. Once either source becomes empty, every node in the other suffix is at least the merged tail and already internally sorted, so the whole suffix can be attached without further comparisons.

**Trace a representative input**

For `[1, 2, 4]` and `[1, 3, 4]`, choose the first list's 1, then the second list's 1, followed by 2, 3, and the first 4. The second list's remaining 4 is already a sorted suffix and is attached directly, giving `[1, 1, 2, 3, 4, 4]`.

**Why the smaller head is globally next**

Each current head is the smallest unconsumed value in its own list. Therefore no hidden node in either suffix can be smaller than both heads, and choosing the smaller head appends the next value in the global sorted order.

After that node is removed from consideration, the same statement holds for the new pair of heads, so the merged prefix remains exactly the smallest consumed values in order. Once one list is empty, every remaining value lies in the other already-sorted suffix and is no smaller than the merged tail; attaching it completes the merge without further choices.

#### Complexity detail

Every node becomes the selected head at most once. At most $m + n - 1$ value comparisons are needed before one list is exhausted, so time is $O(m + n)$. The merge stores only source, head, and tail pointers and reuses all nodes, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Copy values into a new list:** remains linear but allocates $O(m + n)$ new storage instead of reusing nodes.
- **Recursive merge:** expresses the same choice compactly but uses $O(m + n)$ call-stack space in the worst case.
- **Repeatedly search for the merged tail:** is unnecessary because retaining a tail pointer avoids quadratic traversal.
- If values are equal, either node may be selected first; both choices preserve nondecreasing order and multiplicity.
- If both inputs are empty, the returned head is empty. If only one is empty, the other list can be returned unchanged.

</details>
