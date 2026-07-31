## General

Sort the values. The first operation must remove the values at the two ends of the sorted order. After those are removed, the next minimum and maximum are the next inward pair, and this continues until all values are paired. Ties do not change the numeric pair selected, so they cannot change any average.

Walk through the first half of the sorted array with index `left` and pair it with index `n - 1 - left`. An average $(a+b)/2$ is equal to another average $(c+d)/2$ exactly when the integer sums $a+b$ and $c+d$ are equal. Store those sums rather than floating-point averages, avoiding fractional representation entirely. The set size is the requested number of distinct averages.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting takes $O(n\log n)$ time and scanning the $n/2$ pairs takes $O(n)$ time, so total time is $O(n\log n)$.

The sorted copy and set each use $O(n)$ storage in the worst case, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeated extreme search:** Finding and removing a minimum and maximum on every round directly simulates the statement but takes $O(n^2)$ time on an array.
- **Frequency table:** Because values are bounded by `100`, counts plus inward value pointers can solve the problem in $O(n+V)$ time and $O(V)$ space for value range $V=101$; the sorting solution remains independent of that small bound.
- **Floating-point set:** Storing `(minimum + maximum) / 2` works for integer inputs, but storing the doubled average as an integer is exact and simpler.
- **Tied extremes:** Removing any occurrence of an equal minimum or maximum produces the same numeric pair.
- **Two elements:** Exactly one pair is removed, so the result is always `1`.
- **Repeated averages:** Different extreme pairs may have the same sum and therefore contribute only one set entry.
