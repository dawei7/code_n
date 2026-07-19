## General
**Each position receives a suffix of the operations**

The operation at index `j` affects positions $0$ through $j$. Therefore the character at position `i` receives exactly the shifts whose indices satisfy $j \geq i$. Its total advance is

$$
T_i = \sum_{j=i}^{n-1} \texttt{shifts[j]}.
$$

Computing every $T_i$ independently would repeat work. Instead, scan from right to left while maintaining `total_shift`. Add `shifts[i]` before converting `s[i]`; the accumulator now equals $T_i$.

**Reduce the accumulated shift around the alphabet**

Only the remainder modulo 26 affects a lowercase letter. Keep `total_shift = (total_shift + shifts[i]) % 26` so even the largest input values stay small. Convert `s[i]` to its zero-based alphabet index, add the remainder modulo 26, and convert the result back to a character.

At each index, the maintained remainder equals $T_i \bmod 26$, so the produced letter is exactly the result of every prefix operation that covers that position. Since the scan fills all positions, joining the transformed characters yields the required final string.

## Complexity detail
The reverse scan processes each of the $n$ positions once, taking $O(n)$ time. The mutable character list used to construct the returned immutable string contains $n$ characters, so the implementation uses $O(n)$ space.

## Alternatives and edge cases
- **Simulate every prefix:** Applying each operation directly is straightforward and correct, but performs $Theta(n^2)$ character updates in the worst case.
- **Store all suffix sums:** A separate suffix-sum array also gives $O(n)$ time, but uses an additional $O(n)$ integers beyond the output buffer.
- **Difference-array view:** Prefix range additions can be encoded by endpoint differences and accumulated once; it is linear but less direct here than the right-to-left suffix total.
- **Zero shifts:** A zero contributes nothing, and an all-zero array returns `s` unchanged.
- **Large shift counts:** Reducing modulo 26 preserves the result and avoids carrying unnecessary large totals.
- **Wraparound:** Any transformed alphabet index at least 26 wraps back to the beginning.
- **Single character:** The sole value in `shifts` applies to that one character.
- **Repeated coverage:** Earlier characters receive at least as many indexed operations as later characters, but the operation magnitudes can still make their final remainders arbitrary.
