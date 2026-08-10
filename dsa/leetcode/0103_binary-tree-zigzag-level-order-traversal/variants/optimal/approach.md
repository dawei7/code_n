## General

Zigzag traversal changes how each completed level is written, not which nodes belong to that level. The selected solution therefore performs ordinary left-to-right breadth-first search and reverses the collected value list on every other depth.

This separation is valuable: queue logic always follows one invariant, while a small direction flag controls presentation.

**Frontier invariant**

When an outer `while` iteration begins, `q` contains exactly all real nodes at one depth in left-to-right order. The root alone establishes this invariant for depth zero.

The expression `range(len(q))` captures the frontier size before children are appended. If there are $k$ current nodes, exactly $k$ are removed. Their children remain queued for the next outer iteration rather than leaking into the current row.

**Collecting nodes in natural order**

For each current node, the method appends `node.val` to `t`, then enqueues its left child before its right child when they exist.

Since parents are dequeued left-to-right and each parent's children are added left-before-right, the queue remaining after the loop is exactly the next level's natural left-to-right ordering. Missing children produce no queue entries or output placeholders.

The traversal never reverses node enqueueing. Trying to alternate child insertion order would make the queue invariant much harder to reason about and can misorder descendants across different parents.

**Using the direction flag**

`left` begins as integer one, which is truthy. The first level therefore appends `t` unchanged.

For the next level, `left ^= 1` toggles the low bit from one to zero. Zero is falsy, so the code appends `t[::-1]`, a reversed copy. Every later XOR toggles between zero and one, alternating directions.

The variable name means “emit left-to-right,” not “traverse left children.” Child discovery remains left-to-right at every depth.

**Why slicing is safe**

On a reverse level, `t[::-1]` creates a new list. The original `t` is no longer needed after that outer iteration, so copying cannot interfere with queue processing. On a forward level, the exact `t` object is stored.

Each outer iteration creates a fresh `t`, so output rows never alias one mutable list. Later appends cannot change earlier results.

**Trace for `[3,9,20,null,null,15,7]`**

The first frontier `[3]` creates `t = [3]`. Since `left` is one, the first row is `[3]`. Children nine and twenty form the next queue.

The second frontier creates natural row `[9, 20]`. The flag is zero, so the stored row is `[20, 9]`. Children fifteen and seven are still enqueued in natural order.

The third frontier creates `[15, 7]`. The flag has returned to one, so that row is unchanged. The result is `[[3], [20, 9], [15, 7]]`.

**Why every result row is correct**

Inductively, the queue contains exactly one level in natural order. Processing its fixed original length collects exactly those values and constructs the next natural frontier. For even depths, storing `t` gives left-to-right order; for odd depths, storing its reversal gives right-to-left order.

The flag toggles once per completed level, so directions alternate without skipping or repeating. Every node has one parent, is enqueued once, and contributes once.

**Exact source details**

The initial `ans = []` appears twice for nonempty input. The second assignment is redundant but harmless because no answer has been added yet.

More importantly, the file calls `deque` without importing it. A standalone Python execution raises `NameError` at `deque([root])` unless the harness injects the name. The intended source needs `from collections import deque`.

## Complexity detail

Each of the $n$ nodes is enqueued, dequeued, and processed once, giving $O(n)$ traversal time. Reversing odd rows touches each value on those rows once; across disjoint levels, that adds at most $O(n)$ work, so total time remains $O(n)$.

Let $w$ be maximum tree width. During a transition, the queue holds portions of at most two adjacent levels, bounded by $O(w)$. The current row and any reversed copy ultimately belong to output. Excluding returned storage, auxiliary space is $O(w)$, matching the manifest. Including all output values, total memory is $O(n)$.

On an odd level, both `t` and its reversed copy briefly coexist. Their lengths are at most $w$, so this peak is still $O(w)$ beyond previously completed output. After the iteration, the unreversed temporary becomes unreachable.

## Alternatives and edge cases

- **Deque-valued row:** Append values to the right on forward levels and to the left on reverse levels, avoiding a final slice while retaining $O(n)$ time.
- **Two frontier lists:** Build `next_level` explicitly instead of mutating one queue.
- **Depth-first recursion:** Use depth-indexed rows and insert values at opposite ends; traversal stack costs $O(h)$.
- **Output ownership:** Forward rows store `t` directly, while reverse rows store a copy. Since `t` is never mutated afterward, both choices are safe.
- **Empty root:** Returns `[]` before the missing `deque` name is evaluated.
- **Single node:** Produces one unchanged row.
- **Sparse levels:** Only real nodes are returned; their relative horizontal order is preserved.
- **Direction toggle:** XOR is valid because `left` is maintained strictly as zero or one.
- **Missing import:** Add the `collections.deque` import for self-contained execution.
- **Avoid list head insertion:** Repeated `insert(0, value)` could make a wide reverse level quadratic; slicing reverses it linearly once.
