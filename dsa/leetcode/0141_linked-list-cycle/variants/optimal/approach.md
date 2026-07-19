## General
**Different speeds turn a cycle into a modular-distance collision**

Advance `slow` by one edge and `fast` by two. Before each fast move, ensure both `fast` and `fast.next` exist. If either is null, the finite next-chain has ended and no cycle exists. Otherwise, if a cycle exists, both pointers eventually enter its finite node set.

**Inside the cycle, relative distance advances by one**

Once both pointers are inside a cycle of length `c`, fast gains one cycle position per iteration relative to slow. The relative distance therefore visits residues modulo `c` and must reach zero within at most `c` iterations. Compare node identity, not stored value, because distinct nodes may carry equal values.

**Pointer movement either proves termination or preserves the speed ratio**

After each complete iteration, `slow` has followed one edge per step and `fast` two, unless the acyclic end was encountered.

**Trace a self-loop and a longer cycle**

For a one-node self-loop, slow and fast both move back to the same node on the first iteration. In a longer cycle, fast may enter first, but slow eventually enters; from then on their modular gap closes by one position per iteration.

**Relative speed makes meeting equivalent to a cycle**

In an acyclic finite list, the faster pointer eventually reaches null, proving no edge returns to an earlier node. In a cyclic list, both pointers eventually enter the cycle.

Once inside a cycle of length `c`, the fast pointer gains one position on the slow pointer per iteration modulo `c`. That relative gap must become zero within at most `c` steps, forcing a meeting. The algorithm therefore meets exactly when a cycle exists.

## Complexity detail
Both pointers traverse at most a constant multiple of `n` distinct-prefix and cycle edges before terminating or meeting, giving $O(n)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Visited-node set:** is straightforward but uses $O(n)$ space.
- **Compare node values:** fails when distinct nodes share a value.
- **Modify pointers as markers:** destroys caller-owned list structure.
- An empty list and a one-node list without a self-loop are acyclic. A one-node self-loop is detected on the first movement.
- Meeting is sufficient for existence; locating the cycle's entry requires the second phase from problem 142.
