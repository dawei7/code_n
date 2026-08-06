## General
**First obtain a meeting point inside the cycle**

Advance `slow` by one edge and `fast` by two while both fast-pointer hops exist. Reaching null proves that the list is acyclic. If the pointers meet, the meeting node lies somewhere in the cycle but is not necessarily its entry.

**Equal-speed pointers from head and the meeting converge at the entry**

Let $a$ be the prefix length before the entry, $b$ the distance from entry to the first meeting, and $c$ the remaining distance around the cycle. At that meeting, `slow` has traveled $a + b$ edges and `fast` has traveled twice as far, differing by some integer number $k$ of complete cycles:

$$
2(a + b) = a + b + k(b + c).
$$

Rearranging gives $a = (k - 1)(b + c) + c$. A pointer starting at the meeting therefore reaches the entry after the same number of steps, modulo complete cycles, as a pointer starting at `head`. Reset `entry` to `head`, move it and `slow` one edge at a time, and return their first identical node.

The candidate's app adapter then walks from `head` to that returned node and counts `position`, converting the native node identity into the required zero-based serialized result without changing the list.

## Complexity detail
Detection and entry convergence each traverse at most a constant multiple of the $n$ reachable nodes. The app-local position conversion adds at most one prefix traversal, so total time remains $O(n)$. A fixed number of node references and one scalar counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Visited-node map:** can return the first repeated node and its position in $O(n)$ time but uses $O(n)$ auxiliary space.
- **Compare stored values:** is invalid because distinct nodes may contain equal values.
- **Break or mark links:** violates the requirement not to modify the list.
- Empty and acyclic inputs return `-1` in the app and null natively.
- A self-loop and a cycle entering at the head both produce app position `0`.
- The first Floyd meeting need not be the entry; the equal-speed second phase is essential.
