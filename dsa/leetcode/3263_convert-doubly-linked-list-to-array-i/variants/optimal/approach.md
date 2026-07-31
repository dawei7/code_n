## General

Let $n$ be the number of nodes in the doubly linked list.

**Follow the forward chain**

Start a cursor at `root`. While the cursor is not `None`, append its `val` to the result and replace the cursor with its `next` neighbor. Reaching `None` means the tail has been processed.

The `prev` links are not needed: the required order starts at the head and moves forward. The list's unique forward chain visits every node exactly once and in precisely the order requested. Appending on each visit therefore puts each value in its matching array position, including any duplicates.

## Complexity detail

The cursor visits all $n$ nodes once, so the running time is $O(n)$. The returned array stores $n$ integers, giving $O(n)$ total space; excluding the required output, the cursor uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Repeatedly rescan from the head:** Finding the node for every array position works but can take $O(n^2)$ time.
- **Recursive traversal:** Recursion preserves forward order but uses $O(n)$ call-stack space without simplifying the iteration.
- **Traverse through `prev`:** Starting at the head provides no previous node and would move in the wrong direction.
- A one-node list produces a one-element array.
- Repeated values must appear separately rather than being deduplicated.
- Values at the inclusive bounds 1 and 50 are ordinary entries.
- The output must preserve node order and must not sort the values.
- The list is guaranteed non-empty, but traversal still stops only when `next` reaches `None`.
