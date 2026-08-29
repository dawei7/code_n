## General

**Turn valid jumps into bidirectional inversion edges**

Take two indices `i < j`. If `nums[i] > nums[j]`, the jump from `i` to `j` is allowed because it moves right to a smaller value.

The reverse jump from `j` to `i` is also allowed: it moves left to the larger value `nums[i]`. Thus every inversion pair—an earlier larger value and a later smaller value—connects its two indices in both directions.

Reachability can therefore be viewed as connected components of an undirected graph whose vertices are array indices and whose edges are inversion pairs. Every index in one component can reach every other index in that component, so its answer is the maximum `nums` value inside that component.

The challenge is finding these components without building up to `O(n^2)` inversion edges.

**Characterize a boundary between components**

Consider a cut after index `i`, separating prefix `[0, i]` from suffix `[i + 1, n - 1]`.

An inversion edge crosses this cut exactly when some prefix value is greater than some suffix value. Such an edge exists precisely when

`maximum(prefix) > minimum(suffix)`.

Therefore the cut is a true separation with no cross-component edge exactly when

`maximum(prefix) <= minimum(suffix)`.

The non-strict comparison matters. Equal values do not form an inversion because both jump rules use strict inequalities. A prefix maximum equal to the suffix minimum creates no edge by itself.

The inversion graph has the interval-component property: each connected component occupies a contiguous segment of indices. If a component contains indices on both sides of a position, inversion edges and their transitive connections absorb the indices between its extremes. Consequently, the cuts satisfying the no-cross-inversion condition are exactly the boundaries between consecutive components.

Once these boundaries are known, every index in one segment receives that segment’s maximum.

**Precompute every prefix maximum**

The source builds `pre_max`:

`pre_max[i] = max(nums[0], nums[1], ..., nums[i])`.

It initializes every entry from `nums[0]` and fills later entries with

`max(pre_max[i - 1], nums[i])`.

At a component’s right endpoint, this prefix maximum is also that component’s maximum. Any earlier components have values no greater than the suffix component boundary permits; the running prefix maximum records the largest value reachable within the block being closed.

**Scan possible cuts from right to left**

Variable `suf_min` stores the minimum value strictly to the right of the current index. It begins at infinity for `i = n - 1` because that position has an empty right suffix.

For each index from right to left, the source compares `pre_max[i]` with `suf_min`.

If

`pre_max[i] <= suf_min`,

there is no inversion crossing the cut after `i`. A component ends at `i`, and its maximum reachable value is `pre_max[i]`. The source assigns that value to `ans[i]`.

If

`pre_max[i] > suf_min`,

some inversion crosses the cut, so index `i` lies in the same component as index `i + 1`. Its answer must equal the component value already computed on the right:

`ans[i] = ans[i + 1]`.

After making the decision, the source updates

`suf_min = min(suf_min, nums[i])`

so the next iteration sees the minimum of the suffix strictly to its right.

**Why the update happens after the comparison**

The boundary after `i` compares prefix `[0, i]` with suffix `[i + 1, n - 1]`. Including `nums[i]` in `suf_min` before the comparison would make the two sides overlap and test the wrong cut.

Updating afterward maintains the exact invariant: at the start of the next iteration for `i - 1`, `suf_min` contains the minimum over indices `i` through `n - 1`, which is precisely that next cut’s right side.

**Why propagating `ans[i + 1]` gives the component maximum**

At the rightmost index of a component, the cut to its right is a separation, so the source writes the component’s prefix maximum there.

Every earlier index inside the same component encounters a crossing inversion at its cut and copies the answer from the next index. The value propagates left across the entire segment.

When another separation is reached, propagation stops and a new prefix-maximum value starts for the component on its left. This assigns one maximum to each component without storing explicit component boundaries.

**The rightmost access is safe**

At `i = n - 1`, `suf_min` is infinity, so finite `pre_max[i] > suf_min` is false. Python’s conditional expression evaluates only the selected branch, and the source chooses `pre_max[i]` rather than evaluating `ans[i + 1]`.

Thus the apparent `ans[n]` reference is never accessed. After that first iteration, `i + 1` is always a valid index.

**Trace the examples**

For `[2, 1, 3]`, prefix maxima are `[2, 2, 3]`.

At the rightmost index, answer three is established. The cut after index one has prefix maximum two and suffix minimum three, so it is a valid boundary; index one receives two. At the cut after index zero, prefix maximum two exceeds suffix minimum one, so indices zero and one share a component and index zero copies answer two. The result is `[2, 2, 3]`.

For `[2, 3, 1]`, the value one in the suffix is below both earlier prefix maxima. Inversions cross the internal cuts, so the rightmost component maximum three propagates across all indices, producing `[3, 3, 3]`.

**Why explicit path simulation is unnecessary**

One starting index may have many possible jump sequences, and cycles are common because every inversion edge is bidirectional. Breadth-first search from every index would repeat component exploration.

The prefix-maximum/suffix-minimum condition extracts all component boundaries in two linear scans. Once a component is identified, reachability inside it means every member shares the same maximum answer.

## Complexity detail

Let `n` be the array length. Building `pre_max` takes `O(n)` time. The right-to-left scan computes all answers in another `O(n)` time, so total time is `O(n)`.

The answer array and prefix-maximum array each contain `n` values. Excluding the required output, the explicit auxiliary structure is `pre_max`, so auxiliary space is `O(n)`. `suf_min` and loop indices use `O(1)`.

The conceptual inversion graph may contain `O(n^2)` edges, but the algorithm never constructs it. The boundary characterization compresses all cross-edge information into one prefix maximum and one suffix minimum per cut.

## Alternatives and edge cases

- **Build the inversion graph:** Test every index pair and then find connected components. This costs `O(n^2)` time and potentially `O(n^2)` space.
- **Search from every starting index:** Repeated DFS or BFS revisits the same reachability components and is far too expensive.
- **Monotonic-stack components:** Inversion components can also be merged during a left-to-right stack scan in `O(n)` time and `O(n)` space.
- **Use `>=` as the merge test:** Equal values do not permit either strict jump, so equality alone must leave a boundary. The source correctly merges only when `pre_max[i] > suf_min`.
- **Update suffix minimum before testing:** That includes the current element on both sides and checks the wrong partition.
- **Strictly increasing array:** Every cut satisfies prefix maximum less than or equal to suffix minimum. No inversion edges exist, so each answer is its own value.
- **Strictly decreasing array:** Every pair is an inversion, all indices share one component, and every answer is the global maximum.
- **All values equal:** Strict jump conditions allow no movement. Every index remains its own component, though all returned values are numerically equal.
- **Single element:** The empty right suffix is represented by infinity, and the source returns the element itself.
- **Duplicate values with other connectors:** Equal-valued indices have no direct edge but may still belong to one component through inversions involving different values.
- **Global maximum near the left:** It can propagate to later and earlier connected positions only when inversion crossings join their cuts; position alone does not determine reachability.
- **Input preservation:** The source reads `nums` and creates new arrays without modifying the input.
- **Missing imports:** The stored source uses `List` and `inf` without imports. Standalone Python needs the appropriate `typing` and `math` imports unless supplied by the harness.
