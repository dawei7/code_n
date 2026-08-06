## General

**Collapse the operation sequence into one offset.** Treat a right shift as positive and a left shift as negative. Sum every signed amount into `net_right`. Rotations compose by addition: after any prefix of the operations, a character's cyclic displacement equals the sum of that prefix's signed amounts. The complete sum therefore describes the same final arrangement as executing the operations one by one.

**Normalize before slicing.** Reduce `net_right` modulo `len(s)` so it lies between zero and `len(s) - 1`. This normalization handles totals larger than the string, negative totals whose net direction is left, and exact cancellation. Python's modulo produces the nonnegative right-shift representative directly.

If the normalized offset is zero, return `s`. Otherwise, split before the final `net_right` characters and concatenate that suffix before the prefix. Each character then moves to exactly the cyclic index obtained from the summed displacement, so the one rotation is equivalent to the full operation sequence.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$ and $q = \lvert\texttt{shift}\rvert$. Summing the $q$ operations takes $O(q)$ time, and constructing the rotated string copies $O(n)$ characters, for $O(n+q)$ total time. The returned string requires $O(n)$ space.

## Alternatives and edge cases

- **Apply each operation with slicing:** This follows the statement literally but constructs a new length-$n$ string for every row and can take $O(nq)$ time.
- **Move one character at a time:** Repeating a unit rotation for every requested position can take $O\!\left(n\sum_i \texttt{amount_i}\right)$ time.
- **Deque simulation:** A deque can rotate incrementally, but it retains operation-by-operation work and is less direct than combining offsets.
- **Opposite directions:** Signed amounts cancel without any special branching.
- **Negative net total:** Modulo normalization converts a net left shift into the equivalent nonnegative right shift.
- **Amounts larger than the string:** Only the final total needs reduction modulo $n$; individual amounts require no separate handling.
- **Zero amount:** The operation contributes zero and leaves the current arrangement unchanged.
- **Net zero:** Returning early avoids the misleading `s[-0:]` slice and preserves the original string.
- **Single-character string:** Every normalized rotation is zero, regardless of the operation sequence.
