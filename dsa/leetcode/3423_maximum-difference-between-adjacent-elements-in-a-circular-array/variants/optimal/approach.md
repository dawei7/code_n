## General

A circular array of length $n$ has exactly $n$ adjacent unordered pairs: the $n-1$ consecutive internal pairs and the pair joining the last value back to the first. No other pair belongs to the required neighborhood.

Initialize the answer with the wrap-around difference. Then scan indices `1` through `n - 1`, compare each value with its predecessor, and retain the largest absolute difference. This lists every eligible pair exactly once, so the final maximum cannot omit a candidate or include an ineligible non-adjacent pair.

## Complexity detail

The scan performs constant work for each of the $n$ circular edges, taking $O(n)$ time. The running maximum and loop index use $O(1)$ auxiliary space.

The benchmark defines `size` as $n$ and uses legal alternating-extreme arrays of lengths 8, 32, and 100, spanning 12.5x. The accepted scan is linear. A correct implementation that first materializes every pairwise difference uses $O(n^2)$ time and space before reading the circular-neighbor entries, and must fail only scaling.

## Alternatives and edge cases

- **Compare only consecutive indices:** This omits the required last-to-first edge and can miss the answer.
- **Compare every pair:** It eventually contains all circular neighbors but performs quadratic irrelevant work.
- **Use signed differences:** The requirement is absolute difference, so direction must not change the result.
- **Two elements:** The two circular directions describe the same value pair; its absolute difference is the answer.
- **All equal values:** Every eligible difference is zero.
- **Negative values:** Subtraction followed by absolute value handles them without special cases.
- **Wrap-around maximum:** Initializing with the last-to-first edge ensures it participates before the internal scan.
