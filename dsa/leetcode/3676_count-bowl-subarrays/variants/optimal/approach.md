## General

**Rephrase the bowl condition around the smaller endpoint**

For endpoints `l < r`, the bowl condition is

`min(nums[l], nums[r]) > every interior value`.

Because all values are distinct, one endpoint is strictly smaller. The condition says that this smaller endpoint must still be larger than every element between the endpoints.

There are two cases:

- If `nums[l] < nums[r]`, then `r` is the first position to the right of `l` with a value greater than `nums[l]`; otherwise an earlier greater interior value would violate the bowl.
- If `nums[l] > nums[r]`, then `l` is the nearest position to the left of `r` with a value greater than `nums[r]`.

A monotonic decreasing stack identifies both kinds of endpoint pair in one left-to-right scan.

**Maintain a decreasing stack**

The stack stores pairs `(value, index)` with values strictly decreasing from bottom to top.

When new `value = nums[right]` arrives, every top value smaller than it is popped. After all smaller values are removed, the remaining top, if any, is greater than the current value.

Each stored index represents a candidate endpoint that has not yet encountered a greater value to its right.

**Count bowls when a smaller left endpoint is popped**

Suppose stack entry `(v, left)` is popped because `v < value`.

The current `right` is the first index after `left` with a value greater than `v`. If any earlier interior value had exceeded `v`, it would have popped this entry sooner.

Therefore every value strictly between `left` and `right` is less than `v`. Since `v` is the smaller endpoint,

`min(v, value) = v`

is greater than every interior element. The pair forms a bowl whenever it has at least one interior position.

The source checks

`right - left >= 2`,

which is exactly the length-at-least-three requirement.

One new large value can pop several entries. Each popped entry defines a different left endpoint and therefore a different bowl subarray ending at `right`.

**Count a bowl with the nearest greater left endpoint**

After all smaller stack values are popped, suppose the stack is nonempty. Its top value is greater than current `value`.

It is also the nearest greater value to the left that remains relevant. Any index between that top and `right` has value below the current value; if an interior value were greater, it would remain above the chosen top after smaller elements were popped and would be the actual stack top.

Thus current `value` is the smaller endpoint and all interior values are below it. The top and current index form one bowl if their distance is at least two.

The source adds exactly one for this case because only the nearest greater left endpoint can have every interior value below current `value`. A farther greater endpoint would contain the nearer greater value in its interior, violating the strict condition.

**Why every bowl is counted**

Take any bowl `[l, r]`.

If the right endpoint is larger, the left endpoint is the smaller boundary and no interior value exceeds it. Its stack entry survives until `r` and is popped by `nums[r]`, so the while-loop counts it.

If the left endpoint is larger, no interior value exceeds the smaller right endpoint. After popping values below `nums[r]`, index `l` is the nearest greater stack entry and the post-loop check counts it.

The two cases are disjoint because endpoint values are distinct. Each bowl is counted exactly once at its right endpoint.

**Why non-bowls are not counted**

A popped entry has no earlier greater interior value by the “first greater to the right” property. A remaining top has no nearer greater interior value and all popped interior candidates are smaller than current.

Therefore every counted endpoint pair satisfies the interior maximum condition. The explicit distance check removes adjacent pairs, which would have length two and no valid bowl length.

**Trace `[2, 5, 3, 1, 4]`**

Value five pops two, but they are adjacent, so no bowl is counted.

Values three and one are pushed below five. When four arrives, it pops one; indices three and four are adjacent, so that pair is ignored. It then pops three at index two. The distance is two, producing bowl `[3, 1, 4]`.

After popping smaller values, five remains as the nearest greater left endpoint. Its index one is three positions away from four, producing `[5, 3, 1, 4]`.

**Trace the increasing tail example**

For `[5, 1, 2, 3, 4]`, each new tail value pops the previous smaller value. After popping, five remains the nearest greater left endpoint.

At right endpoints two, three, and four, the distance from index zero is at least two, creating the three bowls listed in the example.

**Why distinctness matters**

The problem uses strict inequalities and guarantees distinct values. The stack pops only on `<` and treats a remaining top as greater.

With duplicates, equality would require separate reasoning because equal endpoints or interiors do not satisfy strict greater-than. The exact algorithm relies on the distinctness guarantee.

## Complexity detail

Each array element is pushed onto the stack once. It can be popped at most once. The total number of while-loop iterations across the whole scan is therefore `O(n)`, even though one iteration may pop many entries.

All other work per index is constant, giving total time `O(n)`.

The decreasing stack can contain all `n` elements for a strictly decreasing array, so auxiliary space is `O(n)`.

The answer can be quadratic in magnitude even though it is computed in linear time. Python integers handle the count automatically.

## Alternatives and edge cases

- **Enumerate all subarrays:** Checking interior maxima directly costs at least `O(n^2)` and often `O(n^3)` without preprocessing.
- **Range-maximum queries for every endpoint pair:** A sparse table makes each test fast but still leaves `O(n^2)` pairs.
- **Nearest-greater arrays:** Precompute first greater to the right and nearest greater to the left, then count qualifying distances. This is equivalent monotonic-stack reasoning with extra arrays.
- **Use an increasing stack:** It tracks the wrong dominance relationship for endpoints that must exceed interiors.
- **Pop on `<=`:** Distinctness makes no difference here, but with duplicates it would not automatically preserve the strict bowl condition.
- **Adjacent endpoints:** They are not bowls because length must be at least three; `right - left >= 2` enforces this.
- **Strictly decreasing array:** No right endpoint has a qualifying interior-lower pair of length at least three, so the answer is zero.
- **Strictly increasing array:** Symmetrically, popped pairs are adjacent and no greater-left bowls form, giving zero.
- **Large outer endpoints:** One right endpoint may complete several bowls by popping multiple smaller candidates.
- **Nearest greater on the left:** Only the nearest can pair with a smaller right endpoint; any farther candidate contains that nearer greater value inside.
- **Distinct-value guarantee:** It ensures every endpoint pair has one uniquely smaller value and avoids equality cases.
- **Input preservation:** The source stores value-index pairs without modifying `nums`.
