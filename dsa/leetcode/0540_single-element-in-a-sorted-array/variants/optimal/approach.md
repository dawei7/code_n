## General
**Observe where pair alignment changes**

Before the singleton, every duplicate pair begins at an even index and ends at the following odd index. The singleton consumes one position, so every pair after it begins at an odd index instead.

**Compare an even midpoint with its partner**

Choose the midpoint and move it one position left when it is odd, making it the possible start of a pair. If `nums[mid] = nums[mid + 1]`, pair alignment is still normal through that pair, so the singleton lies strictly to its right. Otherwise the alignment has already broken, so the singleton is at `mid` or to its left.

**Maintain a search interval containing the singleton**

On a matching pair, move the lower bound past both elements. On a mismatch, retain the even midpoint as the new upper bound. Each update preserves the singleton and removes at least half of the remaining candidates.

**Why convergence identifies the unique value**

The parity rule is true for every complete pair before and after the singleton. Therefore a matching even-index pair proves the singleton is later, while a mismatch proves it is no later than that index. When the bounds meet, the invariant leaves exactly the singleton index, whose value is returned.

## Complexity detail
Each comparison halves the search interval, so the algorithm takes $O(\log n)$ time. It uses only bounds and a midpoint, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **XOR every value:** cancels duplicate pairs in $O(n)$ time and $O(1)$ space but misses the logarithmic requirement.
- **Linear neighbor scan:** can return the first unpaired value but also takes $O(n)$ time.
- **Frequency map:** is correct without sorted input but costs $O(n)$ time and space.
- **Singleton at the first index:** the first even comparison mismatches and keeps the left boundary.
- **Singleton at the last index:** every preceding even pair matches and is discarded.
- **One element:** the bounds already coincide, so that value is returned immediately.
- **Negative values:** only equality and sorted positions matter.
