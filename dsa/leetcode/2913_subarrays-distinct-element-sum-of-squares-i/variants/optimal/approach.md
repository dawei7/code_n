## General

**Reuse the distinct set while extending one start.** Fix a left endpoint and
start with an empty set. Move the right endpoint from that position to the end
of `nums`, inserting each newly included value. The set then contains exactly
the distinct values of the current subarray: it initially represents the
one-element interval, and extending the interval changes it only by possibly
adding the new rightmost value. Add the square of its size after every
extension.

**Enumerate every subarray exactly once.** Repeat the extension scan for every
possible left endpoint, creating a fresh set each time. Every non-empty
contiguous subarray has one unique pair of inclusive endpoints, so one loop
iteration accounts for it. Conversely, each loop iteration describes a valid
subarray and contributes its squared distinct count. Summing those
contributions therefore produces precisely the requested total.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. There are $n(n+1)/2$ endpoint pairs, and
each extension performs one expected-$O(1)$ hash-set insertion and size query,
for expected $O(n^2)$ time. The set for one starting position contains at most
$n$ values, so the auxiliary space is $O(n)$. With the stated value bound, a
fixed boolean table can replace the hash set and make each update worst-case
$O(1)$ while preserving the same asymptotic bounds.

## Alternatives and edge cases

- **Rebuild a set for every endpoint pair:** Constructing `set(nums[left:right + 1])` rescans each subarray and raises the running time to $O(n^3)$; retain one growing set per left endpoint instead.
- **Segment-tree range updates:** The more advanced companion problem needs this machinery for much larger inputs, but it adds substantial complexity that the $n\le100$ contract does not require.
- **Single element:** There is one subarray with one distinct value, so its contribution is one.
- **All values equal:** Every one of the $n(n+1)/2$ subarrays contributes $1^2$.
- **All values distinct:** A subarray of length $L$ contributes $L^2$, which produces the largest distinct counts for a given length.
- **Repeated sequences at different positions:** Subarrays are identified by endpoints, so equal-looking subarrays still contribute separately.
