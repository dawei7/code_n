## General
**Reject impossible instances by counting windows**

A length-$n$ string has exactly $n-k+1$ starting positions for a length-$k$
substring when $k\le n$, and none otherwise. Each position can contribute at
most one distinct code. Therefore, if

$$
n-k+1 < 2^k,
$$

covering all codes is impossible. Return `false` before allocating the seen
structure. Besides being a useful shortcut, this guard ensures that whenever
the main scan runs, $2^k\le n-k+1\le n$, so its memory is bounded by the
input scale.

**Encode each window as a rolling integer**

Interpret a length-$k$ binary substring as an integer from $0$ through
$2^k-1$. Maintain `window`, the value of the most recent at-most-$k$ bits,
and `mask = (1 << k) - 1`, whose lowest $k$ bits are set.

For each character, shift `window` left, add the new bit, and apply the mask:
`window = ((window << 1) & mask) | new_bit`. The shift moves every retained
bit one place toward its proper significance, the mask discards the bit that
has just left the window, and the new bit occupies the lowest position. Once
at least $k$ characters have been read, `window` is exactly the integer value
of the current length-$k$ substring.

**Count each distinct code only once**

Use a byte array of length $2^k$ indexed by the rolling value. Initialize
`remaining` to $2^k$. When a window value has not been seen, mark it and
decrement `remaining`; duplicate occurrences do nothing.

Return `true` immediately when `remaining` reaches zero, because every code
has then appeared and later characters cannot invalidate that fact. If the
scan ends with a positive remainder, at least one required code is absent.

The rolling update is exact by binary positional notation, so the algorithm
visits the encoded value of every length-$k$ substring in order. The seen array
therefore marks exactly the set of codes occurring in `s`. Its remaining
counter reaches zero exactly when that set is the complete universe
$\{0,1,\ldots,2^k-1\}$, which proves the returned result.

## Complexity detail
The impossibility test is constant time. When scanning is necessary, each of
the $n$ characters causes constant bit work and at most one seen-array update,
for $O(n)$ time. The byte array has $2^k$ entries, so auxiliary space is
$O(2^k)$. The early guard implies this allocation is also $O(n)$ on instances
that reach it.

## Alternatives and edge cases
- **Substring set:** Insert every slice `s[i:i+k]` into a hash set and compare
  its size with $2^k$. This is concise but materializes and hashes $k$-character
  strings, taking $O(nk)$ character work and $O(2^k k)$ stored characters in
  the worst case.
- **Search for every code:** Generate all $2^k$ binary strings and search for
  each in `s`. It is correct but can take $O(2^k(n+k))$ time.
- **`k > n`:** No length-$k$ substring exists, so return `false`.
- **Too few window positions:** Even when $k\le n$, fewer than $2^k$ windows
  proves that complete coverage is impossible.
- **`k = 1`:** Both `"0"` and `"1"` must occur.
- **Overlapping occurrences:** Every starting position is considered, so codes
  may share characters.
- **Duplicate windows:** Marking a code twice does not reduce the remaining
  count twice.
- **All-zero or all-one string:** It contains only one distinct code for any
  feasible $k$, so it fails whenever $2^k>1$.
- **Early completion:** Return as soon as the final unseen code is discovered.
