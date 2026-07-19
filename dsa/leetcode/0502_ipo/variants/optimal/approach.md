## General
**Reveal projects in capital order**

Sort `(required_capital, profit)` pairs by their requirement. Maintain a pointer to the first project not yet made available. At each selection step, advance the pointer while requirements are no greater than current capital and insert those profits into a max-heap.

**Choose the largest currently feasible profit**

Pop the maximum profit and add it to current capital. If the heap is empty, no unselected project is affordable, so no further selection can change capital and the process stops early.

**Why the greedy choice is safe**

Suppose an optimal plan chooses a smaller affordable profit while a larger one is available. Swapping the larger project into that step leaves at least as much capital afterward. Since project feasibility depends only on having enough capital, every later project in the original plan remains feasible. Repeating this exchange proves that taking the maximum affordable profit at each step can achieve an optimal final capital.

**Never select a project twice**

Each sorted project crosses the pointer and enters the heap once, and each chosen profit is removed once. Projects left in the heap remain available for later steps.

## Complexity detail
Sorting `n` projects costs $O(n \log n)$. Each project is pushed at most once, and at most `k` profits are popped, adding $O((n + k) \log n)$ heap work. The sorted pairs and heap use $O(n)$ space.

## Alternatives and edge cases
- **Two heaps:** a min-heap by capital plus a max-heap by profit avoids the initial sort but keeps the same asymptotic bounds.
- **Scan every project each round:** is correct but takes $O(k \cdot n)$ time.
- **Dynamic programming over subsets:** is exponential and unnecessary because profits never reduce capital.
- **No affordable project:** return the current capital immediately.
- **$k = 0$:** no project may be selected.
- **Zero-profit project:** selecting it cannot unlock anything beyond the current capital and may be skipped when no positive alternative exists.
- **More selections than projects:** the heap eventually empties after every project is used.
