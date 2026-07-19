## General
**First obtain any meeting point inside the cycle**

Run Floyd's one-step/two-step pointers exactly as in cycle detection. Reaching a null fast path proves there is no entry. A meeting does not generally occur at the entry; it only provides a cycle position with the distance relationship needed for phase two.

**Equal-speed pointers from head and meeting converge at the entry**

After the first meeting, place `entry` at `head` and leave `slow` at the meeting node. Move both one edge per iteration. In the app adapter, count `entry`'s moves; because it begins at list index zero, that count is the zero-based entry index when identities match.

**Distance algebra explains the second convergence**

Let prefix length be `a`, entry-to-meeting distance be `b`, and the remaining cycle distance back to entry be `c`. At the first meeting, slow traveled $a + b$; fast traveled twice that and also differs by an integer number `k` of complete cycles:

```text
2(a + b) = a + b + k(b + c)
```

Thus $a = (k - 1)(b + c) + c$. Walking `a` steps from the meeting advances through some full cycles plus the final `c` edges to entry, exactly while a head pointer walks its `a`-edge prefix.

**Phase-specific invariants connect identity and app index**

During detection, `fast` has traversed twice as many edges as `slow`. During entry search, both pointers advance equally, preserving the modular-distance argument above. The app implementation also counts the head pointer's steps, which is the entry index.

## Complexity detail
Detection and entry location each traverse at most a constant multiple of the list's distinct nodes, so total time is $O(n)$. Only a fixed number of pointers and one counter are stored.

## Alternatives and edge cases
- **Visited-node map:** can return the first repeated node and its index, but requires $O(n)$ extra space.
- **Compare values:** is invalid because separate nodes may contain equal values.
- **Break or mark links:** mutates caller-owned structure and violates the contract.
- Return `-1` for an empty or acyclic list. A self-loop has entry index `0`; a cycle may also begin after a long acyclic prefix.
- The native platform returns the node object, while the app's counted head steps expose the serialized entry index without changing the pointer proof.
