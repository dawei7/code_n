## General

**A component is a maximal run of selected nodes**

The values in `nums` identify which linked-list nodes are selected. A connected component is not merely a collection of selected values; it is one uninterrupted run of selected nodes along the list's `next` links.

For the list `0 -> 1 -> 2 -> 3` with selected values `{0,1,3}`, nodes 0 and 1 form one run, node 2 breaks the connection, and node 3 forms another run. The answer is therefore 2.

The key counting idea is simple: count each selected run once, not every selected node. The exact solution repeatedly skips unselected nodes, counts one component when it reaches a selected node, and then skips the entire selected run before looking for the next component.

**Use a set for membership tests**

The statement supplies selected values as an array `nums`. The code converts it to `s = set(nums)`.

A set answers `value in s` in expected `O(1)` time. Testing membership directly in the list would take `O(m)` time per linked-list node, where `m = len(nums)`, potentially making the complete scan `O(nm)`. The one-time set construction makes the later membership work linear overall.

The list values and `nums` values are unique, but the algorithm does not need to map values to positions. It encounters nodes in linked-list order and uses the set only to classify each node as selected or unselected.

**Skip the gap before the next component**

The outer loop runs while `head` is not `None`. At the start of one iteration, `head` is simply the first node not yet processed.

The first inner loop is

`while head and head.val not in s`.

It advances across every consecutive unselected node. Such a node cannot belong to a component, and it separates any selected node before it from any selected node after it. No count should be added while traversing this gap.

The `head` check appears before reading `head.val` because the scan may move beyond the final node. Python's short-circuit `and` then prevents an attempt to access a value through `None`.

**Count exactly when a run begins**

After the unselected-gap loop, one of two things is true:

- `head is None`, meaning the list ended without another selected node;
- `head` points to a selected node, which is the first node of the next component.

The statement

`ans += head is not None`

uses the fact that Python booleans act as 1 and 0 in arithmetic. It adds 1 only in the second case. At that moment, the algorithm has found the start of one new maximal selected run, so one is exactly the right amount to add.

It is important that the increment occurs once before scanning the run. Incrementing for every selected node would count component length rather than number of components.

**Skip the entire component**

The second inner loop is

`while head and head.val in s`.

It advances across all consecutive selected nodes in the newly counted component. These nodes are connected through `next` pointers and belong to the same run, so none should add another count.

This loop ends either at `None` or at the first unselected node following the component. The outer loop then repeats, and the first inner loop skips that unselected gap before the next component.

The two inner loops therefore alternate between maximal unselected runs and maximal selected runs. Each selected run is counted exactly once at its first node.

**A full trace**

Consider `0 -> 1 -> 2 -> 3 -> 4` and `nums = [0,3,1,4]`, so `s = {0,1,3,4}`.

- The first gap loop stops immediately at 0 because 0 is selected.
- `ans` becomes 1.
- The selected-run loop advances through 0 and 1, stopping at 2.
- The next gap loop advances over 2 and stops at 3.
- `ans` becomes 2.
- The selected-run loop advances through 3 and 4, reaching the end.
- The outer loop terminates and returns 2.

The two counted runs are exactly `[0,1]` and `[3,4]`.

**Why maximality is automatic**

A component must be maximal: it should not be a selected sub-run contained inside a longer selected run. The algorithm never chooses arbitrary boundaries. It begins a component only after the previous scan has passed an unselected gap or the start of the list, and it continues until the first unselected node or the end.

Therefore, the node immediately before a counted start is either absent or unselected, and the node immediately after the scanned run is either absent or unselected. The run cannot be extended in either direction while keeping every node selected, so it is maximal.

Every component is eventually found because the pointer moves through the list in order and cannot jump over a selected node during the unselected-gap loop. No component is counted twice because the selected-run loop consumes all of its nodes before the next increment.

## Complexity detail

Let `n` be the number of linked-list nodes and `m = len(nums)`.

Building `s` from `nums` takes `O(m)` expected time. Although the code contains nested loops, the list pointer only moves forward. Every linked-list node is advanced over exactly once, by either the unselected loop or the selected loop. With expected constant-time set membership, scanning costs `O(n)`. Total expected time is therefore `O(n + m)`.

The set stores `m` selected values, using `O(m)` auxiliary space. The counter and pointer variables use `O(1)` additional space. No list nodes are copied and no recursion stack is used.

The nested visual structure does not mean quadratic time: neither inner loop resets `head` to an earlier node. Amortized across the outer loop, their combined number of iterations is exactly the number of nodes.

## Alternatives and edge cases

- **Count selected-run endings:** One can increment when a selected node's next node is absent or unselected. That is equally linear. The exact solution counts starts by explicitly skipping gaps and runs.

- **Boolean in-component flag:** A single pass can track whether the previous node was selected and count a transition from unselected to selected. It uses the same set and complexity; the two-loop form mirrors maximal runs directly.

- **Membership in the original list:** Checking `head.val in nums` repeatedly can cost `O(m)` per node. A set avoids that multiplicative factor.

- **First node selected:** The initial gap loop performs zero advances, and the component is counted immediately.

- **First node unselected:** The gap loop skips nodes until the first selected value or the end.

- **Last node selected:** The selected-run loop reaches `None` after consuming it; the component was already counted at its start.

- **Every node selected:** There is one uninterrupted run, so `ans` is incremented once and the second inner loop consumes the whole list.

- **Selected nodes alternate with unselected nodes:** Every selected node is isolated and therefore forms its own component. The loops count each one after its preceding gap.

- **One selected value:** Since `nums` is nonempty and a subset of list values, the scan eventually finds it and returns 1.

- **Value order in `nums`:** It is irrelevant. Connectivity comes only from linked-list adjacency, while the set discards array order.

- **Unique values:** The contract lets value membership identify a node unambiguously. The run logic would still classify repeated values consistently, but uniqueness is guaranteed.

- **Input mutation:** The local variable `head` advances, but no `next` pointer or node value is changed. The linked list itself remains intact.
