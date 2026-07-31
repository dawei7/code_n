## General

Scan `towers` from left to right. Compute each tower's Manhattan distance from `center` and skip it when that distance exceeds `radius`. For a reachable tower, compare its quality with the best reachable quality seen so far. Replace the current answer when the quality is larger, or when the quality is equal and the new `[x, y]` coordinate is lexicographically smaller.

The maintained state is the best tower under the problem's complete ordering: higher quality wins first, and smaller coordinates decide equal-quality ties. Before the scan, the quality sentinel is `-1`; this is below every legal quality, including zero, while `[-1, -1]` is already the required empty-set answer. After any prefix of the array, the state therefore represents the required winner among exactly the reachable towers in that prefix. An unreachable next tower cannot change that winner. A reachable next tower replaces it precisely when the problem's ordering says the new tower is better. By induction, the final state is the required winner among all reachable towers, or remains the fallback when there are none.

The reachability comparison is inclusive. A distance equal to `radius` must remain eligible, so only distances strictly greater than the radius are skipped.

## Complexity detail

Let $N$ be the number of towers. The scan performs constant work for each entry, giving $O(N)$ time. It retains only the center coordinates, one quality, and one answer coordinate, so its auxiliary space is $O(1)$.

The benchmark defines size as $N$. Every benchmark tower is reachable, forcing a complete scan; the slower control compares every reachable candidate with every other reachable tower before choosing the undominated one.

## Alternatives and edge cases

- **Collect and sort:** Filtering all reachable towers and sorting by descending quality followed by ascending coordinates is correct, but costs $O(N\log N)$ time and $O(N)$ additional space.
- **Repeated pairwise comparison:** Testing every reachable tower against every other tower finds the same winner but takes $O(N^2)$ time.
- **Distance exactly equal to the radius:** The bound is inclusive, so the tower is reachable.
- **Equal quality:** Compare the $x$ coordinates first; compare $y$ only when the $x$ coordinates are equal.
- **Quality factor zero:** Zero is legal and must beat the `-1` sentinel when the tower is reachable.
- **No reachable tower:** Leave the initialized answer unchanged and return `[-1, -1]`.
- **Repeated coordinates:** Multiple tower entries may produce the same coordinate; their qualities are still evaluated normally.
