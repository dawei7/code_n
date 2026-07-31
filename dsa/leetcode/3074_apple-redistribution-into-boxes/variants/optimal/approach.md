## General

**Reduce the packs to one total.** Because apples from any pack may be split among boxes, pack boundaries impose no restriction on the redistribution. Let $A$ be the sum of `apple`. A chosen set of boxes is feasible exactly when its combined capacity is at least $A$.

**Use the most capacity for each box count.** Sort `capacity` from largest to smallest. For any fixed count $k$, the first $k$ values in this order have at least as much total capacity as every other selection of $k$ boxes: replacing any selected smaller box with an unselected larger one cannot decrease the sum. Thus, if these $k$ largest boxes cannot hold $A$ apples, no selection of $k$ boxes can do so.

**Stop at the first feasible prefix.** Subtract capacities from the remaining apple count in descending order. The first prefix that makes the remainder non-positive is feasible. Every shorter prefix contains the largest possible capacities for its box count and was still insufficient, so no solution using fewer boxes exists. The prefix length at that point is therefore the required minimum.

## Complexity detail

Let $n$ be the number of apple packs and $m$ the number of boxes. Summing the packs takes $O(n)$ time, sorting a copied capacity list takes $O(m \log m)$ time, and the prefix scan takes $O(m)$ time. The total is $O(n + m \log m)$ time. The sorted copy uses $O(m)$ auxiliary space.

## Alternatives and edge cases

- **Repeated maximum selection:** Choosing the largest remaining capacity without sorting is correct, but a linear search for every box can require $O(m^2)$ time.
- **Min-heap of selected boxes:** Maintaining a heap can identify large capacities, but pushing all boxes and extracting maxima is still $O(m \log m)$ and less direct than sorting once.
- **Counting capacities:** Since every capacity is at most $50$, a frequency array can achieve $O(n + m)$ time for this specific bounded contract, but sorting is the conventional comparison-based solution and generalizes without relying on the small value bound.
- **Exact fit:** Stop when the accumulated capacity equals the apple total; unused capacity is not required.
- **One sufficient box:** The largest box is considered first, so the answer is immediately `1` when it alone holds all apples.
- **All boxes required:** Feasibility is guaranteed, so the scan reaches a valid total no later than the final box.
- **Pack splitting:** Never require one box to accommodate an entire pack; only the sum of all apples matters.
- **Duplicate capacities:** Equal box sizes may appear in any order and do not affect the greedy prefix argument.
