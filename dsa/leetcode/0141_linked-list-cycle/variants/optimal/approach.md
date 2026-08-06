## General
**Different speeds turn a cycle into a modular-distance collision**

Initialize `slow` and `fast` at `head`. While `fast` and `fast.next` exist, advance `slow` by one edge and `fast` by two. Reaching null proves that the finite `next` chain terminates and therefore has no cycle. Compare node identity rather than values, because distinct nodes may store the same value.

If a cycle exists, both pointers eventually enter it. For a cycle of length $c$, `fast` gains one position on `slow` per iteration modulo $c$, so their relative distance must become zero within at most $c$ further iterations. They then reference the same node and the function returns true. Conversely, two forward traversals cannot revisit the same node at different speeds in an acyclic chain, so a meeting occurs only in a cycle.

## Complexity detail
Let $n$ be the number of reachable nodes. The pointers traverse only a constant multiple of the noncyclic prefix and cycle length before reaching null or meeting, giving $O(n)$ time. Two node references use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Visited-node set:** detects the first repeated identity in $O(n)$ time but uses $O(n)$ auxiliary space.
- **Compare node values:** fails when distinct nodes contain equal values.
- **Modify pointers as markers:** destroys caller-owned list structure.
- Empty input and a one-node list ending at null are acyclic.
- A one-node self-loop is detected after the first pair of pointer moves.
- Detecting a meeting proves existence; locating the entry requires the additional phase used in problem 142.
