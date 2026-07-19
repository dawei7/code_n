## General
**Turning cut coordinates into segment lengths**

Horizontal cuts determine only the possible heights of pieces. If their coordinates are sorted and the cake boundaries `0` and `h` are included, each consecutive difference is the height of one horizontal strip. Vertical coordinates behave independently: after adding `0` and `w` and sorting, consecutive differences are the possible piece widths.

Including both physical borders is essential. A largest strip can lie above the first cut or below the last cut, just as a largest width can touch the left or right edge. The borders are not supplied as cuts, but they still delimit pieces.

**Why only the two maximum gaps matter**

Every horizontal cut spans the full width and every vertical cut spans the full height. Consequently, every horizontal strip intersects every vertical strip, and each pair of gaps forms one actual rectangular piece. If the height gaps are $a_1,\ldots,a_{H+1}$ and the width gaps are $b_1,\ldots,b_{V+1}$, the set of piece areas is exactly $a_i b_j$ over all valid pairs.

All gap lengths are positive. Let $a_{\max}$ be the greatest height gap and $b_{\max}$ the greatest width gap. For every piece, $a_i \le a_{\max}$ and $b_j \le b_{\max}$, so $a_i b_j \le a_{\max}b_{\max}$. The strip with height $a_{\max}$ and the strip with width $b_{\max}$ physically intersect, which means a piece attaining that upper bound exists. There is no need to enumerate all $(H+1)(V+1)$ rectangles.

**Scanning adjacent sorted coordinates**

Sort a copy of each cut array with its two borders. Scan adjacent coordinates and retain the largest difference for that axis. Multiply the two maxima using the original integer values, then reduce the product modulo $1{,}000{,}000{,}007$.

The modulo must not be applied to individual gap lengths before their maxima are chosen. Modular reduction does not preserve numeric order: a genuinely larger gap or area can have a smaller remainder. First determine and multiply the true maximum dimensions; reduce only the final answer.

## Complexity detail
Sorting the $H$ horizontal coordinates costs $O(H\log H)$ and sorting the $V$ vertical coordinates costs $O(V\log V)$. Each sorted list is then scanned once, adding $O(H+V)$ work that is dominated by sorting. Total time is $O(H\log H+V\log V)$.

The implementation creates sorted coordinate lists, including two borders per axis, and therefore uses $O(H+V)$ auxiliary space. The largest unreduced area can approach $10^{18}$, so fixed-width implementations should multiply in a sufficiently wide integer type before applying the modulus.

## Alternatives and edge cases
- **Sort the input arrays in place:** This retains the same time bound and can reduce auxiliary container space, but it mutates caller-owned inputs and still uses the sorting implementation's stack or workspace.
- **Ordered set of cuts:** Inserting coordinates into balanced search trees also yields ordered gaps, but costs $O(H\log H+V\log V)$ with substantially more structural overhead than sorting static arrays.
- **Coordinate-sized marking arrays:** Marking every possible coordinate and scanning for cuts can take $O(h+w)$ space and time, which is infeasible because `h` and `w` may each be $10^9$ even when there are few cuts.
- **Enumerate all rectangles:** Multiplying every height gap by every width gap takes $O(HV)$ after sorting. Independence and positivity prove that the product of the separate maxima is sufficient.
- **Unsorted input:** Never subtract coordinates in their given order. The arrays may be arbitrarily permuted, so adjacent input entries need not bound a piece.
- **Border gaps:** Compare `first_cut - 0` and `dimension - last_cut` as well as gaps between cuts; the maximum can touch any edge.
- **Large answer:** Compute the actual maximum gap product before taking modulo $10^9+7$. Reducing candidates early can select the wrong piece.
- **One cut on an axis:** That axis has exactly two gaps, both of which must be considered even though the cut list has only one element.
