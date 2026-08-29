## General

Each zero must become a positive even integer and each one a positive odd integer. Both arrays must increase internally, and no integer may appear in both. Imagine merging the final two increasing arrays into one globally sorted sequence. This merge preserves the order of elements from each input. Conversely, assigning increasing distinct integers along any such interleaving produces two valid increasing arrays.

The DP chooses the best interleaving. `f[i][j]` is the smallest possible last assigned integer after consuming the first `i` requirements of `nums1` and first `j` requirements of `nums2` in some merged order.

Helper `nxt(x,y)` returns the smallest positive integer strictly greater than `x` with parity `y`. If `x`'s parity differs from `y`, `x+1` has the desired parity. If parities match, `x+1` has the wrong parity and `x+2` is needed. The expression `(x & 1 ^ y) == 1` tests parity difference.

Starting from zero is safe: the next odd is one, while the next positive even is two. Zero itself is never assigned.

Boundary `f[i][0]` has only one possible interleaving: consume `nums1` in order, repeatedly applying `nxt`. `f[0][j]` does the same for `nums2`.

For an interior state, the final assigned value comes from one of two arrays. If it is `nums1[i-1]`, the previous state is `f[i-1][j]` and the smallest possible new value is `nxt(f[i-1][j],x)`. If it is `nums2[j-1]`, the candidate is `nxt(f[i][j-1],y)`. Taking the minimum chooses the better last step:

`f[i][j] = min(nxt(f[i - 1][j], x), nxt(f[i][j - 1], y))`.

Choosing the smallest feasible next value is always safe. A smaller current maximum gives at least as many options for every future parity requirement because `nxt` is monotone in its first argument.

Every legal pair of final arrays has a sorted merge order, so the DP considers it as a path through the grid. Every DP path assigns globally strictly increasing integers, guaranteeing uniqueness across both arrays and internal increase. Thus minimizing the final value over all paths gives the requested smallest possible largest integer.

For an empty `nums1`, the boundary recurrence alone constructs `nums2`. Requirements `[1,0,1,1]` yield one, two, three, and five, so the answer is five.

**Why global increasing order is not an extra restriction.** Any two individually increasing arrays with distinct values can be merged by numeric order. Their elements appear in original order within each source. The DP merely chooses that merge explicitly; it does not exclude any feasible assignment.

## Complexity detail

Let $m=len(nums1)$ and $n=len(nums2)$. The table has $(m+1)(n+1)$ states, and each uses constant work, so time is $O(mn)$.

The exact source stores the full two-dimensional table, using $O(mn)$ auxiliary space. This conflicts with the manifest's $O(m)$ rolling-space claim. Each row depends only on the previous row and the current row's preceding cell, so a one-dimensional DP could reduce space to $O(n)$, or to the smaller dimension after swapping roles.

Values grow by at most two per consumed element, so the answer is at most roughly $2(m+n)$.

## Alternatives and edge cases

- **Rolling one-dimensional DP:** Update a row left to right while retaining previous-row values. It preserves $O(mn)$ time and reduces auxiliary space to one dimension.
- **Greedy fixed merge:** Always taking from one array when possible can block a better parity alignment later. DP compares both interleavings at every prefix.
- **Shortest path on a grid:** States are grid vertices and transitions have `nxt`-defined labels. This is equivalent to the DP formulation.
- **One array empty:** Boundary initialization handles it without interior states.
- **Both next requirements equal:** Either source may go next; the minimum transition keeps the better future state.
- **Parity differs from current value:** One increment suffices; matching parity requires two.
- **First even requirement:** It becomes two, not zero, because replacements must be positive.
- **Uniqueness:** Global strict increase in the chosen merge ensures no integer is reused.
- **Long runs of one parity:** Assigned values advance by two within that run.
- **Source-space mismatch:** The recurrence supports rolling space, but the exact `f` table is quadratic in the two lengths.
- **Interleaving ties:** Two different merge paths can reach the same `(i,j)` with different last values. Keeping only the smaller last value is sufficient because every future `nxt` result is no larger from a smaller predecessor.
- **No reconstruction required:** The DP returns only the minimum possible maximum, so it does not store which transition won. Producing the actual replacement arrays would require parent choices or a backward reconstruction pass.
- **Array-order preservation:** A path may alternate between sources, but it can consume only the next unconsumed item from either array. This enforces each input's original order and therefore the required internal increasing positions.
- **Distinctness across arrays:** Assigning globally increasing values along the merge is stronger than checking duplicates afterward and automatically prevents an integer chosen for one array from appearing in the other.
