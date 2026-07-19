## General
**Only the first difference between adjacent words constrains order**

Create a graph node for every observed character. For each adjacent word pair, the first differing characters define one directed edge. If the first word strictly extends an otherwise identical second word, the dictionary is invalid.

**Emit characters whose prerequisites are satisfied**

Track indegrees and repeatedly remove zero-indegree characters, decrementing their outgoing neighbors. A min-heap makes the app reference deterministic when several valid choices exist.

Every emitted character currently has no unmet predecessor. Removing it deletes exactly its satisfied outgoing constraints, so remaining indegrees count precisely the unmet prerequisites.

**Prefix invalidity and graph cycles cover both failure modes**

At the first unequal characters of adjacent words, the earlier word proves one directed precedence relation; later characters cannot add constraints because lexicographic comparison is already decided. If no difference exists, a longer word preceding its own prefix is impossible. For all other inputs, Kahn's algorithm emits only characters whose predecessors are already placed, so its complete result satisfies every edge. Failure to emit all nodes means the remaining constraints contain a cycle and no alphabet order exists.

## Complexity detail
Adjacent comparisons inspect at most `c` total relevant characters and graph processing is $O(a + e)$ apart from the small deterministic heap factor. Graph and indegree storage use $O(a + e)$ space.

## Alternatives and edge cases
- **Compare every word pair:** adds unnecessary quadratic work.
- **Ignore the prefix rule:** incorrectly accepts `["abc","ab"]`.
- Repeated words add no edge; isolated characters must still appear in the returned order.
