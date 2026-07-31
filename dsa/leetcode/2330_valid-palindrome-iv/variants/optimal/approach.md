## General

A palindrome requires every character to equal its mirror. One replacement can repair one mismatched pair by changing either endpoint to the other endpoint's character. Different mismatched pairs share no positions, so none of their required repairs can be combined.

Scan the first half of the string and compare position `left` with position `~left`, its mirror from the end. If more than two pairs disagree, at least three operations are necessary and the answer is false. If at most two disagree, repair each with one operation.

The word “exactly” does not exclude zero mismatches. For an odd-length palindrome, changing the center to any different letter uses one operation without breaking symmetry. For an even-length palindrome, changing both endpoints of any mirrored pair to the same different letter uses two. Thus every zero-, one-, or two-mismatch string can meet the required operation count, and the mismatch threshold is both necessary and sufficient.

## Complexity detail

Let $n$ be the string length. At most $\lfloor n/2\rfloor$ mirrored pairs are inspected, taking $O(n)$ time. Only the loop index and mismatch counter are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Reverse and compare:** Constructing `s[::-1]` also reveals disagreements, but allocates $O(n)$ extra memory and counts every mismatched pair twice unless adjusted.
- **Dynamic programming:** General palindrome-edit DP is unnecessary because replacements do not shift positions and only two edits are allowed.
- **Already a palindrome:** It remains valid under exactly one or two operations as described in the derivation.
- **Odd center:** The unpaired middle character never contributes a mismatch and can be changed freely when a padding operation is needed.
- **Early rejection:** The scan may stop at the third mismatch because later characters cannot reduce the number of independent repairs.
