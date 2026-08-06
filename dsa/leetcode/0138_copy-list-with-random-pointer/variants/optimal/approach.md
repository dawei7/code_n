## General
**Interleaving makes each clone an implicit map entry**

Walk the original `next` chain and insert a newly allocated clone immediately after each original node. Once this pass is complete, `original.next` is the clone corresponding to every original, providing constant-time lookup without an explicit hash map.

**Random targets can then be translated locally**

For an original node whose clone is `original.next`, a non-null random target's clone is `original.random.next`. Assign that node to the clone's `random` field; preserve null when the original target is null. This must happen while all original-to-clone adjacencies are still intact.

In a final pass, restore each original node's saved successor and connect each clone to the clone following that successor. The first interleaved clone becomes the result head. Every original link is restored, every clone link stays inside the copied list, and exactly one fresh clone exists for each original, so values, sharing, cycles through `random`, and `next` order are all preserved without aliasing the input.

**The app adapter preserves the same semantics in serialized form**

The candidate converts each `[value, random_index]` row into local nodes, runs the same interleaving method, and serializes the copied nodes back with `position_by_node`. This adapter storage belongs to translating the app representation; the native linked-list algorithm itself uses no size-dependent auxiliary structure.

## Complexity detail
The native algorithm makes three passes over $n$ nodes, giving $O(n)$ time and $O(1)$ auxiliary space beyond the required cloned output. The app adapter also takes $O(n)$ time and uses $O(n)$ representation storage to materialize and serialize the node graph.

## Alternatives and edge cases
- **Map each original node to its clone:** is simpler and remains $O(n)$ time, but requires $O(n)$ auxiliary space.
- **Copy only the `next` chain:** loses or aliases the `random` topology.
- **Leave the lists interleaved:** mutates caller-owned structure and does not return an independent list.
- Empty input returns empty, and one node is still newly allocated even when both pointers are null.
- A self-random pointer maps to the same clone because the original's adjacent node is already its unique copy.
- The random-pointer pass must precede separation, and separation must restore every original `next` edge.
