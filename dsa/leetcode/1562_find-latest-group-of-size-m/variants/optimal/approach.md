## General
**Store each run length at its boundaries**

Maintain an array `length` with sentinel zeros outside positions `1..N`. For every active one-run, store its complete length at the run's left and right boundary positions. Interior entries do not need to be current because a newly activated position can touch only the right boundary of the run immediately to its left and the left boundary of the run immediately to its right.

When activating `position`, read `left = length[position - 1]` and `right = length[position + 1]`. The new maximal run has length `left + 1 + right`, begins at `position - left`, and ends at `position + right`. Writing the merged length at those two endpoints restores the boundary invariant in constant time.

**Track whether the target length currently exists**

Keep the number of active groups whose length is exactly `m`. Before the merge, remove one contribution when the left run has length `m` and one when the right run has length `m`. Then add one contribution if the merged run has length `m`. These are the only groups changed by the activation; every other group's maximal boundaries remain untouched.

After each merge, if the target-group count is positive, record the current step. Because steps are processed in increasing order, overwriting the answer produces the latest qualifying step. If the count never becomes positive, the initial `-1` remains correct.

## Complexity detail
Each of the $N$ activations performs a fixed number of boundary reads, writes, and count updates, for $O(N)$ total time.

The boundary-length array contains $N+2$ integers, so auxiliary space is $O(N)$. No explicit binary string, interval tree, or per-step scan is required.

## Alternatives and edge cases
- **Union-find:** activate positions as singleton sets, union active neighbors, and maintain counts by component size. This has near-linear time and expresses the same merging invariant with parent pointers.
- **Reverse deletion:** begin with all ones and remove positions in reverse activation order while maintaining zero boundaries. It can find the latest step naturally but requires careful interval bookkeeping.
- **Direct bitstring scan:** rebuild maximal runs after every activation. It is simple and correct but takes $O(N^2)$ time.
- **Target equals `N`:** the only qualifying state is the final all-one string, so the answer is `N`.
- **Target one:** isolated active positions count only while neither adjacent bit extends their group.
- **Merge two target groups:** activating the gap removes two size-`m` groups before possibly creating a different-sized group.
- **No qualifying step:** the permutation can skip directly over a target length when two neighboring runs merge, so `-1` is possible.
- **Boundary activations:** sentinel zeros make positions `1` and `N` follow the same merge formula as interior positions.
