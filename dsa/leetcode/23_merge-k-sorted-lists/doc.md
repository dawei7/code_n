# Merge k Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 23 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) |

## Problem Description
### Goal
You are given an array containing `k` linked-list heads. Every linked list is sorted in ascending order, but different lists may contain equal values, have different lengths, or be empty. The array itself may also be empty.

Merge all linked lists into one list sorted in ascending order and return its head. Preserve every duplicate occurrence and omit no node. The app encodes lists as integer arrays for execution, while the native platform method reconnects the original linked-list nodes into the combined result.

### Function Contract
**Inputs**

- `lists`: `List[List[int]]`, with each inner list sorted in nondecreasing order

**Return value**

A sorted `List[int]` containing every input value with multiplicity preserved.

### Examples
**Example 1**

- Input: `lists = [[1, 4, 5], [1, 3, 4], [2, 6]]`
- Output: `[1, 1, 2, 3, 4, 4, 5, 6]`

**Example 2**

- Input: `lists = []`
- Output: `[]`

**Example 3**

- Input: `lists = [[]]`
- Output: `[]`

### Required Complexity

- **Time:** $O(N \log k)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**The heap needs only one exposed node per list**

The first unconsumed value of each sorted list is that list's smallest remaining value. Put those at most `k` candidates into a min-heap. Repeatedly remove the global minimum, append it to the result, and insert the next value from the same source list. Values deeper in a list do not belong in the heap yet because they cannot precede that list's current head.

For linked nodes, attach the popped node directly to the merged tail and push its successor. For the app's nested-array representation, heap entries also store the source-list and element indices. A deterministic source index or monotonic counter should be included as a tie-breaker in languages whose heap would otherwise try to compare node objects when values are equal.

**Restore the frontier after every extraction**

Before every heap pop, the heap contains exactly the smallest unconsumed value from each nonempty source. Consequently its root is the smallest value not yet emitted across all lists. Replacing it with its same-list successor restores the invariant.

**Trace an uneven merge**

For `[[1, 4, 5], [1, 3, 4], [2, 6]]`, initialize the heap with `1, 1, 2`. Pop the first 1 and expose 4; pop the other 1 and expose 3; then pop 2 and expose 6. Continuing in heap order produces `1, 1, 2, 3, 4, 4, 5, 6`.

**The heap contains the complete merge frontier**

For each nonempty source, its current head is the smallest value not yet emitted from that list. Any hidden node is no smaller than its own head, so no hidden value can be smaller than the minimum among all heads in the heap.

Popping that heap minimum therefore chooses the globally next value. Advancing only its source exposes the sole new value that can enter the frontier; every other source head remains unchanged. Repeating preserves one candidate per nonempty suffix and emits the complete sorted multiset union.

#### Complexity detail

Each of the `N` values enters and leaves a heap of at most `k` entries once. Heap operations cost $O(\log k)$, giving $O(N \log k)$ time; when `k` is zero or one, the corresponding behavior is constant overhead or a direct list traversal. The heap uses $O(k)$ auxiliary space. The app's returned array is output storage, while the official form relinks existing nodes.

#### Alternatives and edge cases

- **Scan all `k` heads for every output:** uses little storage but requires $O(Nk)$ time.
- **Merge lists one at a time:** can degrade to $O(Nk)$ as the accumulated list is repeatedly scanned.
- **Pairwise divide and conquer:** also achieves $O(N \log k)$ and constant pointer overhead, but the heap exposes the invariant more directly for uneven list sizes.
- Empty source lists contribute no heap entry. If every list is empty, the heap begins empty and so does the result.
- Equal values from different lists must all be retained; the heap tie-breaker orders them but must not deduplicate them.

</details>
