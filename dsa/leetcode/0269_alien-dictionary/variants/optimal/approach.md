## General
**Only the first difference between adjacent words constrains order**

Create a graph node for every observed character. For each adjacent word pair, the first differing characters define one directed edge. If the first word strictly extends an otherwise identical second word, the dictionary is invalid.

**Emit characters whose prerequisites are satisfied**

Track indegrees and repeatedly remove zero-indegree characters from a queue, decrementing their outgoing neighbors. When several characters are available, any of their valid topological orders satisfies the contract.

Every emitted character currently has no unmet predecessor. Removing it deletes exactly its satisfied outgoing constraints, so remaining indegrees count precisely the unmet prerequisites.

**Prefix invalidity and graph cycles cover both failure modes**

At the first unequal characters of adjacent words, the earlier word proves one directed precedence relation; later characters cannot add constraints because lexicographic comparison is already decided. If no difference exists, a longer word preceding its own prefix is impossible. For all other inputs, Kahn's algorithm emits only characters whose predecessors are already placed, so its complete result satisfies every edge. Failure to emit all nodes means the remaining constraints contain a cycle and no alphabet order exists.

## Complexity detail

Across adjacent pairs, each word participates in at most two comparisons, so prefix checks and first-difference scans
take $O(c)$ time. Kahn's algorithm processes each of the $a$ letters and $e$ distinct edges once, for
$O(c + a + e) = O(c + e)$ total time because every observed letter contributes to $c$. The graph, indegree map, queue,
and result use $O(a + e)$ space.

## Alternatives and edge cases

- **Compare every word pair:** adds unnecessary quadratic work.
- **Ignore the prefix rule:** incorrectly accepts `["abc","ab"]`.
- **Repeated words:** they add no precedence edge and leave existing graph state unchanged.
- **Isolated characters:** graph initialization records them even when no comparison creates an incident edge, so they still appear in the order.
