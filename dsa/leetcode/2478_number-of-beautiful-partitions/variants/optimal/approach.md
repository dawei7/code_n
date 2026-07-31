## General

**Reduce valid substrings to valid boundaries.** A split position `i` lies between `s[i - 1]` and `s[i]`. It can separate two beautiful parts only when the character on its left is non-prime and the character on its right is prime. Position `0` and position $n$ serve as the outer boundaries. Consequently, the whole answer is zero immediately if `s[0]` is non-prime, `s[n - 1]` is prime, or $k \cdot \texttt{minLength} > n$.

**Build one partition layer at a time.** Let `ways[i]` be the number of valid ways for the already-built number of parts to cover the prefix ending at boundary `i`. Initially, zero parts cover the empty prefix in one way, so `ways[0] = 1`. To build the next part ending at boundary `end`, its previous boundary can be any valid `previous_end` satisfying `previous_end <= end - minLength`.

**Replace the inner sum with a running prefix sum.** Scan `end` from left to right. When it advances, the newly eligible predecessor is exactly `end - minLength`. If that position is a valid boundary, add `ways[end - minLength]` to a running sum. Whenever `end` itself is a valid boundary, that running sum is precisely the number of ways to form the current partition layer at `end`.

The scan can be restricted further: after forming `part` substrings, at least `part * minLength` characters must have been consumed, and enough characters must remain for the other parts. Every counted transition therefore joins a valid earlier partition to a new substring of sufficient length. Conversely, every beautiful partition has valid boundaries and appears exactly once when its endpoints are scanned, proving that the final value at boundary $n$ is the required count.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each of the $k$ dynamic-programming layers scans at most $n$ boundaries and performs constant work per boundary, for $O(kn)$ time. Only the previous and current layers are stored, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate every previous boundary:** This direct dynamic-programming transition is correct, but testing all earlier starts for every endpoint costs $O(kn^2)$ time.
- **Top-down substring recursion:** Memoizing a state by position and remaining parts still loops over many candidate endings and can retain the same $O(kn^2)$ bottleneck.
- **Invalid outer digits:** The first part cannot start correctly if `s[0]` is non-prime, and the final part cannot end correctly if `s[n - 1]` is prime.
- **Insufficient total length:** If $k \cdot \texttt{minLength} > n$, no placement of boundaries can satisfy all minimum lengths.
- **Minimum length one:** A beautiful substring still needs a prime starting digit and a non-prime ending digit, so its actual length is necessarily at least two.
- **Modulo arithmetic:** Apply the modulus while updating the running sum so counts remain bounded without changing the final residue.
