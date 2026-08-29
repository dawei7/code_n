## General

**Scan from the ocean side**

The ocean lies to the right. A building at index `i` has a view exactly when its height is strictly greater than the height of every building at a larger index.

Scanning left to right would require knowing a future maximum. The exact solution instead scans from right to left, so all buildings that could block the current one have already been seen. It summarizes them with one scalar `mx`, the maximum height strictly to the right of the current index.

The current building qualifies when:

`heights[i] > mx`.

If it qualifies, its index is appended to `ans` and `mx` is updated to its height.

**Why strict greater-than is required**

The definition says every building to the right must have a smaller height. An equal-height building blocks the view just as a taller building does.

Therefore `heights[i] == mx` must not qualify. The strict `>` comparison implements that boundary correctly. A non-strict `>=` would wrongly accept the left building of two equal-height buildings.

**Initialize the suffix maximum**

`mx` begins at zero. All building heights are at least one, so the rightmost building is guaranteed to be greater than `mx`. It is appended, as it should be: with no building to its right, the “all buildings to the right are smaller” condition is vacuously true.

After processing an index, `mx` equals the maximum height among that index and every position to its right. Before the next iteration one step left, that is exactly the maximum strictly to the new current building's right.

If heights could be zero or negative, zero would not be a universally safe sentinel. Under the stated positive-height constraint, it is exact.

**Why only record heights need update mx**

The source updates `mx` only inside the qualifying branch. If `heights[i] <= mx`, the current building is no taller than the known suffix maximum, so it cannot change that maximum.

If `heights[i] > mx`, it becomes the new suffix maximum and must replace `mx`. Thus the conditional update produces the same value as assigning `mx = max(mx, heights[i])` on every iteration.

**Trace the first example**

For `[4,2,3,1]`, scan from index three:

- Height one is greater than initial zero, so record index three and set `mx = 1`.
- Height three is greater than one, so record index two and set `mx = 3`.
- Height two is not greater than three, so index one is blocked.
- Height four is greater than three, so record index zero.

The recorded list is `[3,2,0]` because discovery happened right to left.

**Restore increasing index order**

The contract requires indices sorted increasingly. The scan naturally appends them in decreasing order, so the source returns `ans[::-1]`.

The slice with step minus one creates a reversed copy: `[0,2,3]` in the example. Reversal affects only presentation order. It does not change which buildings qualified.

**Suffix-maximum invariant**

Before processing index `i`, `mx` is the greatest height among indices `i + 1` through `n - 1`. This holds initially for the rightmost building because its right suffix is empty and the positive-domain sentinel zero is below it.

If `heights[i] > mx`, every right-side building is shorter, so index `i` has a view and its height becomes the new maximum. If the inequality fails, at least one right-side building has height greater than or equal to the current height, so it blocks the view, and the suffix maximum remains unchanged.

This maintains the invariant and classifies every building exactly according to the definition.

**Why the final answer is correct**

Every appended index was taller than the complete suffix maximum, so all buildings to its right are strictly smaller. Every omitted index was no taller than that maximum, proving that some right-side building blocked it.

Thus `ans` contains exactly the ocean-view indices. Reversing it puts those indices in the required increasing order without changing membership.

## Complexity detail

Let $n$ be the number of buildings. The reverse range visits every index once with constant-time comparison, append, and possible assignment. Reversing the answer takes $O(v)$ time where $v \le n$ is the number of qualifying buildings. Total time is $O(n)$.

`ans` holds $O(v)$ indices, and `ans[::-1]` allocates another list of the same size for the returned result. The exact peak space is therefore $O(n)$ including this output construction, matching the manifest. Aside from result storage, `mx`, `i`, and loop state use $O(1)$ auxiliary space.

The input list is read only and is not reversed or modified.

## Alternatives and edge cases

- **Suffix-maximum array:** Precompute the maximum to the right of every index. It also gives $O(n)$ time but uses $O(n)$ extra storage beyond the result.
- **Monotonic stack:** Scan left to right and remove previously recorded buildings blocked by the current one. It is linear but more stateful than a single suffix maximum.
- **Check every right suffix:** Directly testing all blockers for each building costs $O(n^2)$ time.
- **Strictly decreasing heights:** Every building is a new suffix maximum, so all indices are returned.
- **Strictly increasing heights:** Only the rightmost, tallest building has a view.
- **Equal neighboring heights:** The left equal-height building is blocked because the comparison is strict.
- **One building:** It is appended against sentinel zero and returned.
- **Rightmost building:** It always qualifies because nothing lies to its right.
- **Positive-height guarantee:** It makes initial `mx = 0` safe.
- **Very tall leftmost building:** It qualifies if it exceeds the maximum of the entire remaining array.
- **Discovery order:** Right-to-left scanning requires reversal to satisfy increasing output order.
- **Reversed slice:** It creates a new list rather than reversing `ans` in place.
- **No building identity changes:** Only indices are stored; heights remain in the original array.
- **Large height values:** Only comparisons are used, so magnitude does not affect complexity.
