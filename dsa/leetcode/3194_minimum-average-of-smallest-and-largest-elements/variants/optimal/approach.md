## General

**Expose every removal pair by sorting**

After sorting the values into ascending order, the first removal must pair the
value at index `0` with the value at index `n - 1`. Removing those values
leaves the next smallest and largest at indices `1` and `n - 2`, and the same
reasoning continues inward. Therefore the pair removed at step $i$ is exactly
`ordered[i]` and `ordered[n - 1 - i]` for $0 \le i < n/2$.

This correspondence means there is no need to mutate the remaining array or
store all produced averages. Scan the symmetric pairs with two indices and
keep the smallest average seen. Every legal removal step appears once in the
scan, and no other pair is considered, so the tracked minimum is precisely the
minimum element that the conceptual `averages` array would contain.

## Complexity detail

Sorting $n$ values takes $O(n\log n)$ time, and examining the $n/2$ symmetric
pairs takes $O(n)$ additional time. The sorted copy uses $O(n)$ auxiliary
space. The native submission sorts its input in place; Python's sorting
implementation can still require $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Repeated minimum and maximum searches:** Simulating each removal directly
  is correct, but scanning and deleting from a list on every step takes
  $O(n^2)$ time.
- **Frequency counting:** Because every value lies in $[1,50]$, counts can
  expose the extremes in $O(n+50)$ time and $O(50)$ space, but the two-ended
  bookkeeping is less direct than sorting for these constraints.
- With exactly two values, their single average is necessarily the answer.
- Duplicate minima or maxima cause no ambiguity: equal copies are
  interchangeable and produce the same sequence of multiset states.
- Pair sums are integers, so every possible result is an integer or a
  half-integer; ordinary division preserves the required floating-point value.
- Sorting a copy in the app-local adapter preserves the caller's input array.
