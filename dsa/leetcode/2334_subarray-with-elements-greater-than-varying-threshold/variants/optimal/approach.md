## General

For a subarray of length $k$, requiring every element to exceed
$\texttt{threshold}/k$ is equivalent to

$$
k\min(\text{subarray})>\texttt{threshold}.
$$

For each array value, it is therefore enough to know the widest contiguous
interval in which that value can serve as a minimum.

**Resolve minimum intervals with a monotonic stack**

Keep indices whose values are nondecreasing. When the current value is smaller
than the stack top, pop that index. The current position is its first smaller
boundary on the right, and the new stack top is its first smaller-or-equal
boundary on the left. Thus `right - left - 1` is a valid widest interval whose
minimum is the popped value.

Test `minimum * length > threshold` using integer multiplication. A sentinel
smaller than every legal value flushes the remaining stack after the array.
If a popped value succeeds for its widest interval, every cell in that interval
is at least the popped minimum, so the returned length is valid.

Conversely, take any valid subarray and one of its minimum elements. The
minimum's maximal stack interval contains that subarray and is at least as
long; multiplying the same positive minimum by the larger length still exceeds
the threshold. Therefore some pop must detect a valid length whenever one
exists.

## Complexity detail

Every index enters and leaves the stack at most once, giving $O(n)$ time. The
monotonic stack can hold all $n$ indices and uses $O(n)$ space.

## Alternatives and edge cases

- **Union-find by descending values:** Activating indices from largest value
  downward and joining adjacent active components also finds a valid length,
  but sorting costs $O(n\log n)$.
- **Enumerate all subarrays:** Checking every interval minimum takes at least
  $O(n^2)$ time and is too slow at the maximum length.
- **Multiple valid lengths:** The contract accepts any valid length; no
  smallest or largest answer is required.
- **Strict inequality:** Test `minimum * length > threshold`, never `>=`.
- **Duplicate minima:** Keeping equal values on the stack assigns different
  boundaries temporarily, but the leftmost equal value eventually receives
  the full plateau width.
