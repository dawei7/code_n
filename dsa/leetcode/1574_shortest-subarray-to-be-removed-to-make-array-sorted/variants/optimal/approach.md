## General

**Any surviving elements form a prefix plus a suffix**

Removing one contiguous subarray leaves some prefix `arr[0:l+1]` followed by some suffix `arr[r:n]`. Either piece may be empty.

For the remainder to be non-decreasing, the kept prefix and suffix must each already be non-decreasing, and when both exist their boundary values must satisfy `arr[l] <= arr[r]`.

The source first finds the largest naturally sorted prefix and suffix, then searches for the shortest removable gap that can join portions of them.

**Find the longest sorted prefix**

Pointer `i` starts at zero and advances while `arr[i] <= arr[i+1]`.

When the loop stops, `arr[0:i+1]` is non-decreasing. Any longer prefix would include the first descent and would not be valid without deleting an element inside it.

Equal adjacent values are allowed because the target order is non-decreasing, not strictly increasing.

**Find the longest sorted suffix**

Pointer `j` starts at `n-1` and moves left while `arr[j-1] <= arr[j]`.

Afterward, `arr[j:n]` is a maximal non-decreasing suffix.

If `i >= j`, these sorted regions overlap or meet, meaning the entire array is already non-decreasing. The source returns zero.

**Establish removal-only baselines**

Without joining both sides, one option is to keep the sorted prefix and remove everything after it. That removes `n-i-1` elements.

The other is to remove everything before the sorted suffix, costing `j` elements.

`ans = min(n - i - 1, j)` records the better of these valid extreme choices.

They also ensure an answer exists even if no useful prefix-suffix bridge is found.

**Join a prefix endpoint to the sorted suffix**

For every `l` from zero through `i`, the kept left part `arr[0:l+1]` is non-decreasing.

The source uses `bisect_left(arr, arr[l], lo=j)` to find the first index `r` in the sorted suffix whose value is at least `arr[l]`.

Then concatenating the prefix through `l` with suffix from `r` preserves non-decreasing order at the junction.

The removed interval is `l+1` through `r-1`, with length `r-l-1`.

If no suffix value is large enough, `bisect_left` returns `n`. This represents keeping the prefix and removing the entire remaining tail, still a valid candidate.

**Why binary search is valid**

Although the full array is not sorted, the search begins at `lo=j`, and `arr[j:n]` is sorted.

Python's bisect operation only relies on the searched range being sorted. It does not inspect ordering before `j` for its comparisons.

Finding the first qualifying suffix index minimizes `r` for the fixed `l` and therefore minimizes the removed length for that prefix endpoint.

**Why testing all prefix endpoints is complete**

Any valid one-interval removal that keeps elements on both sides ends after some kept prefix index `l` and resumes at some suffix index `r`.

The kept prefix must lie within the maximal sorted prefix, so `l <= i`. The kept suffix must lie within the maximal sorted suffix, so `r >= j`.

For each possible `l`, binary search finds the earliest compatible `r`, at least as good as the one from any valid solution with that `l`.

Taking the minimum over all `l` plus the two empty-side baselines covers every possible optimum.

**Tracing the first example**

For one, two, three, ten, four, two, three, five, the maximal prefix ends at ten's index three. The maximal suffix starts at the later two's index five.

For prefix endpoint value three at index two, binary search in suffix two, three, five finds the suffix three at index six.

Removing indices three through five removes ten, four, and two, length three. The remaining one, two, three, three, five is non-decreasing.

**Exact source versus the linear alternative**

The editorial also presents a two-pointer merge. Because prefix endpoint values are non-decreasing, the compatible suffix pointer never needs to move backward. That realizes $O(N)$ time.

The stored solution instead performs a fresh binary search for every prefix endpoint. It is simpler to reason about locally but has a logarithmic factor.

## Complexity detail

Finding prefix and suffix boundaries costs $O(N)$. There can be $O(N)$ prefix endpoints, and each `bisect_left` costs $O(\log N)$. Exact worst-case time is $O(N\log N)$.

This differs from the manifest's $O(N)$ time, which describes the two-pointer merge alternative rather than the exact stored source.

The implementation stores only scalar indices and the answer. `bisect_left` is iterative library logic and allocates no size-dependent structure, so auxiliary space is $O(1)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Two-pointer merge:** Advance one suffix pointer monotonically while scanning the prefix, achieving $O(N)$ time and $O(1)$ space.
- **Remove only suffix:** Cost `n-i-1` is one baseline.
- **Remove only prefix:** Cost `j` is the other baseline.
- **Already sorted:** Prefix and suffix overlap, so answer is zero.
- **Strictly decreasing:** Only one element can remain, giving removal length `N-1`.
- **Duplicate values:** `bisect_left` finds the first value greater than or equal to the prefix boundary, correctly allowing equality.
- **No compatible suffix value:** Returned index `N` means remove everything after the kept prefix.
- **Empty removal:** It is valid and detected before any binary searches when the array is sorted.
- **One-element array:** Both scans leave overlapping boundaries and return zero.
- **Middle-only removal:** A compatible prefix-suffix bridge produces it.
- **Sorted search range:** Only suffix `arr[j:]` must be sorted; the earlier array may be arbitrary.
- **No input mutation:** The method reads indices and values without changing `arr`.
- **Manifest mismatch:** Linear time belongs to the two-pointer implementation, not this per-prefix binary search.
