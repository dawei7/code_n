## General

Treat every length-`k` window independently. In one window, scan from the left through the longest non-decreasing prefix and from the right through the longest non-decreasing suffix. If those scans meet, the whole window is already sorted and contributes zero.

Otherwise, the first descent and the last descent enclose an **inversion core**. Every valid segment must contain that core: leaving either descent untouched would leave two adjacent elements in decreasing order. Find the minimum and maximum values inside the core.

The tentative left boundary may still be too far right. While the element immediately before it is greater than the core minimum, that element would remain before a smaller value after the core is sorted, so it must also be included. Expand the left boundary until this is no longer true. Symmetrically, include each element immediately after the right boundary that is smaller than the core maximum.

After both expansions, the prefix outside the segment is non-decreasing and ends at a value no greater than the segment minimum. The suffix is non-decreasing and begins at a value no smaller than the segment maximum. Sorting the selected segment therefore makes all three pieces and both joins non-decreasing. Conversely, every position added during expansion would form an out-of-order join if excluded, so no shorter segment can work.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $w=n-k+1$ be the number of windows. Each window is copied and scanned a constant number of times, taking $O(k)$ time and $O(k)$ temporary space. Across all windows, the total time is $O(wk)=O((n-k+1)k)$ and the auxiliary space is $O(k)$, excluding the required output.

## Alternatives and edge cases

- **Sort and compare every window:** Sorting a copy and trimming equal prefixes and suffixes is straightforward, but costs $O((n-k+1)k\log k)$ time.
- **Adjacent descents alone:** Returning only the interval between the first and last descent is insufficient; a smaller value inside that interval may force the left boundary farther out, and a larger value may force the right boundary farther out.
- **Already sorted window:** When no adjacent descent exists, no operation is necessary and the answer is zero.
- **Singleton window:** A one-element window is always non-decreasing, so every returned value is zero when `k == 1`.
- **Equal values:** Non-decreasing order permits equality. Boundary expansion therefore uses strict `>` on the left and strict `<` on the right.
- **Decreasing window:** Its inversion core spans the entire window, so the answer is `k`.
