## General

The number of size-`k` subarrays containing an occurrence depends strongly on whether that occurrence lies at an endpoint or in the interior. Separating the two boundary values of `k` exposes a much simpler structure than enumerating every window.

When `k == n`, the complete array is the only window. Every distinct value therefore appears in exactly one window, regardless of how many times it occurs inside that window, so the answer is simply the maximum array value.

When `k == 1`, every index forms its own window. A value then appears in exactly as many windows as its total frequency in `nums`. Count all values once and select the largest whose frequency is one.

Now suppose $1<k<n$. An occurrence at index `0` belongs only to the first window, and an occurrence at index `n - 1` belongs only to the last window. Every interior index belongs to at least two size-`k` windows: its range of legal window starts contains a start on each side of one boundary shift. Consequently, any value occurring at an interior index is present in at least two windows and cannot qualify.

Only `nums[0]` and `nums[n - 1]` remain as candidates. An endpoint value qualifies exactly when its total frequency is one: its sole occurrence is then confined to the corresponding boundary window, while any additional occurrence would belong to another window as well. Test the frequencies of both endpoints and return the larger qualifying value, or `-1` if neither qualifies.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building the frequency map takes $O(n)$ time, and all remaining checks take $O(1)$ time. The map stores at most $n$ distinct values, so the space complexity is $O(n)$. Because the value domain is limited to $0$ through $50$, a fixed counting array could reduce auxiliary space to $O(1)$ under the stated constraints without changing the linear running time.

## Alternatives and edge cases

- **Enumerate every window:** Building a set for each size-`k` subarray and counting its distinct values is direct and correct, but it takes $O(nk)$ time instead of using the endpoint structure.
- **Count windows by occurrence intervals:** For each value, the union of legal window-start intervals containing its occurrences gives an exact general count, but that machinery is unnecessary once the three cases for `k` are recognized.
- **One element:** `k == 1` and `k == n` are simultaneously true; treating the whole-array case first correctly returns the sole value even though no frequency map is needed.
- **Repeated values in the sole window:** With `k == n`, multiplicity inside that one window does not create additional subarrays, so the maximum value still qualifies.
- **Repeated endpoint values:** For $1<k<n$, an endpoint value must be globally unique; another occurrence prevents it from being almost missing.
- **No qualifying value:** Return `-1`, which cannot conflict with an input value because all elements are nonnegative.
