## General

Treat every array index as a graph vertex. From index `i`, the original value `arr[i]` defines up to two directed edges:

`i + arr[i]` and `i - arr[i]`,

provided the destination stays inside the array. The question becomes graph reachability: is any zero-valued vertex reachable from `start`?

The intended Optimal approach is breadth-first search with a visited marker. A queue stores indices discovered but not yet processed. Marking prevents cycles such as one index jumping back to an earlier index and guarantees linear work.

The exact source contains the main pieces of this design, but their ordering leaves a material correctness defect when an index enters the queue more than once. A faithful explanation must distinguish the intended invariant from what the submitted lines actually guarantee.

**Normal processing of a first-time index**

The queue starts with `start`. On a pop, the code first checks `arr[i] == 0`. If true, a legal sequence of earlier jumps reached this index, so returning `True` is correct.

For a positive unvisited value, `x = arr[i]` saves the jump distance. The line `arr[i] = -1` then uses an impossible input value as the visited sentinel because all original elements are nonnegative.

The loop tries `i + x` and `i - x`. It enqueues a destination only if it lies in `[0, len(arr))` and currently has a nonnegative value. The bounds check enforces the rule against leaving the array. The sign check is meant to exclude already visited destinations.

If every index were enqueued at most once, this would be a standard BFS or worklist traversal. Every reached index would be tested for zero, marked, and expanded through its two legal jumps.

**Why a visited state is required**

The graph can contain cycles. For example, one index can jump to a second and the second can jump back. Without a visited marker, the queue could alternate forever.

In-place marking avoids allocating a separate Boolean array. It also mutates the caller's input, which is an important behavioral consequence.

For a correct mark-on-pop design, the pop logic must begin by skipping an already marked index. The editorial version does that with an `arr[node] < 0` guard. Alternatively, a mark-on-enqueue design can guarantee that no duplicate is ever placed in the queue.

**The duplicate-enqueue defect in the exact source**

The exact code checks whether a destination is unvisited before enqueueing it, but it does not mark that destination at enqueue time. Two already-popped parents can therefore both enqueue the same still-nonnegative child before the child is first popped.

When the first copy is popped, it is processed normally and its array entry becomes $-1$. When the duplicate copy is later popped, the code does not skip it. The zero test fails because the entry is now $-1$, then `x = arr[i]` assigns `x = -1`. The loop consequently explores `i - 1` and `i + 1` as though they were legal jumps. Those edges did not come from the original array value.

This is not just redundant work; it can reach a zero through an illegal adjacent move and return a false positive. Therefore, the exact source as written does not support a complete correctness proof for all valid inputs.

The smallest conceptual repair is either:

- mark a destination visited at the moment it is first enqueued while preserving its jump value elsewhere or using a separate visited set, or
- after popping, add a guard that immediately continues when `arr[i] < 0` before reading `x`.

The second form matches the local editorial's BFS structure. One must still save the positive jump value before replacing it with a negative sentinel.

**Why the corrected BFS is correct**

With duplicate processing prevented, every enqueued index has a real path from `start`: the base index has an empty path, and each neighbor is added only by applying one legal jump from a reachable index.

Conversely, consider any reachable index. Along a legal path to it, the corrected traversal processes the start and then tries both legal outgoing jumps at each step. Unless a destination was already visited through another path, it is enqueued; if it was already visited, it has already been reached. By induction on path length, every reachable vertex is examined.

Thus, returning true occurs exactly when a reachable index has original value zero. If the finite queue empties, all reachable vertices have been processed and none contains zero, so false is correct.

Breadth-first order is not required merely to answer existence—depth-first search works too—but a queue provides a simple iterative worklist and avoids recursion depth.

**Special role of zero**

The zero check must occur before overwriting the current cell. A zero-valued vertex is the goal and should return immediately. Its two mathematical jumps would both point back to itself, so expanding it would add no useful information.

Because the sentinel is negative and original zeros are nonnegative, a separate visited structure is not needed in a correctly guarded in-place version. The distinction between $0$ and $-1$ remains clear.

## Complexity detail

For the intended corrected traversal, let $n$ be the array length. Each index is processed at most once, and each processing checks two possible edges. Time complexity is $O(n)$.

The queue can contain $O(n)$ indices, so auxiliary space is $O(n)$ in the worst case. In-place marking uses no additional visited array. These are the bounds stated by the manifest and editorial.

For the exact unguarded source, duplicate queue entries can occur. The graph still has only two outgoing edges per first-time vertex, but duplicate pops use fabricated sentinel-based edges and invalidate the intended “process each original index once” argument. More importantly, correctness fails before asymptotic optimization is the central concern. The stated optimal bounds belong to the corrected visited invariant, not a proof that the exact lines are safe.

The input array is modified in place. If preserving it is required, a separate `set` or Boolean list costs another $O(n)$ space while retaining linear time.

## Alternatives and edge cases

- **Visited set with BFS:** Store indices in a set when enqueuing them and never mutate `arr`. This cleanly prevents duplicate queue entries and preserves the input, at $O(n)$ extra space.
- **Guard marked pops:** Keeping the exact mark-on-pop style is valid only if `arr[i] < 0` causes an immediate skip before `x` is read. This is the minimal logical repair shown by the editorial.
- **Iterative DFS:** A stack can replace the queue because only reachability matters. It has the same $O(n)$ time and space bounds with correct visited handling.
- **Recursive DFS:** It is concise but can recurse through $O(n)$ indices and exceed Python's recursion limit near the maximum input size.
- **Start already at zero:** The first pop returns true before any mutation.
- **Jump outside the array:** The bounds condition rejects that destination without enqueuing it.
- **Two jumps to the same destination:** When `arr[i] = 0`, the goal returns before expansion. For positive values, `i + x` and `i - x` differ, but different parent indices can still target the same child, causing the exact duplicate bug.
- **Cycles:** Correct visited marking ensures a cycle does not cause infinite traversal.
- **Unreachable zero:** After all genuinely reachable indices are processed, a corrected queue empties and returns false.
- **In-place sentinel:** $-1$ is safe only because the contract guarantees every original value is at least zero.
- **Input mutation visible to callers:** Visited positive entries become $-1$. A caller needing the original data must copy it or use separate visited storage.
- **Exact-source limitation:** The approach artifact should not claim the submitted code is correct for all valid inputs until duplicate pops are skipped or duplicate enqueues are prevented.
