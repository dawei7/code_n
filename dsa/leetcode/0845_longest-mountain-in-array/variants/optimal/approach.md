## General

**A mountain is determined by a peak and two strict slopes**

For index `i` to be the peak of a mountain:

- at least one strictly increasing step must lead into `i` from the left;
- at least one strictly decreasing step must leave `i` to the right.

If we know the longest increasing run ending at each index and the longest decreasing run starting at each index, then every valid peak's mountain length follows immediately.

The exact solution stores these two quantities in arrays `f` and `g`.

**Increasing length ending at each index**

Every `f[i]` begins at one because a single element is a trivial run of length one.

Scanning left to right, when `arr[i] > arr[i-1]`, the increasing run ending at `i-1` can extend through `i`:

`f[i] = f[i - 1] + 1`.

If the comparison is equal or decreasing, no strict increasing run crosses that boundary, so `f[i]` remains one.

Thus, `f[i]` is exactly the number of consecutive elements in the maximal strictly increasing suffix ending at `i`.

**Decreasing length starting at each index**

Every `g[i]` also begins at one. Scanning right to left, when `arr[i] > arr[i+1]`, index `i` begins a descending step and can extend the decreasing run starting at `i+1`:

`g[i] = g[i + 1] + 1`.

If values are equal or rise to the right, `g[i]` remains one.

Therefore, `g[i]` is the length of the maximal strictly decreasing prefix starting at `i`.

**Recognize a valid peak**

The source considers a candidate only inside the branch `arr[i] > arr[i+1]`. This guarantees `g[i] > 1`: there is at least one downward edge.

It then requires `f[i] > 1`, guaranteeing at least one upward edge into `i`.

Together, these conditions ensure `i` is not an endpoint and that both sides of the mountain are nonempty.

**Combine the two slope lengths**

The increasing run includes the peak `i`, and the decreasing run also includes it. Adding `f[i] + g[i]` counts the peak twice, so the mountain length is:

`f[i] + g[i] - 1`.

`ans` retains the maximum over all valid peaks.

For `[2,1,4,7,3,2,5]`, the peak at value 7 has increasing run `[1,4,7]` of length three and decreasing run `[7,3,2]` of length three. The combined mountain length is `3+3-1=5`.

**Why plateaus break mountains**

Both update conditions use strict `>`. Equal adjacent values extend neither an increasing nor decreasing run. A plateau at or along a candidate peak therefore makes at least one relevant run reset to length one and prevents an invalid mountain from being counted across it.

**Why maximal runs give the longest mountain at a peak**

For a fixed peak, extending left while values strictly increase toward the peak can only make its mountain longer, and extending right while values strictly decrease can only make it longer. `f[i]` and `g[i]` capture those maximal extensions.

Every mountain has one peak. Its increasing portion is no longer than `f` at that peak, and its decreasing portion is no longer than `g`. The computed candidate is therefore the longest mountain using that peak.

Taking the maximum over every peak gives the global longest mountain. If no index has both slopes, `ans` remains zero, matching the required no-mountain result.

**Why the second pass can compute and use `g` together**

The right-to-left loop calculates `g[i]` only from `g[i+1]`, which is already known. As soon as `g[i]` is set, `f[i]` has already been completed by the earlier left-to-right pass. The algorithm can therefore evaluate peak `i` immediately without a third scan.

## Complexity detail

Let `n = len(arr)`. Initializing `f` and `g` takes `O(n)` time. The forward and backward scans each process `O(n)` positions with constant work. Total time is `O(n)`.

The exact protected source allocates two length-`n` arrays, so its auxiliary space is `O(n)`.

The manifest's `O(1)` space target is achievable with a one-pass slope-state or expanding-window approach that tracks only the current mountain boundaries. It is not the precise storage bound of this two-array implementation. The source explained here trades linear storage for especially direct per-index slope meanings.

## Alternatives and edge cases

- **One-pass mountain window:** Skip flat/down regions, climb strictly, then descend strictly while measuring boundaries. It achieves `O(1)` space and `O(n)` time but requires careful pointer transitions.

- **Expand left and right from every peak:** Without reusing slope lengths, repeated expansion can become `O(n^2)`.

- **Entirely increasing array:** Every `g[i]` remains one, so no peak has a descending side and answer is zero.

- **Entirely decreasing array:** No `f[i]` exceeds one at a descending index, so answer is zero.

- **All equal values:** Strict comparisons fail everywhere and answer is zero.

- **Exactly three values up then down:** Both slope lengths are two at the center, producing the minimum mountain length three.

- **Plateau at the top:** Equality prevents a strict peak, splitting any possible runs.

- **Plateau on a slope:** It resets the relevant run and cannot belong to a mountain spanning across it.

- **Mountain at array boundary:** A peak at index zero lacks an increasing side; a peak at the final index lacks a decreasing side. Neither is counted.

- **Several mountains:** Each peak produces a candidate, and `max` retains the longest.

- **Overlapping possible subarrays:** The maximal candidate at a peak subsumes shorter mountains using the same peak.

- **Input immutability:** Only `f`, `g`, and scalar variables are written.
