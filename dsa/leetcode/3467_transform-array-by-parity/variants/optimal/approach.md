## General

After the first two required operations, every array element is either `0` or `1`. Therefore, the final non-decreasing order is determined completely by how many values belong to each parity class; the positions and magnitudes of the original values no longer matter.

Scan `nums` once and count the odd values. If that count is `odd_count`, then the other `n - odd_count` values are even. Construct the result with exactly `n - odd_count` zeroes followed by exactly `odd_count` ones. This is the same multiset produced by the parity replacements, and zero is smaller than one, so the constructed order is precisely the required sorted order.

Counting only one class is sufficient because every integer is either even or odd. It also avoids performing a general comparison sort on an array whose only possible transformed values are already known.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan and construction each take $O(n)$ time. The returned list contains $n$ elements, so total space is $O(n)$; excluding the required output, the parity counter uses $O(1)$ auxiliary space. Linear time is asymptotically optimal because every input value can change the parity counts and every output position must be produced.

## Alternatives and edge cases

- **Transform and comparison-sort:** Replacing every value and sorting is direct, but a general sort takes $O(n\log n)$ time even though only two output values are possible.
- **Two output buckets:** Appending each transformed value to a zero bucket or one bucket is also $O(n)$, but it stores two growing collections before joining them instead of keeping one count.
- **All values have the same parity:** One repeated block has length zero, and the other fills the entire result.
- **Single element:** The sole value becomes either `[0]` or `[1]`, already in non-decreasing order.
- **Repeated or boundary values:** Equality and magnitude are immaterial; only each value's parity contributes to the result.
