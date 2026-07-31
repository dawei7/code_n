## General

The selected student's rank after any processed prefix is the smallest rank in that prefix. Initialize `best_rank` with the first arrival, which is selected by default, and initialize the replacement count to zero. Then inspect each rank in arrival order.

When an arrival is strictly smaller than `best_rank`, it is better than the current selection: increment the count and update `best_rank`. Otherwise leave both values unchanged. After processing a prefix, `best_rank` is still its minimum and the counter equals the number of times that minimum strictly decreased. This invariant matches the replacement rule exactly, so the final counter is the requested total. The app adapter also returns zero directly when every rank equals the first; its `list.count` check uses constant auxiliary space and preserves the same linear bound.

## Complexity detail

Let $n=\lvert\texttt{ranks}\rvert$. Each rank is inspected a constant number of times, so the algorithm takes $O(n)$ time. It stores only the current best rank and the counter, using $O(1)$ auxiliary space.

The benchmark uses strictly decreasing ranks, making every later student a replacement. The accepted scan remains linear, while a calibrated correct alternative recomputes the minimum of every preceding prefix and takes $O(n^2)$ time.

## Alternatives and edge cases

- **Recompute each prefix minimum:** It is correct but repeats earlier comparisons and can take $O(n^2)$ time.
- **Sort the ranks:** Sorting destroys arrival order, which determines when replacements occur, and costs unnecessary time and space.
- **Single student:** The initial selection causes no replacement, so return `0`.
- **Equal rank:** A replacement requires a strictly smaller number; ties do not count.
- **Strictly increasing ranks:** The first student remains selected and the answer is `0`.
- **Strictly decreasing ranks:** Every later arrival replaces the selection, giving `n - 1` replacements.
- **Rank 1 selected:** No later positive rank can improve it.
- **Repeated former minimum:** Once that rank is already selected, another copy is equal and does not count again.
