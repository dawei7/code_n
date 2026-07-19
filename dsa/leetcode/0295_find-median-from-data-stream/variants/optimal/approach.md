## General
**What a median query actually needs**

Keeping the entire stream sorted makes the middle element easy to read, but inserting into the middle of an array shifts $O(n)$ values. A stream of `n` insertions then costs $O(n^2)$. The query does not need the full sorted order: it only needs the largest value in the lower half and the smallest value in the upper half.

**Represent the two halves with heaps**

Maintain:

- `lower`, a max-heap containing the smaller half;
- `upper`, a min-heap containing the larger half.

Python provides only a min-heap, so values in `lower` are negated. Its root `-lower[0]` is therefore the largest lower-half value.

Two structural conditions make the roots sufficient:

1. every value in `lower` is at most every value in `upper`;
2. `lower` has either the same number of elements as `upper` or exactly one more.

With an odd number of values, `lower` owns the extra element and its root is the median. With an even number, the median is the average of the two roots.

**Insert without losing the partition**

Compare the new number with the largest lower-half value. Put it into `lower` when it belongs on that side; otherwise put it into `upper`. Then rebalance sizes:

- if `lower` is more than one element larger, move its maximum to `upper`;
- if `upper` is larger, move its minimum to `lower`.

Moving a root preserves the ordering condition because it transfers the boundary value between the two halves.

For the stream `[5, 1, 9, 2]`, the balanced halves evolve conceptually as follows:

| After insertion | Lower half | Upper half | Median |
|---|---|---|---:|
| `5` | `[5]` | `[]` | `5.0` |
| `1` | `[1]` | `[5]` | `3.0` |
| `9` | `[1, 5]` | `[9]` | `5.0` |
| `2` | `[1, 2]` | `[5, 9]` | `3.5` |

The heaps do not store each half in displayed sorted order, but their roots and membership are equivalent to these conceptual halves.

**Why every reported median is correct**

After rebalancing, the size condition places the global middle rank at the root of `lower`, or between the two roots. The ordering condition guarantees that no element hidden deeper in either heap crosses that boundary. Those are exactly the definitions of the odd and even medians, so every query is correct independent of arrival order.

## Complexity detail
Each insertion performs a constant number of heap operations on at most `n` values, costing $O(\log n)$. Reading a median costs $O(1)$. Producing all `n` running medians therefore costs $O(n \log n)$ time, and the heaps store $O(n)$ values.

## Alternatives and edge cases
- **Maintain a sorted array:** median queries are constant-time, but arbitrary insertion is $O(n)$ and the full stream becomes quadratic.
- **Sort on every query:** repeats even more work, taking $O(n \log n)$ for each prefix.
- **Order-statistic tree:** supports logarithmic insertion and median selection but requires a more complex balanced-tree implementation.
- Duplicates, negatives, and extreme values need no special placement rule. Averaging the two boundary values must return a floating-point result.
