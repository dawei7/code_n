## General

Only an interior index has both neighbors required by the definition, so scan
indices `1` through `len(mountain) - 2`. For each such index `i`, compare its
height directly with `mountain[i - 1]` and `mountain[i + 1]`. Append `i` only
when both comparisons are strict.

Every appended index is eligible and greater than both neighbors, so it is a
peak. Conversely, the scan visits every eligible index and appends any index
that satisfies the two defining comparisons, so no peak is missed. Visiting
indices from left to right also returns them in increasing order, which is one
valid form of the contract's any-order result.

## Complexity detail

Let $N=\lvert\texttt{mountain}\rvert$ and let $P$ be the number of peaks. The
single scan takes $O(N)$ time. The returned list uses $O(P)$ output space; no
auxiliary data structure grows with the input, so auxiliary space excluding
the result is $O(1)$.

## Alternatives and edge cases

- **Repeatedly locate each index:** Rescanning the array to retrieve each candidate's neighbors remains correct but takes $O(N^2)$ time.
- **First or last element:** Neither endpoint has two neighbors, so neither can be a peak regardless of its height.
- **Equal neighbor:** The comparison is strictly greater; equality on either side disqualifies the index.
- **Monotone array:** No interior element is greater than both neighbors, so the result is empty.
- **Alternating heights:** Several nonadjacent interior positions may all be peaks.
- **Minimum length:** For three elements, only index `1` is eligible.
