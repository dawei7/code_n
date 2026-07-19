## General
**Represent only frequency parity**

Whether a multiset can form a palindrome depends on odd versus even counts, not on the full counts. Encode the parity of the ten digits in a ten-bit mask: bit `d` is one exactly when digit `d` has appeared an odd number of times.

As the scan consumes a digit, toggle its bit with XOR. This produces the parity mask of every prefix. Because XOR subtracts parities as well as it adds them, the mask of a substring ending at the current index is the XOR of the current prefix mask and the mask immediately before the substring.

**Recognize the two valid mask differences**

A substring can be permuted into a palindrome when its parity mask has either no set bits or exactly one set bit. Consequently, for a current prefix mask `mask`, a valid earlier prefix must have:

- the same mask, yielding zero odd counts; or
- `mask ^ (1 << digit)` for one of the ten digits, yielding exactly one odd count.

Store the earliest index at which each of the 1024 possible prefix masks occurs. At each position, compare against the earliest identical mask and against the ten one-bit neighbors. The earliest matching prefix produces the longest substring ending at this position.

**Preserve the earliest occurrence**

Initialize mask zero at conceptual index `-1`, representing the empty prefix. This allows a valid substring beginning at index zero to use its full length. Record a mask only on its first occurrence; replacing that index later could only shorten every future candidate using the same mask.

The scan checks every possible valid parity relationship for each right endpoint. Any awesome substring has zero or one odd digit, so its two boundary prefix masks must be among exactly those eleven comparisons. Conversely, each comparison that matches creates a substring with a palindrome-compatible parity pattern. Taking the maximum therefore returns precisely the longest awesome substring.

## Complexity detail
For each of the $n$ positions, the algorithm performs eleven constant-time mask lookups, so the total time is $O(10n) = O(n)$. The table has exactly $2^{10} = 1024$ entries, independent of $n$, and therefore uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every substring:** incrementally maintaining a parity mask avoids recounting digits, but checking all two endpoints still takes $O(n^2)$ time.
- **Store full frequency vectors:** prefix counts can test a chosen interval, but comparing many vectors does not eliminate the quadratic endpoint search and uses more state than parity masks.
- Every one-character substring is awesome, so the answer is always at least one.
- A substring with all even digit counts is valid, as is one with exactly one odd count.
- Two or more odd digit counts cannot be repaired by rearrangement alone.
- Repeated prefix masks identify even-count intervals; a one-bit difference identifies the possible palindrome center digit.
- The longest valid interval may start at zero, which is why the empty-prefix mask must be stored at index `-1`.
