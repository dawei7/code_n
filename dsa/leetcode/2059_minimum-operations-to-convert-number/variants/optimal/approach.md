## General
**Values form an unweighted state graph**

Treat each expandable integer as a graph vertex. From a value, every operand creates three one-operation neighbors through addition, subtraction, and XOR. Breadth-first search explores this unweighted graph by operation count, so the first generated occurrence of `goal` has minimum distance from `start`.

**Separating success from expandable states**

Check every generated candidate against `goal` before applying the range restriction. This permits a final operation to leave `[0,1000]`. Only an in-range candidate may enter the queue, and a visited set enqueues each such value at most once. Out-of-range non-goal values are terminal and discarded.

Breadth-first layers contain exactly the values reachable in successive operation counts. Generating all three operations for every operand covers every legal transition, while visited-state suppression removes only longer revisits. Therefore returning upon first reaching `goal` is optimal, and exhausting the queue proves impossibility.

## Complexity detail
Each of the $R$ reachable expandable values is removed from the queue once and tries three operations for each of the $m$ operands, giving $O(Rm)$ time. The queue and visited set hold at most $R\le1001$ values and use $O(R)$ space.

## Alternatives and edge cases
- **Depth-first search:** It can establish reachability with cycle detection but does not naturally guarantee the minimum operation count.
- **List-based visited membership:** Keeping visited states in a list is correct but each membership test can cost $O(R)$, increasing the search to $O(R^2m)$.
- **Repeated operand validation:** Rescanning all operands before expanding each one preserves the transitions but adds an unnecessary factor of $m$.
- Test `candidate == goal` before rejecting out-of-range values; otherwise valid final operations are lost.
- XOR with negative operands follows the language's integer bitwise semantics and is still a permitted transition.
- Reusing an operand is allowed, but revisiting the same in-range value cannot improve a BFS distance.
