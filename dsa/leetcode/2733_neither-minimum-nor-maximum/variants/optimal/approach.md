## General

If the array contains fewer than three distinct values, every value is a global extreme: the only value is both extremes, or the two values are the minimum and maximum. Return `-1`.

Otherwise inspect any three values, such as the first three. Their median has one inspected value smaller than it and another inspected value larger than it. Those two witnesses also belong to the complete array, so the median cannot be the global minimum or global maximum, regardless of any remaining values.

For three numbers `a`, `b`, and `c`, subtracting their minimum and maximum from their sum leaves exactly the median. This uses a fixed number of operations and avoids sorting even the three-element prefix.

## Complexity detail

The algorithm reads at most three values and performs a constant number of comparisons and arithmetic operations, so it takes $O(1)$ time and $O(1)$ auxiliary space independent of $n=\lvert\texttt{nums}\rvert$. The matching $\Omega(1)$ output-decision lower bound is recorded in the asymptotic-optimality certificate.

## Alternatives and edge cases

- **Find global extremes:** Scanning for the minimum and maximum and then finding a different value is correct but takes $O(n)$ time unnecessarily.
- **Sort the complete array:** Any interior sorted value works, but sorting costs $O(n\log n)$ time and may mutate the input.
- **Sort three values:** Sorting the first triplet is still $O(1)$ and correct, though arithmetic removal of its extremes is simpler.
- Arrays of length one or two must return `-1`.
- Distinctness is essential: it makes the triplet median strictly between its two witnesses.
- Values after the first triplet cannot turn its median into a global extreme because both witnesses remain in the array.
- The returned value need not be the only valid answer.
