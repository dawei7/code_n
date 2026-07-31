## General

The target is the reversal of the original binary string, so original position $i$ must eventually equal the original bit at mirrored position $B-1-i$. A flip affects only its chosen position; it cannot help any other target position.

Compare each mirrored pair once. If its two original bits are equal, both positions already match their reversed targets and require no flip. If they differ, the left position must become the right bit and the right position must become the left bit, requiring exactly two flips. An odd-length string's center mirrors itself and never contributes.

Adding two for every unequal mirrored pair is both necessary, because each mismatched target position must change, and sufficient, because flipping precisely those positions constructs the reversed string. This yields the minimum.

## Complexity detail

Let $B$ be the bit length of `n`. Constructing and scanning the binary representation takes $O(B)$ time. The binary string occupies $O(B)$ auxiliary space. Under the source bound $n \leq 10^9$, $B \leq 30$.

## Alternatives and edge cases

- **Full Hamming distance:** Comparing `s` with `reversed(s)` at all $B$ positions returns the same answer; each unequal pair is intentionally observed twice.
- **Bitwise mirrored extraction:** The comparison can be performed with shifts and masks in $O(B)$ time and $O(1)$ auxiliary space, avoiding the binary string.
- **Build and mutate the target:** Explicitly flipping a character array is unnecessary because each position's target is already known.
- **Binary palindrome:** When every mirrored pair matches, the original equals its reverse and the answer is `0`.
- **Odd bit length:** The center bit maps to itself and never needs a flip.
- **Leading zeros:** They are not part of `s`; reversing may place the original final zero at the first target position, as in `"10"` becoming `"01"`.
