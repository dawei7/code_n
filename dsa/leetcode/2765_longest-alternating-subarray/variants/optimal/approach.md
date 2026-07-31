## General

Scan adjacent differences once. Maintain the length of the alternating run ending at the current position and the next required difference, which starts at $+1$.

When the current difference equals the expected value, extend the run and flip the expectation between $+1$ and $-1$. If it does not match but is $+1$, the current pair can immediately start a new length-two run, whose next expected difference is $-1$. Every other mismatch leaves only the current element as a possible future start, so reset the length to one and the expectation to $+1$.

After each step, use any length of at least two to update the maximum. The maintained run is the longest valid alternating subarray ending at the current index: matching extends it, a mismatching rise creates the only possible valid suffix of length two, and any other difference cannot belong to a valid starting pair. Taking the maximum over all ending positions therefore returns the requested length.

## Complexity detail

The scan examines each of the $n - 1$ adjacent pairs once and performs constant work per pair, so the running time is $O(n)$. Only the current length, expected difference, and best length are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every start:** Expanding a candidate from each index is direct and valid for the small constraint, but a fully alternating array makes it take $O(n^2)$ time.
- **Enumerate every subarray:** Checking each interval from scratch follows the definition closely but repeats even more work and can take $O(n^3)$ time.
- **Falling first step:** A pair with difference $-1$ cannot start an alternating subarray; the first difference must be $+1$.
- **Repeated rises:** A second consecutive $+1$ does not extend the current run, but it starts a new length-two candidate at the previous index.
- **No valid pair:** If the scan never sees a difference of $+1$, the required result remains `-1`.
