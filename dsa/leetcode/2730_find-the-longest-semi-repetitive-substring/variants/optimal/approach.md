## General

View every index `right` with `s[right] == s[right - 1]` as the right endpoint of an equal adjacent pair. A valid window may contain one such endpoint but not two.

Keep the left boundary of the current window and the right endpoint of the most recent equal pair. When a new equal pair appears and no earlier pair is present, record it without shrinking the window. When another appears, move `left` to the stored endpoint of the older pair. Starting at that character excludes the older pair's left character and therefore breaks the older adjacency, while retaining the newer pair as the window's single allowed repetition.

After this adjustment, the window ending at `right` is valid and is the longest valid window with that endpoint: moving `left` any farther right would only shorten it, while leaving it farther left would retain both equal pairs. Taking the maximum of these window lengths therefore finds the global optimum.

## Complexity detail

Each character is processed once as the right boundary, and `left` only moves forward. The running time is $O(n)$ for $n=\lvert s \rvert$. The algorithm stores only indices and the best length, so its auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every substring:** Expanding from every left endpoint and tracking equal pairs is correct but takes $O(n^2)$ time even when pair counts are updated incrementally.
- **Recount each candidate substring:** Scanning every substring again for equal pairs increases the brute-force cost to $O(n^3)$.
- **Queue of equal-pair positions:** A queue can maintain the same window condition, but only the latest pair endpoint is needed, so extra storage is unnecessary.
- A one-character string has answer one even though the main scan has no iteration.
- Runs such as `"111"` contain overlapping pairs at two different adjacent boundaries.
- Leading zeroes are ordinary string characters and must not be discarded.
- If the complete string has at most one equal pair, its full length is the answer.
