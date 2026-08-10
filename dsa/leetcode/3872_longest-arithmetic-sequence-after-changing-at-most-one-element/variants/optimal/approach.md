## General

**Represent arithmetic structure through adjacent differences**

A contiguous sequence is arithmetic when every adjacent difference is equal. The source builds

`d[i] = nums[i] - nums[i - 1]`

for `i\ge1`. Entry `d[0]` is unused and remains zero.

Changing one element can affect only the two adjacent differences touching that index. Every other difference stays fixed. This locality suggests precomputing unchanged arithmetic runs on both sides of every possible replacement position.

**Longest unchanged run ending at each index**

`f[i]` is the length, in elements, of the longest unchanged arithmetic subarray ending at index `i`.

The base values are `f[0]=1` and `f[i]=2` for `i\ge1`, because any two-element subarray is arithmetic: it has only one adjacent difference.

For `i\ge2`, if

`d[i] == d[i - 1]`,

then the difference from `i-1` to `i` continues the same arithmetic run ending at `i-1`. The source sets

`f[i] = f[i - 1] + 1`.

If the differences differ, the longest run ending at `i` resets to the final two elements, so the initialized value two remains.

**Longest unchanged run starting at each index**

Symmetrically, `g[i]` is the longest unchanged arithmetic subarray starting at `i`. The last position has length one, and other positions begin at length two.

Scanning right to left, if `d[i+1] == d[i+2]`, the edge from `i` to `i+1` continues the run starting at `i+1`, so

`g[i] = g[i + 1] + 1`.

These arrays allow the main loop to know in constant time how far a fixed common difference already extends on either side.

**A length of three is always achievable**

The constraints give `N\ge4`. Any three consecutive integers can be made arithmetic by changing one endpoint. For values `a,b,c`, replace `a` by `2b-c`; then both adjacent differences equal `c-b`. The replacement may be any integer, so this is always legal.

The source safely initializes `ans=3`. Longer candidates are then discovered from unchanged runs and each possible changed index.

**Possibility one: do not need the change**

The operation is optional. An already arithmetic subarray remains valid, so the loop includes `f[i]` and `g[i]` in the maximum. Either family alone could cover all unchanged runs; checking both is harmless and aligns with later one-sided cases.

**Possibility two: the changed element is an endpoint**

If index `i` becomes the right endpoint of a selected arithmetic subarray, take the unchanged run ending at `i-1` and choose a new `nums[i]` that continues its common difference. This yields length

`f[i - 1] + 1`.

The source considers it whenever `i>0`.

If `i` becomes the left endpoint, take the unchanged run starting at `i+1` and choose `nums[i]` to extend it backward. This yields

`g[i + 1] + 1`.

The source considers it whenever `i+1<N`.

For a neighboring run of length one, no common difference is established, but the resulting length two is automatically arithmetic; `ans=3` already dominates it. For runs of length at least two, the extension value is uniquely determined and always an integer.

**Possibility three: bridge fixed runs through an interior change**

For `0<i<N-1`, suppose the selected subarray includes fixed neighbors `nums[i-1]` and `nums[i+1]` on both sides of the changed value.

If the final common difference is `q` and the replacement is `z`, then

$$
z-\texttt{nums}[i-1]=q
$$

and

$$
\texttt{nums}[i+1]-z=q.
$$

Adding gives

$$
2q=\texttt{nums}[i+1]-\texttt{nums}[i-1].
$$

Thus the neighbor difference must be even for integer `q`. The source checks `diff % 2 == 0` and then divides by two. Python's parity test also works for negative differences.

The three central elements can then be made arithmetic, so `k` begins at three. To extend left, the newly required difference `q` must equal the difference already entering `nums[i-1]`, which is `d[i-1]`. If so, the full run of length `f[i-1]` can join. Since its final element `nums[i-1]` is already included in the central three, the source adds `f[i-1]-1`.

To extend right, `q` must equal `d[i+2]`, the difference leaving `nums[i+1]` toward `nums[i+2]`. The source adds `g[i+1]-1` because `nums[i+1]` is already counted.

Both sides may extend simultaneously, producing one long arithmetic subarray across the replacement.

For `[9,7,5,10,1]` at `i=3`, the fixed neighbors are five and one. Their difference is minus four, so `q=-2` and the replacement is three. The left run `9,7,5` already uses difference minus two, allowing all five elements to combine as `9,7,5,3,1`.

**Why these cases are exhaustive**

Take an optimal selected subarray after at most one replacement.

If the changed index lies outside it or no change is used, the subarray is an unchanged run captured by `f` or `g`.

If the changed index lies at one endpoint, it is captured by one of the one-sided extensions.

If it lies strictly inside, both fixed neighbors belong to the subarray and force the replacement to their midpoint. The bridge calculation checks exactly whether that midpoint is an integer and extends through every matching unchanged run on both sides.

There is no other position the changed element can occupy relative to a contiguous selected subarray. Taking the maximum over all indices and cases therefore finds the global optimum.

## Complexity detail

Constructing `d`, `f`, and `g` requires three linear passes. The final loop performs constant work per index. Total time is `O(N)`.

Each of the three arrays has length `N`, so auxiliary space is `O(N)`. The remaining variables are constant-sized. These bounds match the manifest.

All differences fit comfortably in ordinary signed integer types under the stated values. Python integers also handle the midpoint arithmetic exactly without overflow.

## Alternatives and edge cases

- **Enumerate replacement values:** The allowed replacement is any integer, an infinite set. Structural equations determine the only useful endpoint continuation or interior midpoint instead.
- **Check every subarray:** Testing arithmetic structure and one possible defect over `O(N^2)` intervals is too slow for `N=10^5`.
- **Change one adjacent difference independently:** Replacing an interior element changes two differences together; they cannot be optimized separately. The midpoint equation couples them.
- **No replacement:** Already arithmetic runs must remain candidates because the operation is “at most” one, not exactly one.
- **Change at a selected endpoint:** Only one neighboring difference must match, so an arbitrary integer extension is always possible.
- **Interior odd neighbor difference:** No integer can be exactly halfway between the fixed neighbors, so a two-sided bridge is impossible. One-sided candidates may still work.
- **Negative difference:** Arithmetic sequences may decrease. Equality tests and evenness work identically for negative values.
- **Zero difference:** Constant runs are arithmetic, and an interior replacement can bridge equal neighbors with the same value.
- **Array already arithmetic:** An unchanged run reaches length `N`, and no candidate can exceed it.
- **Minimum allowed length:** With `N=4`, initialization to three is valid and all boundary checks avoid out-of-range access.
- **Difference-array indexing:** `d[i]` describes the edge from `i-1` to `i`. Left extension compares `d[i-1]`; right extension compares `d[i+2]`.
- **Avoid double-counting neighbors:** The central bridge starts with three elements, so extensions add run length minus one on each side.
- **Space reduction:** One could precompute only one directional array and maintain the other direction with a more involved scan, but the three linear arrays keep the exact logic clear and meet the required bounds.
- **Import dependency:** The annotation uses `List`, which must be available in environments that evaluate annotations.
