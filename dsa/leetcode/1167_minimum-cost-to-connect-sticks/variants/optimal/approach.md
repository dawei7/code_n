## General
**Make the cheapest merge first.** Every combined length is charged immediately and may be charged again when that combined stick participates in later merges. Suppose an optimal merge tree has two smallest current lengths, $a$ and $b$, at different deepest positions. Exchanging the deeper leaves with any larger lengths cannot increase cost, because deeper leaves contribute to at least as many merge sums. The two smallest lengths can therefore be made siblings at maximum depth, meaning some optimal solution merges them first.

**Maintain the current minimum pair.** Put all lengths in a min-heap. Repeatedly execute `combined = heappop(heap) + heappop(heap)`, add `combined` to the running total, and push it back. The exchange argument applies again to the reduced collection after each merge, so every greedy choice preserves an optimal completion.

When the heap has one element, exactly $n-1$ connections have occurred and the accumulated total contains every paid sum once. A single input stick skips the loop and correctly returns zero.

## Complexity detail
Heap construction takes $O(n)$ time. Each of the $n-1$ merges performs two removals and one insertion, each costing $O(\log n)$, for $O(n \log n)$ total time. The heap stores $O(n)$ current lengths and therefore uses $O(n)$ space.

## Alternatives and edge cases
- **Sort after every merge:** Selecting the two shortest sticks remains correct, but repeatedly sorting the entire collection can take $O(n^2 \log n)$ time.
- **Merge in input order:** This can make a large partial stick participate repeatedly and does not minimize total cost.
- **Choose the two longest:** Charging large lengths early is the opposite of the needed greedy rule and can be much more expensive.
- **Single stick:** No merge is performed, so the cost is `0`.
- **Equal lengths:** Any two current minimum sticks may be chosen; ties do not affect optimality.
- **Input mutation:** Heapifying a copy preserves the caller's array while retaining the same asymptotic bounds.
