## General

**Why this is a shortest-path problem**

Every legal jump has the same cost: one jump. Positions and legal jump histories can therefore be viewed as vertices in an unweighted graph, with each allowed forward or backward jump forming an edge. The requested minimum number of jumps is the shortest path from the initial state to any state whose position is `x`. Breadth-first search is the natural algorithm because it explores every state reachable in zero jumps, then every state reachable in one jump, then two jumps, and so forth. The first time it removes a state at the target position, no shorter route can still be undiscovered.

A graph state cannot be represented by position alone. Suppose two routes both reach position `i`, but one route arrived by moving forward while the other arrived by moving backward. A backward move is permitted next in the first case and forbidden next in the second. Those states have different possible futures even though their coordinates are identical.

The source represents a state as a pair `(i, k)`:

- `i` is the current nonnegative position;
- `k == 1` means a backward jump is currently allowed;
- `k == 0` means the preceding jump was backward, so another backward jump is not allowed.

The initial queue contains `(0, 1)`. There was no previous backward jump before the journey began, so both a forward jump and, subject to the nonnegative-position rule, a backward jump are conceptually available. A forward transition always produces `(i + a, 1)` because moving forward resets permission to jump backward. A backward transition, when allowed, produces `(i - b, 0)` because it consumes that permission.

**Representing blocked and already explored states**

The expression `s = set(forbidden)` converts the forbidden list into a hash set. A membership test such as `j not in s` is then expected $O(1)$ time. This check rejects a landing position; a jump may pass over forbidden coordinates because the rules prohibit landing there, not crossing over them.

The visited set begins with `(0, 1)` and stores complete state pairs rather than positions. This prevents the search from repeatedly following cycles such as moving forward and later backward. At the same time, it correctly permits `(i, 0)` and `(i, 1)` to be explored separately. Marking a state when it is appended, rather than later when it is removed, ensures that two parents in the same breadth-first layer cannot enqueue duplicate copies.

**Generating exactly the legal transitions**

For every removed state, the code first creates the forward candidate `(i + a, 1)`. Forward movement is always allowed by the consecutive-backward rule. If `k & 1` is true, it also creates `(i - b, 0)`. Because `k` is always zero or one, this bit test is equivalent to checking `k == 1`.

Each candidate `(j, k)` passes three filters:

1. `0 <= j < 6000` keeps the bug on a nonnegative coordinate and inside the finite search region.
2. `j not in s` ensures the landing coordinate is not forbidden.
3. `(j, k) not in vis` ensures that this exact position-and-permission state has not already been discovered.

Only a candidate satisfying all three conditions enters the queue and visited set.

The finite upper boundary matters because forward jumps could otherwise generate positions forever even when the target is unreachable. The numeric constraints place the target, every forbidden coordinate, and both jump lengths at no more than `2000`. The hard boundary `6000` is a conservative three-times-constraint search ceiling used by this exact implementation. Beyond the region containing the target and all obstacles, an excursion is useful only insofar as a later backward jump can bring the bug into a smaller relevant coordinate; continuing still farther merely repeats the same unrestricted arithmetic movement above every distinguished coordinate. A shortest successful route can be chosen without requiring position `6000` or a larger coordinate. Thus the cap makes the graph finite without removing a necessary shortest route under the stated limits. This justification depends on those published bounds; `6000` must not be treated as a universal constant for enlarged inputs.

**How the layer counter measures jumps**

The variable `ans` is the number of jumps used by every state currently in the queue at the start of an outer-loop iteration. Initially the queue contains only the start state and `ans = 0`. The inner loop runs exactly `len(q)` times, with that length captured before children are appended. It therefore removes the entire current layer while leaving all newly discovered next-layer states for the next outer iteration.

The target check occurs immediately after a state is removed. If `i == x`, the method returns the current `ans`. After the entire layer has been processed, `ans` is incremented once, matching the one additional jump used by all children. This organization also handles `x == 0`: the initial state matches before any transition, so the answer is zero.

**Why the returned result is correct**

Every enqueued edge corresponds to a legal jump: its distance is exactly `a` forward or `b` backward, the state flag enforces the no-two-backward-jumps rule, and the filters enforce coordinate, forbidden, and duplication restrictions. Conversely, from any explored state, the code generates every legal next move: the forward move always appears and the backward move appears exactly when history permits it. The search therefore explores precisely the reachable finite state graph.

Breadth-first layering guarantees that a state first enters the queue using the smallest possible number of jumps. When a target-position state is removed at layer `ans`, a route of that length exists, and no shorter target route exists because every earlier layer has already been exhausted. If the queue becomes empty, every reachable state has been processed without finding `x`, so no legal route exists and returning `-1` is correct.

## Complexity detail

Let `f` be the number of forbidden positions and let `L = 6000` be the implementation’s position limit. There are fewer than `L` possible coordinates and two permission states per coordinate, for fewer than `2L` search states. Each state is enqueued at most once and generates at most two candidates. Constructing the forbidden set costs $O(f)$ expected time, and breadth-first search costs $O(L)$ expected time, giving $O(f + L)$ expected total time.

The “expected” qualification comes from Python hash-set membership and insertion. The queue operations are constant time because `deque.popleft()` removes from the front without shifting the remaining entries.

The forbidden set uses $O(f)$ space. The queue and visited set can together hold $O(L)$ states, so total auxiliary space is $O(f + L)$. With the problem’s fixed bound, `L` is a constant numerically, but retaining it in the complexity notation explains how the search region controls both resource bounds.

## Alternatives and edge cases

- **Position-only visited set:** This is incorrect because arriving after a backward jump and arriving after a forward jump allow different next moves. The permission bit must be part of the visited identity.
- **Depth-first search:** DFS can determine reachability in a bounded graph, but the first target it finds need not use the fewest jumps. It would need extra distance handling, whereas BFS obtains the minimum directly from its layers.
- **Distance stored in each queue entry:** A triple such as position, permission, and distance is equivalent to the level loop. It may be easier to read locally, but stores a repeated distance value in every queued state.
- **A tighter calculated boundary:** One can derive an input-specific ceiling from the largest forbidden position, `x`, `a`, and `b`. That may explore fewer states, but the proof and off-by-one choice must be handled carefully; this source deliberately uses the fixed bound supported by the constraints.
- **Target at zero:** The start state is checked before any jump, so the method returns `0` immediately.
- **Forward overshoot:** Passing `x` is legal, and BFS does not stop at the target coordinate’s right side. A later backward move may be essential, as in a route that jumps past home and then returns.
- **Negative backward landing:** A candidate below zero fails `0 <= j` and is discarded; the bug may never occupy a negative position.
- **Forbidden landing:** Only the destination of a jump is tested. Jumping across a forbidden coordinate remains legal.
- **Backward then backward:** After a backward move the flag is zero, so no second backward candidate is generated. Any forward move changes the flag back to one.
- **Same coordinate with different history:** Both states are intentionally allowed into `vis` because one may have a legal backward successor that the other lacks.
- **Unreachable target:** Cycles cannot keep the algorithm alive forever because each bounded state is inserted only once. Exhausting the queue leads to `-1`.
