# Insertion Sort List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 147 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/insertion-sort-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, sort its nodes in nondecreasing order using insertion-sort behavior. Progress through the original chain and place each encountered node into the appropriate position among the nodes that have already been arranged.

Return the head of the sorted list, reusing the original nodes and reconnecting their `next` pointers rather than returning only sorted values. Equal values may remain adjacent in either identity order, and negative values participate normally. The final chain must contain every input node exactly once and end at `null`; an empty or one-node list is already sorted.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of integer values in app cases

**Return value**

The head node of the same linked-list nodes rearranged into nondecreasing order.

### Examples
**Example 1**

- Input: `head = [4,2,1,3]`
- Output: `[1,2,3,4]`

**Example 2**

- Input: `head = [-1,5,3,4,0]`
- Output: `[-1,0,3,4,5]`

**Example 3**

- Input: `head = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A dummy-headed chain owns all processed nodes in sorted order**

Use a dummy node before the sorted output so insertion before the current minimum needs no head special case. Take nodes one at a time from the original traversal. Starting at the dummy, advance while the next sorted value is less than or equal to the current value; the stopping link is its insertion position.

**Save the unprocessed suffix before changing the node's links**

Save `next_unsorted = current.next` first. Then assign `current.next = position.next` and `position.next = current`. Resume from the saved original successor. This order keeps the unprocessed list reachable while moving the existing node into the sorted chain.

**Every iteration transfers exactly one node between disjoint regions**

Before each iteration, the list after `dummy` contains exactly the processed nodes in nondecreasing order. The `current` pointer begins the unprocessed original suffix. Inserting at the first greater value preserves sorted order and membership.

**Trace repeated insertion before earlier nodes**

For `[4,2,1,3]`, the sorted prefix evolves as `[4]`, `[2,4]`, `[1,2,4]`, then `[1,2,3,4]`. Each step moves one existing node into place.

**The insertion boundary preserves the sorted prefix**

The scan through the sorted prefix stops after all values no greater than the current node and before the first larger value. Splicing at that boundary keeps every predecessor value at most current and every successor value greater, so the enlarged prefix remains sorted.

Each iteration removes one node from the untouched suffix and inserts that same node once. When the suffix is empty, the sorted prefix contains every original node exactly once.

#### Complexity detail

The `i`th insertion may scan $O(i)$ sorted nodes, totaling $O(n^2)$ in the worst case. Only a dummy node and a constant number of pointers are used.

#### Alternatives and edge cases

- **Merge sort:** sorts a linked list in $O(n \log n)$ time, but this problem specifically asks for insertion-sort behavior.
- **Copy into an array:** enables library sorting but uses $O(n)$ extra space and does not demonstrate node insertion.
- **Swap node values:** can sort values but violates the stronger node-relinking interpretation.
- Empty and one-node lists are already sorted. Equal values remain adjacent; using `<=` while scanning preserves their relative order.
- Already sorted input still performs scans and exhibits the quadratic worst case for this straightforward implementation; reverse-sorted input inserts repeatedly near the front.

</details>
