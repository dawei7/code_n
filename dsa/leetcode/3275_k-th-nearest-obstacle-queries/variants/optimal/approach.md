## General

**Keep only distances that can still determine the answer**

After any query, the requested value is the largest among the $k$ smallest distances seen so far. Distances larger than all of those $k$ candidates can never become the $k$th smallest later: adding more obstacles may push the answer downward, but it cannot make a discarded larger distance relevant again.

Maintain those candidates in a max-heap of at most $k$ values. Python provides a min-heap, so store each distance with a negative sign. The most negative stored number—the heap root—then represents the largest retained distance.

For each coordinate, compute its Manhattan distance and push its negation. If the heap grows beyond $k$, pop its root, which removes the largest distance among the $k+1$ candidates. Once the heap contains $k$ values, negating its root yields the current $k$th nearest distance; before then, append `-1`.

The heap invariant is that it contains exactly the $min(k, i+1)$ smallest distances from the processed prefix. It starts true for an empty prefix. A new distance is added, and removing the largest candidate when necessary leaves precisely the $k$ smallest values, including repeated distances as separate heap entries. Therefore the reported root has the required rank after every query.

## Complexity detail

For $n$ queries, every distance is pushed once and at most one value is popped per query. The heap size never exceeds $k+1$, so the total time is $O(n \log k)$. The heap uses $O(k)$ auxiliary space. The returned list itself contains $n$ values.

## Alternatives and edge cases

- **Sort every prefix:** Retaining all distances and sorting after each query is direct, but costs $O(n^2 \log n)$ in total.
- **Maintain one globally sorted list:** Binary search finds an insertion position quickly, yet inserting into an array can shift $O(n)$ elements per query.
- **Min-heap of every obstacle:** Its root exposes only the nearest distance, not the arbitrary $k$th nearest distance without destructive removals.
- When fewer than $k$ obstacles exist, the result must be `-1` even though the heap already contains distances.
- For $k=1$, the heap root tracks the smallest distance seen so far.
- Multiple distinct coordinates may have equal Manhattan distances, and each must occupy one rank.
- An obstacle at the origin has distance zero and is processed normally.
- Negative coordinates contribute through absolute values; signs do not otherwise affect ordering.
- Coordinates at either numeric bound can produce distance $2 \cdot 10^9$, which remains an ordinary integer value.
