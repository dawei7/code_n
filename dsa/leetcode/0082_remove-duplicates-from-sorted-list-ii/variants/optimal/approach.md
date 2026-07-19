## General
**Sorted order turns global frequency into contiguous run length**

For each run, remember `run_start` and advance `current` while its successor has the same value. After this scan, the run is unique exactly when `run_start is current`; comparing node identity distinguishes one node from multiple nodes that happen to share a value.

Save `next_run = current.next` before relinking anything. It is the first node whose value differs and the start of the next classification step.

**Build the retained chain only from one-node runs**

Maintain result head and tail pointers. Append a run's sole node only when it is unique; otherwise do not connect any node from that run. This handles duplicate runs at the original head without a special predecessor search.

At the end, set `result_tail.next = None` when a retained tail exists. Its old `next` pointer may still lead into a duplicate run that was logically skipped, so explicit termination is required.

**The result contains complete decisions for processed runs**

Before each run, the result contains exactly the unique-valued nodes from all processed runs in original order, and the current pointer begins the next unprocessed run.

**Trace duplicate runs at both middle positions**

For `[1,2,3,3,4,4,5]`, runs 1 and 2 each contain one node and are linked. The 3 and 4 runs contain multiple nodes and are skipped. Run 5 is linked, yielding `[1,2,5]`.

**Sorted runs decide retention as a whole**

All occurrences of one value form a contiguous run. If the run has one node, that value appears exactly once in the complete list and the node must be linked into the result. If the run has multiple nodes, it contains every occurrence of a duplicated value and the entire run must be bypassed.

Advancing from run to run classifies every value exactly once. Linking only singleton runs therefore preserves precisely the values with global frequency one, in their original sorted order.

## Complexity detail
Each node is visited once, giving $O(n)$ time. A constant number of pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count values in a hash map:** works without sorted order but uses $O(n)$ extra space and a second pass.
- **Delete duplicate nodes one at a time:** complicates links and can leave one copy accidentally.
- **Recursive run removal:** is concise but consumes $O(n)$ call-stack space in the worst case.
- If every value is duplicated, no result head is created and the answer is empty. Empty input also returns empty directly.
- This problem removes all nodes of a repeated value; retaining one representative would solve problem 83 instead.
