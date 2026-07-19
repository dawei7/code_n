## General
Replace each value conceptually by its parity. For every position, let the current prefix count be the number of odd values seen from the start of `nums` through that position. A subarray contains exactly `k` odd values precisely when its ending prefix count exceeds the prefix count immediately before its start by `k`.

**Turning every endpoint into a counting query**

Maintain a frequency table for prefix odd counts already encountered. Before scanning any element, prefix count zero has occurred once: this represents choosing a subarray that starts at index zero. When the current prefix count is $p$, every earlier prefix equal to $p-k$ supplies one distinct valid start, so add that stored frequency to the answer.

**Why each nice subarray is counted once**

Every subarray has one unique prefix immediately before its start and one unique prefix at its end. Their odd-count difference is `k` exactly for a nice subarray. The scan counts that pair when it reaches the subarray's end, never earlier or later, establishing both that every valid subarray is included and that none is duplicated.

After querying $p-k$, record the current prefix $p$ for future endpoints. This order also makes the construction valid without relying on `k` being positive, although the contract already guarantees it.

## Complexity detail
The algorithm performs constant expected-time hash-table work for each of the $n$ values, for $O(n)$ total time. There can be at most $n+1$ distinct prefix counts in the frequency table, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Two at-most windows:** Compute the number of subarrays with at most `k` odd values minus the number with at most `k - 1`; this also runs in $O(n)$ time and uses $O(1)$ auxiliary space, but requires two window counts.
- **Odd-index gap products:** Store the positions of odd values and multiply the choices of left and right even extensions for every block of `k` consecutive odds; it is linear but needs careful sentinel handling.
- **Enumerating all subarrays:** Testing every start and end is direct but takes $O(n^2)$ time and cannot handle the largest input.
- **No odd values:** The answer is zero because `k` is always positive.
- **Exactly `k` odds in the whole array:** The entire array qualifies, and leading or trailing even values may create additional qualifying boundaries.
